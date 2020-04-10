Gem::Specification.new do |s|
  s.name = 'fake_gem__'
  s.version = '0.0.0'
  s.authors = ['Paul Morgan']
  s.summary = 'pre-commit hooks for ruby projects'
  s.description = 'pre-commit hooks for ruby projects'
  s.add_dependency 'mdl', '0.5.0'
  s.bindir = 'pre_commit_hooks_ruby'
  s.executables = [
    'run-mdl',
  ]
end
