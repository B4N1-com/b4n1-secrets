<?php
// Smoke test del wrapper PHP de b4n1-secrets: el motor empaquetado responde
// con su franja de versión.
require __DIR__ . "/../src/SecretsClient.php";

$client = new B4N1\Secrets\SecretsClient();
$version = $client->version();

if (!preg_match('/secrets v?\d+\.\d+\.\d+/i', $version)) {
    fwrite(STDERR, "version inesperada: {$version}\n");
    exit(1);
}

echo "ok {$version}\n";
