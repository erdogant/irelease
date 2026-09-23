CLI Documentation
###################

Overview of the CLI Generation Workflow
======================================

The *clizard* framework is employed to generate a command‑line interface that faithfully mirrors the logic defined in ``irelease.py``.  When a user launches the generated entry point, typically named ``clizard_main.py``, the script first resolves configuration files such as ``.clizard`` and ``.pypirc``.  These files provide both user overrides for command metadata—like the CLI name and description—and authentication details required to publish packages to PyPI or other registries.  

After loading these settings, a :class:`~cli_builder.GenericCLI` instance is created.  This object encapsulates all parsing logic, command registration, and interactive prompts that give the tool its natural feel.  The CLI registers a single high‑level command, ``/run``, which delegates directly to :func:`irelease.main`.  By exposing only this command, the user interface remains intentionally simple while still providing access to the full release workflow.  

Finally, the script enters the CLI loop by invoking ``.run()`` on the :class:`~cli_builder.GenericCLI` instance.  From that point forward, users can interactively answer prompts or pass arguments to control every step of packaging, signing, and uploading.  The entire flow is self‑contained; developers need only supply the configuration files and the underlying ``irelease.py`` logic.  Because any changes to the release script are automatically reflected in the generated CLI, maintenance overhead stays low while delivering a polished user experience.

The auto‑generation mechanism guarantees that the command line remains up‑to‑date with the core logic without manual edits to ``clizard_main.py``.  This separation of concerns keeps the executable lightweight and maintainable, allowing developers to focus on the release workflow itself rather than boilerplate interface code.

.. code-block:: python
   :caption: Auto‑generated entry point

   # clizard_main.py – auto‑generated entry point
   from cli_builder import build_cli, main

   if __name__ == "__main__":
       main()

The *build_cli* Function
========================

Creating the interactive release engine begins with the :func:`build_cli` function.  Its primary role is to assemble a fully configured :class:`~cli_builder.GenericCLI` object that will drive the user interface.  The function follows a clear sequence of steps: first, it loads any user‑supplied overrides from the ``.clizard`` configuration file; next, it merges those overrides with hard‑coded defaults that describe the CLI’s name and description.

After merging, :func:`build_cli` instantiates the :class:`~cli_builder.GenericCLI`, passing in the combined configuration dictionary.  This object is now ready to accept commands.  The function then registers a single command, ``/run``, which internally calls :func:`irelease.main`.  By exposing this command, users can trigger the entire release pipeline with a simple invocation.  Finally, the fully configured CLI instance is returned for execution.

The design of :func:`build_cli` emphasizes clarity and extensibility.  Adding new commands or altering metadata requires only changes to the configuration files rather than the generated code itself.  This approach keeps the auto‑generated script lightweight and maintainable.

.. list-table:: build_cli Parameters
   :widths: 15 10 75
   :header-rows: 0

   * - **None**

Example usage:

.. code-block:: python
   :caption: Building the CLI

   def build_cli():
       # Load overrides from .clizard if present
       overrides = load_clizard_overrides()
       defaults = {
           "name": "Release Tool",
           "description": "Interactive release workflow for Python packages"
       }
       config = {**defaults, **overrides}

       cli = GenericCLI(**config)
       # Register the /run command that triggers irelease.main
       cli.register_command("/run", irelease.main)
       return cli

The *main* Function
===================

The :func:`main` function serves as the entry point for the CLI executable.  Its implementation is intentionally minimal: it calls :func:`build_cli()` to obtain a fully configured :class:`~cli_builder.GenericCLI` instance and then immediately starts its execution loop with ``.run()``.  This pattern allows users to launch the tool in two convenient ways: by executing ``python clizard_main.py`` directly or through a generated wrapper script that forwards arguments to the underlying Python interpreter.

Because ``main()`` delegates all logic to :func:`build_cli`, any future enhancements—such as additional command registration or configuration tweaks—can be made without touching this function.  This separation of concerns keeps the executable thin and focused solely on orchestration.

