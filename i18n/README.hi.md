# b4n1-secrets

[English](../README.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português (BR)](README.pt-BR.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [中文](README.zh-CN.md)

> **📖 पूर्ण मैनुअल — [b4n1-com.github.io/b4n1-secrets](https://b4n1-com.github.io/b4n1-secrets/)** · ऑफ़लाइन, बाइनरी के अंदर: `b4n1-secrets docs`

सॉवरेन ऑफ़लाइन वॉल्ट - प्रतिबद्ध एन्क्रिप्टेड रहस्य।

![b4n1-secrets](b4n1secrets_presentation.png)

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-secrets.svg)](https://pypi.org/project/b4n1-secrets/)
[![npm](https://img.shields.io/npm/v/@b4n1/secrets.svg)](https://www.npmjs.com/package/@b4n1/secrets)
[![NuGet](https://img.shields.io/nuget/v/b4n1-secrets.svg)](https://www.nuget.org/packages/b4n1-secrets)
[![RubyGems](https://badge.fury.io/rb/b4n1-secrets.svg)](https://rubygems.org/gems/b4n1-secrets)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-secrets.svg)](https://packagist.org/packages/b4n1/b4n1-secrets)


**b4n1-secrets** एक स्व-निहित, ऑफ़लाइन-प्रथम गुप्त तिजोरी है। प्रत्येक मान को व्यक्तिगत रूप से एन्क्रिप्ट किया गया है (XChaCha20-Poly1305 + Argon2id) और एक YAML फ़ाइल में संग्रहीत किया गया है (`secrets.enc.yaml`) कि आप गिट के लिए प्रतिबद्ध हैं। पासफ़्रेज़ कभी भी डिस्क को नहीं छूता - यह केवल डेमॉन के माध्यम से रैम में रहता है, और `close` उसे पोंछ देता है.

कोई सास नहीं. कोई बादल नहीं. कोई टेलीमेट्री नहीं. एक देशी बाइनरी, सात एसडीके रैपर।

## स्थापना - 7 रजिस्ट्रियाँ, 1 कोर

| रजिस्ट्री | भाषा | पैकेट | आज्ञा |
|----------|----------|---------|---------|
| पीईपीआई | पायथन 3.8+ | b4n1-secrets | `pip install b4n1-secrets` |
| NPM | नोड.जे.एस | @b4n1/रहस्य | `npm install @b4n1/secrets` |
| नुगेट | .नेट/सी# | b4n1-secrets | `dotnet add package b4n1-secrets` |
| रूबीजेम्स | रूबी | b4n1-secrets | `gem install b4n1-secrets` |
| पैकेजिस्ट | पीएचपी 7.4+ | b4n1/b4n1-secrets | `composer require b4n1/b4n1-secrets` |
| जाना | 1.21+ जाओ | b4n1-secrets/sdks/go | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

सभी पैकेज एक ही मूल कोर (पूर्व-संकलित, किसी कंपाइलर की आवश्यकता नहीं) शिप करते हैं। एसडीके पतले रैपर होते हैं जो बंडल बाइनरी को उत्पन्न करते हैं।

## त्वरित शुरुआत

### अजगर
```python
from b4n1secrets import SecretsClient
client = SecretsClient()
print(client.version())
print(client.list(".secrets"))
```

### नोड.जे.एस
```javascript
const { SecretsClient } = require('@b4n1/secrets');
const client = new SecretsClient();
console.log(client.version());
```

### .नेट/सी#
```csharp
using B4N1.Secrets;
var client = new SecretsClient();
Console.WriteLine(client.Version());
```

### रूबी
```ruby
require 'b4n1secrets'
client = B4n1Secrets::Client.new
puts client.version
```

### पीएचपी
```php
$client = new \B4N1\Secrets\SecretsClient();
echo $client->version();
```

### जाना
```go
import b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
client := b4n1secrets.NewClient()
v, _ := client.Version()
fmt.Println(v)
```

## सीएलआई उपयोग

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

## विन्यास

SDK मूल बाइनरी को स्वचालित रूप से हल करता है। पर्यावरण चर के साथ ओवरराइड करें:

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

## सुरक्षा मॉडल

- **mlock**: मास्टर कुंजी RAM में लॉक है (डिस्क में बदलने योग्य नहीं)
- **ज़ीरोइज़**: बंद करने पर कुंजियाँ मिटा दी जाती हैं
- **प्रति-मूल्य एन्क्रिप्शन**: प्रत्येक रहस्य स्वतंत्र रूप से एन्क्रिप्ट किया गया
- **`run` क्रिया**: रहस्यों को चाइल्ड प्रोसेस के एनवी वर्र्स के रूप में इंजेक्ट किया जाता है - कभी भी स्टडआउट/टर्मिनल से नहीं गुज़रता
- **कोई नेटवर्क नहीं**: पूरी तरह ऑफ़लाइन, कोई टेलीमेट्री नहीं, कोई क्लाउड नहीं

## प्लेटफार्म समर्थन

| प्लैटफ़ॉर्म | वास्तुकला |
|----------|---------------|
| लिनक्स | x86_64, आर्क64 |
| मैक ओएस | x86_64, आर्म64 |
| खिड़कियाँ | x86_64 |

## लाइसेंस

बिजनेस सोर्स लाइसेंस 1.1 - लाइसेंस और EULA.txt देखें।