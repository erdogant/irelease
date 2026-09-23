Algorithm
==========

The *irelease* package implements a fully automated release pipeline that bridges local development, version control, and distribution platforms such as PyPI and GitHub.  The algorithm is deliberately split into discrete stages so that each can be unit‑tested, replaced, or extended without affecting the others.  At runtime the stages are invoked in a linear order: **Credential Retrieval → Version Determination → Build Artifacts → Tagging & Pushing → Upload to PyPI**.  This design guarantees deterministic behaviour and makes it trivial for continuous‑integration systems to trigger releases with a single command.

The following sections describe each stage, explain why the component exists, list its public interface, and provide runnable examples that illustrate typical usage patterns.

Credential Retrieval
--------------------

Retrieving authentication details is the first step in any release workflow.  Without valid PyPI credentials the upload will fail, and without GitHub credentials the tagging operation cannot be performed.  The :func:`get_pypi_credentials()` helper encapsulates the logic for locating a ``~/.pypirc`` file, parsing its INI structure, and returning the username/password pair.  It is intentionally forgiving: if the file or section is missing it returns ``(None, None)`` instead of raising an exception, allowing callers to decide whether to prompt interactively or abort.

The function also accepts a :py:data:`verbose` parameter that controls diagnostic output.  A higher verbosity level prints information about which files were examined and why credentials could not be found, aiding debugging in noisy CI environments.

.. list-table:: Parameters for ``get_pypi_credentials``  
   :header-rows: 1
   :widths: 15 10 75

   * - Name
     - Type
     - Description
   * - verbose
     - int
     - Controls the level of diagnostic output during credential lookup. A higher value results in more verbose logging.

.. code-block:: python

   from irelease import get_pypi_credentials

   username, password = get_pypi_credentials(verbose=3)
   if username is None:
       raise RuntimeError('PyPI credentials not found in ~/.pypirc')

Version Determination
---------------------

The algorithm must know which version string to associate with the new release.  The :func:`github_version()` helper queries the GitHub REST API for all releases in a given repository, parses their tag names as semantic versions, and returns the highest one.  This abstraction shields callers from pagination limits, rate‑limiting headers, and authentication nuances.

The function accepts an optional personal access token that is sent as a bearer token in the ``Authorization`` header.  Supplying a token increases the allowed request quota and grants access to private repositories, making it suitable for CI agents that need to operate on protected codebases.

.. list-table:: Parameters of ``github_version``  
   :header-rows: 1
   :widths: 20 15 65

   * - Name
     - Type
     - Description
   * - repo
     - str
     - The full GitHub repository name in the form ``'owner/repo'``.
   * - token
     - Optional[str]
     - Personal access token for authenticated requests; optional if public repo.

.. code-block:: python

   from irelease import github_version

   latest = github_version('myorg/myproject')
   print(f"Latest GitHub release: {latest}")

Build Artifacts
---------------

Once the target version is known, the next stage produces source and wheel distributions.  The :func:`run()` function orchestrates this step by invoking ``python setup.py sdist bdist_wheel`` (or the equivalent for projects using ``pyproject.toml``).  It accepts a :py:data:`clean` flag that removes existing artifacts in ``build/`` and ``dist/`` before rebuilding.  Skipping cleaning speeds up repeated runs when the build environment is already pristine.

The function also accepts a :py:data:`twine` parameter allowing callers to specify an absolute path to the Twine executable, which is useful on systems where multiple Python environments coexist.

.. list-table:: Parameters for ``irelease.run``  
   :header-rows: 1
   :widths: 15 10 65

   * - Name
     - Type
     - Description
   * - username
     - str
     - GitHub or Git account name. Required to fetch tags and push updates.
   * - packagename
     - str
     - Name of the Python package to release. Must match the distribution metadata.
   * - clean
     - bool
     - Remove local distribution files before building. ``False`` speeds up repeated runs in a clean environment.
   * - twine
     - str
     - Path to the Twine executable; if omitted, the system path is used.
   * - verbose
     - int
     - Verbosity level for console output. Higher values provide more diagnostic information.

