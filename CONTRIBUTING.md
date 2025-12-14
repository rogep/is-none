# Contributing to is-none

Thank you for your interest in contributing to `is-none`.

Before opening an issue or pull request, please read the guidelines below carefully.

---

## Scope of Contributions

`is-none` is intentionally minimal and feature-complete.

The public API consists of a single function with fully specified behavior.
As such, most feature requests will fall outside the scope of this project.

Examples of changes that are **unlikely to be accepted** include:

- Adding new public functions
- Changing or extending the semantics of `is_none`
- Introducing configuration options or flags
- Expanding the package into a broader utility library

---

## Bug Reports

Bug reports are welcome if they demonstrate a deviation from the documented behavior.

A good bug report includes:
- A minimal reproducible example
- The Python version used
- The observed behavior
- The expected behavior, as defined by the documentation

Reports that describe expected Python language behavior (e.g. how `None` works)
may be closed without action.

---

## Pull Requests

Pull requests are accepted for:

- Documentation improvements
- Typing or annotation refinements
- Test coverage improvements
- Build, packaging, or tooling maintenance

All pull requests should:
- Preserve the existing public API
- Include appropriate tests where relevant
- Pass linting and type checking

---

## Design Philosophy

The guiding principle of this project is **explicit simplicity**.

Any change that increases conceptual complexity, expands the public API,
or alters the deterministic nature of the function is unlikely to be accepted.

---

## Code of Conduct

This project follows a standard open source code of conduct.
Be respectful and constructive in all interactions.
