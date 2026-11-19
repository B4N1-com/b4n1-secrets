package com.b4n1.secrets;

import java.io.*;
import java.nio.file.*;

public class SecretsClient {
    private final String binary;

    public SecretsClient() { this.binary = getBinaryPath(); }
    public SecretsClient(String binaryPath) { this.binary = binaryPath; }

    public static String getBinaryPath() {
        String env = System.getenv("B4N1SECRETS_BIN_PATH");
        if (env != null) return env;
        String dir = System.getProperty("user.dir") + "/bin";
        String name = "b4n1secrets-linux-amd64";
        if (new File(dir + "/" + name).exists()) return dir + "/" + name;
        return "b4n1secrets";
    }

    private String run(String... args) throws IOException, InterruptedException {
        ProcessBuilder pb = new ProcessBuilder();
        pb.command(binary);
        for (String a : args) pb.command().add(a);
        pb.redirectErrorStream(true);
        Process p = pb.start();
        BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = r.readLine()) != null) sb.append(line).append("\n");
        p.waitFor();
        return sb.toString().trim();
    }

    public String version() throws Exception { return run("--version"); }
    public String list(String dir, boolean meta) throws Exception {
        if (meta) return run("list", dir, "--meta");
        return run("list", dir);
    }
    public String get(String dir, String key) throws Exception { return run("get", dir, key); }
    public String close(String dir) throws Exception { return run("close", dir); }
}