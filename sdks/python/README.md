# b4n1-secrets

Sovereign offline vault — committable encrypted secrets.

## Install

```bash
pip install b4n1-secrets
```

## Quick start

```python
from b4n1secrets import SecretsClient

client = SecretsClient()
print(client.version())
print(client.list(".secrets"))
```

## CLI usage

```bash
python -m b4n1secrets --help
python -m b4n1secrets init .secrets
```

## License

Business Source License 1.1 (BUSL-1.1). See LICENSE.