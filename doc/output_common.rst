.. _output_common:

Common Output Formatting Options
================================

All `as_<format>` methods accept an `options` dictionary containing options that control the output formatting. Many
of these options are the same across all available formats. All options (and in fact the `options` parameter) are
optional.

.. option:: float_places (int)

    If a float is printed to a table cell (and no `float_format` option is set), it is rounded to this number of decimal
    places. *Default*: 2

.. option:: float_format (function float -> str)

    If this is set to a function that accepts a float and returns a string, this is being used to format all floats which
    are output into table cells.

.. option:: cell-align-horizontal (any of 'c', 'r' or 'l')

    Controls whether the cell contents are centered, right-aligned or left-aligned. *Default*: 'c'