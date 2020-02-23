# Pre-commit git hooks

Git hooks to integrate with [pre-commit](http://pre-commit.com).

## Table of contents

- [Configure pre-commit](#configure-pre-commit)
- [Two ways to invoke pre-commit](#two-ways-to-invoke-pre-commit)
- [Available hooks](#available-hooks)
  * [`check-mailmap`](#check-mailmap)
  * [`forbid-binary`](#forbid-binary)
  * [`git-check`](#git-check)
  * [`git-dirty`](#git-dirty)

## Configure pre-commit

Add to `.pre-commit-config.yaml` in your git repo:

    - repo: https://github.com/jphppd/pre-commit-hooks.git
      rev: a.b.c  # Use the ref you want to point at
      hooks:
        - id: check-mailmap
        - id: forbid-binary
        - id: git-check  # Configure in .gitattributes
        - id: git-dirty  # Configure in .gitignore

## Two ways to invoke pre-commit

If you want to invoke the checks as a git pre-commit hook, run:

    pre-commit install

If you want to run the checks on-demand (outside of git hooks), run:

    pre-commit run --all-files --verbose

The [test harness](TESTING.md) of this git repo uses the second approach
to run the checks on-demand.


## Available hooks


### `check-mailmap`

**What it does**

Detect botched name/email translations in git history.

`git shortlog -sn` is useful to summarize contributors.

However, it gets muddy when an email address is associated with multiple names.<br/>
Reasons include:

* the author's full name was messed up
* not always written the same way
* the author has multiple email addresses

**More info**

Sample output for good condition:

    $ pre-commit run check-mailmap --all-files --verbose
    [check-mailmap] Detect if an email address needs to be added to mailmap.......................Passed


Sample output for bad condition: TODO


### `forbid-binary`

**What it does**

Prevent binary files from being committed.

**More info**

Fail if a file appears to be a [binary filetype](https://pre-commit.com/#filtering-files-with-types).
Override with an `exclude` regular expression,
such as the example [**here**](.pre-commit-config.yaml).

### `git-check`

**What it does**

Check both committed and uncommitted files for git conflict markers and
whitespace errors according to `core.whitespace` and `conflict-marker-size`
configuration in a git repo.

**More info**

This hook uses `git` itself to perform the checks.<br/>
The git-scm book describes
[**here**](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_code_core_whitespace_code)
that there are six `core.whitespace` checks.

Enabled by default:

* `blank-at-eol`, which looks for spaces at the end of a line
* `blank-at-eof`, which looks for blank lines at the end of a file
* `space-before-tab`, which looks for spaces before tabs at the beginning of a line

Disabled by default:

* `indent-with-non-tab`, which
  looks for lines that begin with spaces instead of tabs
  (and is controlled by the `tabwidth` option)
* `tab-in-indent`, which looks for tabs in the indentation portion of a line
* `cr-at-eol`, which looks for carriage returns at the end of a line

**Custom configuration (overrides)**

The git documentation describes
[**here**](https://git-scm.com/docs/git-config#git-config-corewhitespace)
how to configure the various checks.

The recommended place to persist the configuration is the `.gitattributes` file,
described [**here**](https://git-scm.com/docs/gitattributes#_checking_whitespace_errors).
It provides fine control over configuration per file path for both
`core.whitespace` and `conflict-marker-size`.

Real-world examples of `.gitattributes` file to configure overrides per path:

* https://github.com/jumanjihouse/devenv/blob/master/.gitattributes


### `git-dirty`

**What it does**

During the pre-commit stage, do nothing.<br/>
Otherwise, detect whether the git tree contains modified, staged, or untracked files.

**More info**

This is useful to run near the end of a CI process to
see if a build step has modified the git tree in unexpected ways.

**Custom configuration (overrides)**

The recommended place to persist the configuration is the `.gitignore` file,
described [**here**](https://git-scm.com/docs/gitignore).
