using System;
using System.Diagnostics;
using System.IO;

namespace B4N1.Secrets
{
    public class SecretsClient
    {
        private readonly string _binary;
        public SecretsClient(string binaryPath = null)
        {
            _binary = binaryPath ?? GetBinaryPath();
        }
        public static string GetBinaryPath()
        {
            var env = Environment.GetEnvironmentVariable("B4N1SECRETS_BIN_PATH");
            if (env != null) return env;
            var dir = Path.Combine(AppContext.BaseDirectory, "bin");
            var name = "b4n1secrets-linux-amd64";
            if (File.Exists(Path.Combine(dir, name))) return Path.Combine(dir, name);
            return "b4n1secrets";
        }
        private string Run(params string[] args)
        {
            var psi = new ProcessStartInfo(_binary);
            foreach (var a in args) psi.ArgumentList.Add(a);
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.UseShellExecute = false;
            using var p = Process.Start(psi);
            p.WaitForExit();
            return p.StandardOutput.ReadToEnd().Trim();
        }
        public string Version() => Run("--version");
        public string List(string dir, bool meta = false) => meta ? Run("list", dir, "--meta") : Run("list", dir);
        public string Get(string dir, string key) => Run("get", dir, key);
        public string Close(string dir) => Run("close", dir);
    }
}