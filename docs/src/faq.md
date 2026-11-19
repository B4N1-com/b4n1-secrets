# Frequently Asked Questions

## Is this a replacement for a cloud KMS?

No. A KMS gives you a policy engine, audit log and HSM-backed keys served over a
network. This gives you ciphertext you own, in a file you control, with no
network at all. Different trade-offs; teams often run both.

## What happens if I lose the passphrase?

The vault is unrecoverable. There is no recovery key and no escrow — that is the
consequence of nobody else holding a copy. Store the passphrase in whatever
system already holds your account recovery material, and do it before you need
it.

## Can I commit the vault to a public repository?

Technically yes: the file is ciphertext. Practically, careful teams use a private
repository, because the metadata (key names, tags, expiry dates) reveals your
infrastructure shape even though the values are sealed.

## Can I share one secret with a contractor?

Not yet. v0.1 supports exactly one passphrase per vault. Separate vaults, or a
separate repository, are the current answer. Per-receiver envelopes are on the
roadmap.

## Why is the daemon Unix-only?

It requires `mlock` and a Unix domain socket for the RAM-only key. Windows has
equivalents (`VirtualLock`, named pipes) but they are not implemented and this
project does not publish untested security code. On Windows, use the vault for
storage and reading via a platform build once that lands.

## Does `run` protect me from a compromised CI runner?

It protects the value from appearing in logs, shell history and process
arguments. It does not protect a value from a process that is already running as
your user. If the runner is compromised while the vault is unlocked, the value is
reachable — as it is with any local tool.

## How does the SDK find the binary?

The package ships one per platform and selects it at runtime. `B4N1SECRETS_BIN_PATH`
overrides that. The resolution never falls back to a `b4n1secrets` found on
`PATH`, so a stale global install cannot shadow the bundled version.

## Why do the SDKs spawn a process instead of using FFI?

Because a spawned binary works from every package manager with no compiler on the
consumer's machine, and because one implementation of the format is a better
guarantee than seven. See [Architecture](architecture.md).

## Is there a server mode?

No. There is no service to run, no port to open and nothing to administer.
