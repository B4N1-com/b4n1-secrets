"""b4n1-secrets SDK — Sovereign Offline Vault.

Thin Python wrapper around the b4n1-secrets binary. The wheel bundles the engine
for the supported platforms and resolves the matching one at import time.

Overrides:
    B4N1SECRETS_BIN_PATH=/path/to/b4n1-secrets   exact binary, wins over the bundle
    B4N1SECRETS_BINARY=/path/to/b4n1-secrets      same, kept for older callers

Quick start:
    from b4n1secrets import SecretsClient

    client = SecretsClient()
    print(client.version())
    print(client.list(".secrets"))

CLI usage:
    python -m b4n1secrets --help
    python -m b4n1secrets install
"""

from .binary import (
    get_b4n1secrets_binary,
    get_b4n1secrets_version,
    run,
)

SDK_VERSION = "0.1.1"

__version__ = SDK_VERSION
__author__ = "Bani Montoya"
__email__ = "banimontoya@gmail.com"

__all__ = [
    "get_b4n1secrets_binary",
    "get_b4n1secrets_version",
    "run",
    "SecretsClient",
]


class SecretsClient:
    """High-level client wrapping the b4n1-secrets binary."""

    def __init__(self, binary_path: str = None):
        self._binary = binary_path or get_b4n1secrets_binary()
        if not self._binary:
            raise RuntimeError(
                "b4n1-secrets binary not found. Set B4N1SECRETS_BIN_PATH or install "
                "the binary."
            )

    def _run(self, *args, capture=True, timeout=30):
        import subprocess

        result = subprocess.run(
            [self._binary] + list(args),
            capture_output=capture,
            text=True,
            timeout=timeout,
        )
        return result

    def version(self) -> str:
        r = self._run("--version")
        return (r.stdout or r.stderr).strip()

    def init(self, directory, passphrase):
        import subprocess
        r = subprocess.run(
            [self._binary, "init", directory],
            input=passphrase + "\n",
            capture_output=True,
            text=True,
            timeout=30,
        )
        return r

    def unlock(self, directory, passphrase):
        import subprocess
        r = subprocess.run(
            [self._binary, "unlock", directory],
            input=passphrase + "\n",
            capture_output=True,
            text=True,
            timeout=30,
        )
        return r

    def close(self, directory):
        return self._run("close", directory)

    def set(self, directory, key, value, expires_epoch=None, tags=None, force=False):
        args = ["set", directory, key, "--value", value]
        if expires_epoch is not None:
            args.extend(["--expires-epoch", str(expires_epoch)])
        if tags:
            args.extend(["--tags", ",".join(tags)])
        if force:
            args.append("--force")
        return self._run(*args)

    def get(self, directory, key):
        r = self._run("get", directory, key)
        return (r.stdout or "").strip()

    def list(self, directory, meta=False):
        args = ["list", directory]
        if meta:
            args.append("--meta")
        r = self._run(*args)
        return (r.stdout or r.stderr).strip()

    def remove(self, directory, key):
        return self._run("remove", directory, key)

    def run(self, directory, secrets, command):
        args = ["run", directory]
        for env_var, key in secrets.items():
            args.extend(["--secret", f"{env_var}={key}"])
        args.append("--")
        args.extend(command)
        return self._run(*args, capture=False)

    def help(self) -> str:
        r = self._run("--help")
        return (r.stdout or r.stderr).strip()