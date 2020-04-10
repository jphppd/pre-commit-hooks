Gem::Specification.new do |s|
  s.name = 'fake_gem__'
  s.version = '0.0.0'
  s.authors = ['John Doe']
  s.summary = 'pre-commit hooks for ruby projects'
  s.description = 'pre-commit hooks for ruby projects'
  s.add_dependency 'bigdecimal' # needed by reek
  s.add_dependency 'bundler-audit'
  s.add_dependency 'fasterer'
  s.add_dependency 'mdl'
  s.add_dependency 'puppet-lint'
  s.add_dependency 'rake'
  s.add_dependency 'reek'
  s.add_dependency 'rubocop'
  s.add_dependency 'rubocop-rspec'
  s.bindir = 'hooks/ruby'
  s.executables = %w[
    markdown-linter
    puppet-erb-validate
    puppet-epp-validate
    puppet-g10k-validate
    puppet-r10k-validate
    puppet-validate
    ruby-bundle-auditer
    ruby-fasterer
    ruby-reek
    ruby-rubocop
    ruby-validate
  ]
end
