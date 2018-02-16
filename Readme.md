Tableprinter
============

Tableprinter is a small python module that allows you to print your data in tables, be it as ASCII table, HTML table or
LaTeX tabular. It allows for hierarchical columns and rows (see the hierarchical example below). To jump right in, you can have
a look at the examples below, or you can read the [documentation](https://tinloaf.github.io/tableprinter/).

Examples
========

Data is passed to tableprinter as a list of dictionaries. Each dictionary represents one cell of your table, and must
contain fields that specify the content of the table, as well as which row and column the cell should be in. More
options can be specified for each cell, which you can find in the [documentation](https://tinloaf.github.io/tableprinter/).

A simple first example
----------------------
*Note*: this is a (somewhat ugly) export of a notebook that can be found in the
examples folder.


```python
# This is only necessary to execute this notebook from the examples folder.
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from tableprinter import Tableprinter

# For displaying the HTML output directly in the notebook
from IPython.display import HTML
```


```python
data = [
    {'x': 'a', 'y': 1, 'content': 'Top Left'},
    {'x': 'b', 'y': 1, 'content': 'Top Right'},
    {'x': 'a', 'y': 2, 'content': 'Bottom Left'},
    {'x': 'b', 'y': 2, 'content': 'Bottom Right'}
]
```


```python
tp = Tableprinter(data, x_dimensions=('x',), y_dimensions=('y',))
```

Text Output
===========


```python
print(tp.as_ascii())
```

    #==#=============#==============#
    |  |      a      |      b       |
    #==#=============#==============#
    |1 |  Top Left   |  Top Right   |
    |--+-------------+--------------+
    |2 | Bottom Left | Bottom Right |
    +--+-------------+--------------+




```python
print(tp.as_unicode())
```

    ┏━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
    ┃  ┃      a      ┃      b       ┃
    ┣━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━━┫
    │1 │  Top Left   │  Top Right   │
    │──├─────────────┼──────────────┤
    │2 │ Bottom Left │ Bottom Right │
    └──┴─────────────┴──────────────┘



HTML Output
===========


```python
HTML(tp.as_html())
```





<table class = "tableprinted">
        <tr> <th class="toplabel" colspan="1"></th><th colspan="1" style="padding: 0px; text-align: center;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">a</div></th><th colspan="1" style="padding: 0px; text-align: center;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">b</div></th></tr>
<tr><th class="leftlabel" rowspan="1" style="">1</td><td class="content" style="text-align: center;">Top Left</td><td class="content" style="text-align: center;">Top Right</td></tr>
<tr><th class="leftlabel" rowspan="1" style="">2</td><td class="content" style="text-align: center;">Bottom Left</td><td class="content" style="text-align: center;">Bottom Right</td></tr>
</table>



*Note*: The produced HTML sets various `class` attributes and can therefore be arbitrarily styled.

LaTeX Output
============
*Note*: LaTeX output only produces the tabular environment. You probably want to wrap it into a table environment.


```python
print(tp.as_latex())
```


    \begin{tabular}{ rcc }
    \toprule
    \multicolumn{ 1 }{c}{  } & a& b\\

    \midrule
    \multirow{ 1 }{*}{1} & Top Left & Top Right\\
    \multirow{ 1 }{*}{2} & Bottom Left & Bottom Right\\

    \bottomrule
    \end{tabular}
