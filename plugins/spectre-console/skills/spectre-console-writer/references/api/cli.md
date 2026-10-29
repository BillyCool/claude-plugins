# cli — API (generated from source)

## `public sealed class ArgumentStyle`

*cli* · `src/Spectre.Console.Cli/Help/HelpProviderStyles.cs`

Defines styles for specifying arguments in a command.

**Properties**

- `Style? Header { get; set; }` — Gets or sets the style for the header in the arguments.
- `Style? RequiredArgument { get; set; }` — Gets or sets the style for required arguments.
- `Style? OptionalArgument { get; set; }` — Gets or sets the style for optional arguments.

## `public abstract class AsyncCommand : ICommand<EmptyCommandSettings>`

*cli* · `src/Spectre.Console.Cli/AsyncCommand.cs`

Base class for an asynchronous command with no settings.

**Methods**

- `abstract Task<int> ExecuteAsync(CommandContext context, CancellationToken cancellationToken)` — Executes the command.

## `public abstract class AsyncCommand<TSettings> : ICommand<TSettings> where TSettings : CommandSettings`

*cli* · `src/Spectre.Console.Cli/AsyncCommandOfT.cs`

Base class for an asynchronous command.

**Methods**

- `virtual ValidationResult Validate(CommandContext context, TSettings settings)` — Validates the specified settings and remaining arguments.
- `abstract Task<int> ExecuteAsync(CommandContext context, TSettings settings, CancellationToken cancellationToken)` — Executes the command.

## `public abstract class Command : ICommand<EmptyCommandSettings>`

*cli* · `src/Spectre.Console.Cli/Command.cs`

Base class for a command without settings.

**Methods**

- `abstract int Execute(CommandContext context, CancellationToken cancellationToken)` — Executes the command.

## `public abstract class Command<TSettings> : ICommand<TSettings> where TSettings : CommandSettings`

*cli* · `src/Spectre.Console.Cli/CommandOfT.cs`

Base class for a command.

**Methods**

- `virtual ValidationResult Validate(CommandContext context, TSettings settings)` — Validates the specified settings and remaining arguments.
- `abstract int Execute(CommandContext context, TSettings settings, CancellationToken cancellationToken)` — Executes the command.

## `public sealed class CommandApp : ICommandApp`

*cli* · `src/Spectre.Console.Cli/CommandApp.cs`

The entry point for a command line application.

**Constructors**

- `CommandApp(ITypeRegistrar? registrar = null)` — Initializes a new instance of the `CommandApp` class.

**Methods**

- `void Configure(Action<IConfigurator> configuration)` — Configures the command line application.
- `DefaultCommandConfigurator SetDefaultCommand<TCommand>() where TCommand : class, ICommand` — Sets the default command.
- `int Run(IEnumerable<string> args, CancellationToken cancellationToken = default)` — Runs the command line application with specified arguments.
- `async Task<int> RunAsync(IEnumerable<string> args, CancellationToken cancellationToken = default)` — Runs the command line application with specified arguments.

## `public sealed class CommandApp<TDefaultCommand> : ICommandApp where TDefaultCommand : class, ICommand`

*cli* · `src/Spectre.Console.Cli/CommandAppOfT.cs`

The entry point for a command line application with a default command.

**Constructors**

- `CommandApp(ITypeRegistrar? registrar = null)` — Initializes a new instance of the `CommandApp{TDefaultCommand}` class.

**Methods**

- `void Configure(Action<IConfigurator> configuration)`
- `int Run(IEnumerable<string> args, CancellationToken cancellationToken = default)`
- `Task<int> RunAsync(IEnumerable<string> args, CancellationToken cancellationToken = default)`
- `CommandApp<TDefaultCommand> WithDescription(string description)` — Sets the description of the default command.
- `CommandApp<TDefaultCommand> WithData(object data)` — Sets data that will be passed to the command via the `CommandContext`.

## `public abstract class CommandAppException : Exception`

*cli* · `src/Spectre.Console.Cli/CommandAppException.cs`

Represents errors that occur during application execution.

**Properties**

- `IRenderable? Pretty { get; }` — Gets the pretty formatted exception message.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `Exception`: `GetRenderable`

## `public sealed class CommandArgumentAttribute : Attribute`

*cli* · `src/Spectre.Console.Cli/Annotations/CommandArgumentAttribute.cs`

An attribute representing a command argument.

**Constructors**

- `CommandArgumentAttribute(int position, string template)` — Initializes a new instance of the `CommandArgumentAttribute` class.

**Properties**

- `int Position { get; }` — Gets the argument position.
- `string ValueName { get; }` — Gets the value name of the argument.
- `bool IsRequired { get; }` — Gets a value indicating whether the argument is required.

## `public class CommandConfigurationException : CommandAppException`

*cli* · `src/Spectre.Console.Cli/CommandConfigurationException.cs`

