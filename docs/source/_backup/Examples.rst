Examples
#########

The *irelease* library is designed to streamline the release process of Python packages by automating metadata detection, version bumping, distribution building, and publishing to PyPI.  This page walks through three practical examples that illustrate how to use the core API functions in both their simplest form and with a full set of optional parameters.  Each example contains detailed prose explaining why each step is necessary, a parameter table for the function under discussion, and a runnable code snippet that can be copied directly into a Python REPL or script.

Overview
##################

The primary goal of *irelease* is to reduce the cognitive load associated with releasing a package.  Instead of remembering a long chain of shell commands such as ``python -m build`` followed by ``twine upload``, users can invoke a single function that performs all necessary steps: bumping the version number, building source and wheel distributions, uploading to PyPI, creating GitHub tags, and optionally installing the new wheel locally.  By inferring project metadata from standard files (`setup.py` or `pyproject.toml`) *irelease* eliminates the need for manual configuration in most cases.

Because the library is written in pure Python, it can be executed both as a module import and as a command‑line tool.  The dual interface allows developers to embed release logic into scripts or CI pipelines while still providing an interactive experience for local development.  The examples below demonstrate how to leverage each of these interfaces effectively.

Basic Release Workflow
####################################


The most common way to invoke *irelease* in an everyday workflow is by importing the package and calling :func:`irelease.run` followed by :func:`irelease.make_script`.  The first call generates a reusable shell script named ``release.sh`` that can be executed later, while the second call executes the entire release pipeline with default settings.  This pattern is useful for quick, ad‑hoc releases when you are working in the root directory of a repository that follows the standard layout (i.e., it contains either a ``setup.py`` or a ``pyproject.toml``).

Calling :func:`irelease.run` in this manner is advantageous because it reduces the cognitive load of remembering a long chain of shell commands such as ``python -m build`` followed by ``twine upload``.  Instead, you get a single line that encapsulates the entire workflow: bump the version, build distributions, upload to PyPI, and create a GitHub release—all with sensible defaults inferred from the project metadata.

The :func:`irelease.make_script` function is optional but highly recommended for reproducibility.  By generating a script that copies ``irelease.py`` into the current directory, you ensure that future releases can be performed without importing the package again, which is particularly handy in CI environments where the Python environment may not persist between jobs.

.. code-block:: python

   # Import the irelease package
   import irelease

   # Create the release script (optional)
   irelease.make_script()

   # Run the release workflow for the current project
   irelease.run()


Custom Release Parameters
------------------------

When you need finer control over the release process, :func:`irelease.run` accepts a number of keyword arguments that allow you to specify the GitHub user, project name, and various flags controlling cleaning, dependency installation, Twine configuration, and verbosity.  The following table lists all parameters accepted by ``run`` along with their types, default values, and descriptions.

.. list-table:: Parameters for :func:`irelease.run`
   :widths: 20 15 65
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - user
     - str
     - GitHub username or identifier (default: ``None``)
   * - project
     - str
     - Name of the project to release (default: ``None``)
   * - clean
     - bool
     - Remove existing build artifacts before running (default: ``False``)
   * - install
     - bool
     - Install dependencies from ``requirements.txt`` (default: ``False``)
   * - twine
     - any
     - Twine configuration or ``None`` (default: ``None``)
   * - verbose
     - int
     - Verbosity level for logging (0 = silent, higher numbers increase diagnostic output) (default: ``0``)

By setting ``clean=False`` and ``install=False``, you can skip the corresponding steps, which is useful when testing locally or when build artifacts are already present.  The ``twine`` parameter allows passing custom Twine options if you need to upload to a private repository or use alternative authentication methods.

.. code-block:: python

   # Run a release with custom parameters
   import irelease
   irelease.run('erdogant', 'pca',
                clean=False,
                install=False,
                twine=None,
                verbose=3)


Command–Line Interface
---------------------

The *irelease* package can also be executed directly from the terminal.  The entry point is defined in :func:`irelease.main`, which internally parses command‑line arguments using ``argparse`` and then delegates to :func:`irelease.run`.  The following table describes the sole parameter accepted by ``main``.

.. list-table:: Parameters for :func:`irelease.main`
   :widths: 20 15 65
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - argv
     - list[str]
     - System command‑line arguments parsed by ``argparse`` (default: ``sys.argv``)

Using the CLI is straightforward: simply type ``irelease`` in a shell while positioned at the root of your package, and the default workflow will execute.  Adding ``--help`` displays all available options and their descriptions, providing an interactive way to discover the tool’s capabilities without consulting the source code.

.. code-block:: text

   $ irelease            # runs with default settings
   $ irelease --help     # displays help information


Important Notes
---------------

* All examples assume the current working directory is the root of the package you wish to release.
* The :func:`irelease.make_script` function generates a ``release.sh`` script and copies ``irelease.py`` into the current directory for future use.
* When using :func:`irelease.run()` with positional arguments, the first argument is interpreted as the GitHub username and the second as the project name.
* Verbose levels: 0 = silent, higher numbers increase diagnostic output.

.. include:: add_bottom.add