Example usage:

.. code-block:: python
   :caption: Running the CLI

   def main():
       cli = build_cli()
       cli.run()

The *get_pypi_credentials* Function
===================================

Retrieving PyPI credentials is a critical step in the release process.  The :func:`get_pypi_credentials` function parses the local ``.pypirc`` configuration file and extracts the username and password for the target PyPI repository.  It accepts an optional ``verbose`` parameter that controls diagnostic output; higher values produce more detailed logs, which can be helpful when troubleshooting authentication failures.

The function returns a tuple ``(username, password)``.  If the credentials are missing or malformed, it returns ``(None, None)`` to signal failure.  This return value is consumed by :func:`irelease.main()` during the upload phase, ensuring that only authenticated requests reach PyPI.

.. list-table:: get_pypi_credentials Parameters
   :widths: 20 10 70
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - verbose
     - int
     - Controls diagnostic output verbosity. Default is ``3``.

Example usage:

.. code-block:: python
   :caption: Parsing PyPI credentials

   def get_pypi_credentials(verbose: int = 3):
       """
       Parse .pypirc and return credentials.
       """
       # Implementation would read the file, parse sections,
       # and extract username/password for the default PyPI index.
       pass

The *make_script* Function
=========================

The :func:`make_script` function simplifies repeated releases by generating a helper shell script named ``release.sh``.  This script invokes Python to run ``irelease.py`` with any supplied arguments, making it trivial to execute the full release workflow from the command line.  In addition to creating the shell wrapper, :func:`make_script` copies the original configuration files into the working directory so that subsequent runs have immediate access to the necessary metadata and authentication details.

.. code-block:: python
   :caption: Generating a release helper script

   def make_script():
       # Create release.sh with shebang and command invocation
       with open("release.sh", "w") as f:
           f.write("#!/usr/bin/env bash\n")
           f.write("python -m irelease \"$@\"\n")
       os.chmod("release.sh", 0o755)

CLI Reference — Interactive Release Tool
========================================

Module Overview & Entry Points
-----------------------------

The CLI wrapper for the Interactive Release Tool is built on top of the *Clizard* framework, which provides a lightweight yet powerful way to expose command‑line interfaces that can be both scripted and interactive.  The module’s primary responsibility is to translate user intent expressed through command‑line arguments into concrete calls to the underlying :mod:`irelease` core logic.  By doing so it abstracts away the intricacies of configuration handling, argument parsing, and execution routing, allowing developers to focus on the release workflow itself.

At its heart are two entry points: :func:`build_cli()` and :func:`main()`.  The former constructs a fully‑featured CLI object that knows how to present help text, validate input types, and merge static defaults with dynamic overrides from ``.clizard`` configuration files.  The latter is the script entry point used by setuptools’ console scripts; it orchestrates argument parsing, restores global state after execution, and delegates to :func:`irelease.main()` with the appropriate parameters.  Together they form a clean separation between interface concerns and business logic.

The design intentionally follows a factory pattern: configuration data is loaded lazily during CLI construction, ensuring that any runtime changes (for example, editing ``.clizard`` mid‑session) are respected without requiring a restart.  This flexibility is critical for interactive use cases where users may tweak parameters on the fly.  Moreover, by keeping :func:`main()` lightweight and side‑effect free—except for temporarily manipulating ``sys.argv``—the module guarantees that repeated invocations in the same process do not interfere with each other.

The module also defines a set of default constants (``_DEFAULT_*``) that act as fallbacks when configuration files are missing or incomplete.  These defaults provide sensible values for common scenarios (e.g., default verbosity level, whether to clean local builds) and allow developers to override them globally without touching the code base.  The interplay between static defaults and dynamic overrides is a key feature that gives users fine‑grained control over release behavior.