Represents errors that occur during configuration.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `Exception`: `GetRenderable`

## `public sealed class CommandContext`

*cli* · `src/Spectre.Console.Cli/CommandContext.cs`

Represents a command context.

**Constructors**

- `CommandContext( IEnumerable<string> arguments, IRemainingArguments remaining, string name, object? data)` — Initializes a new instance of the `CommandContext` class.

**Properties**

- `IRemainingArguments Remaining { get; }` — Gets the remaining arguments.
- `IReadOnlyList<string> Arguments { get; }` — Gets all the arguments that were passed to the application.
- `string Name { get; }` — Gets the name of the command.
- `object? Data { get; }` — Gets the data that was passed to the command during registration (if any).

## `public sealed class CommandOptionAttribute : Attribute`

*cli* · `src/Spectre.Console.Cli/Annotations/CommandOptionAttribute.cs`

An attribute representing a command option.

**Constructors**

- `CommandOptionAttribute(string template, bool isRequired = false)` — Initializes a new instance of the `CommandOptionAttribute` class.

**Properties**

- `IReadOnlyList<string> LongNames { get; }` — Gets the long names of the option.
- `IReadOnlyList<string> ShortNames { get; }` — Gets the short names of the option.
- `string? ValueName { get; }` — Gets the value name of the option.
- `bool ValueIsOptional { get; }` — Gets a value indicating whether the value is optional.
- `bool IsRequired { get; }` — Gets a value indicating whether the value is required.
- `bool IsHidden { get; set; }` — Gets or sets a value indicating whether this option is hidden from the help text.

## `public sealed class CommandParameterContext`

*cli* · `src/Spectre.Console.Cli/CommandParameterContext.cs`

Represents a context for `ICommandParameterInfo` related operations.

**Constructors**

- `CommandParameterContext(ICommandParameterInfo parameter, ITypeResolver resolver, object? value)` — Initializes a new instance of the `CommandParameterContext` class.

**Properties**

- `ICommandParameterInfo Parameter { get; }` — Gets the parameter.
- `ITypeResolver Resolver { get; }` — Gets the type resolver.
- `object? Value { get; }` — Gets tje parameter value.

## `public sealed class CommandParseException : CommandRuntimeException`

*cli* · `src/Spectre.Console.Cli/CommandParseException.cs`

Represents errors that occur during parsing.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `Exception`: `GetRenderable`

## `public class CommandRuntimeException : CommandAppException`

*cli* · `src/Spectre.Console.Cli/CommandRuntimeException.cs`

Represents errors that occur during runtime.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `Exception`: `GetRenderable`

## `public abstract class CommandSettings`

*cli* · `src/Spectre.Console.Cli/CommandSettings.cs`

Base class for command settings.

**Methods**

- `virtual ValidationResult Validate()` — Performs validation of the settings.

## `public sealed class CommandStyle`

*cli* · `src/Spectre.Console.Cli/Help/HelpProviderStyles.cs`

Defines styles for specifying subcommands or nested commands.

**Properties**

- `Style? Header { get; set; }` — Gets or sets the style for the header in the command section.
- `Style? ChildCommand { get; set; }` — Gets or sets the style for child commands in the command section.
- `Style? RequiredArgument { get; set; }` — Gets or sets the style for required arguments in the command section.

## `public sealed class CommandTemplateException : CommandConfigurationException`

*cli* · `src/Spectre.Console.Cli/CommandTemplateException.cs`

Represents errors related to parameter templates.

**Properties**

- `string Template { get; }` — Gets the template that contains the error.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `Exception`: `GetRenderable`

## `public sealed class DefaultCommandConfigurator`

*cli* · `src/Spectre.Console.Cli/DefaultCommandConfigurator.cs`

Fluent configurator for the default command.

**Methods**

- `DefaultCommandConfigurator WithDescription(string description)` — Sets the description of the default command.
- `DefaultCommandConfigurator WithData(object data)` — Sets data that will be passed to the command via the `CommandContext`.

## `public sealed class DescriptionStyle`

*cli* · `src/Spectre.Console.Cli/Help/HelpProviderStyles.cs`

Defines styles for describing the purpose or details of a command.

**Properties**

- `Style? Header { get; set; }` — Gets or sets the style for the header in the description.

## `public sealed class EmptyCommandSettings : CommandSettings`

*cli* · `src/Spectre.Console.Cli/EmptyCommandSettings.cs`

Represents empty settings.

## `public sealed class ExampleStyle`

*cli* · `src/Spectre.Console.Cli/Help/HelpProviderStyles.cs`

Defines styles for providing examples of command usage.

**Properties**

- `Style? Header { get; set; }` — Gets or sets the style for the header in the examples.
- `Style? Arguments { get; set; }` — Gets or sets the style for arguments in the examples.

