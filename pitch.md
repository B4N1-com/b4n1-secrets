# b4n1-secrets — Pitch

## What it is
Offline, committable secret vault (XChaCha20-Poly1305 + Argon2id). Each value
encrypted individually. Safe to commit and push — no plaintext ever leaves
the vault.

## Who it is for
Dev teams and solo developers who need to share secrets across machines
without a SaaS vault or a separate infra.

## Pain it removes
- "Where do I store the API keys?" → in the repo, encrypted, versioned.
- No more `.env` files in `.gitignore` and lost on new machines.
- No more sharing secrets over Slack/Telegram.

## Value bullets
1. Offline-first: no network, no SaaS, no account.
2. Committable: `git push` is safe — every value is individually encrypted.
3. Unlock once per session: passphrase lives only in RAM (unix socket, 0600).

## Demonstrable metric
`b4n1-secrets init . && echo "secret" | b4n1-secrets set . app/KEY --value secret`
then `git diff` shows only ciphertext.

## Call to action
`b4n1-secrets docs` for the full manual (offline). Try `b4n1-secrets demo` (coming soon).