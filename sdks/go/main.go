package b4n1secrets

import (
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
)

func binaryPath() string {
	if p := os.Getenv("B4N1SECRETS_BIN_PATH"); p != "" {
		return p
	}
	name := "b4n1secrets-linux-amd64"
	switch runtime.GOOS {
	case "darwin":
		if runtime.GOARCH == "arm64" {
			name = "b4n1secrets-macos-arm64"
		} else {
			name = "b4n1secrets-macos-x64"
		}
	case "windows":
		name = "b4n1secrets-windows-amd64.exe"
	case "linux":
		if runtime.GOARCH == "arm64" {
			name = "b4n1secrets-linux-arm64"
		}
	}
	bundled := filepath.Join("bin", name)
	if _, err := os.Stat(bundled); err == nil {
		return bundled
	}
	return "b4n1secrets"
}

func Run(args ...string) (string, error) {
	cmd := exec.Command(binaryPath(), args...)
	out, err := cmd.Output()
	return string(out), err
}

type Client struct{ Binary string }

func NewClient() *Client { return &Client{Binary: binaryPath()} }
func (c *Client) Version() (string, error) { return Run("--version") }
func (c *Client) List(dir string, meta bool) (string, error) {
	args := []string{"list", dir}
	if meta {
		args = append(args, "--meta")
	}
	return Run(args...)
}
func (c *Client) Get(dir, key string) (string, error) { return Run("get", dir, key) }
func (c *Client) Close(dir string) (string, error) { return Run("close", dir) }