## `public sealed class FlagValue<T> : IFlagValue`

*cli* · `src/Spectre.Console.Cli/FlagValue.cs`

Implementation of a flag with an optional value.

**Properties**

- `bool IsSet { get; set; }` — Gets or sets a value indicating whether the flag was set or not.
- `T Value { get; set; }` — Gets or sets the flag's value.

**Methods**

- `override string ToString()`

## `public class HelpProvider : IHelpProvider`

*cli* · `src/Spectre.Console.Cli/Help/HelpProvider.cs`

The help provider for Spectre.Console.

**Constructors**

- `HelpProvider(ICommandAppSettings settings)` — Initializes a new instance of the `HelpProvider` class.

**Properties**

- `protected virtual int MaximumIndirectExamples { get; }` — Gets a value indicating how many examples from direct children to show in the help text.
- `protected virtual bool ShowOptionDefaultValues { get; }` — Gets a value indicating whether any default values for command options are shown in the help text.
- `protected virtual bool TrimTrailingPeriod { get; }` — Gets a value indicating whether a trailing period of a description is trimmed in the help text.
- `protected virtual bool RenderMarkupInline { get; }` = `false` — Gets a value indicating whether to emit the markup styles, inline, when rendering the help text.

**Methods**

- `virtual IEnumerable<IRenderable> Write(ICommandModel model, ICommandInfo? command)` — Writes help information for the application.
- `virtual IEnumerable<IRenderable> GetHeader(ICommandModel model, ICommandInfo? command)` — Gets the header for the help information.
- `virtual IEnumerable<IRenderable> GetDescription(ICommandModel model, ICommandInfo? command)` — Gets the description section of the help information.
- `virtual IEnumerable<IRenderable> GetUsage(ICommandModel model, ICommandInfo? command)` — Gets the usage section of the help information.
- `virtual IEnumerable<IRenderable> GetExamples(ICommandModel model, ICommandInfo? command)` — Gets the examples section of the help information.
- `virtual IEnumerable<IRenderable> GetArguments(ICommandModel model, ICommandInfo? command)` — Gets the arguments section of the help information.
- `virtual IEnumerable<IRenderable> GetOptions(ICommandModel model, ICommandInfo? command)` — Gets the options section of the help information.
- `virtual IEnumerable<IRenderable> GetCommands(ICommandModel model, ICommandInfo? command)` — Gets the commands section of the help information.
- `virtual IEnumerable<IRenderable> GetFooter(ICommandModel model, ICommandInfo? command)` — Gets the footer for the help information.

## `public sealed class HelpProviderStyle`

*cli* · `src/Spectre.Console.Cli/Help/HelpProviderStyles.cs`

Styles for the HelpProvider to use when rendering help text.

**Properties**

- `DescriptionStyle? Description { get; set; }` — Gets or sets the style for describing the purpose or details of a command.
- `UsageStyle? Usage { get; set; }` — Gets or sets the style for specifying the usage format of a command.
- `ExampleStyle? Examples { get; set; }` — Gets or sets the style for providing examples of command usage.
- `ArgumentStyle? Arguments { get; set; }` — Gets or sets the style for specifying arguments in a command.
- `OptionStyle? Options { get; set; }` — Gets or sets the style for specifying options or flags in a command.
- `CommandStyle? Commands { get; set; }` — Gets or sets the style for specifying subcommands or nested commands.
- `static HelpProviderStyle Default { get; }` — Gets the default HelpProvider styles.

## `public interface IBranchConfigurator`

*cli* · `src/Spectre.Console.Cli/IBranchConfigurator.cs`

Represents a branch configurator.

**Methods**

- `IBranchConfigurator WithAlias(string name)` — Adds an alias (an alternative name) to the branch being configured.

## `public interface ICommand`

*cli* · `src/Spectre.Console.Cli/ICommand.cs`

Represents a command.

**Methods**

- `ValidationResult Validate(CommandContext context, CommandSettings settings)` — Validates the specified settings and remaining arguments.
- `Task<int> ExecuteAsync(CommandContext context, CommandSettings settings, CancellationToken cancellationToken)` — Executes the command.

## `public interface ICommand<TSettings> : ICommandLimiter<TSettings> where TSettings : CommandSettings`

*cli* · `src/Spectre.Console.Cli/ICommandOfT.cs`

Represents a command.

**Methods**

- `Task<int> ExecuteAsync(CommandContext context, TSettings settings, CancellationToken cancellationToken)` — Executes the command.

## `public interface ICommandApp`

*cli* · `src/Spectre.Console.Cli/ICommandApp.cs`

Represents a command line application.

**Methods**

- `void Configure(Action<IConfigurator> configuration)` — Configures the command line application.
- `int Run(IEnumerable<string> args, CancellationToken cancellationToken = default)` — Runs the command line application with specified arguments.
- `Task<int> RunAsync(IEnumerable<string> args, CancellationToken cancellationToken = default)` — Runs the command line application with specified arguments.

