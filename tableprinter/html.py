from .tabulator import Tabulator

class HTMLPrinter(Tabulator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    HTML_DEFAULT_OPTIONS = {
        'table_class': 'tableprinted',
        'float_places': 2
    }

    def _html_format_cell(self, contents, options):
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

        style = ""

        if 'color' in contents:
            rgb_scaled = (int(255 * x) for x in contents['color'])
            color_str = "".join(map(lambda x : hex(x)[2:], rgb_scaled))
            style += "background-color: #{}".format(color_str)

        cell_str = "<td class=\"content\" style=\"{}\">".format(style)
        cell_str += format_val(contents[self._value_dimension])
        cell_str += "</td>"

        cell_str = cell_str.replace("\n", "<br />")

        return cell_str

    def as_html(self, options=HTML_DEFAULT_OPTIONS):
        sorted_rows, left_labels = self._make_rows()
        sorted_cols, top_labels = self._make_cols()

        html_str = """
<table class = "{}">
        """.format(options.get('table_class', ''))

        left_label_count = len(left_labels)

        #
        # Output table header
        #
        for i in range(0, len(self._x)):
            label = self._x_labels[i].get('dimension', "")

            # Label
            html_str += "<tr> <th class=\"toplabel\" colspan=\"{}\">{}</th>".format(left_label_count, label)

            column = left_label_count + 1
            for (key, colspan) in top_labels[i]:
                col_label = self._x_labels[i].get('values', {}).get(key, key)

                cell_style_str = "text-align: center; padding: 0px;"

                div_style_str = "border-bottom: 1px solid black;"
                div_style_str += "margin-left: 3px; margin-right: 7px;"

                html_str += "<th colspan=\"{}\" style=\"{}\">"\
                            .format(colspan, cell_style_str)
                html_str += "<div style=\"{}\">".format(div_style_str)

                html_str += "{}".format(col_label)

                html_str += "</div></th>"

                column += colspan

            html_str += "</tr>\n"


        #
        # Table Content
        #
        row_no = 1
        current_left_label_index = [-1] * len(left_labels)
        left_labels_rows_remaining = [0] * len(left_labels)
        for row in sorted_rows:
            html_str += "<tr>"
            #
            # Output left labels
            #
            # Output one cell per left label dimension. If this is the first cell for the label,
            # output a multirow. Else, output an empty cell
            top_bordered = False
            for d in range(0, len(left_labels)):

                if left_labels_rows_remaining[d] == 0:
                    current_left_label_index[d] += 1
                    label, rowspan = left_labels[d][current_left_label_index[d]]

                    row_label = self._y_labels[d].get('values', {}).get(label, label)

                    cell_style = ""
                    if (d < len(left_labels) - 1 or top_bordered) and (row_no > 1):
                        cell_style += "border-top: 1px solid black;"
                        top_bordered = True

                    html_str += "<th class=\"leftlabel\" rowspan=\"{}\" style=\"{}\">".format(rowspan, cell_style)

                    html_str += "{}</td>".format(row_label)
                    left_labels_rows_remaining[d] = rowspan - 1

                else:
                    #empty cell
                    left_labels_rows_remaining[d] -= 1

            #
            # Output Data
            #
            for col in sorted_cols:
                if (row,col) not in self._cells:
                    html_str += "<td class=\"content empty\">" + self._empty_symbol + "</td>"
                else:
                    d = self._cells[(row,col)]
                    html_str += self._html_format_cell(d, options)

            html_str += "</tr>\n"
            row_no += 1

        html_str += "</table>"


        return html_str
