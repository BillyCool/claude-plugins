# console — API (generated from source)

## `public static partial class AnsiConsole`

*core* · `src/Spectre.Console/AnsiConsole.cs`

A console capable of writing ANSI escape sequences.

**Properties**

- `static IAnsiConsole Console { get; set; }` — Gets or sets the underlying `IAnsiConsole`.
- `static IAnsiConsoleCursor Cursor { get; }` — Gets the `IAnsiConsoleCursor`.
- `static Profile Profile { get; }` — Gets the console profile.
- `static Color Foreground { get; set; }` — Gets or sets the foreground color.
- `static Color Background { get; set; }` — Gets or sets the background color.
- `static Decoration Decoration { get; set; }` — Gets or sets the text decoration.

**Methods**

- `static IAnsiConsole Create(AnsiConsoleSettings settings)` — Creates a new `IAnsiConsole` instance from the provided settings.
- `static void Clear()` — Clears the console.
- `static void WriteException(Exception exception, ExceptionFormats format = ExceptionFormats.Default)` — Writes an exception to the console.
- `static void WriteException(Exception exception, ExceptionSettings settings)` — Writes an exception to the console.
- `static LiveDisplay Live(IRenderable target)` — Creates a new `LiveDisplay` instance.
- `static void Markup(string value)` — Writes the specified markup to the console.
- `static void Markup(string format, params object[] args)` — Writes the specified markup to the console.
- `static void MarkupInterpolated(FormattableString value)` — Writes the specified markup to the console. All interpolation holes which contain a string are automatically escaped.
- `static void Markup(IFormatProvider provider, string format, params object[] args)` — Writes the specified markup to the console.
- `static void MarkupInterpolated(IFormatProvider provider, FormattableString value)` — Writes the specified markup to the console. All interpolation holes which contain a string are automatically escaped.
- `static void MarkupLine(string value)` — Writes the specified markup, followed by the current line terminator, to the console.
- `static void MarkupLine(string format, params object[] args)` — Writes the specified markup, followed by the current line terminator, to the console.
- `static void MarkupLineInterpolated(FormattableString value)` — Writes the specified markup, followed by the current line terminator, to the console. All interpolation holes which contain a string are automatically escaped.
- `static void MarkupLine(IFormatProvider provider, string format, params object[] args)` — Writes the specified markup, followed by the current line terminator, to the console.
- `static void MarkupLineInterpolated(IFormatProvider provider, FormattableString value)` — Writes the specified markup, followed by the current line terminator, to the console. All interpolation holes which contain a string are automatically escaped.
- `static Progress Progress()` — Creates a new `Progress` instance.
- `static Status Status()` — Creates a new `Status` instance.
- `static T Prompt<T>(IPrompt<T> prompt)` — Displays a prompt to the user.
- `static Task<T> PromptAsync<T>(IPrompt<T> prompt, CancellationToken cancellationToken = default)` — Displays a prompt to the user.
- `static T Ask<T>(string prompt)` — Displays a prompt to the user.
- `static Task<T> AskAsync<T>(string prompt, CancellationToken cancellationToken = default)` — Displays a prompt to the user.
- `static T Ask<T>(string prompt, T defaultValue)` — Displays a prompt to the user with a given default.
- `static Task<T> AskAsync<T>(string prompt, T defaultValue, CancellationToken cancellationToken = default)` — Displays a prompt to the user with a given default.
- `static bool Confirm(string prompt, bool defaultValue = true)` — Displays a prompt with two choices, yes or no.
- `static Task<bool> ConfirmAsync(string prompt, bool defaultValue = true, CancellationToken cancellationToken = default)` — Displays a prompt with two choices, yes or no.
- `static void Record()` — Starts recording the console output.
- `static string ExportText()` — Exports all recorded console output as text.
- `static string ExportHtml()` — Exports all recorded console output as HTML text.
- `static string ExportCustom(IAnsiConsoleEncoder encoder)` — Exports all recorded console output using a custom encoder.
- `static void AlternateScreen(Action action)` — Switches to an alternate screen buffer if the terminal supports it.
- `static void Reset()` — Resets colors and text decorations.
- `static void ResetDecoration()` — Resets the current applied text decorations.
- `static void ResetColors()` — Resets the current applied foreground and background colors.
- `static void Write(IRenderable renderable)` — Renders the specified `IRenderable` to the console.
- `static void Write(string value)` — Writes the specified string value to the console.
- `static void Write(int value)` — Writes the text representation of the specified 32-bit signed integer value to the console.
- `static void Write(IFormatProvider provider, int value)` — Writes the text representation of the specified 32-bit signed integer value to the console.
- `static void Write(uint value)` — Writes the text representation of the specified 32-bit unsigned integer value to the console.
- `static void Write(IFormatProvider provider, uint value)` — Writes the text representation of the specified 32-bit unsigned integer value to the console.
- `static void Write(long value)` — Writes the text representation of the specified 64-bit signed integer value to the console.
- `static void Write(IFormatProvider provider, long value)` — Writes the text representation of the specified 64-bit signed integer value to the console.
- `static void Write(ulong value)` — Writes the text representation of the specified 64-bit unsigned integer value to the console.
- `static void Write(IFormatProvider provider, ulong value)` — Writes the text representation of the specified 64-bit unsigned integer value to the console.
- `static void Write(float value)` — Writes the text representation of the specified single-precision floating-point value to the console.
- `static void Write(IFormatProvider provider, float value)` — Writes the text representation of the specified single-precision floating-point value to the console.
- `static void Write(double value)` — Writes the text representation of the specified double-precision floating-point value to the console.
- `static void Write(IFormatProvider provider, double value)` — Writes the text representation of the specified double-precision floating-point value to the console.
- `static void Write(decimal value)` — Writes the text representation of the specified decimal value, to the console.
- `static void Write(IFormatProvider provider, decimal value)` — Writes the text representation of the specified decimal value, to the console.
- `static void Write(bool value)` — Writes the text representation of the specified boolean value to the console.
- `static void Write(IFormatProvider provider, bool value)` — Writes the text representation of the specified boolean value to the console.
- `static void Write(char value)` — Writes the specified Unicode character to the console.
- `static void Write(IFormatProvider provider, char value)` — Writes the specified Unicode character to the console.
- `static void Write(char[] value)` — Writes the specified array of Unicode characters to the console.
- `static void Write(IFormatProvider provider, char[] value)` — Writes the specified array of Unicode characters to the console.
- `static void Write(string format, params object[] args)` — Writes the text representation of the specified array of objects, to the console using the specified format information.
- `static void Write(IFormatProvider provider, string format, params object[] args)` — Writes the text representation of the specified array of objects, to the console using the specified format information.
- `static void WriteLine()` — Writes an empty line to the console.
- `static void WriteLine(string value)` — Writes the specified string value, followed by the current line terminator, to the console.
- `static void WriteLine(int value)` — Writes the text representation of the specified 32-bit signed integer value, followed by the current line terminator, to the console.
- `static void WriteLine(IFormatProvider provider, int value)` — Writes the text representation of the specified 32-bit signed integer value, followed by the current line terminator, to the console.
- `static void WriteLine(uint value)` — Writes the text representation of the specified 32-bit unsigned integer value, followed by the current line terminator, to the console.
- `static void WriteLine(IFormatProvider provider, uint value)` — Writes the text representation of the specified 32-bit unsigned integer value, followed by the current line terminator, to the console.
- `static void WriteLine(long value)` — Writes the text representation of the specified 64-bit signed integer value, followed by the current line terminator, to the console.
- `static void WriteLine(IFormatProvider provider, long value)` — Writes the text representation of the specified 64-bit signed integer value, followed by the current line terminator, to the console.
- `static void WriteLine(ulong value)` — Writes the text representation of the specified 64-bit unsigned integer value, followed by the current line terminator, to the console.
- `static void WriteLine(IFormatProvider provider, ulong value)` — Writes the text representation of the specified 64-bit unsigned integer value, followed by the current line terminator, to the console.
- `static void WriteLine(float value)` — Writes the text representation of the specified single-precision floating-point value, followed by the current line terminator, to the console.
- `static void WriteLine(IFormatProvider provider, float value)` — Writes the text representation of the specified single-precision floating-point value, followed by the current line terminator, to the console.
- `static void WriteLine(double value)` — Writes the text representation of the specified double-precision floating-point value, followed by the current line terminator, to the console.
- `static void WriteLine(IFormatProvider provider, double value)` — Writes the text representation of the specified double-precision floating-point value, followed by the current line terminator, to the console.
- `static void WriteLine(decimal value)` — Writes the text representation of the specified decimal value, followed by the current line terminator, to the console.
- `static void WriteLine(IFormatProvider provider, decimal value)` — Writes the text representation of the specified decimal value, followed by the current line terminator, to the console.
- `static void WriteLine(bool value)` — Writes the text representation of the specified boolean value, followed by the current line terminator, to the console.
- `static void WriteLine(IFormatProvider provider, bool value)` — Writes the text representation of the specified boolean value, followed by the current line terminator, to the console.
- `static void WriteLine(char value)` — Writes the specified Unicode character, followed by the current line terminator, value to the console.
- `static void WriteLine(IFormatProvider provider, char value)` — Writes the specified Unicode character, followed by the current line terminator, value to the console.
- `static void WriteLine(char[] value)` — Writes the specified array of Unicode characters, followed by the current line terminator, value to the console.
- `static void WriteLine(IFormatProvider provider, char[] value)` — Writes the specified array of Unicode characters, followed by the current line terminator, value to the console.
- `static void WriteLine(string format, params object[] args)` — Writes the text representation of the specified array of objects, followed by the current line terminator, to the console using the specified format information.
- `static void WriteLine(IFormatProvider provider, string format, params object[] args)` — Writes the text representation of the specified array of objects, followed by the current line terminator, to the console using the specified format information.

## `public sealed class AnsiConsoleOutput : IAnsiConsoleOutput`

*core* · `src/Spectre.Console/AnsiConsoleOutput.cs`

Represents console output.

**Constructors**

- `AnsiConsoleOutput(TextWriter writer)` — Initializes a new instance of the `AnsiConsoleOutput` class.

**Properties**

- `TextWriter Writer { get; }` — Gets the `TextWriter` used to write to the output.
- `bool IsTerminal { get; }` — Gets a value indicating whether or not the output is a terminal.
- `int Width { get; }` — Gets the output width.
- `int Height { get; }` — Gets the output height.

