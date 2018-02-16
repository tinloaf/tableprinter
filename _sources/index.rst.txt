.. Tableprinter documentation master file, created by
   sphinx-quickstart on Thu Jan 18 14:21:57 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Tableprinter's documentation!
========================================

Tableprinter is a small python module that allows you to print your data in tables, be it as ASCII or Unicode table, HTML table or
LaTeX tabular. It allows for hierarchical columns and rows (see an example TODO of this). To jump right in, you can have
a look at the :ref:`examples <examples>`, or you can read the :ref:`API docs <api>`.

Big Picture
===========

You supply the Tableprinter with your data as a list of dictionaries. Every dictionary becomes one cell of the table.
Together with the list of dictionaries, you provide the constructor with a list of options describing your data.
See the :py:meth:`constructor documentation <tableprinter.Tableprinter.__init__>`. Then, you can call various
`as_<format>` methods, which produce output in the requested format. Each of these methods accepts a list of options
controlling various specifics of the output formatting. See the the :ref:`output format documentation <output_formats>`
for details.

Installing
==========

This should do the trick: ::

   pip install tableprinter


Documentation Contents
======================

.. toctree::
   :maxdepth: 2

   dataformat
   api
   output_formats
   examples

.. _examples:
Examples
========

* :ref:`A Simple Example <example_simple>`
* :ref:`An Example of Hierarchic Data <example_hierarchic>`

.. _resources:
Resources
=========

* `Source code on Github <https://github.com/tinloaf/tableprinter>`_
* `Issue tracker <https://github.com/tinloaf/tableprinter/issues>`_
* `PyPi package <https://pypi.python.org/pypi/tableprinter>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. raw:: html

   <a href="https://github.com/tinloaf/tableprinter"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://camo.githubusercontent.com/365986a132ccd6a44c23a9169022c0b5c890c387/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f7265645f6161303030302e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png"></a>
