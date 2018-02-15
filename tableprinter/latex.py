from .tabulator import Tabulator

class LatexPrinter(Tabulator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _latex_format_cell(self, contents, options):
        if not options.get('float_format'):
            float_fmt = lambda f : ("{{:.{}}}".format(options['float_places'])).format(f)
        else:
            float_fmt = options['float_format']

        def format_val(val):
            if isinstance(val, float):
                return float_fmt(val)
            else:
                return str(val)

        if not isinstance(contents, dict):
            contents = {self._value_dimension: contents}

        cell_str = ""

        if 'color' in contents:
            cell_str += "\\cellcolor[rgb]{{{},{},{}}}".format(*contents['color'])


        cell_str += format_val(contents[self._value_dimension])

        if cell_str.find("\n") > -1:
            cell_str = "\\makecell{" + cell_str + "}"
            cell_str = cell_str.replace("\n", "\\\\")

        return cell_str

    LATEX_DEFAULT_FORMAT = {
        'float_format': None,
        'float_places': 2
    }

    def as_latex(self, options = LATEX_DEFAULT_FORMAT):
        sorted_rows, left_labels = self._make_rows()
        sorted_cols, top_labels = self._make_cols()

        left_label_count = len(left_labels)

        column_str = "r" * left_label_count + "c" * len(sorted_cols)

        latex_str = ""

        #
        # Output table header
        #
        latex_str += """
\\begin{{tabular}}{{ {} }}
\\toprule
""".format(column_str)

        for i in range(0, len(self._x)):
            label = self._x_labels[i].get('dimension', "")

            # Label
            latex_str += "\\multicolumn{{ {} }}{{c}}{{ {} }} ".format(left_label_count, label)

            column = left_label_count + 1
            midrules = []
            for (key, colspan) in top_labels[i]:
                col_label = self._x_labels[i].get('values', {}).get(key, key)
                if colspan > 1:
                    latex_str += "& \\multicolumn{{ {} }}{{c}}{{ {} }} ".format(colspan, col_label)
                    midrules += [(column, colspan)]
                    column += colspan
                else:
                    latex_str += "& {}".format(col_label)
                    column += 1

            latex_str += "\\\\ \n"

            for (col, span) in midrules:
                latex_str += "\\cmidrule(lr){{ {} - {} }} ".format(col, (col + (span - 1)))
            latex_str += "\n"

        latex_str += "\\midrule \n"

        #
        # Table Content
        #
        row_no = 1
        current_left_label_index = [-1] * len(left_labels)
        left_labels_rows_remaining = [0] * len(left_labels)
        for row in sorted_rows:
            #
            # Output left labels
            #
            # Output one cell per left label dimension. If this is the first cell for the label,
            # output a multirow. Else, output an empty cell
            left_label_midrule_start = None
            for d in range(0, len(left_labels)):
                if d > 0:
                    latex_str += " & "

                if left_labels_rows_remaining[d] == 0:
                    #print("======= Switching in dimension " + str(d))
                    #print("Old Index is:" + str(current_left_label_index[d]))
                    current_left_label_index[d] += 1
                    label, rowspan = left_labels[d][current_left_label_index[d]]

                    row_label = self._y_labels[d].get('values', {}).get(label, label)

                    #print("Printing label: " + str(row_label))
                    latex_str += "\\multirow{{ {} }}{{*}}{{{}}}".format(rowspan, row_label)
                    left_labels_rows_remaining[d] = rowspan - 1
                else:
                    #empty cell
                    left_labels_rows_remaining[d] -= 1
                    if (left_labels_rows_remaining[d] == 0) and (d < len(left_labels) - 1) and \
                            (row_no < len(sorted_rows)) and (not left_label_midrule_start):
                        left_label_midrule_start = d + 1
            #
            # Output Data
            #
            for col in sorted_cols:
                latex_str += " & "

                if (row,col) not in self._cells:
                    latex_str += self._empty_symbol
                else:
                    d = self._cells[(row,col)]
                    latex_str += self._latex_format_cell(d, options)

            latex_str += "\\\\ \n"

            if left_label_midrule_start:
                latex_str += "\\cmidrule(lr){{ {} - {} }} \\\\ \n".format(left_label_midrule_start, left_label_count)

            row_no += 1

        #
        # Bottom
        #
        latex_str += """
\\bottomrule
\\end{tabular}
"""

        return latex_str
