# widgets/Tree — API (generated from source)

## `public sealed class Tree : Renderable, IHasTreeNodes`

*core* · `src/Spectre.Console/Widgets/Tree.cs`

Representation of non-circular tree data. Each node added to the tree may only be present in it a single time, in order to facilitate cycle detection.

**Constructors**

- `Tree(IRenderable renderable)` — Initializes a new instance of the `Tree` class.
- `Tree(string label)` — Initializes a new instance of the `Tree` class.

**Properties**

- `Style? Style { get; set; }` — Gets or sets the tree style.
- `TreeGuide Guide { get; set; }` = `TreeGuide.Line` — Gets or sets the tree guide lines.
- `List<TreeNode> Nodes { get; }` — Gets the tree's child nodes.
- `bool Expanded { get; set; }` — Gets or sets a value indicating whether or not the tree is expanded or not.

**Methods**

- `protected override IEnumerable<Segment> Render(RenderOptions options, int maxWidth)` — Renders the object.

**Extension methods on this type** (call as `x.Method(...)`)

- `Style(Style? style) -> Tree` — Sets the tree style.
- `Guide(TreeGuide guide) -> Tree` — Sets the tree guide line appearance.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasTreeNodes`: `AddNode`, `AddNodes`
- via `IRenderable`: `GetSegments`

## `public sealed class TreeNode : IHasTreeNodes`

*core* · `src/Spectre.Console/Widgets/TreeNode.cs`

Represents a tree node.

**Constructors**

- `TreeNode(IRenderable renderable)` — Initializes a new instance of the `TreeNode` class.

**Properties**

- `List<TreeNode> Nodes { get; }` = `[]` — Gets the tree node's child nodes.
- `bool Expanded { get; set; }` = `true` — Gets or sets a value indicating whether or not the tree node is expanded or not.

**Extension methods on this type** (call as `x.Method(...)`)

- `Expand() -> TreeNode` — Expands the tree.
- `Collapse() -> TreeNode` — Collapses the tree.
- `Expand(bool expand) -> TreeNode` — Sets whether or not the tree node should be expanded.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasTreeNodes`: `AddNode`, `AddNodes`

