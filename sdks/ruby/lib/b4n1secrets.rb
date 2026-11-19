require "open3"

module B4n1Secrets
  PLATFORMS = {
    "x86_64-linux" => "b4n1secrets-linux-amd64",
    "aarch64-linux" => "b4n1secrets-linux-arm64",
    "x86_64-darwin" => "b4n1secrets-macos-x64",
    "arm64-darwin" => "b4n1secrets-macos-arm64",
    "x64-mingw32" => "b4n1secrets-windows-amd64.exe",
  }

  def self.binary_path
    return ENV["B4N1SECRETS_BIN_PATH"] if ENV["B4N1SECRETS_BIN_PATH"]
    require "rbconfig"
    key = "#{RbConfig::CONFIG['host_cpu']}-#{RbConfig::CONFIG['host_os']}"
    name = PLATFORMS[key]
    return name ? File.join(__dir__, "..", "bin", name) : "b4n1secrets"
  end

  def self.run(*args)
    stdout, stderr, status = Open3.capture3(binary_path, *args)
    stdout
  end

  class Client
    def initialize(binary_path = nil)
      @binary = binary_path || B4n1Secrets.binary_path
    end
    def version; B4n1Secrets.run("--version").strip; end
    def list(dir, meta = false)
      args = ["list", dir]
      args << "--meta" if meta
      B4n1Secrets.run(*args).strip
    end
    def get(dir, key); B4n1Secrets.run("get", dir, key).strip; end
    def close(dir); B4n1Secrets.run("close", dir).strip; end
  end
end