**Methods**

- `void SetEncoding(Encoding encoding)` — Sets the output encoding.

## `public sealed class AnsiConsoleSettings`

*core* · `src/Spectre.Console/AnsiConsoleSettings.cs`

Settings used when building a `IAnsiConsole`.

**Constructors**

- `AnsiConsoleSettings()` — Initializes a new instance of the `AnsiConsoleSettings` class.

**Properties**

- `AnsiSupport Ansi { get; set; }` — Gets or sets a value indicating whether or not ANSI escape sequences are supported.
- `ColorSystemSupport ColorSystem { get; set; }` = `ColorSystemSupport.Detect` — Gets or sets the color system to use.
- `IAnsiConsoleOutput? Out { get; set; }` — Gets or sets the out buffer.
- `InteractionSupport Interactive { get; set; }` — Gets or sets a value indicating whether or not the terminal is interactive or not.
- `IExclusivityMode? ExclusivityMode { get; set; }` — Gets or sets the exclusivity mode.
- `ProfileEnrichment Enrichment { get; set; }` — Gets or sets the profile enrichments settings.
- `Dictionary<string, string>? EnvironmentVariables { get; set; }` — Gets or sets the environment variables. If not value is provided the default environment variables will be used.

## `public abstract partial class BoxBorder`

*core* · `src/Spectre.Console/BoxBorder.cs`

Represents a border.

**Properties**

- `virtual BoxBorder? SafeBorder { get; }` — Gets the safe border for this border or `null` if none exist.
- `static BoxBorder None { get; }` = `new NoBoxBorder()` — Gets an invisible border.
- `static BoxBorder Ascii { get; }` = `new AsciiBoxBorder()` — Gets an ASCII border.
- `static BoxBorder Double { get; }` = `new DoubleBoxBorder()` — Gets a double border.
- `static BoxBorder Heavy { get; }` = `new HeavyBoxBorder()` — Gets a heavy border.
- `static BoxBorder Rounded { get; }` = `new RoundedBoxBorder()` — Gets a rounded border.
- `static BoxBorder Square { get; }` = `new SquareBoxBorder()` — Gets a square border.
- `static BoxBorder HeavyHorizontal { get; }` = `new HeavyHorizontalBoxBorder()` — Gets a border with heavy horizontal edges and light vertical edges.
- `static BoxBorder HeavyVertical { get; }` = `new HeavyVerticalBoxBorder()` — Gets a border with heavy vertical edges and light horizontal edges.
- `static BoxBorder DoubleHorizontal { get; }` = `new DoubleHorizontalBoxBorder()` — Gets a border with double horizontal edges and single vertical edges.
- `static BoxBorder DoubleVertical { get; }` = `new DoubleVerticalBoxBorder()` — Gets a border with double vertical edges and single horizontal edges.
- `static BoxBorder Dashed { get; }` = `new DashedBoxBorder()` — Gets a dashed border with square corners.
- `static BoxBorder RoundedDashed { get; }` = `new RoundedDashedBoxBorder()` — Gets a dashed border with rounded corners.
- `static BoxBorder HeavyDashed { get; }` = `new HeavyDashedBoxBorder()` — Gets a heavy dashed border.
- `static BoxBorder Dotted { get; }` = `new DottedBoxBorder()` — Gets a dotted border with square corners.
- `static BoxBorder RoundedDotted { get; }` = `new RoundedDottedBoxBorder()` — Gets a dotted border with rounded corners.
- `static BoxBorder HeavyDotted { get; }` = `new HeavyDottedBoxBorder()` — Gets a heavy dotted border.
- `static BoxBorder DashedWide { get; }` = `new DashedWideBoxBorder()` — Gets a wide-dashed border with square corners.
- `static BoxBorder RoundedDashedWide { get; }` = `new RoundedDashedWideBoxBorder()` — Gets a wide-dashed border with rounded corners.
- `static BoxBorder HeavyDashedWide { get; }` = `new HeavyDashedWideBoxBorder()` — Gets a heavy wide-dashed border.
- `static BoxBorder Near { get; }` = `new NearBoxBorder()` — Gets a "near" border that hugs the content using thin block elements.
- `static BoxBorder Beveled { get; }` = `new BeveledBoxBorder()` — Gets a beveled border using thin block edges and diagonal corners.
- `static BoxBorder McGuganHorizontal { get; }` = `new McGuganHorizontalBoxBorder()` — Gets the horizontal variant of the McGugan border.
- `static BoxBorder McGuganVertical { get; }` = `new McGuganVerticalBoxBorder()` — Gets the vertical variant of the McGugan border.

**Methods**

- `abstract string GetPart(BoxBorderPart part)` — Gets the string representation of the specified border part.

**Extension methods on this type** (call as `x.Method(...)`)

- `GetSafeBorder(bool safe) -> BoxBorder` — Gets the safe border for a border.

## `public sealed class Capabilities : AnsiCapabilities, IReadOnlyCapabilities`

*core* · `src/Spectre.Console/Capabilities.cs`

Represents terminal capabilities.

**Properties**

- `bool Legacy { get; set; }` — Gets or sets a value indicating whether or not this is a legacy console (cmd.exe) on an OS prior to Windows 10.
- `bool Interactive { get; set; }` — Gets or sets a value indicating whether or not the console supports interaction.
- `bool Unicode { get; set; }` — Gets or sets a value indicating whether or not the console supports Unicode.

**Methods**

- `static Capabilities Create(TextWriter writer, AnsiConsoleSettings settings, out Encoding encoding)` — Creates a `Capabilities` instance from the provided arguments.

## `public static partial class Emoji`

*core* · `src/Spectre.Console/Emoji.cs`

Utility for working with emojis.

**Methods**

- `static void Remap(string tag, string emoji)` — Remaps a specific emoji tag with a new emoji.
- `static string Replace(string value)` — Replaces emoji markup with corresponding unicode characters.

## `public static class Emoji.Known`

*core* · `src/Spectre.Console/Generated/Spectre.Console.SourceGenerator/Spectre.Console.SourceGenerator.Emojis.EmojiGenerator/Emoji.Generated.g.cs`

Contains well-known emojis.

**Fields / constants**

