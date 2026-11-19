# Installation

Every package ships the same precompiled native core for five platforms. You need
no compiler, no Rust toolchain, and no Python build step.

## Registries

| Registry | Language | Package | Command |
|----------|----------|---------|---------|
| PyPI | Python 3.8+ | `b4n1-secrets` | `pip install b4n1-secrets` |
| npm | Node.js | `@b4n1/secrets` | `npm install @b4n1/secrets` |
| NuGet | .NET / C# | `b4n1-secrets` | `dotnet add package b4n1-secrets` |
| RubyGems | Ruby | `b4n1-secrets` | `gem install b4n1-secrets` |
| Packagist | PHP 7.4+ | `b4n1/b4n1-secrets` | `composer require b4n1/b4n1-secrets` |
| Go modules | Go 1.21+ | `.../sdks/go` | `go get github.com/B4N1-com/b4n1-secrets/sdks/go` |

## Platforms in every package

| Platform | Architecture | Bundled binary |
|---|---|---|
| Linux | x86_64 | `b4n1secrets-linux-amd64` |
| Linux | aarch64 | `b4n1secrets-linux-arm64` |
| macOS | Intel | `b4n1secrets-macos-x64` |
| macOS | Apple Silicon | `b4n1secrets-macos-arm64` |
| Windows | x86_64 | `b4n1secrets-windows-amd64.exe` |

The package selects the right one at runtime from `process.platform` /
`sys.platform` / `RuntimeInformation` and so on. Nothing is downloaded after
install.

## Resolving the binary

The SDK looks for the bundled binary first. To pin a different one — a
statically linked build, a build from your own pipeline, or a binary on a shared
volume — set:

```bash
export B4N1SECRETS_BIN_PATH=/path/to/b4n1secrets-linux-amd64
```

If neither the bundled binary nor that variable resolves to an executable file,
the client raises an error naming the paths it tried. It never silently falls
back to a system-wide `b4n1secrets` that might be an older version.

## Building from source

Only needed if you want to modify the core:

```bash
cargo build --release
cargo test
```

Cross-compilation uses `cargo zigbuild`; the macOS targets additionally require
`SDKROOT` pointing at a macOS SDK. See the project README for the exact matrix.
