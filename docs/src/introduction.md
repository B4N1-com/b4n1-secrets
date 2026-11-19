# Introduction

**b4n1-secrets** is a sovereign, offline-first secret vault. It stores secrets
in a single YAML file (`secrets.enc.yaml`) that you commit to git like any other
source file — the file is useless to anyone who does not hold your passphrase.

Each value is encrypted on its own (XChaCha20-Poly1305 with an Argon2id-derived
key), so a reader can be granted exactly one entry and nothing else. There is no
shared payload to re-encrypt, no server to trust, and no network call anywhere in
the binary.

## What it is not

- Not a SaaS. There is no account, no API key, no hosted control plane.
- Not a cloud KMS. No third party ever sees ciphertext or plaintext.
- Not a `.env` replacement that keeps plaintext on disk. Plaintext exists only in
  the memory of a process that asked for it.

## The three shapes of the same core

| Shape | Use it when |
|---|---|
| **CLI** | You are a human at a terminal, or a script needs one value |
| **SDK** | An application imports the client and reads secrets in its own language |
| **Library binary** | A CI job or container needs the binary with no runtime installed |

All three spawn the same native core. The SDKs are thin wrappers: they resolve
the bundled binary for the current platform, pass arguments, and return the
result. No FFI, no reimplementation, no per-language crypto.

## Why committable ciphertext matters

Configuration lives with the code that needs it. A new developer clones the
repository, receives the passphrase through the channel the team already uses for
credentials, and is productive in one command. There is no "ask someone to send
you the .env file" step, and no secret drifts because it was copied by hand.

Because every value is independently sealed, an audit can answer "who can read
the database password" without answering "who can read everything".

## Platforms

Linux x86_64 and aarch64, macOS Intel and Apple Silicon, Windows x86_64. One
precompiled binary per platform ships inside every SDK package; a consumer never
needs a compiler.
