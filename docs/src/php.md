# PHP SDK

```bash
composer require b4n1/b4n1-secrets
```

```php
<?php
require 'vendor/autoload.php';

use B4N1\Secrets\SecretsClient;

$client = new SecretsClient();
echo $client->version(), PHP_EOL;

$client->set('.secrets', 'app/API_KEY', 'sk_live_...', ['prod']);
$value = $client->get('.secrets', 'app/API_KEY');
print_r($client->list('.secrets'));
```

## Injecting into a subprocess

```php
$client->run('.secrets', ['OPENAI_KEY' => 'b4n1-ia-provider/API_KEY'], ['php', 'agent.php']);
```

## Notes

- PHP 7.4 or newer; no extension required.
- `bin/b4n1secrets` in the package is a launcher that picks the platform binary.
- `B4N1SECRETS_BIN_PATH` overrides resolution, as in every other SDK.
