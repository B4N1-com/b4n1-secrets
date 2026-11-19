# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 Manual completo — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · offline, dentro do binário: `b4n1-secrets docs`

Cofre offline soberano — segredos criptografados que podem ser confirmados.

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** é um cofre secreto independente e offline. Cada valor é criptografado individualmente (XChaCha20-Poly1305 + Argon2id) e armazenado em um único arquivo YAML (`secrets.enc.yaml`) que você compromete com o git. A senha nunca toca o disco - ela reside apenas na RAM por meio de um daemon e `close` limpa.

Sem SaaS. Sem nuvem. Sem telemetria. Um binário nativo, sete wrappers SDK.

## Instalação — 7 registros, 1 núcleo

| Registro | Linguagem | Pacote | Comando |
|----------|----------|---------|---------|
| PyPI | Python 3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| npm | Node.js | @b4n1/segredos | `npm install @b4n1/secrets` |
| NuGet | .NET/C# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| Ruby Gems | Rubi | b4n1-secrets | `gem install b4n1-secrets` |
| Empacotador | PHP 7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| Ir | Vá para 1,21+ | b4n1-secrets/sdks/go | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

Todos os pacotes vêm com o mesmo núcleo nativo (pré-compilado, sem necessidade de compilador). Os SDKs são wrappers finos que geram o binário empacotado.

## Início rápido

### Pitão
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

### Rubi
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

### Ir
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## Uso CLI

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

## Configuração

O SDK resolve o binário nativo automaticamente. Substitua por uma variável de ambiente:

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## Modelo de segurança

- **mlock**: A chave mestra está bloqueada na RAM (não pode ser trocada pelo disco)
- **Zeroize**: as teclas são apagadas ao fechar
- **Criptografia por valor**: cada segredo criptografado de forma independente
- **`run` verbo **: segredos injetados como env vars de processos filhos - nunca passam por stdout/terminal
- **Sem rede**: Totalmente offline, sem telemetria, sem nuvem

## Suporte de plataforma

| Plataforma | Arquiteturas |
|----------|---------------|
| Linux | x86_64, aarch64 |
| macOS | x86_64, braço64 |
| Windows | x86_64 |

## Licença

Licença de origem comercial 1.1 — consulte LICENSE e EULA.txt.