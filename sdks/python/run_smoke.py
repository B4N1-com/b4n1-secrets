import subprocess, sys, os, tempfile, shutil
from pathlib import Path

def main():
    binary = os.environ.get("B4N1SECRETS_BIN_PATH", "private-repos/b4n1-secrets/target/release/b4n1-secrets")
    print(f"Using binary: {binary}")
    # version check
    r = subprocess.run([binary, "--version"], capture_output=True, text=True)
    assert r.returncode == 0 and "0.1.0" in (r.stdout + r.stderr), "version check failed"
    print("✓ version OK")
    # help check
    r = subprocess.run([binary, "--help"], capture_output=True, text=True)
    assert r.returncode == 0 and "run" in (r.stdout + r.stderr), "help check failed"
    print("✓ help OK")
    # end-to-end init/set/get/close
    d = tempfile.mkdtemp()
    try:
        subprocess.run([binary, "init", d], input="testpass123456\n", capture_output=True, text=True, check=True)
        subprocess.run([binary, "unlock", d], input="testpass123456\n", capture_output=True, text=True, check=True)
        subprocess.run([binary, "set", d, "app/KEY", "--value", "secret123"], capture_output=True, text=True, check=True)
        r = subprocess.run([binary, "get", d, "app/KEY"], capture_output=True, text=True)
        assert r.stdout.strip() == "secret123", f"get failed: {r.stdout}"
        print("✓ init/set/get OK")
        subprocess.run([binary, "close", d], capture_output=True, text=True, check=True)
        print("✓ close OK")
    finally:
        shutil.rmtree(d, ignore_errors=True)
    print("ALL SMOKE TESTS PASSED")

if __name__ == "__main__":
    main()