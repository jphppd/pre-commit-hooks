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
  s.add_dependency 'ruby-lint'
  s.bindir = 'hooks/ruby'
  s.executables = [
    'markdown-linter',
    'ruby-bundle-auditer',
    'ruby-fasterer',
    'ruby-reek',
    'ruby-rubocop'
  ]
end
