# cli-testing — API (generated from source)

## `public sealed class CallbackCommandInterceptor : ICommandInterceptor`

*cli-testing* · `src/Spectre.Console.Cli.Testing/CallbackCommandInterceptor.cs`

A `ICommandInterceptor` that triggers a callback when invoked.

**Constructors**

- `CallbackCommandInterceptor(Action<CommandContext, CommandSettings> callback)` — Initializes a new instance of the `CallbackCommandInterceptor` class.

**Methods**

- `void Intercept(CommandContext context, CommandSettings settings)` — Intercepts command information before it's passed to a command.
- `void InterceptResult(CommandContext context, CommandSettings settings, ref int result)` — Intercepts a command result before it's passed as the result.

## `public sealed class CommandAppFailure`

*cli-testing* · `src/Spectre.Console.Cli.Testing/CommandAppFailure.cs`

Represents a `CommandApp` runtime failure.

**Properties**

- `Exception Exception { get; }` — Gets the exception that was thrown.
- `string Output { get; }` — Gets the console output.

## `public sealed class CommandAppResult`

*cli-testing* · `src/Spectre.Console.Cli.Testing/CommandAppResult.cs`

Represents the result of a completed `CommandApp` run.

**Properties**

- `int ExitCode { get; }` — Gets the exit code.
- `string Output { get; }` — Gets the console output.
- `CommandContext? Context { get; }` — Gets the command context.
- `CommandSettings? Settings { get; }` — Gets the command settings.

## `public sealed class CommandAppTester`

*cli-testing* · `src/Spectre.Console.Cli.Testing/CommandAppTester.cs`

A `CommandApp` test harness.

**Constructors**

- `CommandAppTester( ITypeRegistrar? registrar = null, CommandAppTesterSettings? settings = null, TestConsole? console = null)` — Initializes a new instance of the `CommandAppTester` class.
- `CommandAppTester(CommandAppTesterSettings settings)` — Initializes a new instance of the `CommandAppTester` class.

**Properties**

- `TestConsole Console { get; }` — Gets the test console used by both the CommandAppTester and CommandApp.
- `ITypeRegistrar? Registrar { get; set; }` — Gets or sets the Registrar to use in the CommandApp.
- `CommandAppTesterSettings TestSettings { get; set; }` — Gets or sets the settings for the `CommandAppTester`.

**Methods**

- `void SetDefaultCommand<T>(string? description = null, object? data = null) where T : class, ICommand` — Sets the default command.
- `void Configure(Action<IConfigurator> action)` — Configures the command application.
- `CommandAppFailure RunAndCatch<T>(params string[] args) where T : Exception` — Runs the command application and expects an exception of a specific type to be thrown.
- `CommandAppResult Run(params string[] args)` — Runs the command application.
- `async Task<CommandAppResult> RunAsync(string[]? args = null, CancellationToken cancellationToken = default)` — Runs the command application asynchronously.

## `public sealed class CommandAppTesterSettings`

*cli-testing* · `src/Spectre.Console.Cli.Testing/CommandAppTesterSettings.cs`

Represents the configuration settings for the `CommandAppTester` class.

**Properties**

- `bool TrimConsoleOutput { get; set; }` = `true` — Gets or sets a value indicating whether whitespace should be trimmed from the console output.

## `public sealed class FakeTypeRegistrar : ITypeRegistrar`

*cli-testing* · `src/Spectre.Console.Cli.Testing/FakeTypeRegistrar.cs`

A fake type registrar suitable for testing.

**Constructors**

- `FakeTypeRegistrar()` — Initializes a new instance of the `FakeTypeRegistrar` class.

**Properties**

- `Dictionary<Type, List<Type>> Registrations { get; }` — Gets all registrations.
- `Dictionary<Type, List<object>> Instances { get; }` — Gets all singleton registrations.

**Methods**

- `void Register(Type service, Type implementation)` — Registers the specified service.
- `void RegisterInstance(Type service, object implementation)` — Registers the specified instance.
- `void RegisterLazy(Type service, Func<object> factory)` — Registers the specified instance lazily.
- `ITypeResolver Build()` — Builds the type resolver representing the registrations specified in the current instance.

## `public sealed class FakeTypeResolver : ITypeResolver`

*cli-testing* · `src/Spectre.Console.Cli.Testing/FakeTypeResolver.cs`

A fake type resolver suitable for testing.

**Constructors**

- `FakeTypeResolver( Dictionary<Type, List<Type>> registrations, Dictionary<Type, List<object>> instances)` — Initializes a new instance of the `FakeTypeResolver` class.

**Methods**

- `object? Resolve(Type? type)` — Resolves an instance of the specified type.

## `public sealed class TypeRegistrarBaseTests`

*cli-testing* · `src/Spectre.Console.Cli.Testing/Extensibility/TypeRegistrarBaseTests.cs`

This is a utility class for implementors of `ITypeRegistrar` and corresponding `ITypeResolver`.

**Constructors**

- `TypeRegistrarBaseTests(Func<ITypeRegistrar> registrarFactory)` — Initializes a new instance of the `TypeRegistrarBaseTests` class.

**Methods**

- `void RunAllTests()` — Runs all tests.

## `public sealed class TypeRegistrarBaseTests.TestFailedException : Exception`

*cli-testing* · `src/Spectre.Console.Cli.Testing/Extensibility/TypeRegistrarBaseTests.cs`

Exception, to be raised when a test fails.

**Constructors**

- `TestFailedException(string message) : base(message)`
- `TestFailedException(string message, Exception inner) : base(message, inner)`

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `Exception`: `GetRenderable`

