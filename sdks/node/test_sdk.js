'use strict';

// Smoke test del wrapper Node de b4n1-secrets: el módulo carga, el motor
// empaquetado responde con su franja de versión y el help lista los verbos.
const assert = require('node:assert');
const { SecretsClient } = require('./index.js');

const client = new SecretsClient();
assert.strictEqual(typeof SecretsClient, 'function', 'SecretsClient debe exportarse');

const version = client.version();
assert.match(version, /secrets v?\d+\.\d+\.\d+/i, `version inesperada: ${version}`);

const help = client.help();
assert.match(help, /list/, 'help debe listar el verbo list');
assert.match(help, /get/, 'help debe listar el verbo get');

console.log(`ok ${version}`);
