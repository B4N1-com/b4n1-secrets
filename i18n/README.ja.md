# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 完全なマニュアル — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · オフライン、バイナリ内: `b4n1-secrets docs`

Sovereign Offline Vault — コミット可能な暗号化されたシークレット。

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** は、自己完結型のオフラインファーストの Secret Vault です。すべての値は個別に暗号化され (XChaCha20-Poly1305 + Argon2id)、単一の YAML ファイルに保存されます (`secrets.enc.yaml`) git にコミットします。パスフレーズはディスクに触れることはありません。デーモンを介して RAM 内にのみ存在します。 `close` それを拭きます。

SaaS はありません。雲はありません。テレメトリはありません。 1 つのネイティブ バイナリ、7 つの SDK ラッパー。

## インストール — 7 レジストリ、1 コア

| レジストリ | 言語 | パッケージ | 指示 |
|----------|----------|---------|---------|
| PyPI | Python 3.8以降 | b4n1-secrets | `pip install b4n1-secrets` |
| npm | Node.js | @b4n1/秘密 | `npm install @b4n1/secrets` |
| NuGet | .NET / C# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| ルビージェムズ | ルビー | b4n1-secrets | `gem install b4n1-secrets` |
| 梱包担当者 | PHP 7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| 行く | ゴー 1.21+ | b4n1-secrets/sdks/go | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

すべてのパッケージには同じネイティブ コアが同梱されています (コンパイル済み、コンパイラは必要ありません)。 SDK は、バンドルされたバイナリを生成する薄いラッパーです。

## クイックスタート

### パイソン
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

### ルビー
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

### 行く
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## CLIの使用法

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

## 構成

SDK はネイティブ バイナリを自動的に解決します。環境変数でオーバーライドします。

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## セキュリティモデル

- **mlock**: マスター キーは RAM にロックされています (ディスクに交換できません)
- **ゼロ化**: 閉じるときにキーが消去されます
- **値ごとの暗号化**: 各シークレットは個別に暗号化されます
- **`run` 動詞**: シークレットは子プロセスの環境変数として注入されます - stdout/ターミナルを決して通過しません
- **ネットワークなし**: 完全にオフライン、テレメトリ、クラウドなし

## プラットフォームのサポート

| プラットフォーム | アーキテクチャ |
|----------|---------------|
| Linux | x86_64、aarch64 |
| macOS | x86_64、arm64 |
| 窓 | x86_64 |

## ライセンス

ビジネス ソース ライセンス 1.1 — LICENSE および EULA.txt を参照してください。