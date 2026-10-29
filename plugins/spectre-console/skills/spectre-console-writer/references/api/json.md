# json — API (generated from source)

## `public interface IJsonParser`

*json* · `src/Extensions/Spectre.Console.Json/IJsonParser.cs`

Represents a JSON parser.

**Methods**

- `JsonSyntax Parse(string json)` — Parses the provided JSON into an abstract syntax tree.

## `public sealed class JsonArray : JsonSyntax`

*json* · `src/Extensions/Spectre.Console.Json/Syntax/JsonArray.cs`

Represents an array in the JSON abstract syntax tree.

**Constructors**

- `JsonArray()` — Initializes a new instance of the `JsonArray` class.

**Properties**

- `List<JsonSyntax> Items { get; }` — Gets the array items.

## `public sealed class JsonBoolean : JsonSyntax`

*json* · `src/Extensions/Spectre.Console.Json/Syntax/JsonBoolean.cs`

Represents a boolean literal in the JSON abstract syntax tree.

**Constructors**

- `JsonBoolean(string lexeme)` — Initializes a new instance of the `JsonBoolean` class.

**Properties**

- `string Lexeme { get; }` — Gets the lexeme.

## `public sealed class JsonMember : JsonSyntax`

*json* · `src/Extensions/Spectre.Console.Json/Syntax/JsonMember.cs`

Represents a member in the JSON abstract syntax tree.

**Constructors**

- `JsonMember(string name, JsonSyntax value)` — Initializes a new instance of the `JsonMember` class.

**Properties**

- `string Name { get; }` — Gets the member name.
- `JsonSyntax Value { get; }` — Gets the member value.

## `public sealed class JsonNull : JsonSyntax`

*json* · `src/Extensions/Spectre.Console.Json/Syntax/JsonNull.cs`

Represents a null literal in the JSON abstract syntax tree.

**Constructors**

- `JsonNull(string lexeme)` — Initializes a new instance of the `JsonNull` class.

**Properties**

- `string Lexeme { get; }` — Gets the lexeme.

## `public sealed class JsonObject : JsonSyntax`

*json* · `src/Extensions/Spectre.Console.Json/Syntax/JsonObject.cs`

Represents an object in the JSON abstract syntax tree.

**Constructors**

- `JsonObject()` — Initializes a new instance of the `JsonObject` class.

**Properties**

- `List<JsonMember> Members { get; }` — Gets the object's members.

## `public sealed class JsonString : JsonSyntax`

*json* · `src/Extensions/Spectre.Console.Json/Syntax/JsonString.cs`

Represents a string literal in the JSON abstract syntax tree.

**Constructors**

- `JsonString(string lexeme)` — Initializes a new instance of the `JsonString` class.

**Properties**

- `string Lexeme { get; }` — Gets the lexeme.

## `public abstract class JsonSyntax`

*json* · `src/Extensions/Spectre.Console.Json/Syntax/JsonSyntax.cs`

Represents a syntax node in the JSON abstract syntax tree.

## `public sealed class JsonText : JustInTimeRenderable`

*json* · `src/Extensions/Spectre.Console.Json/JsonText.cs`

A renderable piece of JSON text.

**Constructors**

- `JsonText(string json)` — Initializes a new instance of the `JsonText` class.

**Properties**

- `Style? BracesStyle { get; set; }` — Gets or sets the style used for braces.
- `Style? BracketsStyle { get; set; }` — Gets or sets the style used for brackets.
- `Style? MemberStyle { get; set; }` — Gets or sets the style used for member names.
- `Style? ColonStyle { get; set; }` — Gets or sets the style used for colons.
- `Style? CommaStyle { get; set; }` — Gets or sets the style used for commas.
- `Style? StringStyle { get; set; }` — Gets or sets the style used for string literals.
- `Style? NumberStyle { get; set; }` — Gets or sets the style used for number literals.
- `Style? BooleanStyle { get; set; }` — Gets or sets the style used for boolean literals.
- `Style? NullStyle { get; set; }` — Gets or sets the style used for `null` literals.
- `string Indentation { get; set; }` = `" "` — Gets or sets the indentation. Defaults to three spaces.
- `IJsonParser? Parser { get; set; }` — Gets or sets the JSON parser.

**Methods**

- `protected override IRenderable Build()` — Builds the inner renderable.

**Extension methods on this type** (call as `x.Method(...)`)

- `BracesStyle(Style? style) -> JsonText` — Sets the style used for braces.
- `BracketStyle(Style? style) -> JsonText` — Sets the style used for brackets.
- `MemberStyle(Style? style) -> JsonText` — Sets the style used for member names.
- `ColonStyle(Style? style) -> JsonText` — Sets the style used for colons.
- `CommaStyle(Style? style) -> JsonText` — Sets the style used for commas.
- `StringStyle(Style? style) -> JsonText` — Sets the style used for string literals.
- `NumberStyle(Style? style) -> JsonText` — Sets the style used for number literals.
- `BooleanStyle(Style? style) -> JsonText` — Sets the style used for boolean literals.
- `NullStyle(Style? style) -> JsonText` — Sets the style used for `null` literals.
- `BracesColor(Color color) -> JsonText` — Sets the color used for braces.
- `BracketColor(Color color) -> JsonText` — Sets the color used for brackets.
- `MemberColor(Color color) -> JsonText` — Sets the color used for member names.
- `ColonColor(Color color) -> JsonText` — Sets the color used for colons.
- `CommaColor(Color color) -> JsonText` — Sets the color used for commas.
- `StringColor(Color color) -> JsonText` — Sets the color used for string literals.
- `NumberColor(Color color) -> JsonText` — Sets the color used for number literals.
- `BooleanColor(Color color) -> JsonText` — Sets the color used for boolean literals.
- `NullColor(Color color) -> JsonText` — Sets the color used for `null` literals.
- `Indentation(string indentation = " ") -> JsonText` — Sets the indentation.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IRenderable`: `GetSegments`