1429 members like `const string Abacus`: `Abacus`, `AbButtonBloodType`, `AButtonBloodType`, `Accordion`, `AdhesiveBandage`, `AdmissionTickets`, `AerialTramway`, `Airplane`, `AirplaneArrival`, `AirplaneDeparture`, `AlarmClock`, `Alembic`, `Alien`, `AlienMonster`, `Ambulance`, `AmericanFootball`, `Amphora`, `AnatomicalHeart`, `Anchor`, `AngerSymbol`, `AngryFace`, `AngryFaceWithHorns`, `AnguishedFace`, `Ant`, `AntennaBars`, `AnxiousFaceWithSweat`, `Aquarius`, `Aries`, `ArticulatedLorry`, `ArtistPalette`, `AstonishedFace`, `AtmSign`, `AtomSymbol`, `Automobile`, `AutoRickshaw`, `Avocado`, `Axe`, `Baby`, `BabyAngel`, `BabyBottle`, `BabyChick`, `BabySymbol`, `BackArrow`, `BackhandIndexPointingDown`, `BackhandIndexPointingLeft`, `BackhandIndexPointingRight`, `BackhandIndexPointingUp`, `Backpack`, `Bacon`, `Badger`, `Badminton`, `Bagel`, `BaggageClaim`, `BaguetteBread`, `BalanceScale`, `Bald`, `BalletShoes`, `Balloon`, `BallotBoxWithBallot`, `Banana`, `Banjo`, `Bank`, `BarberPole`, `BarChart`, `Baseball`, `Basket`, `Basketball`, `Bat`, `Bathtub`, `Battery`, `BButtonBloodType`, `BeachWithUmbrella`, `BeamingFaceWithSmilingEyes`, `Beans`, `Bear`, `BeatingHeart`, `Beaver`, `Bed`, `BeerMug`, `Beetle`, `Bell`, `BellhopBell`, `BellPepper`, `BellWithSlash`, `BentoBox`, `BeverageBox`, `Bicycle`, `Bikini`, `BilledCap`, `Biohazard`, `Bird`, `BirthdayCake`, `Bison`, `BitingLip`, `BlackCircle`, `BlackFlag`, `BlackHeart`, `BlackLargeSquare`, `BlackMediumSmallSquare`, `BlackMediumSquare`, `BlackNib`, `BlackSmallSquare`, `BlackSquareButton`, `Blossom`, `Blowfish`, `Blueberries`, `BlueBook`, `BlueCircle`, `BlueHeart`, `BlueSquare`, `Boar`, `Bomb`, `Bone`, `Bookmark`, `BookmarkTabs`, `Books`, `Boomerang`, `BottleWithPoppingCork`, `Bouquet`, `BowAndArrow`, `Bowling`, `BowlWithSpoon`, `BoxingGlove`, `Boy`, `Brain`, `Bread`, `BreastFeeding`, `Brick`, `BridgeAtNight`, `Briefcase`, `Briefs`, `BrightButton`, `Broccoli`, `BrokenHeart`, `Broom`, `BrownCircle`, `BrownHeart`, `BrownSquare`, `Bubbles`, `BubbleTea`, `Bucket`, `Bug`, `BuildingConstruction`, `BulletTrain`, `Bullseye`, `Burrito`, `Bus`, `BusStop`, `BustInSilhouette`, `BustsInSilhouette`, `Butter`, `Butterfly`, `Cactus`, `Calendar`, `CallMeHand`, `Camel`, `Camera`, `CameraWithFlash`, `Camping`, `Cancer`, `Candle`, `Candy`, `CannedFood`, `Canoe`, `Capricorn`, `CardFileBox`, `CardIndex`, `CardIndexDividers`, `CarouselHorse`, `CarpentrySaw`, `CarpStreamer`, `Carrot`, `Castle`, `Cat`, `CatFace`, `CatWithTearsOfJoy`, `CatWithWrySmile`, `Chains`, `Chair`, `ChartDecreasing`, `ChartIncreasing`, `ChartIncreasingWithYen`, `CheckBoxWithCheck`, `CheckMark`, `CheckMarkButton`, `CheeseWedge`, `ChequeredFlag`, `Cherries`, `CherryBlossom`, `ChessPawn`, `Chestnut`, `Chicken`, `Child`, `ChildrenCrossing`, `Chipmunk`, `ChocolateBar`, `Chopsticks`, `ChristmasTree`, `Church`, `Cigarette`, `Cinema`, `CircledM`, `CircusTent`, `Cityscape`, `CityscapeAtDusk`, `Clamp`, `ClapperBoard`, `ClappingHands`, `ClassicalBuilding`, `ClButton`, `ClinkingBeerMugs`, `ClinkingGlasses`, `Clipboard`, `ClockwiseVerticalArrows`, `ClosedBook`, `ClosedMailboxWithLoweredFlag`, `ClosedMailboxWithRaisedFlag`, `ClosedUmbrella`, `Cloud`, `CloudWithLightning`, `CloudWithLightningAndRain`, `CloudWithRain`, `CloudWithSnow`, `ClownFace`, `ClubSuit`, `ClutchBag`, `Coat`, `Cockroach`, `CocktailGlass`, `Coconut`, `Coffin`, `Coin`, `ColdFace`, `Collision`, `Comet`, `Compass`, `ComputerDisk`, `ComputerMouse`, `ConfettiBall`, `ConfoundedFace`, `ConfusedFace`, `Construction`, `ConstructionWorker`, `ControlKnobs`, `ConvenienceStore`, `CookedRice`, `Cookie`, `Cooking`, `CoolButton`, `Copyright`, `Coral`, `CouchAndLamp`, `CounterclockwiseArrowsButton`, `CoupleWithHeart`, `Cow`, `CowboyHatFace`, `CowFace`, `Crab`, `Crayon`, `CreditCard`, `CrescentMoon`, `Cricket`, `CricketGame`, `Crocodile`, `Croissant`, `CrossedFingers`, `CrossedFlags`, `CrossedSwords`, `CrossMark`, `CrossMarkButton`, `Crown`, `Crutch`, `CryingCat`, `CryingFace`, `CrystalBall`, `Cucumber`, `Cupcake`, `CupWithStraw`, `CurlingStone`, `CurlyHair`, `CurlyLoop`, `CurrencyExchange`, `CurryRice`, `Custard`, `Customs`, `CutOfMeat`, `Cyclone`, `Dagger`, `Dango`, `DarkSkinTone`, `DashingAway`, `DeafPerson`, `DeciduousTree`, `Deer`, `DeliveryTruck`, `DepartmentStore`, `DerelictHouse`, `Desert`, `DesertIsland`, `DesktopComputer`, `Detective`, `DiamondSuit`, `DiamondWithADot`, `DimButton`, `DisappointedFace`, `DisguisedFace`, `DistortedFace`, `Divide`, `DivingMask`, `DiyaLamp`, `Dizzy`, `Dna`, `Dodo`, `Dog`, `DogFace`, `DollarBanknote`, `Dolphin`, `Donkey`, `Door`, `DottedLineFace`, `DottedSixPointedStar`, `DoubleCurlyLoop`, `DoubleExclamationMark`, `Doughnut`, `Dove`, `DownArrow`, `DowncastFaceWithSweat`, `DownLeftArrow`, `DownRightArrow`, `DownwardsButton`, `Dragon`, `DragonFace`, `Dress`, `DroolingFace`, `Droplet`, `DropOfBlood`, `Drum`, `Duck`, `Dumpling`, `Dvd`, `Eagle`, `Ear`, `EarOfCorn`, `EarWithHearingAid`, `Egg`, `Eggplant`, `EightOClock`, `EightPointedStar`, `EightSpokedAsterisk`, `EightThirty`, `EjectButton`, `ElectricPlug`, `Elephant`, `Elevator`, `ElevenOClock`, `ElevenThirty`, `Elf`, `EMail`, `EmptyNest`, `EndArrow`, `EnragedFace`, `Envelope`, `EnvelopeWithArrow`, `EuroBanknote`, `EvergreenTree`, `Ewe`, `ExclamationQuestionMark`, `ExplodingHead`, `ExpressionlessFace`, `Eye`, `Eyes`, `FaceBlowingAKiss`, `FaceHoldingBackTears`, `FaceSavoringFood`, `FaceScreamingInFear`, `FaceVomiting`, `FaceWithBagsUnderEyes`, `FaceWithCrossedOutEyes`, `FaceWithDiagonalMouth`, `FaceWithHandOverMouth`, `FaceWithHeadBandage`, `FaceWithMedicalMask`, `FaceWithMonocle`, `FaceWithOpenEyesAndHandOverMouth`, `FaceWithOpenMouth`, `FaceWithoutMouth`, `FaceWithPeekingEye`, `FaceWithRaisedEyebrow`, `FaceWithRollingEyes`, `FaceWithSteamFromNose`, `FaceWithSymbolsOnMouth`, `FaceWithTearsOfJoy`, `FaceWithThermometer`, `FaceWithTongue`, `Factory`, `Fairy`, `Falafel`, `FallenLeaf`, `Family`, `FastDownButton`, `FastForwardButton`, `FastReverseButton`, `FastUpButton`, `FaxMachine`, `FearfulFace`, `Feather`, `FemaleSign`, `FerrisWheel`, `Ferry`, `FieldHockey`, `FightCloud`, `FileCabinet`, `FileFolder`, `FilmFrames`, `FilmProjector`, `Fingerprint`, `Fire`, `Firecracker`, `FireEngine`, `FireExtinguisher`, `Fireworks`, `FirstPlaceMedal`, `FirstQuarterMoon`, `FirstQuarterMoonFace`, `Fish`, `FishCakeWithSwirl`, `FishingPole`, `FiveOClock`, `FiveThirty`, `FlagInHole`, `Flamingo`, `Flashlight`, `Flatbread`, `FlatShoe`, `FleurDeLis`, `FlexedBiceps`, `FloppyDisk`, `FlowerPlayingCards`, `FlushedFace`, `Flute`, `Fly`, `FlyingDisc`, `FlyingSaucer`, `Fog`, `Foggy`, `FoldedHands`, `FoldingHandFan`, `Fondue`, `Foot`, `Footprints`, `ForkAndKnife`, `ForkAndKnifeWithPlate`, `FortuneCookie`, `Fountain`, `FountainPen`, `FourLeafClover`, `FourOClock`, `FourThirty`, `Fox`, `FramedPicture`, `FreeButton`, `FrenchFries`, `FriedShrimp`, `Frog`, `FrontFacingBabyChick`, `FrowningFace`, `FrowningFaceWithOpenMouth`, `FuelPump`, `FullMoon`, `FullMoonFace`, `FuneralUrn`, `GameDie`, `Garlic`, `Gear`, `Gemini`, `GemStone`, `Genie`, `Ghost`, `GingerRoot`, `Giraffe`, `Girl`, `Glasses`, `GlassOfMilk`, `GlobeShowingAmericas`, `GlobeShowingAsiaAustralia`, `GlobeShowingEuropeAfrica`, `GlobeWithMeridians`, `Gloves`, `GlowingStar`, `GoalNet`, `Goat`, `Goblin`, `Goggles`, `Goose`, `Gorilla`, `GraduationCap`, `Grapes`, `GreenApple`, `GreenBook`, `GreenCircle`, `GreenHeart`, `GreenSalad`, `GreenSquare`, `GreyHeart`, `GrimacingFace`, `GrinningCat`, `GrinningCatWithSmilingEyes`, `GrinningFace`, `GrinningFaceWithBigEyes`, `GrinningFaceWithSmilingEyes`, `GrinningFaceWithSweat`, `GrinningSquintingFace`, `GrowingHeart`, `Guard`, `GuideDog`, `Guitar`, `HairPick`, `HairyCreature`, `Hamburger`, `Hammer`, `HammerAndPick`, `HammerAndWrench`, `Hamsa`, `Hamster`, `Handbag`, `Handshake`, `HandWithFingersSplayed`, `HandWithIndexFingerAndThumbCrossed`, `Harp`, `HatchingChick`, `Headphone`, `Headstone`, `HearNoEvilMonkey`, `HeartDecoration`, `HeartExclamation`, `HeartHands`, `HeartSuit`, `HeartWithArrow`, `HeartWithRibbon`, `HeavyDollarSign`, `HeavyEqualsSign`, `Hedgehog`, `Helicopter`, `Herb`, `Hibiscus`, `HighHeeledShoe`, `HighSpeedTrain`, `HighVoltage`, `HikingBoot`, `HinduTemple`, `Hippopotamus`, `Hole`, `HollowRedCircle`, `Honeybee`, `HoneyPot`, `Hook`, `HorizontalTrafficLight`, `Horse`, `HorseFace`, `HorseRacing`, `Hospital`, `HotBeverage`, `HotDog`, `Hotel`, `HotFace`, `HotPepper`, `HotSprings`, `HourglassDone`, `HourglassNotDone`, `House`, `Houses`, `HouseWithGarden`, `HundredPoints`, `HushedFace`, `Hut`, `Hyacinth`, `Ice`, `IceCream`, `IceHockey`, `IceSkate`, `IdButton`, `IdentificationCard`, `InboxTray`, `IncomingEnvelope`, `IndexPointingAtTheViewer`, `IndexPointingUp`, `Infinity`, `Information`, `InputLatinLetters`, `InputLatinLowercase`, `InputLatinUppercase`, `InputNumbers`, `InputSymbols`, `JackOLantern`, `JapaneseAcceptableButton`, `JapaneseApplicationButton`, `JapaneseBargainButton`, `JapaneseCastle`, `JapaneseCongratulationsButton`, `JapaneseDiscountButton`, `JapaneseDolls`, `JapaneseFreeOfChargeButton`, `JapaneseHereButton`, `JapaneseMonthlyAmountButton`, `JapaneseNotFreeOfChargeButton`, `JapaneseNoVacancyButton`, `JapaneseOpenForBusinessButton`, `JapanesePassingGradeButton`, `JapanesePostOffice`, `JapaneseProhibitedButton`, `JapaneseReservedButton`, `JapaneseSecretButton`, `JapaneseServiceChargeButton`, `JapaneseSymbolForBeginner`, `JapaneseVacancyButton`, `Jar`, `Jeans`, `Jellyfish`, `Joker`, `Joystick`, `Kaaba`, `Kangaroo`, `Key`, `Keyboard`, `Keycap10`, `Khanda`, `KickScooter`, `Kimono`, `Kiss`, `KissingCat`, `KissingFace`, `KissingFaceWithClosedEyes`, `KissingFaceWithSmilingEyes`, `KissMark`, `KitchenKnife`, `Kite`, `KiwiFruit`, `Knot`, `Koala`, `LabCoat`, `Label`, `Lacrosse`, `Ladder`, `LadyBeetle`, `Landslide`, `Laptop`, `LargeBlueDiamond`, `LargeOrangeDiamond`, `LastQuarterMoon`, `LastQuarterMoonFace`, `LastTrackButton`, `LatinCross`, `LeafFlutteringInWind`, `LeaflessTree`, `LeafyGreen`, `Ledger`, `LeftArrow`, `LeftArrowCurvingRight`, `LeftFacingFist`, `LeftLuggage`, `LeftRightArrow`, `LeftSpeechBubble`, `LeftwardsHand`, `LeftwardsPushingHand`, `Leg`, `Lemon`, `Leo`, `Leopard`, `LevelSlider`, `Libra`, `LightBlueHeart`, `LightBulb`, `LightRail`, `LightSkinTone`, `Link`, `LinkedPaperclips`, `Lion`, `Lipstick`, `LitterInBinSign`, `Lizard`, `Llama`, `Lobster`, `Locked`, `LockedWithKey`, `LockedWithPen`, `Locomotive`, `Lollipop`, `LongDrum`, `LotionBottle`, `Lotus`, `LoudlyCryingFace`, `Loudspeaker`, `LoveHotel`, `LoveLetter`, `LoveYouGesture`, `LowBattery`, `Luggage`, `Lungs`, `LyingFace`, `Mage`, `MagicWand`, `Magnet`, `MagnifyingGlassTiltedLeft`, `MagnifyingGlassTiltedRight`, `MahjongRedDragon`, `MaleSign`, `Mammoth`, `Man`, `ManDancing`, `Mango`, `MansShoe`, `MantelpieceClock`, `ManualWheelchair`, `MapleLeaf`, `MapOfJapan`, `Maracas`, `MartialArtsUniform`, `Mate`, `MeatOnBone`, `MechanicalArm`, `MechanicalLeg`, `MedicalSymbol`, `MediumDarkSkinTone`, `MediumLightSkinTone`, `MediumSkinTone`, `Megaphone`, `Melon`, `MeltingFace`, `Memo`, `MenHoldingHands`, `Menorah`, `MensRoom`, `Merperson`, `Metro`, `Microbe`, `Microphone`, `Microscope`, `MiddleFinger`, `MilitaryHelmet`, `MilitaryMedal`, `MilkyWay`, `Minibus`, `Minus`, `Mirror`, `MirrorBall`, `Moai`, `MobilePhone`, `MobilePhoneOff`, `MobilePhoneWithArrow`, `MoneyBag`, `MoneyMouthFace`, `MoneyWithWings`, `Monkey`, `MonkeyFace`, `Monorail`, `MoonCake`, `MoonViewingCeremony`, `Moose`, `Mosque`, `Mosquito`, `MotorBoat`, `Motorcycle`, `MotorizedWheelchair`, `MotorScooter`, `Motorway`, `Mountain`, `MountainCableway`, `MountainRailway`, `MountFuji`, `Mouse`, `MouseFace`, `MouseTrap`, `Mouth`, `MovieCamera`, `MrsClaus`, `Multiply`, `Mushroom`, `MusicalKeyboard`, `MusicalNote`, `MusicalNotes`, `MusicalScore`, `MutedSpeaker`, `NailPolish`, `NameBadge`, `NationalPark`, `NauseatedFace`, `NazarAmulet`, `Necktie`, `NerdFace`, `NestingDolls`, `NestWithEggs`, `NeutralFace`, `NewButton`, `NewMoon`, `NewMoonFace`, `Newspaper`, `NextTrackButton`, `NgButton`, `NightWithStars`, `NineOClock`, `NineThirty`, `Ninja`, `NoBicycles`, `NoEntry`, `NoLittering`, `NoMobilePhones`, `NonPotableWater`, `NoOneUnderEighteen`, `NoPedestrians`, `Nose`, `NoSmoking`, `Notebook`, `NotebookWithDecorativeCover`, `NutAndBolt`, `OButtonBloodType`, `Octopus`, `Oden`, `OfficeBuilding`, `Ogre`, `OilDrum`, `OkButton`, `OkHand`, `OlderPerson`, `OldKey`, `OldMan`, `OldWoman`, `Olive`, `Om`, `OnArrow`, `OncomingAutomobile`, `OncomingBus`, `OncomingFist`, `OncomingPoliceCar`, `OncomingTaxi`, `OneOClock`, `OnePieceSwimsuit`, `OneThirty`, `Onion`, `OpenBook`, `OpenFileFolder`, `OpenHands`, `OpenMailboxWithLoweredFlag`, `OpenMailboxWithRaisedFlag`, `Ophiuchus`, `OpticalDisk`, `OrangeBook`, `OrangeCircle`, `OrangeHeart`, `OrangeSquare`, `Orangutan`, `Orca`, `OrthodoxCross`, `Otter`, `OutboxTray`, `Owl`, `Ox`, `Oyster`, `Package`, `PageFacingUp`, `Pager`, `PageWithCurl`, `Paintbrush`, `PalmDownHand`, `PalmsUpTogether`, `PalmTree`, `PalmUpHand`, `Pancakes`, `Panda`, `Paperclip`, `Parachute`, `Parrot`, `PartAlternationMark`, `PartyingFace`, `PartyPopper`, `PassengerShip`, `PassportControl`, `PauseButton`, `PawPrints`, `PButton`, `PeaceSymbol`, `Peach`, `Peacock`, `Peanuts`, `PeaPod`, `Pear`, `Pen`, `Pencil`, `Penguin`, `PensiveFace`, `PeopleHugging`, `PeopleWithBunnyEars`, `PeopleWrestling`, `PerformingArts`, `PerseveringFace`, `Person`, `PersonBeard`, `PersonBiking`, `PersonBlondHair`, `PersonBouncingBall`, `PersonBowing`, `PersonCartwheeling`, `PersonClimbing`, `PersonFacepalming`, `PersonFencing`, `PersonFrowning`, `PersonGesturingNo`, `PersonGesturingOk`, `PersonGettingHaircut`, `PersonGettingMassage`, `PersonGolfing`, `PersonInBed`, `PersonInLotusPosition`, `PersonInSteamyRoom`, `PersonInSuitLevitating`, `PersonInTuxedo`, `PersonJuggling`, `PersonKneeling`, `PersonLiftingWeights`, `PersonMountainBiking`, `PersonPlayingHandball`, `PersonPlayingWaterPolo`, `PersonPouting`, `PersonRaisingHand`, `PersonRowingBoat`, `PersonRunning`, `PersonShrugging`, `PersonStanding`, `PersonSurfing`, `PersonSwimming`, `PersonTakingBath`, `PersonTippingHand`, `PersonWalking`, `PersonWearingTurban`, `PersonWithCrown`, `PersonWithSkullcap`, `PersonWithVeil`, `PetriDish`, `Pick`, `PickupTruck`, `Pie`, `Pig`, `PigFace`, `PigNose`, `PileOfPoo`, `Pill`, `Piñata`, `PinchedFingers`, `PinchingHand`, `Pineapple`, `PineDecoration`, `PingPong`, `PinkHeart`, `Pisces`, `Pizza`, `Placard`, `PlaceOfWorship`, `PlayButton`, `PlaygroundSlide`, `PlayOrPauseButton`, `PleadingFace`, `Plunger`, `Plus`, `PoliceCar`, `PoliceCarLight`, `PoliceOfficer`, `Poodle`, `Pool8Ball`, `Popcorn`, `PostalHorn`, `Postbox`, `PostOffice`, `PotableWater`, `Potato`, `PotOfFood`, `PottedPlant`, `PoultryLeg`, `PoundBanknote`, `PouringLiquid`, `PoutingCat`, `PrayerBeads`, `PregnantMan`, `PregnantPerson`, `PregnantWoman`, `Pretzel`, `Prince`, `Princess`, `Printer`, `Prohibited`, `PurpleCircle`, `PurpleHeart`, `PurpleSquare`, `Purse`, `Pushpin`, `PuzzlePiece`, `Rabbit`, `RabbitFace`, `Raccoon`, `RacingCar`, `Radio`, `Radioactive`, `RadioButton`, `RailwayCar`, `RailwayTrack`, `Rainbow`, `RaisedBackOfHand`, `RaisedFist`, `RaisedHand`, `RaisingHands`, `Ram`, `Rat`, `Razor`, `Receipt`, `RecordButton`, `RecyclingSymbol`, `RedApple`, `RedCircle`, `RedEnvelope`, `RedExclamationMark`, `RedHair`, `RedHeart`, `RedPaperLantern`, `RedQuestionMark`, `RedSquare`, `RedTrianglePointedDown`, `RedTrianglePointedUp`, `RegionalIndicatorA`, `RegionalIndicatorB`, `RegionalIndicatorC`, `RegionalIndicatorD`, `RegionalIndicatorE`, `RegionalIndicatorF`, `RegionalIndicatorG`, `RegionalIndicatorH`, `RegionalIndicatorI`, `RegionalIndicatorJ`, `RegionalIndicatorK`, `RegionalIndicatorL`, `RegionalIndicatorM`, `RegionalIndicatorN`, `RegionalIndicatorO`, `RegionalIndicatorP`, `RegionalIndicatorQ`, `RegionalIndicatorR`, `RegionalIndicatorS`, `RegionalIndicatorT`, `RegionalIndicatorU`, `RegionalIndicatorV`, `RegionalIndicatorW`, `RegionalIndicatorX`, `RegionalIndicatorY`, `RegionalIndicatorZ`, `Registered`, `RelievedFace`, `ReminderRibbon`, `RepeatButton`, `RepeatSingleButton`, `RescueWorkersHelmet`, `Restroom`, `ReverseButton`, `RevolvingHearts`, `Rhinoceros`, `Ribbon`, `RiceBall`, `RiceCracker`, `RightAngerBubble`, `RightArrow`, `RightArrowCurvingDown`, `RightArrowCurvingLeft`, `RightArrowCurvingUp`, `RightFacingFist`, `RightwardsHand`, `RightwardsPushingHand`, `Ring`, `RingBuoy`, `RingedPlanet`, `RoastedSweetPotato`, `Robot`, `Rock`, `Rocket`, `RolledUpNewspaper`, `RollerCoaster`, `RollerSkate`, `RollingOnTheFloorLaughing`, `RollOfPaper`, `Rooster`, `RootVegetable`, `Rose`, `Rosette`, `RoundPushpin`, `RugbyFootball`, `RunningShirt`, `RunningShoe`, `SadButRelievedFace`, `SafetyPin`, `SafetyVest`, `Sagittarius`, `Sailboat`, `Sake`, `Salt`, `SalutingFace`, `Sandwich`, `SantaClaus`, `Sari`, `Satellite`, `SatelliteAntenna`, `Sauropod`, `Saxophone`, `Scarf`, `School`, `Scissors`, `Scorpio`, `Scorpion`, `Screwdriver`, `Scroll`, `Seal`, `Seat`, `SecondPlaceMedal`, `Seedling`, `SeeNoEvilMonkey`, `Selfie`, `SevenOClock`, `SevenThirty`, `SewingNeedle`, `ShakingFace`, `ShallowPanOfFood`, `Shamrock`, `Shark`, `ShavedIce`, `SheafOfRice`, `Shield`, `ShintoShrine`, `Ship`, `ShootingStar`, `ShoppingBags`, `ShoppingCart`, `Shortcake`, `Shorts`, `Shovel`, `Shower`, `Shrimp`, `ShuffleTracksButton`, `ShushingFace`, `SignOfTheHorns`, `SixOClock`, `SixThirty`, `Skateboard`, `Skier`, `Skis`, `Skull`, `SkullAndCrossbones`, `Skunk`, `Sled`, `SleepingFace`, `SleepyFace`, `SlightlyFrowningFace`, `SlightlySmilingFace`, `Sloth`, `SlotMachine`, `SmallAirplane`, `SmallBlueDiamond`, `SmallOrangeDiamond`, `SmilingCatWithHeartEyes`, `SmilingFace`, `SmilingFaceWithHalo`, `SmilingFaceWithHeartEyes`, `SmilingFaceWithHearts`, `SmilingFaceWithHorns`, `SmilingFaceWithOpenHands`, `SmilingFaceWithSmilingEyes`, `SmilingFaceWithSunglasses`, `SmilingFaceWithTear`, `SmirkingFace`, `Snail`, `Snake`, `SneezingFace`, `Snowboarder`, `SnowCappedMountain`, `Snowflake`, `Snowman`, `SnowmanWithoutSnow`, `Soap`, `SoccerBall`, `Socks`, `Softball`, `SoftIceCream`, `SoonArrow`, `SosButton`, `SpadeSuit`, `Spaghetti`, `Sparkle`, `Sparkler`, `Sparkles`, `SparklingHeart`, `SpeakerHighVolume`, `SpeakerLowVolume`, `SpeakerMediumVolume`, `SpeakingHead`, `SpeakNoEvilMonkey`, `SpeechBalloon`, `Speedboat`, `Spider`, `SpiderWeb`, `SpiralCalendar`, `SpiralNotepad`, `SpiralShell`, `Splatter`, `Sponge`, `Spoon`, `SportsMedal`, `SportUtilityVehicle`, `SpoutingWhale`, `Squid`, `SquintingFaceWithTongue`, `Stadium`, `Star`, `StarAndCrescent`, `StarOfDavid`, `StarStruck`, `Station`, `StatueOfLiberty`, `SteamingBowl`, `Stethoscope`, `StopButton`, `StopSign`, `Stopwatch`, `StraightRuler`, `Strawberry`, `StudioMicrophone`, `StuffedFlatbread`, `Sun`, `SunBehindCloud`, `SunBehindLargeCloud`, `SunBehindRainCloud`, `SunBehindSmallCloud`, `Sunflower`, `Sunglasses`, `Sunrise`, `SunriseOverMountains`, `Sunset`, `SunWithFace`, `Superhero`, `Supervillain`, `Sushi`, `SuspensionRailway`, `Swan`, `SweatDroplets`, `Synagogue`, `Syringe`, `Taco`, `TakeoutBox`, `Tamale`, `TanabataTree`, `Tangerine`, `Taurus`, `Taxi`, `TeacupWithoutHandle`, `Teapot`, `TearOffCalendar`, `TeddyBear`, `Telephone`, `TelephoneReceiver`, `Telescope`, `Television`, `Tennis`, `TenOClock`, `Tent`, `TenThirty`, `TestTube`, `Thermometer`, `ThinkingFace`, `ThirdPlaceMedal`, `ThongSandal`, `ThoughtBalloon`, `Thread`, `ThreeOClock`, `ThreeThirty`, `ThumbsDown`, `ThumbsUp`, `Ticket`, `Tiger`, `TigerFace`, `TimerClock`, `TiredFace`, `Toilet`, `TokyoTower`, `Tomato`, `Tongue`, `Toolbox`, `Tooth`, `Toothbrush`, `TopArrow`, `TopHat`, `Tornado`, `Trackball`, `Tractor`, `TradeMark`, `Train`, `Tram`, `TramCar`, `TransgenderSymbol`, `TreasureChest`, `TRex`, `TriangularFlag`, `TriangularRuler`, `TridentEmblem`, `Troll`, `Trolleybus`, `Trombone`, `Trophy`, `TropicalDrink`, `TropicalFish`, `Trumpet`, `TShirt`, `Tulip`, `TumblerGlass`, `Turkey`, `Turtle`, `TwelveOClock`, `TwelveThirty`, `TwoHearts`, `TwoHumpCamel`, `TwoOClock`, `TwoThirty`, `Umbrella`, `UmbrellaOnGround`, `UmbrellaWithRainDrops`, `UnamusedFace`, `Unicorn`, `Unlocked`, `UpArrow`, `UpButton`, `UpDownArrow`, `UpLeftArrow`, `UpRightArrow`, `UpsideDownFace`, `UpwardsButton`, `Vampire`, `VerticalTrafficLight`, `VibrationMode`, `VictoryHand`, `VideoCamera`, `Videocassette`, `VideoGame`, `Violin`, `Virgo`, `Volcano`, `Volleyball`, `VsButton`, `VulcanSalute`, `Waffle`, `WaningCrescentMoon`, `WaningGibbousMoon`, `Warning`, `Wastebasket`, `Watch`, `WaterBuffalo`, `WaterCloset`, `Watermelon`, `WaterPistol`, `WaterWave`, `WavingHand`, `WavyDash`, `WaxingCrescentMoon`, `WaxingGibbousMoon`, `WearyCat`, `WearyFace`, `Wedding`, `Whale`, `Wheel`, `WheelchairSymbol`, `WheelOfDharma`, `WhiteCane`, `WhiteCircle`, `WhiteExclamationMark`, `WhiteFlag`, `WhiteFlower`, `WhiteHair`, `WhiteHeart`, `WhiteLargeSquare`, `WhiteMediumSmallSquare`, `WhiteMediumSquare`, `WhiteQuestionMark`, `WhiteSmallSquare`, `WhiteSquareButton`, `WiltedFlower`, `WindChime`, `WindFace`, `Window`, `WineGlass`, `Wing`, `WinkingFace`, `WinkingFaceWithTongue`, `Wireless`, `Wolf`, `Woman`, `WomanAndManHoldingHands`, `WomanDancing`, `WomansBoot`, `WomansClothes`, `WomansHat`, `WomansSandal`, `WomanWithHeadscarf`, `WomenHoldingHands`, `WomensRoom`, `Wood`, `WoozyFace`, `WorldMap`, `Worm`, `WorriedFace`, `WrappedGift`, `Wrench`, `WritingHand`, `XRay`, `Yarn`, `YawningFace`, `YellowCircle`, `YellowHeart`, `YellowSquare`, `YenBanknote`, `YinYang`, `YoYo`, `ZanyFace`, `Zebra`, `ZipperMouthFace`, `Zombie`, `Zzz`, `HuggingFace`, `KnockedOutFace`, `PoutingFace`

