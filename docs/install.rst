.. currentmodule:: package

Install
=======

Create a ``conda`` environment:

.. code-block:: bash
   :substitutions:

   conda create -n package python=|min_python_version|

.. note::
   ``package`` requires Python |min_python_version| or higher.

Install ``package`` using ``pip`` from wheel file:

.. code-block:: bash
   :substitutions:

   conda activate package
   pip install path/to/package-|release|-py3-none-any.whl
