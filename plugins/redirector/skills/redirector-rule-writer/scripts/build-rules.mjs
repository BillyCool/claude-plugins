#!/usr/bin/env node
// Validate, test and export Redirector rules.
//
// The matching logic below is a faithful port of js/redirect.js from
// https://github.com/einaregilsson/Redirector (v3.5.4). Keep it identical:
// the point is that a rule that passes here behaves the same in the extension.
//
// Usage:
//   node build-rules.mjs <draft.json> [--out <import.json>]
//
// <draft.json> is an array of rules, or { "redirects": [...] }. Each rule may
// carry an extra `tests` array: [{ "url": "...", "expect": "<result>" | null }]
// where null means "must NOT be redirected". `tests` is stripped on export.
// Exit code 1 if any rule has an error or any test fails.

import { readFileSync, writeFileSync } from 'node:fs';

const REQUEST_TYPES = ['main_frame', 'sub_frame', 'stylesheet', 'font', 'script', 'image',
  'imageset', 'media', 'object', 'object_subrequest', 'xmlhttprequest', 'history', 'other'];
const PROCESS = ['noProcessing', 'urlEncode', 'urlDecode', 'doubleUrlDecode', 'base64decode'];

function preparePattern(pattern, type) {
  if (!pattern) return null;
  if (type === 'R') return pattern;
  let converted = '^';
  for (const ch of pattern) {
    if ('()[]{}?.^$\\+'.includes(ch)) converted += '\\' + ch;
    else if (ch === '*') converted += '(.*?)';
    else converted += ch;
  }
  return converted + '$';
}

function normalize(o) {
  return {
    description: o.description || '',
    exampleUrl: o.exampleUrl || '',
    exampleResult: '',
    error: null,
    includePattern: o.includePattern || '',
    excludePattern: o.excludePattern || '',
    patternDesc: o.patternDesc || '',
    redirectUrl: o.redirectUrl || '',
    patternType: o.patternType || 'W',
    processMatches: o.processMatches || 'noProcessing',
    disabled: !!o.disabled,
    grouped: !!o.grouped,
    appliesTo: o.appliesTo && o.appliesTo.length ? [...o.appliesTo] : ['main_frame'],
  };
}

// Port of Redirect.getMatch (+ _includeMatch/_excludeMatch). Throws like the extension would.
function getMatch(r, url) {
  const inc = preparePattern(r.includePattern, r.patternType);
  const exc = preparePattern(r.excludePattern, r.patternType);
  const rxInc = inc ? new RegExp(inc, 'gi') : null;
  const rxExc = exc ? new RegExp(exc, 'gi') : null;
  const res = { isMatch: false, isExcludeMatch: false, redirectTo: '' };
  if (!rxInc) return res;
  const m = rxInc.exec(url);
  if (!m) return res;
  let out = r.redirectUrl;
  for (let i = m.length - 1; i > 0; i--) {
    let repl = m[i] || '';
    if (r.processMatches === 'urlDecode') repl = unescape(repl);
    else if (r.processMatches === 'doubleUrlDecode') repl = unescape(unescape(repl));
    else if (r.processMatches === 'urlEncode') repl = encodeURIComponent(repl);
    else if (r.processMatches === 'base64decode') {
      if (repl.includes('%')) repl = unescape(repl);
      repl = atob(repl);
    }
    out = out.replace(new RegExp('\\$' + i, 'gi'), repl);
  }
  if (rxExc && rxExc.test(url)) { res.isExcludeMatch = true; return res; }
  res.isMatch = true;
  res.redirectTo = out;
  return res;
}

