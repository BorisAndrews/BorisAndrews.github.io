# CLAUDE.md — assets/ipynb/

Jupyter notebooks for the private notebooks page. Two subdirectories: `code/` (computational experiments) and `notes/` (mathematical notes). Boris's reading-group talks are Colab notebooks in `notes/`, linked from the schedule in `_includes/reading-group/`.

## Firedrake import cell

Every notebook that uses Firedrake opens with a cell that installs via fem-on-colab when running on Colab and falls back to a direct import when Firedrake is already available locally. Two versions are in use. The older one (`code/enstrophy`, `ferrofluids`, `onsager`, ...) installs the development build:

```python
try:
    !wget "https://fem-on-colab.github.io/releases/firedrake-install-development-real.sh" -O "/tmp/firedrake-install.sh"
    !bash "/tmp/firedrake-install.sh"
    from firedrake import *  # noqa: F401
except:
    from firedrake import *  # noqa: F401
```

The newer one (`notes/long_steps`, `notes/hybridisation`) checks for Colab first, so it never runs `wget` locally, and installs the release build:

```python
try:
    import google.colab  # noqa: F401
except ImportError:
    from firedrake import *
else:
    try:
        from firedrake import *
    except ImportError:
        !wget "https://fem-on-colab.github.io/releases/firedrake-install-release-real.sh" -O "/tmp/firedrake-install.sh"
        !bash "/tmp/firedrake-install.sh"
        from firedrake import *
```

## Running notebooks locally

As of Oct 2026 the laptop's Firedrake venv has **no Jupyter tooling** (no `ipykernel`, `nbclient`, `nbformat` or `IPython`), so there is no kernel to execute a notebook with. Boris has offered to install it:

```sh
~/.firedrake/venv-firedrake/bin/python -m pip install ipykernel nbclient nbformat
```

(None of these touch the source-built PETSc, mpi4py or h5py, so the Firedrake wheel rule in `Software/CLAUDE.md` doesn't bite.) Check whether it's there before improvising.

Outputs saved in a notebook come from wherever it was last run. `notes/hybridisation.ipynb` was executed on the laptop's Firedrake (2026.4.1) by a stand-in runner, **not on Colab**. Its use of `finat.ufl`, odd-degree `"CR"` above 1, `variant="integral"` DG and Slate's `SCPC` is untested against the fem-on-colab release build.

**Never name a notebook global `mesh`.** `from firedrake import *` also exports the `firedrake.mesh` submodule, so if the cell defining `mesh = ...` hasn't run (fresh runtime, cells run out of order), later cells silently pick up the module and fail deep inside Firedrake with `AttributeError: module 'firedrake.mesh' has no attribute 'topology'`. `notes/hybridisation` hit this on Colab; it now uses `demo_mesh`.

Interactive outputs (HTML + `<script>`, e.g. the click-a-DoF coupling diagrams in `notes/hybridisation`) render in Colab and Jupyter but not in GitHub's static notebook viewer.
