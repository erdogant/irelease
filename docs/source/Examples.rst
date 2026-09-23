The *irelease* package offers a concise API that automates the most common tasks involved in publishing Python projects.  This page walks through several representative use cases, explains why each parameter matters in real‑world release workflows, and provides runnable code snippets that can be dropped straight into a Python REPL or script.

Basic Run
##################

The simplest way to trigger a release is to call `irelease` or `pyrelease` with no arguments.
This default invocation relies on module‑level configuration discovered from the current working directory.
By inspecting files such as ``setup.py`` or ``pyproject.toml`` it automatically determines the project name, version, and author information.
The function then performs a minimal set of actions: it builds source and wheel distributions, uploads them to PyPI using the locally configured credentials, and creates a corresponding GitHub release tag if a remote repository is detected.

.. code-block:: bash

    pyrelease
    irelease

Run with Parameters
####################################

Often users need finer control over the release process.  The `irelease` function accepts several optional keyword arguments that let you override the automatic discovery logic, toggle cleaning and installation steps, or supply custom Twine configuration.  Specifying these options is particularly useful when working on multiple projects in a single environment or when integrating with external CI services that provide their own authentication mechanisms.

Parameters of `irelease`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Parameters of irelease.run
   :widths: 20 15 65
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - name
     - str
     - Author/username identifier used for tagging and release metadata.
   * - script_type
     - str
     - Type of script to run (e.g., ``'pca'``) – determines which internal workflow is invoked.
   * - clean
     - bool
     - Whether to remove existing build artifacts before starting a new build cycle. ``True`` guarantees a fresh environment; ``False`` preserves intermediate files for debugging.
   * - install
     - bool
     - Controls whether the freshly built wheel should be installed into the current Python environment.  Handy when you want to test the release immediately after upload.
   * - twine
     - any
     - Path or configuration object passed directly to Twine. ``None`` uses the default ``~/.pypirc`` settings.
   * - verbose
     - int
     - Verbosity level for logging; higher values emit more detailed progress information useful during troubleshooting.
   * - repository_url
     - str or None
     - URL of a custom package registry (for example ``https://nexus.company.com/repository/pypi/``). If omitted, packages are uploaded to PyPI. Use this to target internal registries or testing indexes. Overrides the ``IRELEASE_REPOSITORY_URL`` environment variable.
   * - api_key
     - str or None
     - API token or password for the target registry. When supplied it is passed directly to Twine and takes precedence over credentials found in ``.pypirc``. This is useful for CI systems that inject credentials at runtime. Overrides the ``IRELEASE_API_KEY`` environment variable.
   * - registry
     - str
     - Named section in ``.pypirc`` to read credentials from (default: ``'pypi'``). Use this to select a credentials profile (for example ``'corporate'``) when your ``.pypirc`` contains multiple registry entries. Overrides the ``IRELEASE_REGISTRY`` environment variable.

A typical invocation that disables cleaning and installation while enabling verbose output might look like this:

.. code-block:: bash

    irelease --help

Registry and credentials
------------------------

In many organizations you will want to publish packages to an internal index or use short‑lived API tokens injected by your CI/CD system. The newer ``--repository-url``, ``--api-key``, and ``--registry`` options make that straightforward and safe:

- Explicit ``--repository-url`` lets you target a private Nexus/Artifactory/DevPI server without modifying global config.
- Passing ``--api-key`` on the command line (or via the ``IRELEASE_API_KEY`` environment variable) avoids storing secrets in ``.pypirc`` and enables ephemeral credentials in CI.
- The ``--registry`` option selects an alternate named section from ``.pypirc`` when you maintain multiple registry profiles locally.

Code examples
~~~~~~~~~~~~~

CLI example (upload to a corporate Nexus using a token):

.. code-block:: bash

    irelease --repository-url https://nexus.company.com/repository/pypi/ --api-key "pypi-MyToken123"

CLI example (use a named .pypirc profile):

.. code-block:: bash

    irelease --registry corporate

Python API example (equivalent):

.. code-block:: python

    from irelease import run

    # Upload to a custom registry using an API key supplied at runtime
    run(repository_url="https://nexus.company.com/repository/pypi/", api_key="pypi-MyToken123")

    # Use a named .pypirc section
    run(registry="corporate")


Retrieve PyPI Credentials
####################################

irelease can automatically read authentication details from a local ``.pypirc`` configuration file, which is the standard location for Twine to find your PyPI username and password or API token.
The function returns a tuple ``(username, password)`` if both keys are present in the ``[pypi]`` section; otherwise it falls back to ``(None, None)``.  When the optional ``verbose`` flag is set to a value of three or higher, the function prints diagnostic information and prompts the user to provide missing credentials interactively.

.. code-block:: bash

    irelease --help

.. include:: add_bottom.add
