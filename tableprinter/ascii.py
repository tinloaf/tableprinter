from .tabulator import Tabulator

class ASCIIPrinter(Tabulator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._ascii_matrix = ""
        self._ascii_rowheights = None
        self._ascii_colwidths = None

    ASCII_DEFAULT_OPTIONS = {
        'float_places': 2
    }

    def _ascii_format_cell(self, contents, options):
        if not options.get('float_format'):
            float_fmt = lambda f : ("{{:.{}}}".format(options.get('float_places', 2))).format(f)
        else:
            float_fmt = options['float_format']

        def format_val(val):
            if isinstance(val, float):
                return float_fmt(val)
            else:
                return str(val)

        if not isinstance(contents, dict):
            contents = {self._value_dimension: contents}

        return format_val(contents[self._value_dimension])

    def _ascii_compute_column_widths(self, options):
        # TODO make a list
        self._ascii_colwidths = {
            0: 2
        }

        sorted_rows, left_labels = self._make_rows()
        sorted_cols, top_labels = self._make_cols()

        # Content

        col_no = 1
        for col in sorted_cols:
            colwidth = 2
            for row in sorted_rows:
                if (row, col) in self._cells:
                    d = self._cells[(row,col)]
                    cell_str = self._ascii_format_cell(d, options)
                    max_substr = max(len(substr) for substr in cell_str.split("\n"))
                    colwidth = max(colwidth, max_substr + 2)
            self._ascii_colwidths[col_no] = colwidth
            col_no += 1


        # Header
        for d in range(0, len(self._x)):
            label = self._x_labels[d].get('dimension', "") # TODO actually print the dimension label?

            # First column, for labels
            self._ascii_colwidths[0] = max(self._ascii_colwidths[0], len(label) + 2)

            col_no = 1
            for (key, colspan) in top_labels[d]:
                participating_cols = list(range(col_no, col_no + colspan))
                col_label = self._x_labels[d].get('values', {}).get(key, key)

                needed_size = len(str(col_label)) + 2
                increment_index = 0
                while sum((self._ascii_colwidths[col] for col in participating_cols)) < needed_size:
                    self._ascii_colwidths[participating_cols[increment_index % colspan]] += 1
                    increment_index += 1

                col_no += colspan

        # First column, y-labels
        first_col_width = 0
        for d in range(0, len(self._y)):
            dimension_width = 2
            for (key, rowspan) in left_labels[d]:
                row_label = self._y_labels[d].get('values', {}).get(key, key)
                dimension_width = max(dimension_width, len(str(row_label)) + 1) # TODO line breaks?
            first_col_width += dimension_width
        self._ascii_colwidths[0] = max(self._ascii_colwidths[0], first_col_width)


    def _ascii_compute_row_heights(self, options):
        # TODO make a list
        self._ascii_rowheights = {
            0: 1
        }

        sorted_rows, left_labels = self._make_rows()
        sorted_cols, top_labels = self._make_cols()

        # Content
        row_no = 1
        for row in sorted_rows:
            rowheight = 1
            for col in sorted_cols:
                if (row,col) in self._cells:
                    d = self._cells[(row,col)]
                    cell_str = self._ascii_format_cell(d, options)
                    lines = len(cell_str.split("\n"))
                    rowheight = max(rowheight, lines)

            self._ascii_rowheights[row_no] = rowheight
            row_no += 1


        # First row, x-labels
        first_row_height = 0
        for d in range(0, len(self._x)):
            dimension_height = 1
            for (key, colspan) in top_labels[d]:
                col_label = self._x_labels[d].get('values', {}).get(key, key)
                height = len(str(col_label).split("\n"))
                dimension_height = max(dimension_height, height)
            first_row_height += dimension_height
        self._ascii_rowheights[0] = max(self._ascii_rowheights[0], first_row_height)



    def _ascii_print_to_matrix(self, x, y, s):
        base_pos = y * self._ascii_total_width + x

        for c in s:
            self._ascii_matrix[base_pos] = c
            base_pos += 1

    def _ascii_col_position(self, col):
        return sum(self._ascii_colwidths[c] for c in range(0,col)) + col + 1

    def _ascii_row_position(self, row):
        return sum(self._ascii_rowheights[r] for r in range(0,row)) + row + 1

    def _ascii_draw_borders(self):
        sorted_rows, left_labels = self._make_rows()
        sorted_cols, top_labels = self._make_cols()

        self._ascii_print_to_matrix(0, 0, "=" * self._ascii_total_width)
        self._ascii_print_to_matrix(0, self._ascii_total_height - 1, "=" * self._ascii_total_width)

        x = 0
        for i in range(0, len(sorted_cols) + 1):
            for y in range(0, self._ascii_total_height):
                if y == 0 or y == self._ascii_total_height - 1:
                    self._ascii_print_to_matrix(x, y, "+")
                else:
                    self._ascii_print_to_matrix(x, y, "|")
            x += self._ascii_colwidths[i] + 1

        for y in range(0, self._ascii_total_height):
            if y == 0 or y == self._ascii_total_height - 1:
                self._ascii_print_to_matrix(x, y, "+")
            else:
                self._ascii_print_to_matrix(x, y, "|")

        self._ascii_matrix[0] = '+'
        self._ascii_matrix[self._ascii_total_width - 1] = '+'
        self._ascii_matrix[-1] = '+'
        self._ascii_matrix[-1 * (self._ascii_total_width )] = '+'

    def _ascii_draw_row(self, row_no, sorted_rows, sorted_cols, options):
        row = sorted_rows[row_no - 1]
        coord_y = self._ascii_row_position(row_no)

        # TODO don't generate this for every row…
        border = "|" + " " * (self._ascii_colwidths[0]) + "+"

        for col_no, col in enumerate(sorted_cols, start=1):
            border += "-" * (self._ascii_colwidths[col_no]) + "+"

            if (row,col) not in self._cells:
                # TODO print empty symbol?
                cell_str = self._empty_symbol
            else:
                d = self._cells[(row, col)]
                cell_str = self._ascii_format_cell(d, options)

            coord_x = self._ascii_col_position(col_no)
            for (line_offset, line) in enumerate(cell_str.split("\n")):
                self._ascii_print_to_matrix(coord_x, coord_y + line_offset, line)


        if row_no < len(sorted_rows):
            self._ascii_print_to_matrix(0, coord_y + self._ascii_rowheights[row_no], border)

    def _ascii_draw_top_labels(self, top_labels):
        border = "+"
        for colwidth in self._ascii_colwidths.values():
            border += "=" * colwidth
            border += "+"
        border_y_coord = self._ascii_row_position(0) + self._ascii_rowheights[0]
        self._ascii_print_to_matrix(0, border_y_coord, border)

        for d in range(0, len(self._x)):
            col_no = 1
            for (key, colspan) in top_labels[d]:
                participating_cols = list(range(col_no, col_no + colspan))
                available_width = sum(self._ascii_colwidths[cn] for cn in participating_cols) + colspan - 1

                col_label = str(self._x_labels[d].get('values', {}).get(key, key))
                padding_left = int((available_width - len(col_label)) / 2)
                padding_right = available_width - len(col_label) - padding_left
                coord_x = self._ascii_col_position(col_no)
                coord_y = 1 + d
                self._ascii_print_to_matrix(coord_x, coord_y, " " * padding_left + col_label + " " * padding_right)

                col_no += colspan

    def _ascii_draw_left_labels(self, left_labels):
        # First: Compute the width of the individual dimensions
        dimension_widths = []
        for d in range(0, len(self._y)):
            dimension_width = 2
            for (key, rowspan) in left_labels[d]:
                row_label = self._y_labels[d].get('values', {}).get(key, key)
                dimension_width = max(dimension_width, len(str(row_label)) + 1) # TODO line breaks?
            dimension_widths.append(dimension_width)

        for d in range(0, len(self._y)):
            row_no = 1
            x_coord = 1 + sum(dimension_widths[subdim] for subdim in range(0, d))

            for (label_no, (key, rowspan)) in enumerate(left_labels[d]):
                row_label = str(self._y_labels[d].get('values', {}).get(key, key))
                participating_rows = list(range(row_no, row_no + rowspan))
                available_height = sum(self._ascii_rowheights[rn] for rn in participating_rows) + rowspan - 1
                padding_top = int((available_height - 1) / 2) # TODO multirow?
                y_coord = self._ascii_row_position(row_no) + padding_top
                border_y_coord = self._ascii_row_position(row_no) + available_height
                self._ascii_print_to_matrix(x_coord, y_coord, row_label)
                row_no += rowspan
                if label_no < len(left_labels[d]) - 1:
                    self._ascii_print_to_matrix(x_coord, border_y_coord, "-" * dimension_widths[d])



    def as_text(self, options=ASCII_DEFAULT_OPTIONS):
        sorted_rows, left_labels = self._make_rows()
        sorted_cols, top_labels = self._make_cols()

        self._ascii_compute_column_widths(options)
        self._ascii_compute_row_heights(options)

        self._ascii_total_height = sum(h for h in self._ascii_rowheights.values()) + len(sorted_rows) + 2
        self._ascii_total_width = sum(w for w in self._ascii_colwidths.values()) + len(sorted_cols) + 2

        self._ascii_matrix = [ " " for i in range(0, self._ascii_total_height * self._ascii_total_width)]

        self._ascii_draw_borders()

        for (row_no, row) in enumerate(sorted_rows, start=1):
            self._ascii_draw_row(row_no, sorted_rows, sorted_cols, options)

        self._ascii_draw_top_labels(top_labels)
        self._ascii_draw_left_labels(left_labels)

        with_breaks = [x for y in (self._ascii_matrix[i:i+self._ascii_total_width] + ['\n'] for
                        i in range(0, len(self._ascii_matrix), self._ascii_total_width)) for x in y]

        ascii_str = "".join(with_breaks)

        return ascii_str