## `public interface ICommandAppSettings`

*cli* · `src/Spectre.Console.Cli/ICommandAppSettings.cs`

Represents a command line application settings.

**Properties**

- `CultureInfo? Culture { get; set; }` — Gets or sets the culture.
- `string? ApplicationName { get; set; }` — Gets or sets the application name.
- `string? ApplicationVersion { get; set; }` — Gets or sets the application version (use it to override auto-detected value).
- `int MaximumIndirectExamples { get; set; }` — Gets or sets a value indicating how many examples from direct children to show in the help text.
- `bool ShowOptionDefaultValues { get; set; }` — Gets or sets a value indicating whether any default values for command options are shown in the help text.
- `bool TrimTrailingPeriod { get; set; }` — Gets or sets a value indicating whether a trailing period of a description is trimmed in the help text.
- `HelpProviderStyle? HelpProviderStyles { get; set; }` — Gets or sets the styles to used when rendering the help text.
- `IAnsiConsole? Console { get; set; }` — Gets or sets the `IAnsiConsole`.
- `ICommandInterceptor? Interceptor { get; set; }` — Gets or sets the `ICommandInterceptor` used to intercept settings before it's being sent to the command.
- `ITypeRegistrarFrontend Registrar { get; }` — Gets the type registrar.
- `CaseSensitivity CaseSensitivity { get; set; }` — Gets or sets case sensitivity.
- `bool StrictParsing { get; set; }` — Gets or sets a value indicating whether parsing is strict.
- `bool ConvertFlagsToRemainingArguments { get; set; }` — Gets or sets a value indicating whether flags found on the command line that would normally result in a `CommandParseException` being thrown during parsing with the message "Flags cannot be assigned a value." should instead be added to the remaining argument collection.
- `bool PropagateExceptions { get; set; }` — Gets or sets a value indicating whether exceptions should be propagated. Setting this to `true` will disable default Exception handling and any `ExceptionHandler`, if set.
- `int CancellationExitCode { get; set; }` — Gets or sets the value used as the application exit code when it's aborted through the `CancellationToken`. The default cancellation exit code is 130.
- `bool ValidateExamples { get; set; }` — Gets or sets a value indicating whether examples should be validated.
- `Func<Exception, ITypeResolver?, int>? ExceptionHandler { get; set; }` — Gets or sets a handler for Exceptions. This handler will not be called, if `PropagateExceptions` is set to `true`. The `ITypeResolver` argument will only be not-null, when the exception occurs during execution of a command. I.e. only when the resolver is available.

## `public interface ICommandArgument : ICommandParameter`

*cli* · `src/Spectre.Console.Cli/Help/ICommandArgument.cs`

Represents a command argument.

**Properties**

- `string Value { get; }` — Gets the value of the argument.
- `int Position { get; }` — Gets the position of the argument.

## `public interface ICommandConfigurator`

*cli* · `src/Spectre.Console.Cli/ICommandConfigurator.cs`

Represents a command configurator.

**Methods**

- `ICommandConfigurator WithExample(params string[] args)` — Adds an example of how to use the command.
- `ICommandConfigurator WithAlias(string name)` — Adds an alias (an alternative name) to the command being configured.
- `ICommandConfigurator WithDescription(string description)` — Sets the description of the command.
- `ICommandConfigurator WithData(object data)` — Sets data that will be passed to the command via the `CommandContext`.
- `ICommandConfigurator IsHidden()` — Marks the command as hidden. Hidden commands do not show up in help documentation or generated XML models.

## `public interface ICommandContainer`

*cli* · `src/Spectre.Console.Cli/Help/ICommandContainer.cs`

Represents a command container.

**Properties**

- `IReadOnlyList<string[]> Examples { get; }` — Gets all the examples for the container.
- `IReadOnlyList<ICommandInfo> Commands { get; }` — Gets all commands in the container.
- `ICommandInfo? DefaultCommand { get; }` — Gets the default command for the container.

## `public interface ICommandInfo : ICommandContainer`

*cli* · `src/Spectre.Console.Cli/Help/ICommandInfo.cs`

Represents an executable command.

**Properties**

- `string Name { get; }` — Gets the name of the command.
- `string? Description { get; }` — Gets the description of the command.
- `bool IsBranch { get; }` — Gets a value indicating whether the command is a branch.
- `bool IsDefaultCommand { get; }` — Gets a value indicating whether the command is the default command within its container.
- `bool IsHidden { get; }` — Gets a value indicating whether the command is hidden.
- `IReadOnlyList<ICommandParameter> Parameters { get; }` — Gets the parameters associated with the command.
- `ICommandInfo? Parent { get; }` — Gets the parent command, if any.

## `public interface ICommandInterceptor`