## `public interface IAlignable`

*core* · `src/Spectre.Console/IAlignable.cs`

Represents something that is alignable.

**Properties**

- `Justify? Alignment { get; set; }` — Gets or sets the alignment.

**Extension methods on this type** (call as `x.Method(...)`)

- `Alignment<T>(Justify? alignment) -> T` — Sets the alignment for an `IAlignable` object.
- `LeftAligned<T>() -> T` — Sets the `IAlignable` object to be left aligned.
- `Centered<T>() -> T` — Sets the `IAlignable` object to be centered.
- `RightAligned<T>() -> T` — Sets the `IAlignable` object to be right aligned.

## `public interface IAnsiConsole`

*core* · `src/Spectre.Console/IAnsiConsole.cs`

Represents a console.

**Properties**

- `Profile Profile { get; }` — Gets the console profile.
- `IAnsiConsoleCursor Cursor { get; }` — Gets the console cursor.
- `IAnsiConsoleInput Input { get; }` — Gets the console input.
- `IExclusivityMode ExclusivityMode { get; }` — Gets the exclusivity mode.
- `RenderPipeline Pipeline { get; }` — Gets the render pipeline.

**Methods**

- `void Clear(bool home)` — Clears the console.
- `void Write(IRenderable renderable)` — Writes a `IRenderable` to the console.
- `void WriteAnsi(Action<AnsiWriter> action)` — Writes ANSI/VT escapes sequences to the console.

