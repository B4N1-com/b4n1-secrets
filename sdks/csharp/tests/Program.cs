using System;
using System.Text.RegularExpressions;
using B4N1.Secrets;

internal static class Program
{
    private static int Main()
    {
        var client = new SecretsClient();
        var version = client.Version();

        if (!Regex.IsMatch(version, @"secrets v?\d+\.\d+\.\d+", RegexOptions.IgnoreCase))
        {
            Console.Error.WriteLine($"version inesperada: {version}");
            return 1;
        }

        Console.WriteLine($"ok {version}");
        return 0;
    }
}
