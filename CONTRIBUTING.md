<h1 align="center">Contributing</h1>

# 1. Reporting a bug

If you found a bug, open an issue at https://github.com/cornusandu-org/stlib-ext/issues/new.

Make sure to include an example of the issue appearing, and steps to reproduce the issue.

Start the issue title with "[BUG]"

# 2. Fixing a bug

If you found a bug and want to fix it, first [open an issue](https://github.com/cornusandu-org/stlib-ext/issues/new). If you simply want to fix a bug that already has an Issue, don't open another one.

Create a PR fixing the issue.

In the PR, add yourself to `.github/CODEOWNERS` for any files you created yourself (this does not apply to modified files). Don't forget to also add your name at the bottom of this file (section 6).

# 3. Suggesting a feature

If you have a feature you'd like to get added, [open an issue](https://github.com/cornusandu-org/stlib-ext/issues/new) with more details (such as the feature itself, implementation details, relevant examples, or other similar Issues).

Make sure to start the issue title with "[FEAT]".

# 4. Other kinds of Issues

* "[BUG]": Bugs, unexpected or unwanted behaviour
* "[FEAT]": Requested or planned features
* "[CQ]": Code Quality changes
* "[DOCS]": Documentation changes
* "[MISC]": Miscellaneous, anything that doesn't fit into any of the categories above

# 5. Code Quality Standards

## 1: Linting

Before submitting a PR, run `mypy` to ensure there are no issues with your code. Patch all `mypy` errors and warnings.

## 2: Type Annotations

Use type annotations wherever possible. Example: `collections.abc.Callable`, `typing.Optional`, `collections.abc.Iterable`, `typing.Any`, etc.

# 6. Contributors

1. [@cornusandu](https://github.com/cornusandu)
