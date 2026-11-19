# Java SDK

Add the dependency to your `pom.xml`:

```xml
<dependency>
  <groupId>com.b4n1</groupId>
  <artifactId>b4n1-secrets</artifactId>
  <version>0.1.3</version>
</dependency>
```

```java
import com.b4n1.secrets.SecretsClient;

public class Example {
    public static void main(String[] args) throws Exception {
        SecretsClient client = new SecretsClient();
        System.out.println(client.version());

        client.set(".secrets", "app/API_KEY", "sk_live_...", new String[]{"prod"});
        String value = client.get(".secrets", "app/API_KEY");
        System.out.println(client.list(".secrets"));
    }
}
```

## Injecting into a subprocess

```java
Map<String, String> secrets = Map.of("OPENAI_KEY", "b4n1-ia-provider/API_KEY");
client.run(".secrets", secrets, List.of("java", "-jar", "agent.jar"));
```

## Notes

- Requires Java 11+.
- The JAR embeds all five platform binaries and extracts the matching one to a
  temp directory on first call.
- `SecretsException` carries the exit code and stderr of the failed invocation.

> Maven Central distribution is currently gated by an account quota issue; the
> artifact is published to the other six registries. See the project changelog.
