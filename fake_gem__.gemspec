# frozen_string_literal: true

Gem::Specification.new do |s|
  s.name = 'fake_gem__'
  s.version = '0.0.0'
  s.authors = ['John Doe']
  s.summary = 'pre-commit hooks for ruby projects'
  s.description = 'pre-commit hooks for ruby projects'
  s.bindir = 'hooks/ruby'
  s.executables = %w[
    puppet-erb-validate
    puppet-r10k-validate
    puppet-validate
  ]
end
