# is-none

[![PyPI version](https://img.shields.io/pypi/v/is-none.svg)](https://pypi.org/project/is-none/)
[![Python versions](https://img.shields.io/pypi/pyversions/is-none.svg)](https://pypi.org/project/is-none/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A minimal, deterministic utility for checking whether a value is exactly `None`.

## Overview

`is-none` provides a single, explicit function for identity-based `None` checks in Python.
It exists to make intent unambiguous in codebases where clarity, correctness, and
long-term maintainability are prioritized.

The behavior is deliberately trivial and fully specified. There is no coercion, no
interpretation of truthiness, and no behavior beyond an identity comparison against
the singleton `None`.

This package is suitable for production use, testing utilities, and type-sensitive
environments.

---

## Design Principles

- **Explicit semantics**  
  The function performs an identity comparison (`value is None`) and nothing else.

- **Deterministic behavior**  
  The result depends solely on object identity. There are no side effects.

- **Minimal surface area**  
  A single public function with a stable signature.

- **Zero dependencies**  
  No runtime dependencies and no optional integrations.

- **Long-term stability**  
  The API is intentionally complete and not expected to change.

---

## Installation

```bash
pip install is-none
````

---

## Usage

```python
from is_none import is_none

is_none(None)      # True
is_none(0)         # False
is_none("")        # False
is_none(False)     # False
is_none([])        # False
```

---

## API Reference

### `is_none(value: Any) -> bool`

Determine whether a value is exactly `None`.

The function uses identity comparison and does not consider other falsy values
(e.g. `0`, `""`, `False`, empty containers) to be equivalent to `None`.

#### Parameters

* **value** (`Any`)
  The value to evaluate.

#### Returns

* **bool**
  `True` if and only if `value is None`.

---

## Rationale

In large or long-lived codebases, implicit truthiness checks can obscure intent:

```python
if not value:
    ...
```

This pattern conflates `None` with other falsy values and can lead to subtle bugs or
reduced readability.

`is-none` exists to make the check explicit:

```python
if is_none(value):
    ...
```

This can be particularly useful in:

* shared utility libraries
* validation and normalization layers
* testing and assertion helpers
* codebases with strict linting or typing requirements

---

## Non-Goals

The following are explicitly out of scope for this project:

* Providing aliases such as `is_not_none`
* Supporting custom sentinel values
* Treating falsy values as equivalent to `None`
* Adding configuration, flags, or environment-based behavior
* Expanding into a general-purpose validation or typing library

If your use case requires any of the above, this package is likely not a good fit.

---

## Versioning

This project follows **Semantic Versioning**.

Version `1.0.0` represents a stable, production-ready API.
No breaking changes are anticipated.

---

## Compatibility

* Python **3.13+**
* Platform-independent
* No reliance on implementation-specific behavior

---

## License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## Project Status

This project is complete and maintained.
No additional features are currently planned.
