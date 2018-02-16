.. _output_latex:

LaTeX Output
============

Formatting Options
------------------

Only the :ref:`common formatting options <output_common>` are accepted.

Required Packages
-----------------

To include the generated LaTeX code in your document, you need to have a couple of packages included:
* booktabs
* multirow
* makecell (if you use line breaks within cell contents)
* xcolor with the "table" option (if you use cell background colors)

Limitations
-----------

Please note that the content field of the dictionaries is written to the table cells more or less verbatim. The only thing
that happens is that newlines are replaced by "\\". That means on the one hand that you can include LaTeX in your
cell contents (e.g., math mode). On the other hand you need to quote LaTeX special characters.