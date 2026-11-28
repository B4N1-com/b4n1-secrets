<p align="center">
  <img src="b4n1secrets_presentation.png" alt="B4N1 Secrets — Sovereign offline vault" width="100%">
</p>

# b4n1-secrets

[English](README.md) · [Español](i18n/README.es.md) · [Deutsch](i18n/README.de.md) · [Français](i18n/README.fr.md) · [Italiano](i18n/README.it.md) · [Português (BR)](i18n/README.pt-BR.md) · [Русский](i18n/README.ru.md) · [العربية](i18n/README.ar.md) · [हिन्दी](i18n/README.hi.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [中文](i18n/README.zh-CN.md)

> **📖 Full manual — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · offline, inside the binary: `b4n1-secrets docs`

Sovereign offline vault — committable encrypted secrets.

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![PyPI downloads](https://img.shields.io/pypi/dm/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![Pepy downloads](https://img.shields.io/pepy/dt/b4n1-secrets.svg)](https://pepy.tech/project/b4n1-secrets)
[![npm](https://img.shields.io/npm/v/@b4n1%2fsecrets.svg)](https://www.npmjs.com/package/@b4n1%2fsecrets)
[![npm downloads](https://img.shields.io/npm/dm/@b4n1%2fsecrets.svg)](https://www.npmjs.com/package/@b4n1%2fsecrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![NuGet downloads](https://img.shields.io/nuget/dt/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://img.shields.io/gem/v/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)
[![Go Reference](https://pkg.go.dev/badge/github.com/b4n1-com/b4n1-secrets/sdks/go.svg)](https://pkg.go.dev/github.com/b4n1-com/b4n1-secrets/sdks/go)


**b4n1-secrets** is a self-contained, offline-first secret vault. Every value is encrypted individually (XChaCha20-Poly1305 + Argon2id) and stored in a single YAML file (`secrets.enc.yaml`) that you commit to git. The passphrase never touches disk — it lives only in RAM via a daemon, and `close` wipes it.

No SaaS. No cloud. No telemetry. One native binary, seven SDK wrappers.

## Installation — 7 registries, 1 core

| Registry | Language | Package | Command |
|----------|----------|---------|---------|
| PyPI | Python 3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| npm | Node.js | @b4n1/secrets | `npm install @b4n1/secrets` |
| NuGet | .NET / C# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| RubyGems | Ruby | b4n1-secrets | `gem install b4n1-secrets` |
| Packagist | PHP 7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| Go | Go 1.21+ | b4n1-secrets/sdks/go | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

All packages ship the same native core (pre-compiled, no compiler needed). The SDKs are thin wrappers that spawn the bundled binary.

## Quick Start

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

### Ruby
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

### Go
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## CLI Usage

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

## Configuration

The SDK resolves the native binary automatically. Override with an environment variable:

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## Security Model

- **mlock**: The master key is locked in RAM (not swappable to disk)
- **Zeroize**: Keys are wiped on close
- **Per-value encryption**: Each secret encrypted independently
- **`run` verb**: Secrets injected as env vars of child processes — never pass through stdout/terminal
- **No network**: Fully offline, no telemetry, no cloud

## Platform Support

| Platform | Architectures |
|----------|---------------|
| Linux | x86_64, aarch64 |
| macOS | x86_64, arm64 |
| Windows | x86_64 |

## License

Business Source License 1.1 — see LICENSE and EULA.txt.