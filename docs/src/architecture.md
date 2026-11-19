# Architecture

## One core, seven wrappers

```
        CLI ─┐
             │
   Python ───┤
     Node ───┤
     .NET ───┼──►  b4n1-secrets binary  ──►  secrets.enc.yaml
     Java ───┤        (native core)
      Go  ───┤
      PHP ───┤
     Ruby ───┘
```

The binary owns all crypto, all file format logic and all error semantics. An SDK
that reimplemented any of it would be a second, drifting definition of the
format — so the SDKs do not. They:

1. locate the bundled binary for the current platform,
2. spawn it with the arguments the caller supplied,
3. return stdout, or raise with the exit code and stderr.

A fix in the core therefore lands in all seven SDKs at once.

## Why a binary instead of FFI

FFI ties the package to a compiler at install time and to a specific ABI. A
spawned binary works from a wheel, an npm tarball, a NuGet package and a gem with
no build step on the consumer's machine, and it keeps the core's symbols out of
the host process. The cost is a process spawn per call, which is irrelevant for a
verb that is used at startup or in a job, and is the price of not shipping a
compiler.

## Vault format

```yaml
kdf: Argon2id
version: 1
entries:
  "app/API_KEY":
    nonce: <base64>
    ciphertext: <base64>
    tags: [prod]
    expires: 1800000000
```

Human-readable structure, machine-opaque values. A reviewer sees which keys
exist, when they expire and what they are tagged as — and nothing else.

## Daemon lifecycle

`unlock` is the only verb that ever sees the passphrase in plaintext. It derives
the key, binds the socket, and starts the daemon detached with `setsid` so it
outlives the shell that launched it. Subsequent commands are clients.

`close` sends a drop request; the daemon zeroises and exits. If a daemon is
crash-killed, the socket becomes stale and the next `get` fails loudly rather
than reading an unprotected file.

## Platform gates

The daemon needs Unix domain sockets and `mlock`, so `main.rs`, `commands.rs` and
`lockd.rs` compile those paths behind `#[cfg(unix)]`. On Windows the module is
compiled out and the affected verbs return a typed "unsupported on this platform"
error at exit code 4. Nothing silently degrades.
