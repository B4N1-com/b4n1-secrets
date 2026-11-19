# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 Vollständiges Handbuch — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · offline, innerhalb der Binärdatei: `b4n1-secrets docs`

Souveräner Offline-Tresor – übertragbare verschlüsselte Geheimnisse.

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** ist ein in sich geschlossener geheimer Tresor, der zuerst offline ist. Jeder Wert wird einzeln verschlüsselt (XChaCha20-Poly1305 + Argon2id) und in einer einzigen YAML-Datei gespeichert (`secrets.enc.yaml`), dass Sie sich zu Git verpflichten. Die Passphrase berührt niemals die Festplatte – sie bleibt nur im RAM über einen Daemon und `close` wischt es ab.

Kein SaaS. Keine Wolke. Keine Telemetrie. Eine native Binärdatei, sieben SDK-Wrapper.

## Installation – 7 Register, 1 Kern

| Registrierung | Sprache | Paket | Befehl |
|----------|----------|---------|---------|
| PyPI | Python 3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| npm | Node.js | @b4n1/geheimnisse | `npm install @b4n1/secrets` |
| NuGet | .NET / C# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| RubyGems | Rubin | b4n1-secrets | `gem install b4n1-secrets` |
| Paketist | PHP 7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| Gehen | Gehen Sie 1.21+ | b4n1-secrets/sdks/go | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

Alle Pakete enthalten den gleichen nativen Kern (vorkompiliert, kein Compiler erforderlich). Die SDKs sind Thin Wrapper, die die gebündelte Binärdatei erzeugen.

## Schnellstart

### Python
```python
from b4n1secrets import SecretsClient
client = SecretsClient()
print(client.version())
print(client.list(".secrets"))
```

### Node.js
```javascript
const { SecretsClient } = require('@b4n1/secrets');
const client = new SecretsClient();
console.log(client.version());
```

### .NET / C#
```csharp
using B4N1.Secrets;
var client = new SecretsClient();
Console.WriteLine(client.Version());
```

### Rubin
```ruby
require 'b4n1secrets'
client = B4n1Secrets::Client.new
puts client.version
```

### PHP
```php
$client = new \B4N1\Secrets\SecretsClient();
echo $client->version();
```

### Gehen
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## CLI-Nutzung

```bash
# Initialize a vault
echo "my-passphrase-12chars" | b4n1-secrets init .secrets

# Unlock (passphrase stays in RAM)
echo "my-passphrase-12chars" | b4n1-secrets unlock .secrets

# Set a secret
b4n1-secrets set .secrets app/API_KEY --value sk_live_... --tags prod

# Get a secret
b4n1-secrets get .secrets app/API_KEY

# List secrets (never shows values)
b4n1-secrets list .secrets

# Inject secret into a child process (never touches stdout)
b4n1-secrets run .secrets --secret API_KEY=app/API_KEY -- python my_agent.py

# Close (wipe from RAM)
b4n1-secrets close .secrets
```

## Konfiguration

Das SDK löst die native Binärdatei automatisch auf. Mit einer Umgebungsvariablen überschreiben:

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## Sicherheitsmodell

- **mlock**: Der Hauptschlüssel ist im RAM gesperrt (nicht auf die Festplatte austauschbar)
- **Nullsetzen**: Tasten werden beim Schließen gelöscht
- **Verschlüsselung pro Wert**: Jedes Geheimnis wird unabhängig verschlüsselt
- **`run` Verb**: Geheimnisse, die als Umgebungsvariablen von untergeordneten Prozessen eingefügt werden – passieren niemals stdout/terminal
- **Kein Netzwerk**: Vollständig offline, keine Telemetrie, keine Cloud

## Plattformunterstützung

| Plattform | Architekturen |
|----------|---------------|
| Linux | x86_64, aarch64 |
| macOS | x86_64, arm64 |
| Windows | x86_64 |

## Lizenz

Business Source License 1.1 – siehe LIZENZ und EULA.txt.