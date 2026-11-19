# Go SDK

```bash
go get github.com/B4N1-com/b4n1-secrets/sdks/go
```

```go
package main

import (
    "fmt"
    b4n1secrets "github.com/B4N1-com/b4n1-secrets/sdks/go"
)

func main() {
    client := b4n1secrets.NewClient()
    v, _ := client.Version()
    fmt.Println(v)

    _ = client.Set(".secrets", "app/API_KEY", "sk_live_...", []string{"prod"})
    value, _ := client.Get(".secrets", "app/API_KEY")
    fmt.Println(value)
}
```

## Injecting into a subprocess

```go
err := client.Run(".secrets",
    map[string]string{"OPENAI_KEY": "b4n1-ia-provider/API_KEY"},
    []string{"go", "run", "./agent"})
```

## Notes

- Pure Go, no cgo: the SDK spawns the bundled binary.
- The binary is resolved relative to the module cache, so no `go:embed` of a
  2 MB blob per platform is needed at build time.
- Module path is versioned with tags of the form `sdks/go/vX.Y.Z`.
