# Security Model

## Cryptography

| Layer | Choice |
|---|---|
| Value encryption | XChaCha20-Poly1305, one key per vault, unique nonce per value |
| Key derivation | Argon2id from the passphrase |
| Integrity | AEAD tag per value — a modified entry fails to open, it does not decrypt to garbage |
| Format | YAML, one sealed entry per key |

Each entry is sealed independently. Two entries never share a nonce or a
ciphertext, so the file can be edited, diffed and reviewed without touching
values that did not change.

## Where the key lives

`unlock` derives the key, forks a detached daemon, and hands it the key through
the child's environment (same user, same machine, one `exec` apart). The daemon:

1. binds a Unix socket with mode `0600` inside the vault directory,
2. calls `mlock` on the key buffer so the page cannot be swapped to disk,
3. answers `fetch_key` requests until `close`,
4. on `close`, zeroises the buffer and exits.

The passphrase itself is never stored: not in a file, not in a config, not in an
environment variable that outlives the command.

## Threat model — what this protects against

- **Repository readers.** Anyone with the ciphertext but not the passphrase.
- **History.** A committed value stays sealed in every past commit.
- **Disk forensics after close.** The key was mlocked and then wiped; a swap file
  never contained it.
- **Accidental disclosure through logs.** `run` puts values in a child's
  environment, not in stdout or an argument list.
- **Lateral reading.** Per-value encryption allows granting one entry without
  exposing the rest.

## Threat model — what it does not protect against

- **A compromised machine while the vault is unlocked.** Software running as you
  can read your process memory. `mlock` prevents swapping, not inspection.
- **A keylogger.** The passphrase is typed by a human somewhere.
- **A malicious vault file.** Integrity is per value, so a value cannot be forged,
  but an attacker who can write the file can delete entries or replay an old one.
  Review the diff before committing.
- **Windows RAM daemon.** Not implemented; the Unix socket requirement is real.

Say this out loud when presenting: the guarantee is "no plaintext at rest and no
plaintext on the wire", not "no plaintext ever in memory". No local tool can offer
the second.

## Relationship with b4n1-notary

`b4n1-secrets` seals; `b4n1-notary` proves existence. Seal the value, commit,
then stamp the commit: encryption answers "who can read it", notarisation answers
"when did this exact content exist". The two are complementary and neither
replaces the other.