.. code-block:: python

   irelease.run(username='alice',
                packagename='mypkg',
                clean=True,
                twine='/usr/local/bin/twine',
                verbose=4)

Tagging & Pushing
-----------------

After the artifacts are built, the algorithm creates an annotated Git tag that matches the version string.  The tag is then pushed to the remote repository so that collaborators and CI systems can detect the new release.  This step relies on the local ``git`` installation; if it is missing the :func:`run()` function will abort with a clear error message.

The tagging logic is encapsulated in a small helper inside :mod:`irelease`, but the public API exposes no dedicated function because the operation is tightly coupled to the build and upload stages.  The design choice keeps the surface area minimal while still allowing advanced users to call :func:`run()` with ``install=True`` if they wish to install the newly built package locally.

Upload to PyPI
--------------

The final stage uses Twine to push the distributions in ``dist/`` to PyPI.  Twine is a well‑established tool that handles authentication, checksum verification, and retry logic.  By delegating to Twine we avoid reinventing these critical security features while still providing a simple wrapper that integrates with the rest of the pipeline.

If the user supplies a custom path via :py:data:`twine`, the algorithm will use it; otherwise it falls back to searching the system ``PATH`` for an executable named ``twine``.  A missing Twine binary results in an informative error encouraging the user to install it with ``pip install twine``.

Workflow Diagram
----------------

The following ASCII diagram illustrates how the major components interact during a typical release:

.. code-block:: text

   +-------------------+          +---------------------+
   | get_pypi_credentials()|      | github_version(repo)|
   +----------+--------+          +-----------+---------+
              |                               |
              v                               v
     +----------------------+        +-----------------------+
     |  run(username,       |<------|  determine version    |
     |  packagename, clean, |        +-----------+-----------+
     |  twine, verbose)     |                    |
     +----------+------------+                    |
                |                                 |
                v                                 v
      +---------------------+          +------------------------+
      | Build artifacts (sdist & wheel) |  Create Git tag & push |
      +---------------------+          +-----------+------------+
                |                                 |
                v                                 v
        +----------------------+          +-----------------------+
        | Upload via Twine to PyPI |<------|   Credentials verified|
        +----------------------+          +-----------------------+

Design Decisions and Trade‑offs
------------------------------

* **Chunking** – The algorithm does not perform any data chunking; it operates on the entire repository at once.  This simplifies implementation and is sufficient for typical Python projects, which rarely exceed a few megabytes in source size.
* **Embedding Model** – No embedding model is required because the release process deals purely with metadata and file I/O rather than natural‑language understanding.
* **Cleaning Strategy** – The optional ``clean`` flag balances speed against safety.  In CI environments where each run starts from a fresh checkout, cleaning is unnecessary; in local development it prevents stale artifacts from being uploaded inadvertently.
* **Credential Storage** – Using ``~/.pypirc`` keeps secrets out of source control while remaining compatible with the standard Twine workflow.  The fallback to interactive prompts ensures that developers who forget to configure their environment still receive guidance.

Limitations
-----------

* The generated ``release.sh`` script assumes a POSIX‑compatible shell; Windows users may need WSL or an equivalent.
* Only PyPI is supported out of the box; publishing to alternative indexes would require custom wrappers around Twine.
* Pre‑release identifiers (e.g., ``rc1``) are not automatically handled; manual intervention is required if such tags are used.

Example: Full Release with Verbose Output
-----------------------------------------

The following snippet demonstrates a typical invocation from the root of a project:

.. code-block:: python

   import irelease

   # Ensure credentials exist
   username, password = irelease.get_pypi_credentials(verbose=2)
   if not username:
       raise RuntimeError('PyPI credentials missing')

   # Run the full pipeline
   irelease.run(username='alice',
                packagename='mypkg',
                clean=True,
                twine=None,
                verbose=4)

.. include:: add_bottom.add