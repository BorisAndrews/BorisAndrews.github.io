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

The laptop's Firedrake venv has `ipykernel`, `nbclient` and `nbformat` (installed 13 Oct 2026; they don't touch the source-built PETSc, mpi4py or h5py), so notebooks can be executed with a real kernel. Run it through `Software/firedrake-run` so the kernel inherits Firedrake's environment, with `NotebookClient(nb, timeout=1800, kernel_name="python3", record_timing=False)`.

Boris edits these notebooks in Colab, which saves JSON with **2-space indent** and **text split into lists of lines**. To write an executed notebook back without churning the whole diff:

- dump with `json.dumps(nb, indent=2, ensure_ascii=False)`, not `nbformat.write` (indent 1);
- call `nbformat.v4.rwbase.split_lines(nb)` first, or every output becomes one long string;
- restore the original top-level `metadata`, since the kernel fills `language_info` with the laptop's Python version.

Execute a copy, check it, and only then overwrite: Boris is often mid-edit in Colab, so `git fetch` first and confirm the local file hasn't changed since you copied it.

Outputs saved in a notebook come from wherever it was last run. `notes/hybridisation.ipynb`'s saved outputs (13 Oct 2026) are from the laptop (Firedrake 2026.4.1, Python 3.14), not Colab; Colab runs the same code about 10× slower.

**Don't give notebook globals names that `from firedrake import *` exports.** The star import brings in far more than it looks like, and whichever ran last wins: if the defining cell hasn't run (fresh runtime), or the Firedrake cell is re-run afterwards (common on Colab), later cells silently get Firedrake's object and fail deep inside it. `notes/hybridisation` hit this twice on Colab:

- `mesh` is the `firedrake.mesh` submodule: `AttributeError: module 'firedrake.mesh' has no attribute 'topology'`. Now `demo_mesh`.
- `rhs` is UFL's `rhs(form)`, so a helper `rhs(mesh)` became `as_form(mesh)`: `ValueError: Unable to convert object to a UFL form: Mesh(...)`. Now `forcing`.

Other exported names that look free but aren't: `lhs`, `system`, `split`, `norm`, `solve`, `project`, `interpolate`, `derivative`, `action`, `adjoint`, `replace`, `dot`, `inner`, `sign`, `exp`, and the UFL indices `i`, `j`, `k`, `l`, `p`, `q`, `r`, `s`. To check a notebook, collect its top-level names with `ast` and intersect them with the namespace from `exec("from firedrake import *", ns)`.

Interactive outputs (HTML + `<script>`, e.g. the click-a-DoF coupling diagrams in `notes/hybridisation`) render in Colab and Jupyter but not in GitHub's static notebook viewer.
