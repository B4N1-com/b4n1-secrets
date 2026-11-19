# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 Manuale completo — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · offline, all'interno del binario: `b4n1-secrets docs`

Deposito offline sovrano: segreti crittografati confermabili.

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** è un caveau segreto autonomo, offline-first. Ogni valore viene crittografato individualmente (XChaCha20-Poly1305 + Argon2id) e archiviato in un singolo file YAML (`secrets.enc.yaml`) che ti impegni su git. La passphrase non tocca mai il disco: risiede solo nella RAM tramite un demone e `close` lo pulisce.

Niente SaaS. Nessuna nuvola. Nessuna telemetria. Un binario nativo, sette wrapper SDK.

## Installazione: 7 registri, 1 core

| Registro | Lingua | Pacchetto | Comando |
|----------|----------|---------|---------|
| PyPI | Python 3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| npm | Node.js | @b4n1/segreti | `npm install @b4n1/secrets` |
| NuGet | .NET/C# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| RubyGems | Rubino | b4n1-secrets | `gem install b4n1-secrets` |
| Packagista | PHP7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| Andare | Vai 1.21+ | b4n1-secrets/sdks/vai | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

Tutti i pacchetti vengono forniti con lo stesso core nativo (precompilato, non è necessario alcun compilatore). Gli SDK sono wrapper sottili che generano il file binario in bundle.

## Avvio rapido

### Pitone
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

### .NET/C#
```csharp
using B4N1.Secrets;
var client = new SecretsClient();
Console.WriteLine(client.Version());
```

### Rubino
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

### Andare
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## Utilizzo della CLI

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

## Configurazione

L'SDK risolve automaticamente il file binario nativo. Sostituisci con una variabile di ambiente:

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## Modello di sicurezza

- **mlock**: la chiave principale è bloccata nella RAM (non scambiabile su disco)
- **Azzera**: i tasti vengono cancellati alla chiusura
- **Crittografia per valore**: ogni segreto crittografato in modo indipendente
- **`run` verbo**: segreti inseriti come variabili env dei processi secondari: non passano mai attraverso stdout/terminale
- **Nessuna rete**: completamente offline, senza telemetria, senza cloud

## Supporto della piattaforma

| Piattaforma | Architetture |
|----------|---------------|
| Linux | x86_64, aarch64 |
| macOS | x86_64, arm64 |
| Finestre | x86_64 |

## Licenza

Licenza Business Source 1.1: vedere LICENZA e EULA.txt.