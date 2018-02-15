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


```python
print(tp.as_text())
```

    +==+=============+==============+
    |  |      a      |      b       |
    +==+=============+==============+
    |1 |Top Left     |Top Right     |
    |--+-------------+--------------+
    |2 |Bottom Left  |Bottom Right  |
    +==+=============+==============+




```python
HTML(tp.as_html())
```

<table class = "tableprinted">
        <tr> <th class="toplabel" colspan="1"></th><th colspan="1" style="text-align: center; padding: 0px;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">a</div></th><th colspan="1" style="text-align: center; padding: 0px;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">b</div></th></tr>
<tr><th class="leftlabel" rowspan="1" style="">1</td><td class="content" style="">Top Left</td><td class="content" style="">Top Right</td></tr>
<tr><th class="leftlabel" rowspan="1" style="">2</td><td class="content" style="">Bottom Left</td><td class="content" style="">Bottom Right</td></tr>
</table>

*Note*: The produced HTML sets various `class` attributes and can therefore be arbitrarily styled.

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


An example using hierarchical data
-----------------------------------



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
# Generate hierarchic data. x1 and x2 are the two x-coordinates. y1, y2 and y3 are three levels of y-coordinates.
data = [
    {'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, 'y3': y3, 'content': '{}/{}-{}/{}/{}'.format(x1,x2,y1,y2,y3)}
    for x1 in ['a', 'b'] for x2 in [1,2] for y1 in ['x', 'y'] for y2 in ['3', '4'] for y3 in ['i', 'j']
]

# Not all cells have to be present
_ = data.pop(23)
```


```python
tp = Tableprinter(data, x_dimensions=('x1','x2'), y_dimensions=('y1','y2','y3'))
```


```python
print(tp.as_text())
```

    +======+===========+===========+===========+===========+
    |      |           a           |           b           |
    |      |     1     |     2     |     1     |     2     |
    +======+===========+===========+===========+===========+
    |    i |a/1-x/3/i  |a/2-x/3/i  |b/1-x/3/i  |b/2-x/3/i  |
    |  3 --+-----------+-----------+-----------+-----------+
    |    j |a/1-x/3/j  |a/2-x/3/j  |b/1-x/3/j  |b/2-x/3/j  |
    |x ----+-----------+-----------+-----------+-----------+
    |    i |a/1-x/4/i  |a/2-x/4/i  |b/1-x/4/i  |b/2-x/4/i  |
    |  4 --+-----------+-----------+-----------+-----------+
    |    j |a/1-x/4/j  |a/2-x/4/j  |b/1-x/4/j  |b/2-x/4/j  |
    |------+-----------+-----------+-----------+-----------+
    |    i |a/1-y/3/i  |a/2-y/3/i  |b/1-y/3/i  |b/2-y/3/i  |
    |  3 --+-----------+-----------+-----------+-----------+
    |    j |a/1-y/3/j  |a/2-y/3/j  |b/1-y/3/j  |b/2-y/3/j  |
    |y ----+-----------+-----------+-----------+-----------+
    |    i |a/1-y/4/i  |a/2-y/4/i  |b/1-y/4/i  |b/2-y/4/i  |
    |  4 --+-----------+-----------+-----------+-----------+
    |    j |a/1-y/4/j  |a/2-y/4/j  |--         |b/2-y/4/j  |
    +======+===========+===========+===========+===========+




```python
HTML(tp.as_html())
```





<table class = "tableprinted">
        <tr> <th class="toplabel" colspan="3"></th><th colspan="2" style="text-align: center; padding: 0px;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">a</div></th><th colspan="2" style="text-align: center; padding: 0px;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">b</div></th></tr>
<tr> <th class="toplabel" colspan="3"></th><th colspan="1" style="text-align: center; padding: 0px;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">1</div></th><th colspan="1" style="text-align: center; padding: 0px;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">2</div></th><th colspan="1" style="text-align: center; padding: 0px;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">1</div></th><th colspan="1" style="text-align: center; padding: 0px;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">2</div></th></tr>
<tr><th class="leftlabel" rowspan="4" style="">x</td><th class="leftlabel" rowspan="2" style="">3</td><th class="leftlabel" rowspan="1" style="">i</td><td class="content" style="">a/1-x/3/i</td><td class="content" style="">a/2-x/3/i</td><td class="content" style="">b/1-x/3/i</td><td class="content" style="">b/2-x/3/i</td></tr>
<tr><th class="leftlabel" rowspan="1" style="">j</td><td class="content" style="">a/1-x/3/j</td><td class="content" style="">a/2-x/3/j</td><td class="content" style="">b/1-x/3/j</td><td class="content" style="">b/2-x/3/j</td></tr>
<tr><th class="leftlabel" rowspan="2" style="border-top: 1px solid black;">4</td><th class="leftlabel" rowspan="1" style="border-top: 1px solid black;">i</td><td class="content" style="">a/1-x/4/i</td><td class="content" style="">a/2-x/4/i</td><td class="content" style="">b/1-x/4/i</td><td class="content" style="">b/2-x/4/i</td></tr>
<tr><th class="leftlabel" rowspan="1" style="">j</td><td class="content" style="">a/1-x/4/j</td><td class="content" style="">a/2-x/4/j</td><td class="content" style="">b/1-x/4/j</td><td class="content" style="">b/2-x/4/j</td></tr>
<tr><th class="leftlabel" rowspan="4" style="border-top: 1px solid black;">y</td><th class="leftlabel" rowspan="2" style="border-top: 1px solid black;">3</td><th class="leftlabel" rowspan="1" style="border-top: 1px solid black;">i</td><td class="content" style="">a/1-y/3/i</td><td class="content" style="">a/2-y/3/i</td><td class="content" style="">b/1-y/3/i</td><td class="content" style="">b/2-y/3/i</td></tr>
<tr><th class="leftlabel" rowspan="1" style="">j</td><td class="content" style="">a/1-y/3/j</td><td class="content" style="">a/2-y/3/j</td><td class="content" style="">b/1-y/3/j</td><td class="content" style="">b/2-y/3/j</td></tr>
<tr><th class="leftlabel" rowspan="2" style="border-top: 1px solid black;">4</td><th class="leftlabel" rowspan="1" style="border-top: 1px solid black;">i</td><td class="content" style="">a/1-y/4/i</td><td class="content" style="">a/2-y/4/i</td><td class="content" style="">b/1-y/4/i</td><td class="content" style="">b/2-y/4/i</td></tr>
<tr><th class="leftlabel" rowspan="1" style="">j</td><td class="content" style="">a/1-y/4/j</td><td class="content" style="">a/2-y/4/j</td><td class="content empty">--</td><td class="content" style="">b/2-y/4/j</td></tr>
</table>



*Note*: The produced HTML sets various `class` attributes and can therefore be arbitrarily styled.


```python
print(tp.as_latex())
```


    \begin{tabular}{ rrrcccc }
    \toprule
    \multicolumn{ 3 }{c}{  } & \multicolumn{ 2 }{c}{ a } & \multicolumn{ 2 }{c}{ b } \\
    \cmidrule(lr){ 4 - 5 } \cmidrule(lr){ 6 - 7 }
    \multicolumn{ 3 }{c}{  } & 1& 2& 1& 2\\

    \midrule
    \multirow{ 4 }{*}{x} & \multirow{ 2 }{*}{3} & \multirow{ 1 }{*}{i} & a/1-x/3/i & a/2-x/3/i & b/1-x/3/i & b/2-x/3/i\\
     &  & \multirow{ 1 }{*}{j} & a/1-x/3/j & a/2-x/3/j & b/1-x/3/j & b/2-x/3/j\\
    \cmidrule(lr){ 2 - 3 } \\
     & \multirow{ 2 }{*}{4} & \multirow{ 1 }{*}{i} & a/1-x/4/i & a/2-x/4/i & b/1-x/4/i & b/2-x/4/i\\
     &  & \multirow{ 1 }{*}{j} & a/1-x/4/j & a/2-x/4/j & b/1-x/4/j & b/2-x/4/j\\
    \cmidrule(lr){ 1 - 3 } \\
    \multirow{ 4 }{*}{y} & \multirow{ 2 }{*}{3} & \multirow{ 1 }{*}{i} & a/1-y/3/i & a/2-y/3/i & b/1-y/3/i & b/2-y/3/i\\
     &  & \multirow{ 1 }{*}{j} & a/1-y/3/j & a/2-y/3/j & b/1-y/3/j & b/2-y/3/j\\
    \cmidrule(lr){ 2 - 3 } \\
     & \multirow{ 2 }{*}{4} & \multirow{ 1 }{*}{i} & a/1-y/4/i & a/2-y/4/i & b/1-y/4/i & b/2-y/4/i\\
     &  & \multirow{ 1 }{*}{j} & a/1-y/4/j & a/2-y/4/j & -- & b/2-y/4/j\\

    \bottomrule
    \end{tabular}
