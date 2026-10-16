# PageContentNavigation components — API (generated from source)

## MudPageContentNavigation : IAsyncDisposable

A drawer used to navigate sections on a page.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `Headline` | `string` | `string.Empty` | The text displayed about the section links. Defaults to "Contents" |
| `ScrollContainerSelector` | `string` | `"html"` | The CSS selector used to identify the scroll container |
| `SectionClassSelector` | `string` | `string.Empty` | The class name (without .) to identify the HTML elements that should be observed for viewport changes |
| `HierarchyMapper` | `IDictionary<string, int>` | `new Dictionary<string, int>()` | If there are multiple levels, this can specified to make a mapping between a level class like "second-level" and the level in the hierarchy |
| `ExpandBehaviour` | `ContentNavigationExpandBehaviour` | `ContentNavigationExpandBehaviour.Always` | If there are multiple levels, this property controls they visibility of them. |
| `ActivateFirstSectionAsDefault` | `bool` | `false` | If this option is true the first added section will become active when there is no other indication of an active session. Default value is false |

## MudPageContentSection

A section (nav link) inside the MudPageContentNavigation

_No own parameters._
