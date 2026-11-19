Gem::Specification.new do |s|
  s.name = "b4n1-secrets"
  s.version = "0.1.1"
  s.summary = "Sovereign offline vault — committable encrypted secrets"
  s.description = "Thin Ruby wrapper around the b4n1-secrets binary."
  s.authors = ["Bani Montoya"]
  s.email = "banimontoya@gmail.com"
  s.files = Dir["lib/**/*", "bin/*"]
  s.require_paths = ["lib"]
  s.license = "BUSL-1.1"
  s.homepage = "https://github.com/B4N1-com/b4n1-secrets"
end