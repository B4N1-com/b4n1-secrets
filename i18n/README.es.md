# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 Manual completo — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · fuera de línea, dentro del binario: `b4n1-secrets docs`

Bóveda soberana fuera de línea: secretos cifrados comprometibles.

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** es una bóveda secreta autónoma y fuera de línea. Cada valor se cifra individualmente (XChaCha20-Poly1305 + Argon2id) y se almacena en un único archivo YAML (`secrets.enc.yaml`) que te comprometes con git. La frase de contraseña nunca toca el disco; sólo vive en la RAM a través de un demonio, y `close` lo limpia.

Sin SaaS. Ninguna nube. Sin telemetría. Un binario nativo, siete contenedores SDK.

## Instalación: 7 registros, 1 núcleo

| Registro | Idioma | Paquete | Dominio |
|----------|----------|---------|---------|
| PyPI | Pitón 3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| npm | Nodo.js | @b4n1/misterios | `npm install @b4n1/secrets` |
| NuGet | .NET/C# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| rubígemas | Rubí | b4n1-secrets | `gem install b4n1-secrets` |
| empaquetador | PHP 7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| Ir | Ir 1.21+ | b4n1-secrets/sdks/ir | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

Todos los paquetes incluyen el mismo núcleo nativo (precompilado, no se necesita compilador). Los SDK son envoltorios finos que generan el binario incluido.

## Inicio rápido

### Pitón
```python
from b4n1secrets import SecretsClient
client = SecretsClient()
print(client.version())
print(client.list(".secrets"))
```

### Nodo.js
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

### Rubí
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

## Uso de CLI

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

## Configuración

El SDK resuelve el binario nativo automáticamente. Anular con una variable de entorno:

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## Modelo de seguridad

- **mlock**: La clave maestra está bloqueada en la RAM (no se puede intercambiar con el disco)
- **Poner a cero**: las teclas se borran al cerrar
- **Cifrado por valor**: cada secreto se cifra de forma independiente
- **`run` verbo**: Secretos inyectados como variables de entorno de procesos secundarios; nunca pasen por stdout/terminal
- **Sin red**: Totalmente fuera de línea, sin telemetría, sin nube

## Soporte de plataforma

| Plataforma | Arquitecturas |
|----------|---------------|
| linux | x86_64, aarch64 |
| macos | x86_64, brazo64 |
| ventanas | x86_64 |

## Licencia

Licencia de origen empresarial 1.1: consulte LICENCIA y CLUF.txt.