**Extension methods on this type** (call as `x.Method(...)`)

- `WriteAnsi(string sequence) -> void` — Writes a VT/Ansi control code sequence to the console (if supported).
- `ToAnsi(IRenderable renderable) -> string` — Gets the VT/ANSI control code sequence for a `IRenderable`.
- `Clear() -> void` — Clears the console.
- `WriteException(Exception exception, ExceptionFormats format = ExceptionFormats.Default) -> void` — Writes an exception to the console.
- `WriteException(Exception exception, ExceptionSettings settings) -> void` — Writes an exception to the console.
- `RunExclusive<T>(Func<T> func) -> T` — Runs the specified function in exclusive mode.
- `RunExclusive<T>(Func<Task<T>> func) -> Task<T>` — Runs the specified function in exclusive mode asynchronously.
- `Live(IRenderable target) -> LiveDisplay` — Creates a new `LiveDisplay` instance for the console.
- `Markup(string format, params object[] args) -> void` — Writes the specified markup to the console.
- `MarkupInterpolated(FormattableString value) -> void` — Writes the specified markup to the console. All interpolation holes which contain a string are automatically escaped.
- `Markup(IFormatProvider provider, string format, params object[] args) -> void` — Writes the specified markup to the console.
- `MarkupInterpolated(IFormatProvider provider, FormattableString value) -> void` — Writes the specified markup to the console. All interpolation holes which contain a string are automatically escaped.
- `Markup(string value) -> void` — Writes the specified markup to the console.
- `MarkupLine(string format, params object[] args) -> void` — Writes the specified markup, followed by the current line terminator, to the console.
- `MarkupLineInterpolated(FormattableString value) -> void` — Writes the specified markup, followed by the current line terminator, to the console. All interpolation holes which contain a string are automatically escaped.
- `MarkupLine(string value) -> void` — Writes the specified markup, followed by the current line terminator, to the console.
- `MarkupLine(IFormatProvider provider, string format, params object[] args) -> void` — Writes the specified markup, followed by the current line terminator, to the console.
- `MarkupLineInterpolated(IFormatProvider provider, FormattableString value) -> void` — Writes the specified markup, followed by the current line terminator, to the console. All interpolation holes which contain a string are automatically escaped.
- `Progress() -> Progress` — Creates a new `Progress` instance for the console.
- `Status() -> Status` — Creates a new `Status` instance for the console.
- `Prompt<T>(IPrompt<T> prompt) -> T` — Displays a prompt to the user.
- `Ask<T>(string prompt) -> T` — Displays a prompt to the user.
- `Ask<T>(string prompt, CultureInfo? culture) -> T` — Displays a prompt to the user.
- `Confirm(string prompt, bool defaultValue = true) -> bool` — Displays a prompt with two choices, yes or no.
- `PromptAsync<T>(IPrompt<T> prompt, CancellationToken cancellationToken = default) -> Task<T>` — Displays a prompt to the user.
- `AskAsync<T>(string prompt, CancellationToken cancellationToken = default) -> Task<T>` — Displays a prompt to the user.
- `AskAsync<T>(string prompt, CultureInfo? culture, CancellationToken cancellationToken = default) -> Task<T>` — Displays a prompt to the user.
- `ConfirmAsync(string prompt, bool defaultValue = true, CancellationToken cancellationToken = default) -> Task<bool>` — Displays a prompt with two choices, yes or no.
- `CreateRecorder() -> Recorder` — Creates a recorder for the specified console.
- `AlternateScreen(Action action) -> void` — Switches to an alternate screen buffer if the terminal supports it.
- `Write(string text) -> void` — Writes the specified string value to the console.
- `Write(string text, Style? style) -> void` — Writes the specified string value to the console.
- `WriteLine() -> void` — Writes an empty line to the console.
- `WriteLine(string text) -> void` — Writes the specified string value, followed by the current line terminator, to the console.
- `WriteLine(string text, Style? style) -> void` — Writes the specified string value, followed by the current line terminator, to the console.

