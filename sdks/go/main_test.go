package b4n1secrets

import (
	"regexp"
	"testing"
)

// El motor empaquetado responde con su franja de versión.
func TestVersion(t *testing.T) {
	client := NewClient()
	version, err := client.Version()
	if err != nil {
		t.Fatalf("version: %v", err)
	}
	if !regexp.MustCompile(`secrets v?\d+\.\d+\.\d+`).MatchString(version) {
		t.Fatalf("version inesperada: %q", version)
	}
}
