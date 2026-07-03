release_script_generation
==========================

make_script Function
--------------------

The *irelease* library exposes a single, highly‑polished helper called :func:`make_script`. Its primary role is to introspect the current working directory and emit two ready‑to‑run artifacts: a POSIX‑compliant Bash script named ``release.sh`` and an optional Python wrapper called ``release.py``. The generated scripts encapsulate the entire release pipeline for a Python package, from semantic version bumping through wheel creation, Twine upload to PyPI, GitHub release tagging, and finally cleanup of temporary build directories.

By automating this workflow, developers are freed from maintaining repetitive shell snippets or ad‑hoc Python scripts that often diverge between projects. The generated files become a single source of truth for the release process; any change in the underlying logic is reflected immediately when :func:`make_script` is rerun. This guarantees reproducibility across local machines, CI environments, and even external contributors who may clone the repository and run ``release.sh`` without needing to understand the intricacies of packaging or publishing.

The function performs a lightweight scan for either a ``pyproject.toml`` (PEP 517/518) or a legacy ``setup.py``. Once identified, it writes the scripts with executable permissions by default. The Bash wrapper uses standard utilities such as ``git``, ``python -m build``, and ``twine`` to perform each step, while the Python wrapper merely forwards command‑line arguments to the Bash script, providing a more familiar interface for users who prefer Python over shell scripting.

Because the scripts are generated at runtime, they can incorporate project‑specific metadata (e.g., current version, repository URL) directly into the workflow. This dynamic generation also means that any future changes to packaging tools or release conventions only require updating the :func:`make_script` implementation; downstream users will automatically receive the updated logic without touching their own scripts.

.. list-table::
   :widths: 20 10 70
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - None
     - N/A
     - The function does not accept any parameters; it operates on the current working directory.

.. code-block:: python

   # Generate release scripts for the current package
   from irelease import make_script
   make_script()
   # After execution you will find release.sh (bash) and release.py (Python wrapper) in the project root.
   # Run them:
   # bash release.sh --verbose 2
   # python release.py --clean

Important Notes
---------------

* The current directory must contain either a ``pyproject.toml`` or a ``setup.py``; otherwise :func:`make_script` will raise an informative error.
* The generated scripts are executable by default. On Unix‑like systems, ensure they have the correct permissions with ``chmod +x release.sh release.py`` if necessary.
* Each script supports a ``--help`` flag that lists available options such as ``--verbose``, ``--clean``, and others relevant to the release workflow.

.. include:: add_bottom.add