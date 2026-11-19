# Python SDK

```bash
pip install b4n1-secrets
```

```python
from b4n1secrets import SecretsClient

client = SecretsClient()           # resolves the bundled binary
print(client.version())

# Vault operations
client.init(".secrets")            # passphrase read from stdin
client.unlock(".secrets")
client.set(".secrets", "app/API_KEY", "sk_live_...", tags=["prod"])
value = client.get(".secrets", "app/API_KEY")
names = client.list(".secrets")
client.close(".secrets")
```

## Injecting into a subprocess

```python
client.run(
    ".secrets",
    secrets={"OPENAI_KEY": "b4n1-ia-provider/API_KEY"},
    command=["python", "agent.py"],
)
```

The child receives the variable in its environment; nothing is printed.

## Errors

Every failure raises `SecretsError` carrying the process exit code and stderr.
Codes match the CLI table: `2` key missing or expired, `3` weak passphrase,
`4` corrupt vault or unsupported platform.

## Binary override

```bash
export B4N1SECRETS_BIN_PATH=/opt/b4n1/b4n1secrets-linux-amd64
```
