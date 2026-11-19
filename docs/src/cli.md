# CLI Reference

```
b4n1-secrets <verb> <dir> [flags]
```

`<dir>` is the vault directory. The file inside it is always `secrets.enc.yaml`.

## Verbs

| Verb | Purpose |
|---|---|
| `init <dir>` | Create an empty vault. Passphrase by stdin, minimum 12 characters. |
| `unlock <dir>` | Derive the key and start the RAM-only daemon. `--foreground` keeps it attached. |
| `close <dir>` | Stop the daemon and wipe the key. |
| `set <dir> <app/KEY>` | Seal one value. Flags: `--value`, `--expires-epoch`, `--tags`, `--force`. |
| `get <dir> <app/KEY>` | Print one decrypted value. Requires an active lock. |
| `list <dir>` | Print names, expiry and tags. Never prints values. `--meta` adds KDF and format version. |
| `remove <dir> <app/KEY>` | Delete an entry from the vault. |
| `run <dir> --secret ENV=app/KEY -- <cmd>` | Inject secrets as env vars of a child process. |
| `--version` / `-V` | Print the binary version. |
| `--help` | Print the full usage text. |

## Naming

Keys are `<app>/<KEY>`: a namespace, a slash, and the key name. The namespace is
what makes partial sharing tractable — you grant `billing/prod` without
mentioning `infra/root`.

## Expiry

`--expires-epoch` takes a Unix timestamp. After it passes, `get` fails with a
typed expired-key error instead of returning the stale value. Rotating a
credential is therefore a `set --force` with a new expiry, not a reminder in a
calendar.

## `run`

```bash
b4n1-secrets run .secrets \
  --secret OPENAI_KEY=b4n1-ia-provider/API_KEY \
  --secret DB_URL=infra/DATABASE_URL \
  -- ./worker
```

Each `--secret` is `ENV_NAME=app/KEY`. Everything after `--` is the command and
its arguments, executed with the parent's environment plus those variables.

The value is written into the child's environment block, not into the parent's,
and never into a stream. A process that captures stdout sees nothing; a shell
history holds only the key name.

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 1 | Usage or signature error |
| 2 | Key expired or not found |
| 3 | Passphrase too weak |
| 4 | Corrupt vault, or the operation is unsupported on this platform |

## Platform note

`unlock`, `close` and `run` need a Unix socket and therefore Unix. On Windows the
vault can be initialised and inspected, but the RAM daemon is not available; use
the SDK in-process path or run the CLI under WSL for those verbs.
