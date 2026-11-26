# Release history

Every entry says what changed for you, and a version you install is the same
version on every channel. The current release is **0.1.4**.

## 0.1.4

Version alignment across the seven packages.

## 0.1.3

- New `docs` verb: the full manual is embedded in the binary (`docs`,
  `docs --list`, `docs --section <name>`), so documentation works offline on a
  client machine with no network and no web portal.
- The manual is also published as an mdBook site.
- README translated into the 11 `core` languages (ar, de, es, fr, hi, it, ja,
  ko, pt-BR, ru, zh-CN).

## 0.1.2

- Prebuilt binaries for all five platforms (Linux x86_64/aarch64, macOS
  Intel/Apple Silicon, Windows x86_64), bundled in every SDK.
- **Windows:** the verbs that need the in-memory daemon answer a clear, typed
  error there instead of failing to run.
- `--version` always reports the version of the package you installed.
- Available on every channel: PyPI, npm, NuGet, RubyGems, Packagist and the Go
  module proxy.

## 0.1.1

- Maintenance release: version alignment across the channels.

## 0.1.0

- First public release: `init`, `set`, `get`, `list`, `remove`, `unlock`,
  `close`, `run`.
- Seven SDKs: Python, Node.js, .NET, Java, Go, PHP, Ruby.
- Published to PyPI, npm, NuGet and RubyGems.

## Known limitations

- Windows has no in-memory daemon yet: `unlock`, `close` and `run` are not
  available there.
