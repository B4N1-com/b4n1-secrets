import subprocess
import sys
from pathlib import Path

def test_binary_resolves():
    from b4n1secrets.binary import get_b4n1secrets_binary
    binary = get_b4n1secrets_binary()
    assert binary is not None, "binary not found"
    assert Path(binary).exists()

def test_version():
    from b4n1secrets.binary import get_b4n1secrets_binary
    binary = get_b4n1secrets_binary()
    r = subprocess.run([binary, "--version"], capture_output=True, text=True)
    assert r.returncode == 0
    assert "0.1.0" in (r.stdout + r.stderr)

def test_help():
    from b4n1secrets.binary import get_b4n1secrets_binary
    binary = get_b4n1secrets_binary()
    r = subprocess.run([binary, "--help"], capture_output=True, text=True)
    assert r.returncode == 0
    assert "run" in (r.stdout + r.stderr)

def test_client_init():
    from b4n1secrets import SecretsClient
    client = SecretsClient()
    assert client.version() != ""