*cli* · `src/Spectre.Console.Cli/ICommandInterceptor.cs`

Represents a command settings interceptor that will intercept command settings before it's passed to a command.

**Methods**

- `void Intercept(CommandContext context, CommandSettings settings)` — Intercepts command information before it's passed to a command.
- `void InterceptResult(CommandContext context, CommandSettings settings, ref int result)` — Intercepts a command result before it's passed as the result.

## `public interface ICommandLimiter<out TSettings> : ICommand where TSettings : CommandSettings`

*cli* · `src/Spectre.Console.Cli/ICommandLimiterOfT.cs`

Represents a command limiter.

## `public interface ICommandModel : ICommandContainer`

*cli* · `src/Spectre.Console.Cli/Help/ICommandModel.cs`

Represents a command model.

**Properties**

- `string ApplicationName { get; }` — Gets the name of the application.
- `string? ApplicationVersion { get; }` — Gets the version of the application.

## `public interface ICommandOption : ICommandParameter`

*cli* · `src/Spectre.Console.Cli/Help/ICommandOption.cs`

Represents a command option.

**Properties**

- `IReadOnlyList<string> LongNames { get; }` — Gets the long names of the option.
- `IReadOnlyList<string> ShortNames { get; }` — Gets the short names of the option.
- `string? ValueName { get; }` — Gets the value name of the option, if applicable.
- `bool ValueIsOptional { get; }` — Gets a value indicating whether the option value is optional.

## `public interface ICommandParameter`

*cli* · `src/Spectre.Console.Cli/Help/ICommandParameter.cs`

Represents a command parameter.

**Properties**

- `bool IsFlag { get; }` — Gets a value indicating whether the parameter is a flag.
- `bool IsRequired { get; }` — Gets a value indicating whether the parameter is required.
- `string? Description { get; }` — Gets the description of the parameter.
- `DefaultValueAttribute? DefaultValue { get; }` — Gets the default value of the parameter, if specified.
- `bool IsHidden { get; }` — Gets a value indicating whether the parameter is hidden.

## `public interface ICommandParameterInfo`

*cli* · `src/Spectre.Console.Cli/ICommandParameterInfo.cs`

Represents a command parameter.

**Properties**

- `string PropertyName { get; }` — Gets the property name.
- `Type ParameterType { get; }` — Gets the parameter type.
- `string? Description { get; }` — Gets the description.

## `public interface IConfigurator`

*cli* · `src/Spectre.Console.Cli/IConfigurator.cs`

Represents a configurator.

**Properties**

- `ICommandAppSettings Settings { get; }` — Gets the command app settings.

**Methods**

- `IConfigurator SetHelpProvider(IHelpProvider helpProvider)` — Sets the help provider for the application.
- `IConfigurator SetHelpProvider<T>() where T : IHelpProvider` — Sets the help provider for the application.
- `IConfigurator AddExample(params string[] args)` — Adds an example of how to use the application.
- `ICommandConfigurator AddCommand<TCommand>(string name) where TCommand : class, ICommand` — Adds a command.
- `ICommandConfigurator AddDelegate<TSettings>(string name, Func<CommandContext, TSettings, CancellationToken, int> func) where TSettings : CommandSettings` — Adds a command that executes a delegate.
- `ICommandConfigurator AddAsyncDelegate<TSettings>(string name, Func<CommandContext, TSettings, CancellationToken, Task<int>> func) where TSettings : CommandSettings` — Adds a command that executes an async delegate.
- `IBranchConfigurator AddBranch<TSettings>(string name, Action<IConfigurator<TSettings>> action) where TSettings : CommandSettings` — Adds a command branch.

**Extension methods on this type** (call as `x.Method(...)`)

