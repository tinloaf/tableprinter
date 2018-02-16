.. _output_html:

HTML Output
===========

Formatting Options
------------------

Additionally to the :ref:`common formatting options <output_common>`, the `as_html` method accepts these keywords in
its `options` parameter:

.. option:: table_class

    Specifies a CSS class to tag the resulting table with. Note that some cells, rows etc. are also tagged with
    specific classes. Refer to TODO for an overview.

Limitations
-----------

Please note that the content field of the dictionaries is written to the table cells more or less verbatim. That means
that on the one hand you can use HTML in your cell contents. On the other hand, you need to quote HTML special characters.