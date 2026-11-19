# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 完整手册 — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · 离线，在二进制文件内： `b4n1-secrets docs`

主权离线保管库——可提交的加密秘密。

！[b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** 是一个独立的、离线优先的秘密金库。每个值都单独加密（XChaCha20-Poly1305 + Argon2id）并存储在单个 YAML 文件中（`secrets.enc.yaml`）您承诺使用 git。密码短语永远不会接触磁盘——它仅通过守护进程存在于 RAM 中，并且 `close` 擦拭它。

没有SaaS。没有云。没有遥测。一个本机二进制文件、七个 SDK 包装器。

## 安装 — 7 个注册表，1 个核心

| 登记处 | 语言 | 包裹 | 命令 |
|----------|----------|---------|---------|
| 皮伊 | Python 3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| 新项目管理 | Node.js | @b4n1/秘密 | `npm install @b4n1/secrets` |
| 努格特 | .NET / C# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| 红宝石 | 红宝石 | b4n1-secrets | `gem install b4n1-secrets` |
| 包装学家 | PHP 7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| 去 | 去1.21+ | b4n1-secrets/sdks/去 | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

所有软件包都附带相同的本机核心（预编译，无需编译器）。 SDK 是生成捆绑二进制文件的薄包装器。

## 快速入门

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

### 红宝石
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

### 去
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## CLI 用法

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

## 配置

SDK 自动解析本机二进制文件。使用环境变量覆盖：

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## 安全模型

- **mlock**：主密钥被锁定在 RAM 中（不可交换到磁盘）
- **归零**：关闭时按键被擦除
- **按值加密**：每个秘密都独立加密
- **`run` verb**：作为子进程的环境变量注入的秘密 - 永远不会通过标准输出/终端
- **无网络**：完全离线，无遥测，无云

## 平台支持

| 平台 | 架构 |
|----------|---------------|
| Linux | x86_64、aarch64 |
| macOS | x86_64、arm64 |
| 视窗 | x86_64 |

## 执照

商业源许可证 1.1 — 请参阅 LICENSE 和 EULA.txt。