Summary
========

Background
----------

The *clizard* library is conceived as a bridge between the intricate logic of Python release workflows and the simplicity expected from modern command‑line tools. By introspecting a project's `irelease.py` module, it automatically generates an executable entry point (`clizard_main.py`) that mirrors the developer’s workflow while still permitting interactive overrides. This design eliminates repetitive boilerplate code, reduces human error during packaging, and guarantees that every release follows a consistent set of steps.

Central to *clizard* is its treatment of configuration files—such as `.clizard` for command metadata and `.pypirc` for authentication—as first‑class citizens in the build process. When a user invokes the generated CLI, the framework loads these files, applies any user overrides, and then executes the release logic defined in `irelease.py`. The result is a single command that can be called from scripts, CI pipelines, or directly by developers, providing a unified experience across all environments.

Another driving motivation for *clizard* lies in its lightweight dependency footprint. Unlike full‑blown frameworks such as Click or Typer, it relies on minimal standard library modules while still offering interactive prompts and argument parsing. This makes it an attractive choice for projects that need a quick, maintainable release tool without the overhead of additional packages.

Output
-------

Running the *clizard* command-line interface produces a fully prepared distribution ready for upload to PyPI or any other package index. The output includes a built wheel, source tarball, and optionally a signed artifact if GPG keys are configured. Additionally, the CLI can generate changelogs, update version numbers in source files, and commit these changes back to the repository automatically.

The library’s design ensures that every step of the build process is transparent: from dependency resolution to packaging, each action emits concise log messages. Users can capture this output for audit purposes or integrate it into continuous‑integration pipelines where visibility into the release lifecycle is critical.

A typical invocation might look like:

.. code-block:: console

   $ pyrelease-cli run --dry-run
   INFO: Loading configuration from .clizard
   INFO: Resolving dependencies...
   INFO: Building wheel for myproject==1.2.3
   INFO: Uploading to PyPI...

If the `--dry-run` flag is omitted, the command will push the artifacts to the configured index and commit the updated version tags.

Schematic Overview
------------------

The following ASCII diagram illustrates the high‑level workflow that *clizard* orchestrates when a user executes the generated CLI. Each block represents a distinct phase in the release pipeline, and arrows indicate data flow between them.

.. code-block:: text

   +-------------------+      +--------------------+
   |  User Input (CLI) | ---> |  Parse & Validate  |
   +-------------------+      +--------------------+
             |                           |
             v                           v
   +-------------------+      +--------------------+
   | Load Config Files | ---> | Resolve Dependencies|
   +-------------------+      +--------------------+
             |                           |
             v                           v
   +-------------------+      +--------------------+
   | Build Artifacts    | ---> | Sign & Upload     |
   +-------------------+      +--------------------+
             |                           |
             v                           v
   +-------------------+      +--------------------+
   | Commit Changes     | <--- | Post‑Release Hooks|
   +-------------------+      +--------------------+

The diagram emphasizes that *clizard* treats the release process as a series of composable, deterministic steps. Each step can be overridden or extended via hooks defined in `irelease.py`, allowing developers to inject custom logic without modifying the core CLI generator.

.. include:: add_bottom.add