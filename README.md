# Pre-commit git hooks

Git hooks to integrate with [pre-commit](http://pre-commit.com).

## Table of contents

* [Configure pre-commit](#configure-pre-commit)
* [Two ways to invoke pre-commit](#two-ways-to-invoke-pre-commit)

## Configure pre-commit

Add to `.pre-commit-config.yaml` in your git repo:

```yaml
    - repo: https://github.com/jphppd/pre-commit-hooks.git
      rev: a.b.c  # Use the ref you want to point at
      hooks:
        - id: git-check-mailmap
        - id: git-forbid-binary
        - id: git-check
        - id: git-dirty
        - id: git-check-added-large-files
        - id: git-check-merge-conflict
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
        - id: clang-format
        - id: js-eslint
        - id: js-prettier
        - id: jinja-lint
        - id: json-check-syntax
        - id: json-pretty-format
        - id: markdown-lint
        - id: perl-critic
        - id: perl-tidy
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
        - id: python-pyupgrade
        - id: python-yapf
        - id: python-pylint
        - id: python-pydocstyle
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
        - id: shell-format
        - id: shell-bashate
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
