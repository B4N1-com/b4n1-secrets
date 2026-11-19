"""b4n1-secrets CLI entry point: python -m b4n1secrets."""

import os
import sys
from pathlib import Path

from .binary import get_b4n1secrets_binary, get_b4n1secrets_version


def resolve_install_dir():
    env_install_dir = os.getenv("B4N1SECRETS_INSTALL_DIR")
    if env_install_dir:
        return Path(env_install_dir)
    usr_local = Path("/usr/local/bin")
    if os.access(str(usr_local), os.W_OK):
        return usr_local
    user_local = Path.home() / ".local/bin"
    if os.access(str(user_local), os.W_OK):
        return user_local
    return Path.home() / ".b4n1secrets" / "bin"


def install_command():
    binary = get_b4n1secrets_binary()
    if binary:
        version = get_b4n1secrets_version()
        print(f"b4n1-secrets already available at: {binary}")
        print(f"Version: {version}")
        response = input("Reinstall? (y/N): ").lower().strip()
        if response not in ("y", "yes"):
            print("Installation cancelled.")
            return

    install_dir = resolve_install_dir()
    install_dir.mkdir(parents=True, exist_ok=True)
    binary_path = install_dir / "b4n1secrets"

    print(f"Install directory: {install_dir}")
    print("Manual install: copy the b4n1-secrets binary to this directory.")
    print(f"  cp /path/to/b4n1-secrets {binary_path}")
    print(f"  chmod +x {binary_path}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "install":
        install_command()
        return

    binary = get_b4n1secrets_binary()
    if not binary:
        print("b4n1-secrets binary not found. Set B4N1SECRETS_BIN_PATH or run: python -m b4n1secrets install")
        sys.exit(1)

    import subprocess

    result = subprocess.run([binary] + sys.argv[1:])
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()