- `SetHelpProvider(IHelpProvider helpProvider) -> IConfigurator` — Sets the help provider for the application.
- `SetHelpProvider<T>() -> IConfigurator` — Sets the help provider for the application.
- `SetApplicationCulture(CultureInfo? culture) -> IConfigurator` — Sets the culture for the application.
- `SetApplicationName(string name) -> IConfigurator` — Sets the name of the application.
- `SetApplicationVersion(string version) -> IConfigurator` — Sets the version of the application.
- `UseAssemblyInformationalVersion() -> IConfigurator` — Uses the version retrieved from the `AssemblyInformationalVersionAttribute` as the application's version.
- `HideOptionDefaultValues() -> IConfigurator` — Hides the `DEFAULT` column that lists default values coming from the `DefaultValueAttribute` in the options help text.
- `ConfigureConsole(IAnsiConsole console) -> IConfigurator` — Configures the console.
- `UseStrictParsing() -> IConfigurator` — Sets the parsing mode to strict.
- `TrimTrailingPeriods(bool trimTrailingPeriods) -> IConfigurator` — Tells the help provider whether or not to trim trailing period.
- `PropagateExceptions() -> IConfigurator` — Tells the command line application to propagate all exceptions to the user.
- `CancellationExitCode(int exitCode) -> IConfigurator` — Tells the command line application to return the specified exit code when it's aborted through the `CancellationToken`. The default cancellation exit code is 130.
- `CaseSensitivity(CaseSensitivity sensitivity) -> IConfigurator` — Configures case sensitivity.
- `ValidateExamples() -> IConfigurator` — Tells the command line application to validate all examples before running the application.
- `SetInterceptor(ICommandInterceptor interceptor) -> IConfigurator` — Sets the command interceptor to be used.
- `AddBranch(string name, Action<IConfigurator<CommandSettings>> action) -> IBranchConfigurator` — Adds a command branch.
- `AddBranch<TSettings>(string name, Action<IConfigurator<TSettings>> action) -> IBranchConfigurator` — Adds a command branch.
- `AddDelegate(string name, Func<CommandContext, CancellationToken, int> func) -> ICommandConfigurator` — Adds a command without settings that executes a delegate.
- `AddAsyncDelegate(string name, Func<CommandContext, CancellationToken, Task<int>> func) -> ICommandConfigurator` — Adds a command without settings that executes an async delegate.
- `AddDelegate<TSettings>(string name, Func<CommandContext, CancellationToken, int> func) -> ICommandConfigurator` — Adds a command without settings that executes a delegate.
- `AddAsyncDelegate<TSettings>(string name, Func<CommandContext, CancellationToken, Task<int>> func) -> ICommandConfigurator` — Adds a command without settings that executes an async delegate.
- `SetExceptionHandler(Action<Exception, ITypeResolver?> exceptionHandler) -> IConfigurator` — Sets the ExceptionsHandler. Setting `ICommandAppSettings.ExceptionHandler` this way will use the default exit code of -1.
- `SetExceptionHandler(Func<Exception, ITypeResolver?, int>? exceptionHandler) -> IConfigurator` — Sets the ExceptionsHandler.
- `SafetyOff() -> IUnsafeConfigurator` — Gets an `IUnsafeConfigurator` that allows composition of commands without type safety.
- `SafetyOff<TSettings>() -> IUnsafeConfigurator` — Gets an `IUnsafeConfigurator` that allows composition of commands without type safety.

## `public interface IConfigurator<in TSettings> where TSettings : CommandSettings`

*cli* · `src/Spectre.Console.Cli/IConfiguratorOfT.cs`

Represents a configurator for specific settings.

**Methods**

- `void SetDescription(string description)` — Sets the description of the branch.
- `void AddExample(params string[] args)` — Adds an example of how to use the branch.
- `void SetDefaultCommand<TDefaultCommand>() where TDefaultCommand : class, ICommandLimiter<TSettings>` — Adds a default command.
- `void HideBranch()` — Marks the branch as hidden. Hidden branches do not show up in help documentation or generated XML models.
- `ICommandConfigurator AddCommand<TCommand>(string name) where TCommand : class, ICommandLimiter<TSettings>` — Adds a command.
- `ICommandConfigurator AddDelegate<TDerivedSettings>(string name, Func<CommandContext, TDerivedSettings, CancellationToken, int> func) where TDerivedSettings : TSettings` — Adds a command that executes a delegate.
- `ICommandConfigurator AddAsyncDelegate<TDerivedSettings>(string name, Func<CommandContext, TDerivedSettings, CancellationToken, Task<int>> func) where TDerivedSettings : TSettings` — Adds a command that executes an async delegate.
- `IBranchConfigurator AddBranch<TDerivedSettings>(string name, Action<IConfigurator<TDerivedSettings>> action) where TDerivedSettings : TSettings` — Adds a command branch.

**Extension methods on this type** (call as `x.Method(...)`)