.. list-table:: Parameters of ``main()`` and ``build_cli()``
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``username``
     - ``str``
     - Username on GitHub/GitLab.
   * - ``package``
     - ``str``
     - Package name to be released.
   * - ``clean``
     - ``bool (flag)``
     - Remove local builds.
   * - ``install``
     - ``bool (flag)``
     - Install this version locally.
   * - ``twine``
     - ``str``
     - Path to custom twine binary.
   * - ``verbosity``
     - ``int``
     - Verbosity level (0‑5).

.. code-block:: python
   :caption: Using the CLI entry point

   from clizard_main import main

   if __name__ == '__main__':
       main()

CLI Construction — ``build_cli()``
---------------------------------

The :func:`build_cli()` function is responsible for assembling a fully functional command‑line interface that reflects both static metadata and dynamic configuration.  It starts by loading the ``.clizard`` file located in the current working directory; if this file is absent, it falls back to the ``_DEFAULT_SETTINGS`` dictionary defined within the module.  This approach ensures that every CLI instance has a consistent baseline while still allowing per‑project customizations.

Once configuration data is available, :func:`build_cli()` creates an instance of Clizard’s internal CLI class using a factory method.  The factory receives two key pieces of information: argument definitions (including types, default values, and help strings) and the current configuration state.  By merging these sources, the resulting CLI can present accurate defaults to the user and enforce type safety at runtime.  This design also makes it trivial to add new options or change existing ones without touching the core logic; developers simply update the metadata dictionary.

A notable feature of :func:`build_cli()` is its support for two invocation styles: the default argv‑style, where arguments are parsed from ``sys.argv``, and a keyword‑argument style controlled by ``_DEFAULT_CALL_STYLE``.  The latter allows programmatic callers to invoke the CLI directly with named parameters, which is especially useful in testing or when integrating the tool into larger Python applications.  Regardless of the chosen style, :func:`build_cli()` guarantees that all arguments are validated against the same schema, providing a consistent user experience.

.. code-block:: python
   :caption: Constructing and running the CLI

   cli = build_cli()
   cli.run()

Execution Entry Point — ``main()``
---------------------------------

The :func:`main()` function serves as the canonical entry point for the Interactive Release Tool.  It is invoked by setuptools’ console script mechanism, which passes control to this function when a user runs the ``irelease`` command from the shell.  The primary responsibilities of :func:`main()` are threefold: parse arguments, apply defaults, and delegate execution to the core release logic.

Argument parsing is performed using Clizard’s built‑in parser, which automatically generates help text and validates input types based on the metadata defined in :func:`build_cli()`.  After parsing, :func:`main()` examines whether the user requested a direct keyword‑argument invocation.  If so, it bypasses the usual argv manipulation; otherwise, it temporarily replaces ``sys.argv`` with the reconstructed argument list to preserve compatibility with legacy code that expects command‑line input.

Once arguments are ready, :func:`main()` calls :func:`irelease.main()`, passing along all relevant parameters (e.g., username, package name, verbosity).  This delegation keeps the CLI thin and focused on interface concerns while allowing the core logic to remain agnostic of the surrounding infrastructure.

.. code-block:: python
   :caption: Delegating to the release engine

   def main():
       args = parse_cli_arguments()
       irelease.main(**args)

The *make_script* Function (Revisited)
-------------------------------------

Beyond generating a shell wrapper, :func:`make_script` also ensures that any configuration files required by the release process are available in the working directory.  By copying ``.clizard`` and ``.pypirc`` into the same folder as ``release.sh``, subsequent executions can resolve credentials and metadata without additional user intervention.  This design choice reduces friction for repeat releases, especially in automated CI environments where scripts may be invoked from various directories.

.. code-block:: python
   :caption: Full script generation

   def make_script():
       # Create release.sh with shebang and command invocation
       with open("release.sh", "w") as f:
           f.write("#!/usr/bin/env bash\n")
           f.write("python -m irelease \"$@\"\n")
       os.chmod("release.sh", 0o755)

       # Copy configuration files for convenience
       shutil.copy(".clizard", ".")
       shutil.copy(".pypirc", ".")

.. include:: add_bottom.add