// Port of Redirect.updateExampleResult, plus extra lint the extension does not do.
function check(r) {
  const warnings = [];
  if (!r.exampleUrl) return { error: 'No example URL defined.', warnings };
  if (r.patternType !== 'W' && r.patternType !== 'R') return { error: 'patternType must be "W" or "R".', warnings };
  if (!PROCESS.includes(r.processMatches)) return { error: `processMatches "${r.processMatches}" is not one of ${PROCESS.join(', ')}.`, warnings };
  const badType = r.appliesTo.find((t) => !REQUEST_TYPES.includes(t));
  if (badType) return { error: `Unknown appliesTo type "${badType}".`, warnings };
  for (const [k, label] of [['includePattern', 'Include'], ['excludePattern', 'Exclude']]) {
    if (!r[k]) continue;
    try { new RegExp(preparePattern(r[k], r.patternType), 'gi'); }
    catch { return { error: `Invalid regular expression in ${label} pattern.`, warnings }; }
  }
  if (!r.includePattern) return { error: 'Include pattern is empty.', warnings };
  let m;
  try { m = getMatch(r, r.exampleUrl); } catch (e) { return { error: 'Throws on the example URL: ' + e.message, warnings }; }
  if (m.isExcludeMatch) return { error: 'The exclude pattern excludes the example url.', warnings };
  if (!m.isMatch) return { error: 'The include pattern does not match the example url.', warnings };

  // Lint beyond what the extension checks.
  const refs = [...r.redirectUrl.matchAll(/\$(\d+)/g)].map((x) => +x[1]);
  const groups = new RegExp(preparePattern(r.includePattern, r.patternType) + '|', 'i').exec('').length - 1;
  if (refs.some((n) => n === 0 || n > groups)) warnings.push(`Redirect to uses $N beyond the ${groups} capture group(s) in the include pattern ($0 is never supported).`);
  if (r.patternType === 'R' && !r.includePattern.startsWith('^')) warnings.push('Regex include pattern is not anchored with ^ - it can match mid-URL (e.g. inside a query string).');
  if (r.patternType === 'W' && r.includePattern.includes('|')) warnings.push('"|" in a wildcard pattern is NOT escaped by Redirector and acts as regex alternation.');
  if (r.appliesTo.includes('history') && /\(\?[=!<]/.test(r.includePattern)) warnings.push('"history" rules feed the include regex to webNavigation urlMatches (RE2): lookahead/lookbehind will not work.');
  if (r.processMatches !== 'noProcessing' && groups === 0) warnings.push('processMatches has no effect without capture groups.');
  if (r.processMatches === 'urlDecode' || r.processMatches === 'doubleUrlDecode') warnings.push('URL decode uses unescape(): multi-byte UTF-8 (%C3%A9) decodes to mojibake. Avoid for non-ASCII payloads.');
  if (!/^https?:\/\//i.test(m.redirectTo)) warnings.push(`Example result "${m.redirectTo}" does not start with http(s):// - the browser may refuse it.`);
  if (r.appliesTo.some((t) => t !== 'main_frame')) warnings.push('Non-main_frame types run on every matching sub-request; keep the pattern narrow (performance).');
  return { error: null, result: m.redirectTo, warnings };
}

const args = process.argv.slice(2);
const outIdx = args.indexOf('--out');
const outFile = outIdx >= 0 ? args[outIdx + 1] : null;
const file = args.find((a, i) => !a.startsWith('--') && i !== outIdx + 1);
if (!file) { console.error('Usage: node build-rules.mjs <draft.json> [--out <import.json>]'); process.exit(2); }

let draft = JSON.parse(readFileSync(file, 'utf8'));
if (!Array.isArray(draft)) draft = draft.redirects;
let failed = false;
const finished = [];

draft.forEach((raw, idx) => {
  const r = normalize(raw);
  const c = check(r);
  const label = `#${idx + 1} ${r.description || r.includePattern}`;
  if (c.error) { failed = true; console.log(`FAIL ${label}\n     ${c.error}`); r.error = c.error; }
  else {
    r.exampleResult = c.result;
    console.log(`ok   ${label}\n     ${r.exampleUrl}\n  -> ${c.result}`);
    c.warnings.forEach((w) => console.log(`     warn: ${w}`));
  }
  for (const t of raw.tests || []) {
    let got;
    try { const m = getMatch(r, t.url); got = m.isMatch ? m.redirectTo : null; } catch (e) { got = 'THROWS: ' + e.message; }
    const want = t.expect ?? null;
    const pass = got === want;
    if (!pass) failed = true;
    const show = (v) => (v === null ? '(no redirect)' : v);
    console.log(`     test ${pass ? 'pass' : 'FAIL'}: ${t.url} => ${show(got)}${pass ? '' : `   expected ${show(want)}`}`);
  }
  finished.push(r);
});

// First-match-wins hint: warn if an earlier rule shadows a later rule's example URL.
finished.forEach((later, j) => {
  for (let i = 0; i < j; i++) {
    const earlier = finished[i];
    if (earlier.disabled || !earlier.appliesTo.some((t) => later.appliesTo.includes(t))) continue;
    try {
      if (getMatch(earlier, later.exampleUrl).isMatch) console.log(`warn: rule #${i + 1} also matches the example URL of rule #${j + 1}; the earlier rule wins (first match wins, in list order).`);
    } catch { /* ignore */ }
  }
});

if (outFile && !failed) {
  const exportObj = { createdBy: 'Redirector v3.5.4 (generated)', createdAt: new Date().toISOString(), redirects: finished };
  writeFileSync(outFile, JSON.stringify(exportObj, null, 4) + '\n');
  console.log(`\nWrote ${finished.length} rule(s) to ${outFile}`);
} else if (outFile) {
  console.log('\nNot writing the import file: fix the failures above first.');
}
process.exit(failed ? 1 : 0);
