# Pre-commit git hooks

Git hooks to integrate with [pre-commit](http://pre-commit.com).

## Table of contents

* [Configure pre-commit](#configure-pre-commit)
* [Two ways to invoke pre-commit](#two-ways-to-invoke-pre-commit)

## Configure pre-commit

Add to `.pre-commit-config.yaml` in your git repo:

```yaml
---
# https://pre-commit.com/
# Install pre-commit for your current user:
#   pip3 install --user pre-commit
#
# and then, in the git repo:
#   pre-commit install

repos:
  - repo: https://github.com/jphppd/pre-commit-hooks.git
    rev: a.b.c  # Use the ref you want to point at
    hooks:
      - id: git-check-mailmap
      - id: git-forbid-binary
      - id: git-check
      - id: git-dirty
      - id: git-check-added-large-files
      - id: git-check-merge-conflict
      - id: git-commit-msg
      - id: generic-check-byte-order-marker
      - id: generic-check-case-conflict
      - id: generic-check-executables-have-shebangs
      - id: generic-check-symlinks
      - id: generic-check-vcs-permalinks
      - id: generic-detect-private-key
      - id: generic-end-of-file-fixer
      - id: generic-trailing-whitespace
      - id: generic-crlf-forbid
      - id: generic-crlf-remove
      - id: generic-tabs-forbid
      - id: generic-tabs-remove
      - id: generic-nbsp-forbid
      - id: generic-nbsp-remove
      - id: generic-en-dashes-forbid
      - id: generic-en-dashes-remove
      - id: ansible-lint
      - id: c-cpp-cmake-format
      - id: c-cpp-cmake-lint
      - id: c-cpp-clang-format-c-config
      - id: c-cpp-clang-format-c
      - id: c-cpp-clang-format-cpp
      - id: c-cpp-clang-format-header
      - id: dockerfile-lint
      - id: dockerfile-lint
      - id: html-validate
      - id: html-hint
      - id: html-lint
      - id: html-forbid-img-without-alt-text
      - id: html-forbid-non-std-attributes
      - id: html-detect-missing-css-classes-html
      - id: html-detect-missing-css-classes-css
      - id: html-tags-blacklist
      - id: html-attributes-blacklist
      - id: js-eslint
      - id: js-prettier
      - id: jinja-lint
      - id: json-check-syntax
      - id: json-pretty-format
      - id: markdown-lint
      - id: perl-critic
      - id: perl-tidy
      - id: php-lint-all
      - id: php-lint
      - id: php-unit
      - id: php-cs
      - id: php-cbf
      - id: php-cs-fixer
      - id: puppet-lint
      - id: puppet-validate
      - id: puppet-erb-validate
      - id: puppet-r10k-validate
      - id: puppet-epp-validate
      - id: python-check-ast
      - id: python-check-builtin-literals
      - id: python-check-docstring-first
      - id: python-debug-statements
      - id: python-double-quote-string-fixer
      - id: python-fix-encoding-pragma
      - id: python-requirements-txt-fixer
      - id: python-safetydb
      - id: python-pyupgrade
      - id: python-isort-config
      - id: python-isort-seed-config
      - id: python-isort
      - id: python-black
      - id: python-pylint-config
      - id: python-pylint
      - id: python-pydocstyle
      - id: python-bandit
      - id: python-setup-cfg-fmt
      - id: rst-linter
      - id: ruby-validate
      - id: ruby-bundle-auditer
      - id: ruby-fasterer
      - id: ruby-reek
      - id: ruby-rubocop
      - id: rust-fmt
      - id: rust-check
      - id: rust-clippy
      - id: shell-check-syntax
      - id: shell-check
      - id: shell-script-must-have-extension
      - id: shell-script-must-not-have-extension
      - id: shell-bashate
      - id: shell-beautysh
      - id: toml-check-syntax
      - id: xml-check-syntax
      - id: yaml-check-syntax
      - id: yaml-yamllint
```

## Two ways to invoke pre-commit

If you want to invoke the checks as a git pre-commit hook, run:

```
    pre-commit install
```

If you want to run the checks on-demand (outside of git hooks), run:

```
    pre-commit run --all-files --verbose
```
