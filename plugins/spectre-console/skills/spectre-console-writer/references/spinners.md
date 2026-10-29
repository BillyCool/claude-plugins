# Spinners (generated from `Spectre.Console/Data/spinners_*.json`)

Use as `Spinner.Known.<Name>` (e.g. `.Spinner(Spinner.Known.Dots)`). `Default` and `Ascii` come from `spinners_default.json`; the rest are from sindresorhus/cli-spinners. `unicode: true` means the spinner needs a Unicode-capable terminal (Spectre falls back to `Spinner.Known.Ascii` otherwise).

| Name | Interval (ms) | Unicode | Frames (first 6) |
|---|---|---|---|
| Default | 100 | True | `⣷ ⣯ ⣟ ⡿ ⢿ ⣻` |
| Ascii | 100 | True | `- \ \| / - \` |
| dots | 80 | True | `⠋ ⠙ ⠹ ⠸ ⠼ ⠴` |
| dots2 | 80 | True | `⣾ ⣽ ⣻ ⢿ ⡿ ⣟` |
| dots3 | 80 | True | `⠋ ⠙ ⠚ ⠞ ⠖ ⠦` |
| dots4 | 80 | True | `⠄ ⠆ ⠇ ⠋ ⠙ ⠸` |
| dots5 | 80 | True | `⠋ ⠙ ⠚ ⠒ ⠂ ⠂` |
| dots6 | 80 | True | `⠁ ⠉ ⠙ ⠚ ⠒ ⠂` |
| dots7 | 80 | True | `⠈ ⠉ ⠋ ⠓ ⠒ ⠐` |
| dots8 | 80 | True | `⠁ ⠁ ⠉ ⠙ ⠚ ⠒` |
| dots9 | 80 | True | `⢹ ⢺ ⢼ ⣸ ⣇ ⡧` |
| dots10 | 80 | True | `⢄ ⢂ ⢁ ⡁ ⡈ ⡐` |
| dots11 | 100 | True | `⠁ ⠂ ⠄ ⡀ ⢀ ⠠` |
| dots12 | 80 | True | `⢀⠀ ⡀⠀ ⠄⠀ ⢂⠀ ⡂⠀ ⠅⠀` |
| dots13 | 80 | True | `⣼ ⣹ ⢻ ⠿ ⡟ ⣏` |
| dots14 | 80 | True | `⠉⠉ ⠈⠙ ⠀⠹ ⠀⢸ ⠀⣰ ⢀⣠` |
| dots8Bit | 80 | True | `⠀ ⠁ ⠂ ⠃ ⠄ ⠅` |
| dotsCircle | 80 | True | `⢎  ⠎⠁ ⠊⠑ ⠈⠱  ⡱ ⢀⡰` |
| sand | 80 | True | `⠁ ⠂ ⠄ ⡀ ⡈ ⡐` |
| line | 130 | False | `- \ \| /` |
| line2 | 100 | False | `⠂ - – — – -` |
| pipe | 100 | False | `┤ ┘ ┴ └ ├ ┌` |
| simpleDots | 400 | False | `.   ..  ...    ` |
| simpleDotsScrolling | 200 | False | `.   ..  ...  ..   .    ` |
| star | 70 | True | `✶ ✸ ✹ ✺ ✹ ✷` |
| star2 | 80 | False | `+ x *` |
| flip | 70 | False | `_ _ _ - ` `` |
| hamburger | 100 | True | `☱ ☲ ☴` |
| growVertical | 120 | True | `▁ ▃ ▄ ▅ ▆ ▇` |
| growHorizontal | 120 | True | `▏ ▎ ▍ ▌ ▋ ▊` |
| balloon | 140 | False | `  . o O @ *` |
| balloon2 | 120 | False | `. o O ° O o` |
| noise | 100 | True | `▓ ▒ ░` |
| bounce | 120 | True | `⠁ ⠂ ⠄ ⠂` |
| boxBounce | 120 | True | `▖ ▘ ▝ ▗` |
| boxBounce2 | 100 | True | `▌ ▀ ▐ ▄` |
| triangle | 50 | True | `◢ ◣ ◤ ◥` |
| binary | 80 | False | `010010 001100 100101 111010 111101 010111` |
| arc | 100 | True | `◜ ◠ ◝ ◞ ◡ ◟` |
| circle | 120 | True | `◡ ⊙ ◠` |
| squareCorners | 180 | True | `◰ ◳ ◲ ◱` |
| circleQuarters | 120 | True | `◴ ◷ ◶ ◵` |
| circleHalves | 50 | True | `◐ ◓ ◑ ◒` |
| squish | 100 | True | `╫ ╪` |
| toggle | 250 | True | `⊶ ⊷` |
| toggle2 | 80 | True | `▫ ▪` |
| toggle3 | 120 | True | `□ ■` |
| toggle4 | 100 | True | `■ □ ▪ ▫` |
| toggle5 | 100 | True | `▮ ▯` |
| toggle6 | 300 | True | `ဝ ၀` |
| toggle7 | 80 | True | `⦾ ⦿` |
| toggle8 | 100 | True | `◍ ◌` |
| toggle9 | 100 | True | `◉ ◎` |
| toggle10 | 100 | True | `㊂ ㊀ ㊁` |
| toggle11 | 50 | True | `⧇ ⧆` |
| toggle12 | 120 | True | `☗ ☖` |
| toggle13 | 80 | False | `= * -` |
| arrow | 100 | True | `← ↖ ↑ ↗ → ↘` |
| arrow2 | 80 | True | `⬆️  ↗️  ➡️  ↘️  ⬇️  ↙️ ` |
| arrow3 | 120 | True | `▹▹▹▹▹ ▸▹▹▹▹ ▹▸▹▹▹ ▹▹▸▹▹ ▹▹▹▸▹ ▹▹▹▹▸` |
| bouncingBar | 80 | True | `[    ] [=   ] [==  ] [=== ] [====] [ ===]` |
| bouncingBall | 80 | True | `( ●    ) (  ●   ) (   ●  ) (    ● ) (     ●) (    ● )` |
| smiley | 200 | True | `😄  😝 ` |
| monkey | 300 | True | `🙈  🙈  🙉  🙊 ` |
| hearts | 100 | True | `💛  💙  💜  💚  ❤️ ` |
| clock | 100 | True | `🕛  🕐  🕑  🕒  🕓  🕔 ` |
| earth | 180 | True | `🌍  🌎  🌏 ` |
| material | 17 | True | `█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ███▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ████▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ██████▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ██████▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| moon | 80 | True | `🌑  🌒  🌓  🌔  🌕  🌖 ` |
| runner | 140 | True | `🚶  🏃 ` |
| pong | 80 | True | `▐⠂       ▌ ▐⠈       ▌ ▐ ⠂      ▌ ▐ ⠠      ▌ ▐  ⡀     ▌ ▐  ⠠     ▌` |
| shark | 120 | True | `▐\|\____________▌ ▐_\|\___________▌ ▐__\|\__________▌ ▐___\|\_________▌ ▐____\|\________▌ ▐_____\|\_______▌` |
| dqpb | 100 | False | `d q p b` |
| weather | 100 | True | `☀️  ☀️  ☀️  🌤  ⛅️  🌥 ` |
| christmas | 400 | True | `🌲 🎄` |
| grenade | 80 | True | `،   ′    ´   ‾    ⸌   ⸊` |
| point | 125 | True | `∙∙∙ ●∙∙ ∙●∙ ∙∙● ∙∙∙` |
| layer | 150 | True | `- = ≡` |
| betaWave | 80 | True | `ρββββββ βρβββββ ββρββββ βββρβββ ββββρββ βββββρβ` |
| fingerDance | 160 | True | `🤘  🤟  🖖  ✋  🤚  👆 ` |
| fistBump | 80 | True | `🤜　　　　🤛  🤜　　　　🤛  🤜　　　　🤛  　🤜　　🤛　  　　🤜🤛　　  　🤜✨🤛　　 ` |
| soccerHeader | 80 | True | ` 🧑⚽️       🧑  🧑  ⚽️      🧑  🧑   ⚽️     🧑  🧑    ⚽️    🧑  🧑     ⚽️   🧑  🧑      ⚽️  🧑 ` |
| mindblown | 160 | True | `😐  😐  😮  😮  😦  😦 ` |
| speaker | 160 | True | `🔈  🔉  🔊  🔉 ` |
| orangePulse | 100 | True | `🔸  🔶  🟠  🟠  🔶 ` |
| bluePulse | 100 | True | `🔹  🔷  🔵  🔵  🔷 ` |
| orangeBluePulse | 100 | True | `🔸  🔶  🟠  🟠  🔶  🔹 ` |
| timeTravel | 100 | True | `🕛  🕚  🕙  🕘  🕗  🕖 ` |
| aesthetic | 80 | True | `▰▱▱▱▱▱▱ ▰▰▱▱▱▱▱ ▰▰▰▱▱▱▱ ▰▰▰▰▱▱▱ ▰▰▰▰▰▱▱ ▰▰▰▰▰▰▱` |
| dwarfFortress | 80 | True | ` ██████£££   ☺██████£££   ☺██████£££   ☺▓█████£££   ☺▓█████£££   ☺▒█████£££  ` |
