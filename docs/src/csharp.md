# .NET SDK

```bash
dotnet add package b4n1-secrets
```

```csharp
using B4N1.Secrets;

var client = new SecretsClient();
Console.WriteLine(client.Version());

client.Set(".secrets", "app/API_KEY", "sk_live_...", tags: new[] { "prod" });
var value = client.Get(".secrets", "app/API_KEY");
foreach (var name in client.List(".secrets"))
    Console.WriteLine(name);
```

## Injecting into a subprocess

```csharp
client.Run(".secrets",
    new Dictionary<string, string> { ["OPENAI_KEY"] = "b4n1-ia-provider/API_KEY" },
    new[] { "dotnet", "run" });
```

## Notes

- Targets `netstandard2.0`, so it works from .NET Framework 4.6.2 upward.
- Failures throw `SecretsException` with `ExitCode` and `StandardError`.
- The bundled binary is extracted next to the assembly on first use.
