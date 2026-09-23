Installation
=============


.. note::

   Latest release: ``v0.1.1``

.. note::

   Source code: `irelease on GitHub <https://github.com/erdogant/irelease.git>`_

.. tip::

   Documentation: `https://erdogant.github.io/irelease/ <https://erdogant.github.io/irelease/>`_


Create environment
******************

.. code-block:: console

   conda create -n env_irelease python=3.12
   conda activate env_irelease


Install from PyPI
*****************

.. code-block:: console

   pip install irelease

   # Force update to the latest version
   pip install -U irelease


Install from GitHub
*******************

.. code-block:: console

   pip install git+https://github.com/erdogant/irelease.git

   # Install a specific branch
   pip install git+https://github.com/erdogant/irelease.git@main




Uninstall
================

Remove environment
******************

.. code-block:: console

   conda env list
   conda env remove --name env_irelease
   conda env list


Remove package
**************

.. code-block:: console

   pip uninstall irelease



.. include:: add_bottom.add