# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 전체 매뉴얼 — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · 오프라인, 바이너리 내부: `b4n1-secrets docs`

Sovereign Offline Vault — 커밋 가능한 암호화된 비밀입니다.

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** 독립형 오프라인 우선 비밀 금고입니다. 모든 값은 개별적으로 암호화되고(XChaCha20-Poly1305 + Argon2id) 단일 YAML 파일(`secrets.enc.yaml`) git에 커밋합니다. 암호는 디스크에 닿지 않습니다. 데몬을 통해 RAM에만 존재하며, `close` 그것을 닦는다.

SaaS가 없습니다. 클라우드가 없습니다. 원격 측정이 없습니다. 네이티브 바이너리 1개, SDK 래퍼 7개.

## 설치 — 레지스트리 7개, 코어 1개

| 기재 | 언어 | 패키지 | 명령 |
|----------|----------|---------|---------|
| PyPI | 파이썬 3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| npm | Node.js | @b4n1/기미 | `npm install @b4n1/secrets` |
| NuGet | .NET/C# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| RubyGems | 루비 | b4n1-secrets | `gem install b4n1-secrets` |
| 포장 전문가 | PHP 7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| 가다 | 1.21+로 이동 | b4n1-secrets/sdks/이동 | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

모든 패키지는 동일한 기본 코어를 제공합니다(사전 컴파일되어 컴파일러가 필요하지 않음). SDK는 번들 바이너리를 생성하는 씬 래퍼입니다.

## 빠른 시작

### 파이썬
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

### 루비
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

### 가다
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## CLI 사용법

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

## 구성

SDK는 기본 바이너리를 자동으로 확인합니다. 환경 변수로 재정의합니다.

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## 보안 모델

- **mlock**: 마스터 키가 RAM에 잠겨 있습니다(디스크로 교체할 수 없음).
- **제로화**: 닫으면 키가 지워집니다.
- **값별 암호화**: 각 비밀은 독립적으로 암호화됩니다.
- **`run` 동사**: 하위 프로세스의 환경 변수로 주입된 비밀 — stdout/terminal을 통과하지 않음
- **네트워크 없음**: 완전 오프라인, 원격 측정 없음, 클라우드 없음

## 플랫폼 지원

| 플랫폼 | 아키텍처 |
|----------|---------------|
| 리눅스 | x86_64, aarch64 |
| macOS | x86_64, arm64 |
| 윈도우 | x86_64 |

## 특허

비즈니스 소스 라이선스 1.1 - LICENSE 및 EULA.txt를 참조하세요.