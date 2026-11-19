# Ruby SDK

```bash
gem install b4n1-secrets
```

```ruby
require 'b4n1secrets'

client = B4n1Secrets::Client.new
puts client.version

client.set('.secrets', 'app/API_KEY', 'sk_live_...', tags: ['prod'])
value = client.get('.secrets', 'app/API_KEY')
puts client.list('.secrets')
```

## Injecting into a subprocess

```ruby
client.run('.secrets', { 'OPENAI_KEY' => 'b4n1-ia-provider/API_KEY' }, ['ruby', 'agent.rb'])
```

## Notes

- Ruby 2.7 or newer, no native extension.
- The gem ships every platform binary and selects one at runtime.
- Errors raise `B4n1Secrets::Error` with `exit_code` and `stderr`.
