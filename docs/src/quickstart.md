# Quick Start

## 1. Create a vault

The passphrase is read from stdin — never from an argument, so it does not land
in your shell history.

```bash
read -rs P && echo "$P" | b4n1-secrets init .secrets
```

This writes `.secrets/secrets.enc.yaml`. Commit it:

```bash
git add .secrets/secrets.enc.yaml
git commit -m "feat(secrets): initialise vault"
```

## 2. Unlock it

`unlock` derives the key from the passphrase, holds it **only in RAM** in a
detached daemon, and returns. Every later command talks to that daemon over a
Unix socket with mode `0600`.

```bash
read -rs P && echo "$P" | b4n1-secrets unlock .secrets
```

## 3. Write a secret

```bash
b4n1-secrets set .secrets app/API_KEY --value sk_live_... --tags prod
git add .secrets/secrets.enc.yaml && git commit -m "feat(secrets): add API key"
```

`set` refuses to overwrite an existing key unless you pass `--force`. Optional
`--expires-epoch N` makes the entry unreadable after that timestamp.

## 4. Read it back

```bash
b4n1-secrets get .secrets app/API_KEY
b4n1-secrets list .secrets          # names, expiry and tags — never values
```

## 5. Use it without printing it

This is the important one. `run` injects secrets as environment variables of a
child process; the value never crosses stdout, a log file, or your terminal
scroll-back.

```bash
b4n1-secrets run .secrets \
  --secret API_KEY=app/API_KEY \
  --secret DB_URL=app/DATABASE_URL \
  -- python my_agent.py
```

## 6. Close the vault

```bash
b4n1-secrets close .secrets
```

The daemon exits and the key is wiped. `get`, `set` and `run` fail until the next
`unlock`.

## On another machine

```bash
git pull
read -rs P && echo "$P" | b4n1-secrets unlock .secrets
b4n1-secrets get .secrets app/API_KEY
```

That is the whole workflow: the ciphertext travels with the repository, the
passphrase travels through whatever channel you already trust for credentials.
