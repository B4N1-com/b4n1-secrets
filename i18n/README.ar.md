# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 الدليل كاملاً — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · غير متصل، داخل الثنائي: `b4n1-secrets docs`

قبو سيادي غير متصل بالإنترنت — أسرار مشفرة قابلة للالتزام.

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** عبارة عن قبو سري قائم بذاته وغير متصل بالإنترنت. يتم تشفير كل قيمة بشكل فردي (XChaCha20-Poly1305 + Argon2id) وتخزينها في ملف YAML واحد (`secrets.enc.yaml`) التي تلتزم بها git. عبارة المرور لا تمس القرص أبدًا - فهي تعيش فقط في ذاكرة الوصول العشوائي (RAM) عبر برنامج خفي، و `close` يمسحه.

لا ادارة العلاقات مع. لا سحابة. لا القياس عن بعد. ثنائي أصلي واحد، وسبعة أغلفة SDK.

## التثبيت - 7 سجلات، 1 الأساسية

| التسجيل | لغة | طَرد | يأمر |
|----------|----------|---------|---------|
| بايبي | بايثون 3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| npm | Node.js | @b4n1/أسرار | `npm install @b4n1/secrets` |
| نوجيت | صافي / سي # | b4n1-secrets | `dotnet add package b4n1-secrets` |
| روبيجيمز | روبي | b4n1-secrets | `gem install b4n1-secrets` |
| التعبئة والتغليف | PHP 7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| يذهب | الذهاب 1.21+ | b4n1-secrets/sdks/go | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

جميع الحزم تشحن نفس النواة الأصلية (مترجمة مسبقًا، لا حاجة إلى مترجم). إن حزم SDK عبارة عن أغلفة رفيعة تنتج الملف الثنائي المجمع.

## بداية سريعة

### بايثون
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

### صافي / سي #
```csharp
using B4N1.Secrets;
var client = new SecretsClient();
Console.WriteLine(client.Version());
```

### روبي
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

### يذهب
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## استخدام سطر الأوامر

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

## إعدادات

يقوم SDK بحل الملف الثنائي الأصلي تلقائيًا. التجاوز باستخدام متغير البيئة:

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## نموذج الأمان

- **mlock**: المفتاح الرئيسي مقفل في ذاكرة الوصول العشوائي (غير قابل للتبديل إلى القرص)
- **تصفير**: يتم مسح المفاتيح عند إغلاقها
- **التشفير حسب القيمة**: يتم تشفير كل سر بشكل مستقل
- **`run` الفعل**: الأسرار التي يتم إدخالها على شكل env vars للعمليات الفرعية - لا تمر أبدًا عبر stdout/terminal
- **لا توجد شبكة**: غير متصل بالإنترنت بالكامل، ولا يوجد قياس عن بعد، ولا توجد سحابة

## دعم المنصة

| منصة | أبنية |
|----------|---------------|
| لينكس | x86_64, aarch64 |
| ماك | x86_64, الذراع64 |
| ويندوز | x86_64 |

## رخصة

ترخيص مصدر الأعمال 1.1 — راجع LICENSE وEULA.txt.