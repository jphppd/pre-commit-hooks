# Pre-commit git hooks

Git hooks to integrate with [pre-commit](http://pre-commit.com).

## Table of contents

- [Configure pre-commit](#configure-pre-commit)
- [Two ways to invoke pre-commit](#two-ways-to-invoke-pre-commit)
- [Available hooks](#available-hooks)
  * [`git-check-mailmap`](#git-check-mailmap)
  * [`git-forbid-binary`](#git-forbid-binary)
  * [`git-check`](#git-check)
  * [`git-dirty`](#git-dirty)
  * [`markdown-lint`](#markdown-lint)
  * [`shell-check`](#shellcheck)
  * [`shell-script-must-have-extension`](#shell-script-must-have-extension)
  * [`shell-script-must-not-have-extension`](#shell-script-must-not-have-extension)
  * [`shell-format`](#shell-format)
  * [`rust-fmt`](#rust-fmt)
  * [`rust-check`](#rust-check)
  * [`rust-clippy`](#rust-clippy)


## Configure pre-commit

Add to `.pre-commit-config.yaml` in your git repo:

    - repo: https://github.com/jphppd/pre-commit-hooks.git
      rev: a.b.c  # Use the ref you want to point at
      hooks:
        - id: check-mailmap
        - id: forbid-binary
        - id: git-check  # Configure in .gitattributes
        - id: git-dirty  # Configure in .gitignore
        - id: markdownlint # Configure in .mdlrc
        - id: script-must-have-extension
        - id: script-must-not-have-extension
        - id: shellcheck
        - id: shfmt

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

### `markdown-lint`

**What it does**

Check markdown files and flag style issues.

**More info**

[markdownlint](https://github.com/markdownlint/markdownlint)
is a ruby tool that examines markdown files against various
[style rules](https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md).

**Custom configuration (overrides)**

Provide `.mdlrc` in the top-level of your project git repo.

For an annotated example of overrides, see in this project:

* [`.mdlrc`](.mdlrc)
* [`ci/jumanjistyle.rb`](ci/jumanjistyle.rb)


### `shell-check`

**What it does**

Run shellcheck against scripts.

**More info**

This hook uses the `identify` library of pre-commit to identify shell scripts.
If the file is a shell script, then run shellcheck against the file.

By default, this hooks passes `-e SC1091` to shellcheck.
Override locally with the `args` parameter in `.pre-commit-config.yaml`.

:warning: The `shellcheck` hook requires
[shellcheck](https://github.com/koalaman/shellcheck).


### `shell-script-must-have-extension`

**What it does**

The [Google shell style guide](https://google.github.io/styleguide/shell.xml#File_Extensions)
states:

> Libraries must have a `.sh` extension and should not be executable.

This hook checks for conformance.

**Default**

Filter on files that are both `shell` **and** `non-executable`.

    types: [shell, non-executable]

**Custom configuration (overrides)**

Suppose your local style guide is the opposite of the default.<br/>
In other words, you require **executable** scripts to end with `.sh`.<br/>
Put this in your `.pre-commit-config.yaml`:

    - repo: https://github.com/jumanjihouse/pre-commit-hooks
      rev: <version>
      hooks:
        - id: script-must-have-extension
          name: Local policy is to use .sh extension for shell scripts
          types: [shell, executable]

Note the use of "name" to override the hook's default name and
provide context for the override.


### `shell-script-must-not-have-extension`

**What it does**

The [Google shell style guide](https://google.github.io/styleguide/shell.xml#File_Extensions)
states:

> Executables should have no extension (strongly preferred)

This hook checks for conformance.

**Default**

Filter on files that are both `shell` **and** `executable`.

    types: [shell, executable]

**Custom configuration (overrides)**

You can use this hook to forbid filename extensions on other types of files.<br/>
Put something like this in your `.pre-commit-config.yaml`:

    - repo: https://github.com/jumanjihouse/pre-commit-hooks
      rev: <version>
      hooks:
        - id: script-must-not-have-extension
          name: Local policy is to exclude extension from all shell files
          types: [shell]

        - id: script-must-not-have-extension
          name: Executable Ruby scripts must not have a file extension
          types: [ruby, executable]

Note the use of "name" to override the hook's default name and
provide context for the override.


### `shfmt`

**What it does**

Run `shfmt` against scripts with args.

**More info**

This hook uses the `identify` library of pre-commit to identify shell scripts.
If the file is a shell script, then run shfmt against the file.

By default, this hooks passes `-l -i 2 -ci` to shfmt to conform to the
[Google Shell Style Guide](https://google.github.io/styleguide/shell.xml).
Override locally with the `args` parameter in `.pre-commit-config.yaml`.

:warning: The `shfmt` hook requires
[shfmt](https://github.com/mvdan/sh/releases).


### `rust-fmt`

**What it does**

Run `rust-fmt` against rust files.


### `rust-check`

**What it does**

Run `cargo check` against rust files.



### `rust-clippy`

**What it does**

Run `cargo clippy` against rust files.



## Sources

- [jumanjihouse](https://github.com/jumanjihouse/pre-commit-hooks)