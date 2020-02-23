# Pre-commit git hooks

Git hooks to integrate with [pre-commit](http://pre-commit.com).

## Table of contents

- [Configure pre-commit](#configure-pre-commit)
- [Two ways to invoke pre-commit](#two-ways-to-invoke-pre-commit)
- [Available hooks](#available-hooks)

## Configure pre-commit

Add to `.pre-commit-config.yaml` in your git repo:

    - repo: https://github.com/jphppd/pre-commit-hooks.git
      rev: a.b.c  # Use the ref you want to point at
      hooks:
        - id: ...

## Two ways to invoke pre-commit

If you want to invoke the checks as a git pre-commit hook, run:

    pre-commit install

If you want to run the checks on-demand (outside of git hooks), run:

    pre-commit run --all-files --verbose

The [test harness](TESTING.md) of this git repo uses the second approach
to run the checks on-demand.

## Available hooks

