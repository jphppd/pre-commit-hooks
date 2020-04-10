# Pre-commit git hooks

Git hooks to integrate with [pre-commit](http://pre-commit.com).

## Table of contents

- [Configure pre-commit](#configure-pre-commit)
- [Two ways to invoke pre-commit](#two-ways-to-invoke-pre-commit)

## Configure pre-commit

Add to `.pre-commit-config.yaml` in your git repo:

```yaml
    - repo: https://github.com/jphppd/pre-commit-hooks.git
      rev: a.b.c  # Use the ref you want to point at
      hooks:
        - id: generic-check-byte-order-marker
        - id: generic-check-case-conflict
        - id: generic-check-executables-have-shebangs
        - id: generic-check-symlinks
        - id: generic-check-vcs-permalinks
        - id: generic-crlf-forbid
        - id: generic-crlf-remove
        - id: generic-detect-private-key
        - id: generic-en-dashes-forbid
        - id: generic-en-dashes-remove
        - id: generic-end-of-file-fixer
        - id: generic-nbsp-forbid
        - id: generic-nbsp-remove
        - id: generic-tabs-forbid
        - id: generic-tabs-remove
        - id: generic-trailing-whitespace
        - id: git-check
        - id: git-check-added-large-files
        - id: git-check-mailmap
        - id: git-check-merge-conflict
        - id: git-dirty
        - id: git-forbid-binary
        - id: json-check-syntax
        - id: json-pretty-format
        - id: markdown-lint
        - id: python-check-ast
        - id: python-check-builtin-literals
        - id: python-check-docstring-first
        - id: python-debug-statements
        - id: python-double-quote-string-fixer
        - id: python-fix-encoding-pragma
        - id: python-requirements-txt-fixer
        - id: rust-check
        - id: rust-clippy
        - id: rust-fmt
        - id: shell-check
        - id: shell-check-syntax
        - id: shell-format
        - id: shell-script-must-have-extension
        - id: shell-script-must-not-have-extension
        - id: toml-check-syntax
        - id: xml-check-syntax
        - id: yaml-check-syntax
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
