<?php
namespace B4N1\Secrets;

class SecretsClient {
    private string $binary;
    public function __construct(?string $binaryPath = null) {
        $this->binary = $binaryPath ?? self::getBinaryPath();
    }
    public static function getBinaryPath(): string {
        if ($p = getenv("B4N1SECRETS_BIN_PATH")) return $p;
        $dir = __DIR__ . "/../bin";
        $name = "b4n1secrets-linux-amd64";
        if (file_exists("$dir/$name")) return "$dir/$name";
        return "b4n1secrets";
    }
    public function run(array $args): string {
        $cmd = escapeshellarg($this->binary) . " " . implode(" ", array_map("escapeshellarg", $args));
        return trim(shell_exec($cmd) ?? "");
    }
    public function version(): string { return $this->run(["--version"]); }
    public function list(string $dir, bool $meta = false): string {
        $args = ["list", $dir];
        if ($meta) $args[] = "--meta";
        return $this->run($args);
    }
    public function get(string $dir, string $key): string { return $this->run(["get", $dir, $key]); }
    public function close(string $dir): string { return $this->run(["close", $dir]); }
}