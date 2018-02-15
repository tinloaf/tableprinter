import itertools

class Tabulator(object):
    def __init__(self, data, x_dimensions, y_dimensions, value_dimension='content',
                 aggregator=None,
                 x_sorter=lambda x : x,
                 y_sorter=lambda x : x,
                 x_labels = None,
                 y_labels = None,
                 empty_symbol = "--"):
        self._data = data

        self._aggregator = aggregator
        self._x_sorter = x_sorter
        self._y_sorter = y_sorter
        self._empty_symbol = empty_symbol

        self._value_dimension = value_dimension

        if not (isinstance(x_dimensions, list) or isinstance(x_dimensions, tuple)):
            self._x = (x_dimensions,)
        else:
            self._x = x_dimensions

        if not (isinstance(y_dimensions, list) or isinstance(y_dimensions, tuple)):
            self._y = (y_dimensions,)
        else:
            self._y = y_dimensions

        if not x_labels:
            self._x_labels = [
                {} for x in self._x
            ]
        else:
            self._x_labels = x_labels

        if not y_labels:
            self._y_labels = [
                {} for y in self._y
            ]
        else:
            self._y_labels = y_labels

        self._cells = {}

        self._cols = set()
        self._rows = set()

        self._make_cells()

    def _get_coordinate(self, d):
        row = tuple((d[index] for index in self._y))
        col = tuple((d[index] for index in self._x))

        self._rows.add(row)
        self._cols.add(col)

        return (row, col)

    def _make_cells(self):
        # TODO cache
        for d in self._data:
            coordinate = self._get_coordinate(d)
            if self._aggregator is None:
                if coordinate in self._cells:
                    raise "Duplicate value for cell " + str(coordinate)
                self._cells[coordinate] = d
            else:
                if coordinate not in self._cells:
                    self._cells[coordinate] = [d]
                else:
                    self._cells[coordinate].append(d)

        if self._aggregator:
            for key, values in self._cells:
                self._cells[key] = self._aggregator(values)

    def _make_cols(self):
        # TODO cache
        sorted_cols = sorted(self._cols, key=self._x_sorter)
        dimensions = []

        for d in range(0, len(sorted_cols[0])):
            dimension_header = tuple((k, len(tuple(g))) for k, g in itertools.groupby((col[d] for col in sorted_cols)))
            dimensions.append(dimension_header)

        return (sorted_cols, dimensions)

    def _make_rows(self):
        # TODO cache
        sorted_rows = sorted(self._rows, key=self._y_sorter)
        dimensions = []

        for d in range(0, len(sorted_rows[0])):
            dimension_header = tuple((k, len(tuple(g))) for k, g in itertools.groupby((col[d] for col in sorted_rows)))
            dimensions.append(dimension_header)

        return (sorted_rows, dimensions)

