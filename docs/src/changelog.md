# Changelog

## 0.1.3

- New `docs` verb: the full manual is embedded in the binary (`docs`,
  `docs --list`, `docs --section <name>`), so documentation works offline on a
  client machine with no network and no web portal.
- The manual is also published as an mdBook site.
- README translated into the 11 `core` languages (ar, de, es, fr, hi, it, ja,
  ko, pt-BR, ru, zh-CN).

## 0.1.2

- Cross-compiled binaries for all five platforms (Linux x86_64/aarch64, macOS
  Intel/Apple Silicon, Windows x86_64) and bundled them in every SDK.
- Windows builds compile: the RAM-daemon paths are gated behind `#[cfg(unix)]`
  and the affected verbs return a typed error at exit code 4 instead of failing
  to build.
- `--version` reads the version from the build metadata instead of a literal, so
  it can no longer drift from `Cargo.toml`.
- Packagist and Go modules published; the repository is public.
- Root `composer.json` added so Packagist can index the repository root.

## 0.1.1

- Version bump to reach registries that had already accepted 0.1.0.

## 0.1.0

- First public release: `init`, `set`, `get`, `list`, `remove`, `unlock`,
  `close`, `run`.
- Seven SDKs: Python, Node.js, .NET, Java, Go, PHP, Ruby.
- Published to PyPI, npm, NuGet and RubyGems.

## Known gaps

- Maven Central is blocked by an account-level quota; the artifact ships to the
  other registries in the meantime.
- Windows has no RAM daemon (no `unlock`/`close`/`run` there yet).
