# Smoke test del wrapper Ruby de b4n1-secrets: el motor empaquetado responde
# con su franja de versión.
require_relative "../lib/b4n1secrets"

client = B4n1Secrets::Client.new
version = client.version

unless version =~ /secrets v?\d+\.\d+\.\d+/i
  warn "version inesperada: #{version.inspect}"
  exit 1
end

puts "ok #{version}"
