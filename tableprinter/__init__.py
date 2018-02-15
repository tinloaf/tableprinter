from .latex import LatexPrinter
from .html import HTMLPrinter
from .ascii import ASCIIPrinter

class Tableprinter(LatexPrinter, HTMLPrinter, ASCIIPrinter):
    """The Table Printer.

    This is the main table printer class. It takes your data and configuration via its constructor and
    provides various methods to format the data to HTML / LaTeX / ASCII.
    """
    def __init__(self, data, x_dimensions, y_dimensions, **kwargs):
        """Create and configure a new Tableprinter instance.

        This is the most important method. You supply it with your data and config options specifying how your
        data looks like. Your data has to be a list of dictionaries. Every dictionary in this list corresponds
        to one cell in your table (unless you use aggregation, see TODO). The various kwargs of this constructor
        are used to specify which field of the dictionaries has what meaning.

        :param data: The list of dictionaries that makes up your table's data.
        :param x_dimensions: An iterable that specifies which field(s) of your dictionaries corresponds to the title of the column that the cell should be in. All the dictionaries in `data` must have this field, and all those fields must be iterables of the same length as `x_dimensions`. If your `x_dimensions` has more than one entry, your table's columns will be hierarchic. See TODO.
        :param x_sorter: *(optional)* A function that must take a tuple of `x` values of a cell (i.e., whatever the `x_dimensions` field(s) of the cell contain) and return a key. This key will be used to sort the columns of your table. Note that the function as *always* passed a tuple, even if your `x_dimensions` only contain one entry.
        :param y_dimensions: An iterable that specifies which field(s) of your dictionaries corresponds to the title of the row that the cell should be in. All the dictionaries in `data` must have this field, and all those fields must be iterables of the same length as `y_dimensions`. If your `y_dimensions` has more than one entry, your table's rows will be hierarchic. See TODO.
        :param y_sorter: *(optional)* A function that must take a tuple of `y` values of a cell (i.e., whatever the `y_dimensions` field(s) of the cell contain) and return a key. This key will be used to sort the rows of your table. Note that the function as *always* passed a tuple, even if your `y_dimensions` only contain one entry.
        :param color: *(optional)* Specifies which field of your data to use for the background color of the respective cell. If this is given, the respective field in your dictionaries can contain an RGB value like `#012345` which will be used as background color for the respective cell.
        """
        super(Tableprinter, self).__init__(data, x_dimensions, y_dimensions, **kwargs)