- `SetHelpProvider(IHelpProvider helpProvider) -> IConfigurator` — Sets the help provider for the application.
- `SetHelpProvider<T>() -> IConfigurator` — Sets the help provider for the application.
- `SetApplicationCulture(CultureInfo? culture) -> IConfigurator` — Sets the culture for the application.
- `SetApplicationName(string name) -> IConfigurator` — Sets the name of the application.
- `SetApplicationVersion(string version) -> IConfigurator` — Sets the version of the application.
- `UseAssemblyInformationalVersion() -> IConfigurator` — Uses the version retrieved from the `AssemblyInformationalVersionAttribute` as the application's version.
- `HideOptionDefaultValues() -> IConfigurator` — Hides the `DEFAULT` column that lists default values coming from the `DefaultValueAttribute` in the options help text.
- `ConfigureConsole(IAnsiConsole console) -> IConfigurator` — Configures the console.
- `UseStrictParsing() -> IConfigurator` — Sets the parsing mode to strict.
- `TrimTrailingPeriods(bool trimTrailingPeriods) -> IConfigurator` — Tells the help provider whether or not to trim trailing period.
- `PropagateExceptions() -> IConfigurator` — Tells the command line application to propagate all exceptions to the user.
- `CancellationExitCode(int exitCode) -> IConfigurator` — Tells the command line application to return the specified exit code when it's aborted through the `CancellationToken`. The default cancellation exit code is 130.
- `CaseSensitivity(CaseSensitivity sensitivity) -> IConfigurator` — Configures case sensitivity.
- `ValidateExamples() -> IConfigurator` — Tells the command line application to validate all examples before running the application.
- `SetInterceptor(ICommandInterceptor interceptor) -> IConfigurator` — Sets the command interceptor to be used.
- `AddBranch(string name, Action<IConfigurator<CommandSettings>> action) -> IBranchConfigurator` — Adds a command branch.
- `AddBranch<TSettings>(string name, Action<IConfigurator<TSettings>> action) -> IBranchConfigurator` — Adds a command branch.
- `AddDelegate(string name, Func<CommandContext, CancellationToken, int> func) -> ICommandConfigurator` — Adds a command without settings that executes a delegate.
- `AddAsyncDelegate(string name, Func<CommandContext, CancellationToken, Task<int>> func) -> ICommandConfigurator` — Adds a command without settings that executes an async delegate.
- `AddDelegate<TSettings>(string name, Func<CommandContext, CancellationToken, int> func) -> ICommandConfigurator` — Adds a command without settings that executes a delegate.
- `AddAsyncDelegate<TSettings>(string name, Func<CommandContext, CancellationToken, Task<int>> func) -> ICommandConfigurator` — Adds a command without settings that executes an async delegate.
- `SetExceptionHandler(Action<Exception, ITypeResolver?> exceptionHandler) -> IConfigurator` — Sets the ExceptionsHandler. Setting `ICommandAppSettings.ExceptionHandler` this way will use the default exit code of -1.
- `SetExceptionHandler(Func<Exception, ITypeResolver?, int>? exceptionHandler) -> IConfigurator` — Sets the ExceptionsHandler.
- `SafetyOff() -> IUnsafeConfigurator` — Gets an `IUnsafeConfigurator` that allows composition of commands without type safety.
- `SafetyOff<TSettings>() -> IUnsafeConfigurator` — Gets an `IUnsafeConfigurator` that allows composition of commands without type safety.

## `public interface IFlagValue`

*cli* · `src/Spectre.Console.Cli/IFlagValue.cs`

Represents a flag with an optional value.

**Properties**

- `bool IsSet { get; set; }` — Gets or sets a value indicating whether the flag was set or not.
- `Type Type { get; }` — Gets the flag's element type.
- `object? Value { get; set; }` — Gets or sets the flag's value.

## `public interface IHelpProvider`

*cli* · `src/Spectre.Console.Cli/Help/IHelpProvider.cs`

The help provider interface for Spectre.Console.

**Methods**

- `IEnumerable<IRenderable> Write(ICommandModel model, ICommandInfo? command)` — Writes help information for the application.

## `public interface IRemainingArguments`

*cli* · `src/Spectre.Console.Cli/IRemainingArguments.cs`

Represents the remaining arguments.

**Properties**

- `ILookup<string, string?> Parsed { get; }` — Gets the parsed remaining arguments.
- `IReadOnlyList<string> Raw { get; }` — Gets the raw, non-parsed remaining arguments. This is normally everything after the `--` delimiter.

## `public interface ITypeRegistrar`

*cli* · `src/Spectre.Console.Cli/ITypeRegistrar.cs`

Represents a type registrar.

**Methods**

- `void Register(Type service, Type implementation)` — Registers the specified service.
- `void RegisterInstance(Type service, object implementation)` — Registers the specified instance.
- `void RegisterLazy(Type service, Func<object> factory)` — Registers the specified instance lazily.
- `ITypeResolver Build()` — Builds the type resolver representing the registrations specified in the current instance.

## `public interface ITypeRegistrarFrontend`

*cli* · `src/Spectre.Console.Cli/ITypeRegistrarFrontend.cs`

Represents a user-friendly frontend for a `ITypeRegistrar`.

**Methods**

- `void Register<TService, TImplementation>() where TImplementation : TService` — Registers the type with the type registrar as a singleton.
- `void RegisterInstance<TImplementation>(TImplementation instance)` — Registers the specified instance with the type registrar as a singleton.
- `void RegisterInstance<TService, TImplementation>(TImplementation instance) where TImplementation : TService` — Registers the specified instance with the type registrar as a singleton.

## `public interface ITypeResolver`

*cli* · `src/Spectre.Console.Cli/ITypeResolver.cs`

Represents a type resolver.

**Methods**

- `object? Resolve(Type? type)` — Resolves an instance of the specified type.

