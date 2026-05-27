# CLAUDE.md — assets/ipynb/

Jupyter notebooks for the private notebooks page. Two subdirectories: `code/` (computational experiments) and `notes/` (mathematical notes).

## Firedrake import cell

Every notebook that uses Firedrake opens with this cell, which installs via fem-on-colab when running on Colab and falls back to a direct import when Firedrake is already available locally:

```python
try:
    !wget "https://fem-on-colab.github.io/releases/firedrake-install-development-real.sh" -O "/tmp/firedrake-install.sh"
    !bash "/tmp/firedrake-install.sh"
    from firedrake import *  # noqa: F401
except:
    from firedrake import *  # noqa: F401
```