## `public interface IAnsiConsoleCursor`

*core* · `src/Spectre.Console/IAnsiConsoleCursor.cs`

Represents the console's cursor.

**Methods**

- `void Show(bool show)` — Shows or hides the cursor.
- `void SetPosition(int column, int line)` — Sets the cursor position.
- `void Move(CursorDirection direction, int steps)` — Moves the cursor relative to the current position.

**Extension methods on this type** (call as `x.Method(...)`)

- `Show() -> void` — Shows the cursor.
- `Hide() -> void` — Hides the cursor.
- `MoveUp() -> void` — Moves the cursor up.
- `MoveUp(int steps) -> void` — Moves the cursor up.
- `MoveDown() -> void` — Moves the cursor down.
- `MoveDown(int steps) -> void` — Moves the cursor down.
- `MoveLeft() -> void` — Moves the cursor to the left.
- `MoveLeft(int steps) -> void` — Moves the cursor to the left.
- `MoveRight() -> void` — Moves the cursor to the right.
- `MoveRight(int steps) -> void` — Moves the cursor to the right.

## `public interface IAnsiConsoleInput`

*core* · `src/Spectre.Console/IAnsiConsoleInput.cs`

Represents the console's input mechanism.

**Methods**

- `bool IsKeyAvailable()` — Gets a value indicating whether or not there is a key available.
- `ConsoleKeyInfo? ReadKey(bool intercept)` — Reads a key from the console.
- `Task<ConsoleKeyInfo?> ReadKeyAsync(bool intercept, CancellationToken cancellationToken)` — Reads a key from the console.

## `public interface IAnsiConsoleOutput`

*core* · `src/Spectre.Console/IAnsiConsoleOutput.cs`

Represents console output.

**Properties**

- `TextWriter Writer { get; }` — Gets the `TextWriter` used to write to the output.
- `bool IsTerminal { get; }` — Gets a value indicating whether or not the output is a terminal.
- `int Width { get; }` — Gets the output width.
- `int Height { get; }` — Gets the output height.

**Methods**

- `void SetEncoding(Encoding encoding)` — Sets the output encoding.

## `public interface IColumn : IAlignable, IPaddable`

*core* · `src/Spectre.Console/IColumn.cs`

Represents a column.

**Properties**

- `bool NoWrap { get; set; }` — Gets or sets a value indicating whether or not wrapping should be prevented.
- `int? Width { get; set; }` — Gets or sets the width of the column.

**Extension methods on this type** (call as `x.Method(...)`)

- `NoWrap<T>() -> T` — Prevents a column from wrapping.
- `Width<T>(int? width) -> T` — Sets the width of the column.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IAlignable`: `Alignment`, `LeftAligned`, `Centered`, `RightAligned`
- via `IPaddable`: `PadLeft`, `PadTop`, `PadRight`, `PadBottom`, `Padding`

## `public interface IExclusivityMode`

*core* · `src/Spectre.Console/IExclusivityMode.cs`

Represents an exclusivity mode.

**Methods**

- `T Run<T>(Func<T> func)` — Runs the specified function in exclusive mode.
- `Task<T> RunAsync<T>(Func<Task<T>> func)` — Runs the specified function in exclusive mode asynchronously.

## `public interface IExpandable`

*core* · `src/Spectre.Console/IExpandable.cs`

Represents something that is expandable.

**Properties**

- `bool Expand { get; set; }` — Gets or sets a value indicating whether or not the object should expand to the available space. If `false`, the object's width will be auto calculated.

**Extension methods on this type** (call as `x.Method(...)`)

- `Collapse<T>() -> T` — Tells the specified object to not expand to the available area but take as little space as possible.
- `Expand<T>() -> T` — Tells the specified object to expand to the available area.

## `public interface IHasBorder`

*core* · `src/Spectre.Console/IHasBorder.cs`

Represents something that has a border.

**Properties**

- `bool UseSafeBorder { get; set; }` — Gets or sets a value indicating whether or not to use a "safe" border on legacy consoles that might not be able to render non-ASCII characters.
- `Style? BorderStyle { get; set; }` — Gets or sets the box style.

**Extension methods on this type** (call as `x.Method(...)`)

- `SafeBorder<T>() -> T` — Enables the safe border.
- `NoSafeBorder<T>() -> T` — Disables the safe border.
- `BorderStyle<T>(Style style) -> T` — Sets the border style.
- `BorderColor<T>(Color color) -> T` — Sets the border color.

## `public interface IHasBoxBorder`

*core* · `src/Spectre.Console/IHasBoxBorder.cs`

Represents something that has a box border.

**Properties**

- `BoxBorder Border { get; set; }` — Gets or sets the box.

**Extension methods on this type** (call as `x.Method(...)`)

- `Border<T>(BoxBorder border) -> T` — Sets the border.
- `NoBorder<T>() -> T` — Do not display a border.
- `SquareBorder<T>() -> T` — Display a square border.
- `AsciiBorder<T>() -> T` — Display an ASCII border.
- `RoundedBorder<T>() -> T` — Display a rounded border.
- `HeavyBorder<T>() -> T` — Display a heavy border.
- `DoubleBorder<T>() -> T` — Display a double border.
- `HeavyHorizontalBorder<T>() -> T` — Display a border with heavy horizontal edges and light vertical edges.
- `HeavyVerticalBorder<T>() -> T` — Display a border with heavy vertical edges and light horizontal edges.
- `DoubleHorizontalBorder<T>() -> T` — Display a border with double horizontal edges and single vertical edges.
- `DoubleVerticalBorder<T>() -> T` — Display a border with double vertical edges and single horizontal edges.
- `DashedBorder<T>() -> T` — Display a dashed border with square corners.
- `RoundedDashedBorder<T>() -> T` — Display a dashed border with rounded corners.
- `HeavyDashedBorder<T>() -> T` — Display a heavy dashed border.
- `DottedBorder<T>() -> T` — Display a dotted border with square corners.
- `RoundedDottedBorder<T>() -> T` — Display a dotted border with rounded corners.
- `HeavyDottedBorder<T>() -> T` — Display a heavy dotted border.
- `DashedWideBorder<T>() -> T` — Display a wide-dashed border with square corners.
- `RoundedDashedWideBorder<T>() -> T` — Display a wide-dashed border with rounded corners.
- `HeavyDashedWideBorder<T>() -> T` — Display a heavy wide-dashed border.
- `NearBorder<T>() -> T` — Display a "near" border that hugs the content using thin block elements.
- `BeveledBorder<T>() -> T` — Display a beveled border using thin block edges and diagonal corners.
- `McGuganHorizontalBorder<T>() -> T` — Display the horizontal variant of the McGugan border.
- `McGuganVerticalBorder<T>() -> T` — Display the vertical variant of the McGugan border.

## `public interface IHasCulture`

*core* · `src/Spectre.Console/IHasCulture.cs`

Represents something that has a culture.

**Properties**

- `CultureInfo? Culture { get; set; }` — Gets or sets the culture.

**Extension methods on this type** (call as `x.Method(...)`)

- `Culture<T>(CultureInfo culture) -> T` — Sets the culture.
- `Culture<T>(string name) -> T` — Sets the culture.
- `Culture<T>(int culture) -> T` — Sets the culture.

## `public interface IHasJustification`

*core* · `src/Spectre.Console/IHasJustification.cs`

Represents something that has justification.

**Properties**

- `Justify? Justification { get; set; }` — Gets or sets the justification.

**Extension methods on this type** (call as `x.Method(...)`)

- `Justify<T>(Justify? alignment) -> T` — Sets the justification for an `IHasJustification` object.
- `LeftJustified<T>() -> T` — Sets the `IHasJustification` object to be left justified.
- `Centered<T>() -> T` — Sets the `IHasJustification` object to be centered.
- `RightJustified<T>() -> T` — Sets the `IHasJustification` object to be right justified.

## `public interface IHasTableBorder : IHasBorder`

*core* · `src/Spectre.Console/IHasTableBorder.cs`

Represents something that has a border.

**Properties**

- `TableBorder Border { get; set; }` — Gets or sets the border.

**Extension methods on this type** (call as `x.Method(...)`)

- `NoBorder<T>() -> T` — Do not display a border.
- `SquareBorder<T>() -> T` — Display a square border.
- `AsciiBorder<T>() -> T` — Display an ASCII border.
- `Ascii2Border<T>() -> T` — Display another ASCII border.
- `AsciiDoubleHeadBorder<T>() -> T` — Display an ASCII border with a double header border.
- `RoundedBorder<T>() -> T` — Display a rounded border.
- `MinimalBorder<T>() -> T` — Display a minimal border.
- `MinimalHeavyHeadBorder<T>() -> T` — Display a minimal border with a heavy head.
- `MinimalDoubleHeadBorder<T>() -> T` — Display a minimal border with a double header border.
- `SimpleBorder<T>() -> T` — Display a simple border.
- `SimpleHeavyBorder<T>() -> T` — Display a simple border with heavy lines.
- `HorizontalBorder<T>() -> T` — Display a simple border.
- `HeavyBorder<T>() -> T` — Display a heavy border.
- `HeavyEdgeBorder<T>() -> T` — Display a border with a heavy edge.
- `HeavyHeadBorder<T>() -> T` — Display a border with a heavy header.
- `DoubleBorder<T>() -> T` — Display a double border.
- `DoubleEdgeBorder<T>() -> T` — Display a border with a double edge.
- `MinimalistBorder<T>() -> T` — Display a minimalist border.
- `MarkdownBorder<T>() -> T` — Display a markdown border.
- `Border<T>(TableBorder border) -> T` — Sets the border.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IHasBorder`: `SafeBorder`, `NoSafeBorder`, `BorderStyle`, `BorderColor`

