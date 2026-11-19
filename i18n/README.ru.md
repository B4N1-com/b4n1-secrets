# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 Полное руководство — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · офлайн, внутри двоичного файла: `b4n1-secrets docs`

Суверенное автономное хранилище — зашифрованные секреты, подлежащие передаче.

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** — это автономное секретное хранилище, работающее в автономном режиме. Каждое значение шифруется индивидуально (XChaCha20-Poly1305 + Argon2id) и сохраняется в одном файле YAML (`secrets.enc.yaml`), который вы передаете в git. Парольная фраза никогда не затрагивает диск — она хранится только в оперативной памяти через демон, и `close` вытирает его.

Никакого SaaS. Никакого облака. Никакой телеметрии. Один собственный двоичный файл, семь оболочек SDK.

## Установка — 7 реестров, 1 ядро

| Реестр | Язык | Упаковка | Команда |
|----------|----------|---------|---------|
| ПиПИ | Питон 3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| НПМ | Node.js | @b4n1/секреты | `npm install @b4n1/secrets` |
| NuGet | .NET/С# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| RubyGems | Руби | b4n1-secrets | `gem install b4n1-secrets` |
| Упаковщик | PHP 7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| Идти | Перейти 1.21+ | b4n1-secrets/sdks/иди | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

Все пакеты поставляются с одним и тем же собственным ядром (предварительно скомпилированным, компилятор не требуется). SDK представляют собой тонкие оболочки, которые порождают связанный двоичный файл.

## Быстрый старт

### Питон
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

### .NET/С#
```csharp
using B4N1.Secrets;
var client = new SecretsClient();
Console.WriteLine(client.Version());
```

### Руби
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

### Идти
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## Использование интерфейса командной строки

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

## Конфигурация

SDK автоматически разрешает собственный двоичный файл. Переопределить с помощью переменной среды:

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## Модель безопасности

- **mlock**: главный ключ заблокирован в оперативной памяти (не подлежит замене на диск).
- **Обнуление**: клавиши стираются при закрытии.
- **Шифрование по значению**: каждый секрет шифруется независимо.
- **`run` глагол**: секреты внедряются как переменные окружения дочерних процессов — никогда не проходят через стандартный вывод/терминал.
- **Нет сети**: полностью автономный режим, без телеметрии, без облака.

## Поддержка платформы

| Платформа | Архитектуры |
|----------|---------------|
| Линукс | x86_64, аарх64 |
| macOS | x86_64, рука64 |
| Окна | x86_64 |

## Лицензия

Лицензия Business Source 1.1 — см. ЛИЦЕНЗИЮ и EULA.txt.