## `public interface IUnsafeBranchConfigurator : IUnsafeConfigurator`

*cli* · `src/Spectre.Console.Cli/Unsafe/IUnsafeBranchConfigurator.cs`

Represents an unsafe configurator for a branch.

**Methods**

- `void SetDescription(string description)` — Sets the description of the branch.
- `void AddExample(string[] args)` — Adds an example of how to use the branch.

**Extension methods on this type** (call as `x.Method(...)`)

- `SafetyOn<TSettings>() -> IConfigurator<TSettings>` — Converts an `IUnsafeConfigurator` to a configurator with type safety.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IUnsafeConfigurator`: `SafetyOn`

## `public interface IUnsafeConfigurator`

*cli* · `src/Spectre.Console.Cli/Unsafe/IUnsafeConfigurator.cs`

Represents an unsafe configurator.

**Methods**

- `ICommandConfigurator AddCommand(string name, Type command)` — Adds a command.
- `IBranchConfigurator AddBranch(string name, Type settings, Action<IUnsafeBranchConfigurator> action)` — Adds a command branch.

**Extension methods on this type** (call as `x.Method(...)`)

- `SafetyOn() -> IConfigurator` — Converts an `IUnsafeConfigurator` to a configurator with type safety.

## `public sealed class OptionStyle`

*cli* · `src/Spectre.Console.Cli/Help/HelpProviderStyles.cs`

Defines styles for specifying options or flags in a command.

**Properties**

- `Style? Header { get; set; }` — Gets or sets the style for the header in the options.
- `Style? DefaultValueHeader { get; set; }` — Gets or sets the style for the header of default values in the options.
- `Style? DefaultValue { get; set; }` — Gets or sets the style for default values in the options.
- `Style? RequiredOption { get; set; }` — Gets or sets the style for required options.
- `Style? RequiredOptionValue { get; set; }` — Gets or sets the style for required option values.
- `Style? OptionalOptionValue { get; set; }` — Gets or sets the style for optional options.

## `public abstract class PairDeconstructor<TKey, TValue> : IPairDeconstructor`

*cli* · `src/Spectre.Console.Cli/PairDeconstructor.cs`

Base class for a pair deconstructor.

**Methods**

- `protected abstract (TKey Key, TValue Value) Deconstruct(string? value)` — Deconstructs the provided `string` into a pair.

## `public sealed class PairDeconstructorAttribute : Attribute`

*cli* · `src/Spectre.Console.Cli/Annotations/PairDeconstructorAttribute.cs`

Specifies what type to use as a pair deconstructor for the property this attribute is bound to.

**Constructors**

- `PairDeconstructorAttribute(Type type)` — Initializes a new instance of the `PairDeconstructorAttribute` class.

**Properties**

- `Type Type { get; }` — Gets the `string` that represents the type of the pair deconstructor class to use for data conversion for the object this attribute is bound to.

## `public abstract class ParameterValidationAttribute : Attribute`

*cli* · `src/Spectre.Console.Cli/Annotations/ParameterValidationAttribute.cs`

A base class attribute used for parameter validation.

**Constructors**

- `protected ParameterValidationAttribute(string errorMessage)` — Initializes a new instance of the `ParameterValidationAttribute` class.

**Properties**

- `string ErrorMessage { get; }` — Gets the validation error message.

**Methods**

- `abstract ValidationResult Validate(CommandParameterContext context)` — Validates the parameter value.

## `public abstract class ParameterValueProviderAttribute : Attribute`

*cli* · `src/Spectre.Console.Cli/Annotations/ParameterValueProviderAttribute.cs`

A base class attribute used for parameter completion.

**Methods**

- `abstract bool TryGetValue(CommandParameterContext context, out object? result)` — Gets a value for the parameter.

## `public sealed class UsageStyle`

*cli* · `src/Spectre.Console.Cli/Help/HelpProviderStyles.cs`

Defines styles for specifying the usage format of a command.

**Properties**

- `Style? Header { get; set; }` — Gets or sets the style for the header in the usage.
- `Style? CurrentCommand { get; set; }` — Gets or sets the style for the current command in the usage.
- `Style? Command { get; set; }` — Gets or sets the style for general commands in the usage.
- `Style? Options { get; set; }` — Gets or sets the style for options in the usage.
- `Style? RequiredArgument { get; set; }` — Gets or sets the style for required arguments in the usage.
- `Style? OptionalArgument { get; set; }` — Gets or sets the style for optional arguments in the usage.

## `public enum CaseSensitivity`

*cli* · `src/Spectre.Console.Cli/CaseSensitivity.cs`

Represents case sensitivity.

**Values**

- `None = 0` — Nothing is case-sensitive.
- `LongOptions = 1` — Long options are case-sensitive.
- `Commands = 2` — Commands are case-sensitive.
- `All = LongOptions | Commands` — Everything is case-sensitive.