## `public interface IHasTreeNodes`

*core* · `src/Spectre.Console/IHasTreeNodes.cs`

Represents something that has tree nodes.

**Properties**

- `List<TreeNode> Nodes { get; }` — Gets the tree's child nodes.

**Extension methods on this type** (call as `x.Method(...)`)

- `AddNode<T>(string markup) -> TreeNode` — Adds a tree node.
- `AddNode<T>(IRenderable renderable) -> TreeNode` — Adds a tree node.
- `AddNode<T>(TreeNode node) -> TreeNode` — Adds a tree node.
- `AddNodes<T>(params string[] nodes) -> void` — Add multiple tree nodes.
- `AddNodes<T>(IEnumerable<string> nodes) -> void` — Add multiple tree nodes.
- `AddNodes<T>(params IRenderable[] nodes) -> void` — Add multiple tree nodes.
- `AddNodes<T>(IEnumerable<IRenderable> nodes) -> void` — Add multiple tree nodes.
- `AddNodes<T>(params TreeNode[] nodes) -> void` — Add multiple tree nodes.
- `AddNodes<T>(IEnumerable<TreeNode> nodes) -> void` — Add multiple tree nodes.

## `public interface IHasVisibility`

*core* · `src/Spectre.Console/IHasVisibility.cs`

Represents something that can be hidden.

**Properties**

- `bool IsVisible { get; set; }` — Gets or sets a value indicating whether or not the object should be visible or not.

**Extension methods on this type** (call as `x.Method(...)`)

- `Invisible<T>() -> T` — Marks the specified object as being invisible.
- `Visible<T>() -> T` — Marks the specified object as being visible.

## `public interface IOverflowable`

*core* · `src/Spectre.Console/IOverflowable.cs`

Represents something that can overflow.

**Properties**

- `Overflow? Overflow { get; set; }` — Gets or sets the text overflow strategy.

**Extension methods on this type** (call as `x.Method(...)`)

- `Fold<T>() -> T` — Folds any overflowing text.
- `Crop<T>() -> T` — Crops any overflowing text.
- `Ellipsis<T>() -> T` — Crops any overflowing text and adds an ellipsis to the end.
- `Overflow<T>(Overflow overflow) -> T` — Sets the overflow strategy.

## `public interface IPaddable`

*core* · `src/Spectre.Console/IPaddable.cs`

Represents something that is paddable.

**Properties**

- `Padding? Padding { get; set; }` — Gets or sets the padding.

**Extension methods on this type** (call as `x.Method(...)`)

- `PadLeft<T>(int left) -> T` — Sets the left padding.
- `PadTop<T>(int top) -> T` — Sets the top padding.
- `PadRight<T>(int right) -> T` — Sets the right padding.
- `PadBottom<T>(int bottom) -> T` — Sets the bottom padding.
- `Padding<T>(int left, int top, int right, int bottom) -> T` — Sets the left, top, right and bottom padding.
- `Padding<T>(int horizontal, int vertical) -> T` — Sets the horizontal and vertical padding.
- `Padding<T>(Padding padding) -> T` — Sets the padding.

## `public interface IProfileEnricher`

*core* · `src/Spectre.Console/IProfileEnricher.cs`

Represents something that can enrich a profile.

**Properties**

- `string Name { get; }` — Gets the name of the enricher.

**Methods**

- `bool Enabled(IDictionary<string, string> environmentVariables)` — Gets whether or not this enricher is enabled.
- `void Enrich(Profile profile)` — Enriches the profile.

## `public interface IReadOnlyCapabilities : IReadOnlyAnsiCapabilities`

*core* · `src/Spectre.Console/IReadOnlyCapabilities.cs`

Represents (read-only) terminal capabilities.

**Properties**

- `bool Legacy { get; }` — Gets a value indicating whether or not this is a legacy console (cmd.exe) on an OS prior to Windows 10.
- `bool Interactive { get; }` — Gets a value indicating whether or not the console supports interaction.
- `bool Unicode { get; }` — Gets a value indicating whether or not the console supports Unicode.

## `public readonly struct Padding : IEquatable<Padding>`

*core* · `src/Spectre.Console/Padding.cs`

Represents padding.

**Constructors**

- `Padding(int size) : this(size, size, size, size)` — Initializes a new instance of the `Padding` struct.
- `Padding(int horizontal, int vertical) : this(horizontal, vertical, horizontal, vertical)` — Initializes a new instance of the `Padding` struct.
- `Padding(int left, int top, int right, int bottom)` — Initializes a new instance of the `Padding` struct.

**Properties**

- `int Left { get; }` — Gets the left padding.
- `int Top { get; }` — Gets the top padding.
- `int Right { get; }` — Gets the right padding.
- `int Bottom { get; }` — Gets the bottom padding.

**Operators / conversions**

- `static bool operator ==(Padding left, Padding right)` — Checks if two `Padding` instances are equal.
- `static bool operator !=(Padding left, Padding right)` — Checks if two `Padding` instances are not equal.

**Methods**

- `override bool Equals(object? obj)`
- `override int GetHashCode()`
- `bool Equals(Padding other)`
- `int GetWidth()` — Gets the padding width.
- `int GetHeight()` — Gets the padding height.

**Extension methods on this type** (call as `x.Method(...)`)

- `GetLeftSafe() -> int` — Gets the left padding.
- `GetRightSafe() -> int` — Gets the right padding.
- `GetTopSafe() -> int` — Gets the top padding.
- `GetBottomSafe() -> int` — Gets the bottom padding.

## `public sealed class Profile`

*core* · `src/Spectre.Console/Profile.cs`

Represents a console profile.

**Constructors**

- `Profile(IAnsiConsoleOutput @out, Capabilities capabilities, Encoding encoding)` — Initializes a new instance of the `Profile` class.

**Properties**

- `IReadOnlyCollection<string> Enrichers { get; }` — Gets the enrichers used to build this profile.
- `IAnsiConsoleOutput Out { get; set; }` — Gets or sets the out buffer.
- `Encoding Encoding { get; set; }` — Gets or sets the console output encoding.
- `int Width { get; set; }` — Gets or sets an explicit console width.
- `int Height { get; set; }` — Gets or sets an explicit console height.
- `Capabilities Capabilities { get; set; }` — Gets or sets the capabilities of the profile.

**Methods**

- `bool Supports(ColorSystem colorSystem)` — Checks whether the current profile supports the specified color system.

## `public sealed class ProfileEnrichment`

*core* · `src/Spectre.Console/Enrichment/ProfileEnrichment.cs`

Contains settings for profile enrichment.

**Properties**

- `bool UseDefaultEnrichers { get; set; }` = `true` — Gets or sets a value indicating whether or not any default enrichers should be added.
- `List<IProfileEnricher>? Enrichers { get; set; }` — Gets or sets the list of custom enrichers to use.

## `public class Recorder : IAnsiConsole, IDisposable`

*core* · `src/Spectre.Console/Recorder.cs`

A console recorder used to record output from a console.

**Constructors**

- `Recorder(IAnsiConsole console)` — Initializes a new instance of the `Recorder` class.

**Properties**

- `Profile Profile { get; }` — Gets the console profile.
- `IAnsiConsoleCursor Cursor { get; }` — Gets the console cursor.
- `IAnsiConsoleInput Input { get; }` — Gets the console input.
- `IExclusivityMode ExclusivityMode { get; }` — Gets the exclusivity mode.
- `RenderPipeline Pipeline { get; }` — Gets the render pipeline.

**Methods**

- `void Dispose()`
- `void Clear(bool home)` — Clears the console.
- `void Write(IRenderable renderable)` — Writes a `IRenderable` to the console.
- `void WriteAnsi(Action<AnsiWriter> action)` — Writes ANSI/VT escapes sequences to the console.
- `string Export(IAnsiConsoleEncoder encoder)` — Exports the recorded data.

**Extension methods on this type** (call as `x.Method(...)`)

- `ExportText() -> string` — Exports the recorded content as text.
- `ExportHtml() -> string` — Exports the recorded content as HTML.

**Extension methods inherited from shared interfaces/bases** (full signatures in `api/_shared-extensions.md`)

- via `IAnsiConsole`: `WriteAnsi`, `ToAnsi`, `Clear`, `WriteException`, `RunExclusive`, `Live`, `Markup`, `MarkupInterpolated`, `MarkupLine`, `MarkupLineInterpolated`, `Progress`, `Status`, `Prompt`, `Ask`, `Confirm`, `PromptAsync`, `AskAsync`, `ConfirmAsync`, `CreateRecorder`, `AlternateScreen`, `Write`, `WriteLine`

