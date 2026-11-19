"""Binary resolution for the b4n1-secrets SDK."""

import os
import platform
import subprocess
import sys
from pathlib import Path
from typing import Optional

_PLATFORM_BINARIES = {
    ("linux", "x86_64"): "b4n1secrets-linux-amd64",
    ("linux", "aarch64"): "b4n1secrets-linux-arm64",
    ("darwin", "x86_64"): "b4n1secrets-macos-x64",
    ("darwin", "arm64"): "b4n1secrets-macos-arm64",
    ("windows", "AMD64"): "b4n1secrets-windows-amd64.exe",
}


def _get_platform_binary_name() -> Optional[str]:
    key = (sys.platform, platform.machine())
    return _PLATFORM_BINARIES.get(key)


def get_b4n1secrets_binary() -> Optional[str]:
    """Resolve the b4n1-secrets binary path.

    Resolution order:
    1. B4N1SECRETS_BIN_PATH env var (exact path, wins)
    2. Bundled binary in bin/ (matches current platform)
    3. B4N1SECRETS_BINARY env var
    4. Common install locations + PATH
    """
    if "B4N1SECRETS_BIN_PATH" in os.environ:
        env_path = os.environ["B4N1SECRETS_BIN_PATH"]
        if os.path.exists(env_path) and os.access(env_path, os.X_OK):
            return env_path

    bin_name = _get_platform_binary_name()
    if bin_name:
        bundled = Path(__file__).parent / "bin" / bin_name
        if bundled.exists() and os.access(bundled, os.X_OK):
            return str(bundled)

    env_binary = os.getenv("B4N1SECRETS_BINARY")
    if env_binary and os.path.isfile(env_binary) and os.access(env_binary, os.X_OK):
        return env_binary

    possible = [
        str(Path.home() / ".local/bin/b4n1secrets"),
        str(Path.home() / ".b4n1secrets/bin/b4n1secrets"),
        "/usr/local/bin/b4n1secrets",
        "/usr/bin/b4n1secrets",
    ]
    for d in os.environ.get("PATH", "").split(":"):
        possible.append(os.path.join(d, "b4n1secrets"))

    for loc in possible:
        if os.path.isfile(loc) and os.access(loc, os.X_OK):
            return loc

    return None


def get_b4n1secrets_version() -> Optional[str]:
    """Get the version of the resolved b4n1-secrets binary."""
    binary = get_b4n1secrets_binary()
    if not binary:
        return None
    try:
        result = subprocess.run(
            [binary, "--version"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        return result.stdout.strip() or result.stderr.strip()
    except Exception:
        return None


def run(*args, **kwargs):
    """Run the b4n1-secrets binary with the given arguments.

    Returns a subprocess.CompletedProcess. Raises RuntimeError if the
    binary cannot be resolved.
    """
    binary = get_b4n1secrets_binary()
    if not binary:
        raise RuntimeError(
            "b4n1-secrets binary not found. Set B4N1SECRETS_BIN_PATH or install "
            "the binary. See: https://github.com/B4N1-com/b4n1-secrets"
        )
    return subprocess.run([binary] + list(args), **kwargs)