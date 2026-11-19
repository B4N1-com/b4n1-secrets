# Node.js SDK

```bash
npm install @b4n1/secrets
```

```javascript
const { SecretsClient } = require('@b4n1/secrets');

const client = new SecretsClient();
console.log(client.version());

client.set('.secrets', 'app/API_KEY', 'sk_live_...', { tags: ['prod'] });
const value = client.get('.secrets', 'app/API_KEY');
console.log(client.list('.secrets'));
```

## Injecting into a subprocess

```javascript
client.run('.secrets', { OPENAI_KEY: 'b4n1-ia-provider/API_KEY' }, ['node', 'agent.js']);
```

## Notes

- Synchronous by design: a secret read is a startup concern, not a hot path.
- The package ships every platform binary; `process.platform` picks one.
- Override with `B4N1SECRETS_BIN_PATH` when you need a pinned build.
