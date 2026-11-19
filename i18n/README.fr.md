# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 Manuel complet — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · hors ligne, à l'intérieur du binaire : `b4n1-secrets docs`

Coffre-fort souverain hors ligne : secrets cryptés pouvant être validés.

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** est un coffre-fort secret autonome et hors ligne. Chaque valeur est chiffrée individuellement (XChaCha20-Poly1305 + Argon2id) et stockée dans un seul fichier YAML (`secrets.enc.yaml`) que vous vous engagez à git. La phrase secrète ne touche jamais le disque : elle réside uniquement dans la RAM via un démon, et `close` l'essuie.

Pas de SaaS. Pas de nuage. Pas de télémétrie. Un binaire natif, sept wrappers SDK.

## Installation - 7 registres, 1 noyau

| Enregistrement | Langue | Emballer | Commande |
|----------|----------|---------|---------|
| PyPI | Python3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| npm | Noeud.js | @b4n1/secrets | `npm install @b4n1/secrets` |
| NuGet | .NET/C# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| RubyGemmes | Rubis | b4n1-secrets | `gem install b4n1-secrets` |
| Packagiste | PHP7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| Aller | Allez 1.21+ | b4n1-secrets/sdks/aller | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

Tous les packages sont livrés avec le même noyau natif (précompilé, aucun compilateur n'est nécessaire). Les SDK sont des wrappers minces qui génèrent le binaire fourni.

## Démarrage rapide

### Python
```python
from b4n1secrets import SecretsClient
client = SecretsClient()
print(client.version())
print(client.list(".secrets"))
```

### Noeud.js
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

### Rubis
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

### Aller
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## Utilisation de la CLI

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

Le SDK résout automatiquement le binaire natif. Remplacer par une variable d'environnement :

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## Modèle de sécurité

- **mlock** : La clé principale est verrouillée dans la RAM (non échangeable sur le disque)
- **Zeroize** : les touches sont effacées à la fermeture
- **Chiffrement par valeur** : chaque secret est chiffré indépendamment
- **`run` verbe** : secrets injectés en tant que variables d'environnement de processus enfants – ne passent jamais par la sortie standard/terminal
- **Pas de réseau** : entièrement hors ligne, pas de télémétrie, pas de cloud

## Prise en charge de la plateforme

| Plate-forme | Architectures |
|----------|---------------|
| Linux | x86_64, aarch64 |
| macOS | x86_64, bras64 |
| Fenêtres | x86_64 |

## Licence

Licence Business Source 1.1 — voir LICENCE et EULA.txt.