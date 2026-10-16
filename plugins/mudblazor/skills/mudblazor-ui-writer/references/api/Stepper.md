# Stepper components — API (generated from source)

## MudStep : MudComponentBase

A individual step as part of a `MudStepper`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ChildContent` | `RenderFragment?` | `null` | The content for this step. Defaults to `null`. Only shown when this step is active. Use the `MudStepContext` cascading parameter to access information about the current step inside the template. |
| `Title` | `string?` | `null` | The title of this step. Defaults to `null`. |
| `SecondaryText` | `string?` | `null` | The subtitle describing this step. Defaults to `null`. |
| `CompletedStepColor` | `Color?` | `null` | The color used when this step is completed. Defaults to `null`. |
| `ErrorStepColor` | `Color?` | `null` | The color used when this step has an error. Defaults to `null`. |
| `SkippedStepColor` | `Color?` | `null` | The color used when this step is skipped. Defaults to `null`. |
| `Completed` | `bool` | `false` | Whether this step is completed. Defaults to `false`. |
| `CompletedChanged` | `EventCallback<bool>` | – | Occurs when `Completed` has changed. |
| `Disabled` | `bool` | – | Prevents this step from being selected. |
| `DisabledChanged` | `EventCallback<bool>` | – | Occurs when `Disabled` has changed. |
| `HasError` | `bool` | `false` | Whether this step has an error. Defaults to `false`. |
| `HasErrorChanged` | `EventCallback<bool>` | – | Occurs when `HasError` has changed. |
| `OnClick` | `EventCallback<MouseEventArgs>` | – | Occurs when this step is clicked. |
| `Skippable` | `bool` | `false` | Whether the user can skip this step. Defaults to `false`. |
| `Skipped` | `bool` | `false` | Whether this step has been skipped. Defaults to `false`. |
| `SkippedChanged` | `EventCallback<bool>` | – | Occurs when `Skipped` has changed. |

## MudStepContext

Provides contextual information about a `MudStep` within a `MudStepper`.

_No own parameters._

## MudStepper : MudComponentBase

Guides users through a series of steps to complete a transaction, such as forms or wizards.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `ActiveIndex` | `int` | `-1` | The index of the currently active step. |
| `ActiveIndexChanged` | `EventCallback<int>` | – | Occurs when `ActiveIndex` has changed. |
| `CompletedStepColor` | `Color` | `Color.Primary` | The color of completed steps. Defaults to `Primary`. |
| `CurrentStepColor` | `Color` | `Color.Primary` | The color of the current step. Defaults to `Primary`. |
| `ErrorStepColor` | `Color` | `Color.Error` | The color of steps with errors. Defaults to `Error`. |
| `SkippedStepColor` | `Color` | `Color.Default` | The color of skipped steps. Defaults to `Default`. |
| `StepCompleteIcon` | `string` | `Icons.Material.Outlined.Done` | The icon shown for completed steps. Defaults to `Done`. |
| `StepErrorIcon` | `string` | `Icons.Material.Outlined.PriorityHigh` | The icon shown for steps with errors. Defaults to `PriorityHigh`. |
| `StepSkippedIcon` | `string` | `Icons.Material.Outlined.SkipNext` | The icon shown for skipped steps. Defaults to `SkipNext`. |
| `ResetButtonIcon` | `string` | `Icons.Material.Filled.FirstPage` | The icon shown for the reset button. Defaults to `FirstPage`. |
| `PreviousButtonIcon` | `string` | `Icons.Material.Filled.NavigateBefore` | The icon shown for the `Previous` button. Defaults to `NavigateBefore`. |
| `SkipButtonIcon` | `string` | `@"<svg style=""width:24px;height:24px"" viewBox=""0 0 24 24""><path fill=""currentColor"" d=""M12,14A2,2 0 0,1 14,16A2,2 0 0,1 12,18A2,2 0 0,1 10,16A2,2 0 0,1 12,14M23.46,8.86L21.87,15.75L15,14.16L18.8,11.78C17.39,9.5 14.87,8 12,8C8.05,8 4.77,10.86 4.12,14.63L2.15,14.28C2.96,9.58 7.06,6 12,6C15.58,6 18.73,7.89 20.5,10.72L23.46,8.86Z"" /></svg>"` | The icon shown for the `Skip` button. Defaults to a custom icon. |
| `NextButtonIcon` | `string` | `Icons.Material.Filled.NavigateNext` | The icon shown for the `Next` button. Defaults to `NavigateNext`. |
| `CompleteButtonIcon` | `string` | `Icons.Material.Outlined.Done` | The icon shown for the `Complete` button. Defaults to `Done`. |
| `NavClass` | `string?` | `null` | The CSS classes applied to the navigation bar. Defaults to `null`. Multiple classes must be separated by spaces. |
| `ActionsClass` | `string?` | `null` | The CSS classes applied to the action bar. Defaults to `null`. Multiple classes must be separated by spaces. |
| `NonLinear` | `bool` | `false` | Allows users to move between steps arbitrarily. Defaults to `false`. When `false`, users must complete the active step before being allowed to move to the next step. |
| `ShowResetButton` | `bool` | `false` | Shows a button to start over at the first step. Defaults to `false`. Clicking the reset button sets this stepper back to its initial state, discarding all progress and errors. |
| `Vertical` | `bool` | – | Renders steps vertically. |
| `StepClass` | `string?` | `null` | The CSS classes applied to all steps. Defaults to `null`. Multiple classes must be separated by spaces. |
| `CenterLabels` | `bool` | `false` | Centers the labels for each step below the circle. Defaults to `false`. Only applies when `Vertical` is `false`. |
| `Ripple` | `bool` | `true` | Displays a ripple effect when a step is clicked. Defaults to `false`. Only applies when `NonLinear` is `true`. |
| `ShowSkip` | `bool` | `false` | Displays if a step has been skipped in the label. Defaults to `false`. |
| `ScrollableNavigation` | `bool` | `true` | Shows a scroll bar for steps if needed. Defaults to `true`. |
| `OnPreviewInteraction` | `Func<StepperInteractionEventArgs, Task>?` | – | Occurs when the user attempts to go to a step. Use this function to customize when the user can navigate to a step, such as when a form has been properly completed. The attempted navigation can be prevented by setting `Cancel` to `true`. |
| `ChildContent` | `RenderFragment?` | – | The steps in this component. Must be a set of `MudStep` components. |
| `TitleTemplate` | `RenderFragment<IStepContext>?` | `null` | The custom template for displaying each step's title. Defaults to `null`. The current `MudStep` is passed as context for this render fragment. |
| `LabelTemplate` | `RenderFragment<IStepContext>?` | `null` | The custom template for displaying each step's index and icon. Defaults to `null`. |
| `ConnectorTemplate` | `RenderFragment<IStepContext>?` | `null` | The custom template for displaying lines connecting each step. Defaults to `null`. |
| `CompletedContent` | `RenderFragment?` | – | This content is displayed when all steps are completed |
| `ActionContent` | `RenderFragment<MudStepper>?` | – | Use this to override the default action buttons of the stepper |
