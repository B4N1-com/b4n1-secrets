const { execFileSync } = require("child_process");
const path = require("path");
const fs = require("fs");

const PLATFORMS = {
  "linux-x64": "b4n1secrets-linux-amd64",
  "linux-arm64": "b4n1secrets-linux-arm64",
  "darwin-x64": "b4n1secrets-macos-x64",
  "darwin-arm64": "b4n1secrets-macos-arm64",
  "win32-x64": "b4n1secrets-windows-amd64.exe",
};

function getBinaryPath() {
  if (process.env.B4N1SECRETS_BIN_PATH) return process.env.B4N1SECRETS_BIN_PATH;
  const key = `${process.platform}-${process.arch}`;
  const name = PLATFORMS[key];
  if (!name) throw new Error(`Unsupported platform: ${key}`);
  const bundled = path.join(__dirname, "bin", name);
  if (fs.existsSync(bundled)) return bundled;
  if (process.env.B4N1SECRETS_BINARY) return process.env.B4N1SECRETS_BINARY;
  return "b4n1secrets";
}

function run(...args) {
  const binary = getBinaryPath();
  return execFileSync(binary, args, { encoding: "utf-8" });
}

class SecretsClient {
  constructor(binaryPath) {
    this.binary = binaryPath || getBinaryPath();
  }
  version() { return run("--version").trim(); }
  list(dir, meta = false) {
    const args = ["list", dir];
    if (meta) args.push("--meta");
    return run(...args).trim();
  }
  get(dir, key) { return run("get", dir, key).trim(); }
  set(dir, key, value, opts = {}) {
    const args = ["set", dir, key, "--value", value];
    if (opts.expiresEpoch) args.push("--expires-epoch", String(opts.expiresEpoch));
    if (opts.tags) args.push("--tags", opts.tags.join(","));
    if (opts.force) args.push("--force");
    return run(...args).trim();
  }
  remove(dir, key) { return run("remove", dir, key).trim(); }
  close(dir) { return run("close", dir).trim(); }
  help() { return run("--help").trim(); }
}

module.exports = { SecretsClient, getBinaryPath, run };