## `public readonly struct Region`

*core* · `src/Spectre.Console/Region.cs`

Represents a region.

**Constructors**

- `Region(int x, int y, int width, int height)` — Initializes a new instance of the `Region` struct.

**Properties**

- `int X { get; }` — Gets the x-coordinate.
- `int Y { get; }` — Gets the y-coordinate.
- `int Width { get; }` — Gets the width.
- `int Height { get; }` — Gets the height.

## `public readonly struct Size`

*core* · `src/Spectre.Console/Size.cs`

Represents a size.

**Constructors**

- `Size(int width, int height)` — Initializes a new instance of the `Size` struct.

**Properties**

- `int Width { get; }` — Gets the width.
- `int Height { get; }` — Gets the height.

## `public abstract partial class Spinner`

*core* · `src/Spectre.Console/Generated/Spectre.Console.SourceGenerator/Spectre.Console.SourceGenerator.Spinners.SpinnerGenerator/Spinner.Generated.g.cs`

Represents a spinner used in a `SpinnerColumn`.

**Properties**

- `abstract TimeSpan Interval { get; }` — Gets the update interval for the spinner.
- `abstract bool IsUnicode { get; }` — Gets a value indicating whether or not the spinner uses Unicode characters.
- `abstract IReadOnlyList<string> Frames { get; }` — Gets the spinner frames.

## `public static class Spinner.Known`

*core* · `src/Spectre.Console/Generated/Spectre.Console.SourceGenerator/Spectre.Console.SourceGenerator.Spinners.SpinnerGenerator/Spinner.Generated.g.cs`

Contains well-known spinners.

**Properties**

90 members like `static Spinner Default { get; }`: `Default`, `Ascii`, `Dots`, `Dots2`, `Dots3`, `Dots4`, `Dots5`, `Dots6`, `Dots7`, `Dots8`, `Dots9`, `Dots10`, `Dots11`, `Dots12`, `Dots13`, `Dots14`, `Dots8Bit`, `DotsCircle`, `Sand`, `Line`, `Line2`, `Pipe`, `SimpleDots`, `SimpleDotsScrolling`, `Star`, `Star2`, `Flip`, `Hamburger`, `GrowVertical`, `GrowHorizontal`, `Balloon`, `Balloon2`, `Noise`, `Bounce`, `BoxBounce`, `BoxBounce2`, `Triangle`, `Binary`, `Arc`, `Circle`, `SquareCorners`, `CircleQuarters`, `CircleHalves`, `Squish`, `Toggle`, `Toggle2`, `Toggle3`, `Toggle4`, `Toggle5`, `Toggle6`, `Toggle7`, `Toggle8`, `Toggle9`, `Toggle10`, `Toggle11`, `Toggle12`, `Toggle13`, `Arrow`, `Arrow2`, `Arrow3`, `BouncingBar`, `BouncingBall`, `Smiley`, `Monkey`, `Hearts`, `Clock`, `Earth`, `Material`, `Moon`, `Runner`, `Pong`, `Shark`, `Dqpb`, `Weather`, `Christmas`, `Grenade`, `Point`, `Layer`, `BetaWave`, `FingerDance`, `FistBump`, `SoccerHeader`, `Mindblown`, `Speaker`, `OrangePulse`, `BluePulse`, `OrangeBluePulse`, `TimeTravel`, `Aesthetic`, `DwarfFortress`

## `public abstract partial class TableBorder`

*core* · `src/Spectre.Console/TableBorder.cs`

Represents a border.

**Properties**

- `virtual bool Visible { get; }` = `true` — Gets a value indicating whether or not the border is visible.
- `virtual TableBorder? SafeBorder { get; }` = `null` — Gets the safe border for this border or `null` if none exist.
- `virtual bool SupportsRowSeparator { get; }` = `true` — Gets a value indicating whether the border supports row separators or not.
- `virtual bool UsePadding { get; }` = `true` — Gets a value indicating whether or not the border uses cell padding.
- `static TableBorder None { get; }` = `new NoTableBorder()` — Gets an invisible border.
- `static TableBorder Ascii { get; }` = `new AsciiTableBorder()` — Gets an ASCII border.
- `static TableBorder Ascii2 { get; }` = `new Ascii2TableBorder()` — Gets an ASCII border.
- `static TableBorder AsciiDoubleHead { get; }` = `new AsciiDoubleHeadTableBorder()` — Gets an ASCII border with a double header border.
- `static TableBorder Square { get; }` = `new SquareTableBorder()` — Gets a square border.
- `static TableBorder Rounded { get; }` = `new RoundedTableBorder()` — Gets a rounded border.
- `static TableBorder Minimal { get; }` = `new MinimalTableBorder()` — Gets a minimal border.
- `static TableBorder MinimalHeavyHead { get; }` = `new MinimalHeavyHeadTableBorder()` — Gets a minimal border with a heavy head.
- `static TableBorder MinimalDoubleHead { get; }` = `new MinimalDoubleHeadTableBorder()` — Gets a minimal border with a double header border.
- `static TableBorder Simple { get; }` = `new SimpleTableBorder()` — Gets a simple border.
- `static TableBorder SimpleHeavy { get; }` = `new SimpleHeavyTableBorder()` — Gets a simple border with heavy lines.
- `static TableBorder Horizontal { get; }` = `new HorizontalTableBorder()` — Gets a horizontal border.
- `static TableBorder Heavy { get; }` = `new HeavyTableBorder()` — Gets a heavy border.
- `static TableBorder HeavyEdge { get; }` = `new HeavyEdgeTableBorder()` — Gets a border with a heavy edge.
- `static TableBorder HeavyHead { get; }` = `new HeavyHeadTableBorder()` — Gets a border with a heavy header.
- `static TableBorder Double { get; }` = `new DoubleTableBorder()` — Gets a double border.
- `static TableBorder DoubleEdge { get; }` = `new DoubleEdgeTableBorder()` — Gets a border with a double edge.
- `static TableBorder Minimalist { get; }` = `new MinimalistTableBorder()` — Gets a minimalist border.
- `static TableBorder Markdown { get; }` = `new MarkdownTableBorder()` — Gets a markdown border.

**Methods**

- `abstract string GetPart(TableBorderPart part)` — Gets the string representation of a specified table border part.
- `virtual string GetColumnRow(TablePart part, IReadOnlyList<int> widths, IReadOnlyList<IColumn> columns)` — Gets a whole column row for the specific column row part.
- `protected (string Left, string Center, string Separator, string Right) GetTableParts(TablePart part)` — Gets the table parts used to render a specific table row.

**Extension methods on this type** (call as `x.Method(...)`)

- `GetSafeBorder(bool safe) -> TableBorder` — Gets the safe border for a border.

## `public abstract partial class TreeGuide`

*core* · `src/Spectre.Console/TreeGuide.cs`

Represents tree guide lines.

**Properties**

- `virtual TreeGuide? SafeTreeGuide { get; }` — Gets the safe guide lines or `null` if none exist.
- `static TreeGuide Ascii { get; }` = `new AsciiTreeGuide()` — Gets an `AsciiTreeGuide` instance.
- `static TreeGuide Line { get; }` = `new LineTreeGuide()` — Gets a `LineTreeGuide` instance.
- `static TreeGuide DoubleLine { get; }` = `new DoubleLineTreeGuide()` — Gets a `DoubleLineTreeGuide` instance.
- `static TreeGuide BoldLine { get; }` = `new BoldLineTreeGuide()` — Gets a `BoldLineTreeGuide` instance.

**Methods**

- `abstract string GetPart(TreeGuidePart part)` — Get the set of characters used to render the corresponding `TreeGuidePart`.

**Extension methods on this type** (call as `x.Method(...)`)

- `GetSafeTreeGuide(bool safe) -> TreeGuide` — Gets the safe border for a border.

## `public sealed class ValidationResult`

*core* · `src/Spectre.Console/ValidationResult.cs`

Represents a validation result.

**Properties**

- `bool Successful { get; }` — Gets a value indicating whether or not validation was successful.
- `string? Message { get; }` — Gets the validation error message.

**Methods**

- `static ValidationResult Success()` — Returns a `ValidationResult` representing successful validation.
- `static ValidationResult Error(string? message = null)` — Returns a `ValidationResult` representing a validation error.

## `public enum CursorDirection`

*core* · `src/Spectre.Console/CursorDirection.cs`

Represents cursor direction.

**Values**

- `Up` — Moves cursor up.
- `Down` — Moves cursor down.
- `Left` — Moves cursor left.
- `Right` — Moves cursor right.

## `public enum HorizontalAlignment`

*core* · `src/Spectre.Console/HorizontalAlignment.cs`

Represents horizontal alignment.

**Values**

- `Left` — Left aligned.
- `Center` — Centered.
- `Right` — Right aligned.

## `public enum InteractionSupport`

*core* · `src/Spectre.Console/InteractionSupport.cs`

Determines interactivity support.

**Values**

- `Detect = 0` — Interaction support should be detected by the system.
- `Yes = 1` — Interactivity is supported.
- `No = 2` — Interactivity is not supported.

## `public enum Justify`

*core* · `src/Spectre.Console/Justify.cs`

Represents text justification.

**Values**

- `Left = 0` — Left justified.
- `Right = 1` — Right justified.
- `Center = 2` — Centered.

## `public enum Overflow`

*core* · `src/Spectre.Console/Overflow.cs`

Represents text overflow.

**Values**

- `Fold = 0` — Put any excess characters on the next line.
- `Crop = 1` — Truncates the text at the end of the line.
- `Ellipsis = 2` — Truncates the text at the end of the line and also inserts an ellipsis character.

## `public enum VerticalAlignment`

*core* · `src/Spectre.Console/VerticalAlignment.cs`

Represents vertical alignment.

**Values**

- `Top` — Top aligned.
- `Middle` — Middle aligned.
- `Bottom` — Bottom aligned.

## `public enum VerticalOverflow`

*core* · `src/Spectre.Console/VerticalOverflow.cs`

Represents vertical overflow.

**Values**

- `Crop = 0` — Crop overflow.
- `Ellipsis = 1` — Add an ellipsis at the end.
- `Visible = 2` — Do not do anything about overflow.

## `public enum VerticalOverflowCropping`

*core* · `src/Spectre.Console/VerticalOverflowCropping.cs`

Represent vertical overflow cropping.

**Values**

- `Top = 0` — Crops the top.
- `Bottom = 1` — Crops the bottom.

