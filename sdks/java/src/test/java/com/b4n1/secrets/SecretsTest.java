package com.b4n1.secrets;

import java.util.regex.Pattern;

/** Smoke test del wrapper Java: el motor empaquetado responde con su versión. */
public final class SecretsTest {

    public static void main(String[] args) throws Exception {
        SecretsClient client = new SecretsClient();
        String version = client.version();

        if (!Pattern.compile("secrets v?\\d+\\.\\d+\\.\\d+", Pattern.CASE_INSENSITIVE)
                .matcher(version).find()) {
            throw new AssertionError("version inesperada: " + version);
        }

        System.out.println("ok " + version);
    }
}
