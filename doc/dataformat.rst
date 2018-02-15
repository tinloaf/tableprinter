Data Format
===========

You supply data to Tableprinter as a list of dictionaries. Each dictionary
corresponds to one table cell. Options in Tableprinter's constructor(TODO LINK)
control which field in the dictionaries determines the row, column, content,
color etc. of the table cell. Therefore, you should really read the documentation
on Tableprinter's constructor(TODO LINK).

Here's a quick overview over what can be specified for each cell:

Cell Data
---------
In the following, `d` always stands for the dictionary of the cell we are
interested about. Please also note that the field names below are just default
values which can be overriden via the options in Tableprinter's constructor(TODO LINK).
Where we specify <fields> as field names, no defaults exist and the name(s)
of these field(s) *must* be specified in the constructor.

.. option:: content

  Specifies the content of the cell. If you don't specify a formatter(TODO LINK)
  or an aggregator(TODO LINK), `str(d['content'])` will become the content
  of the cell. A special formatting rule applies to floats.(TODO LINK)

.. option:: <column-fields>

  For every field in your column option(TODO LINK), the value determines in which
  column the cell will be placed. See TODO LINK for details. Note that this is
  usually exactly one field, unless you have hierarchic columns(TODO LINK).

.. option:: <row-fields>

  For every field in your row option(TODO LINK), the value determines in which
  row the cell will be placed. See TODO LINK for details. Note that this is
  usually exactly one field, unless you have hierarchic rows(TODO LINK).

.. option:: color

  If `d['color']` is present, we expect it to contain a hexadecimal RGB value
  (like `#012345`). This RGB value will be used as background color for the
  cell
