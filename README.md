<p align="center">
  <img src="b4n1secrets_presentation.png" alt="B4N1 Net — Sovereign transport. Sealed frames. Zero trust." width="100%" />
</p>

<div align="center">

# 📦 b4n1-secrets

**Sovereign transport. Sealed UDP frames with HMAC, AEAD and acknowledgements — one native core, six SDK wrappers. No third-party broker, no cloud dependency, no telemetry.**

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/b4n1-secrets.svg)](https://www.npmjs.com/package/b4n1-secrets)
[![NuGet](https://img.shields.io/nuget/v/B4n1Net.svg)](https://www.nuget.org/packages/B4n1Net)
[![RubyGems](https://img.shields.io/gem/v/b4n1secrets.svg)](https://rubygems.org/gems/b4n1secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)
[![Go Reference](https://pkg.go.dev/badge/github.com/B4N1-com/b4n1-secrets/sdks/go.svg)](https://pkg.go.dev/github.com/B4N1-com/b4n1-secrets/sdks/go)
[![Tests](https://img.shields.io/badge/tests-51%20passing-brightgreen)](https://github.com/B4N1-com/b4n1-secrets)

</div>

---

## 📦 Installation — 6 registries, 1 core

| Registry | Language | Package | Command |
|----------|----------|---------|---------|
| **PyPI** | Python 3.10+ | `b4n1-secrets` | `pip install b4n1-secrets` |
| **npm** | Node.js | `b4n1-secrets` | `npm install b4n1-secrets` |
| **NuGet** | .NET / C# | `B4n1Net` | `dotnet add package B4n1Net` |
| **RubyGems** | Ruby | `b4n1secrets` | `gem install b4n1secrets` |
| **Packagist** | PHP 8.1+ | `b4n1/b4n1-secrets` | `composer require b4n1/b4n1-secrets` |
| **Go** | Go 1.21+ | `b4n1-secrets/sdks/go` | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

All six packages ship the **same native core** (pre-compiled, no compiler needed). The SDKs are thin wrappers that spawn the bundled binary.

---

## 🚀 Quick Start

```python
# Python
from b4n1secrets import B4n1Net
net = B4n1Net()
print(net.info())
```

```javascript
// Node.js
const { B4n1Net } = require('b4n1-secrets');
const net = new B4n1Net();
console.log(net.info());
```

```csharp
// .NET / C#
using B4n1Net;
var net = new B4n1NetClient();
Console.WriteLine(net.Info());
```

```ruby
# Ruby
require 'b4n1secrets'
net = B4n1Net.new
puts net.info
```

```php
// PHP
$net = new \B4n1Net\Client();
echo $net->info();
```

```go
// Go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
net := b4n1secrets.New()
fmt.Println(net.Info())
```

---

## ⚙️ Configuration

The SDK resolves the native binary automatically. Override with an environment variable:

```bash
export B4N1NET_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

---

## 🖥 Platform Support

| Platform | Architectures |
|----------|---------------|
| **Linux** | x86_64 |

Pre-compiled binaries for additional platforms (macOS, Windows) are tracked as a follow-up.

---

## 📄 License

Business Source License 1.1 — see [LICENSE](LICENSE) and [EULA.txt](EULA.txt).