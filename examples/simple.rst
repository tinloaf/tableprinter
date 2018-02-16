
.. code:: ipython3

    # This is only necessary to execute this notebook from the examples folder.
    import sys
    import os
    sys.path.insert(0, os.path.abspath('..'))
    
    from tableprinter import Tableprinter
    
    # For displaying the HTML output directly in the notebook
    from IPython.display import HTML

.. code:: ipython3

    data = [
        {'x': 'a', 'y': 1, 'content': 'Top Left'},
        {'x': 'b', 'y': 1, 'content': 'Top Right'},
        {'x': 'a', 'y': 2, 'content': 'Bottom Left'},
        {'x': 'b', 'y': 2, 'content': 'Bottom Right'}
    ]

.. code:: ipython3

    tp = Tableprinter(data, x_dimensions=('x',), y_dimensions=('y',))

Text Output
===========

print(tp.as\_ascii())

.. code:: ipython3

    print(tp.as_unicode())


.. parsed-literal::

    ┏━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
    ┃  ┃      a      ┃      b       ┃
    ┣━━╋━━━━━━━━━━━━━╋━━━━━━━━━━━━━━┫
    │1 │  Top Left   │  Top Right   │
    │──├─────────────┼──────────────┤
    │2 │ Bottom Left │ Bottom Right │
    └──┴─────────────┴──────────────┘
    


HTML Output
===========

.. code:: ipython3

    HTML(tp.as_html())




.. raw:: html

    
    <table class = "tableprinted">
            <tr> <th class="toplabel" colspan="1"></th><th colspan="1" style="padding: 0px; text-align: center;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">a</div></th><th colspan="1" style="padding: 0px; text-align: center;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">b</div></th></tr>
    <tr><th class="leftlabel" rowspan="1" style="">1</td><td class="content" style="text-align: center;">Top Left</td><td class="content" style="text-align: center;">Top Right</td></tr>
    <tr><th class="leftlabel" rowspan="1" style="">2</td><td class="content" style="text-align: center;">Bottom Left</td><td class="content" style="text-align: center;">Bottom Right</td></tr>
    </table>



*Note*: The produced HTML sets various ``class`` attributes and can
therefore be arbitrarily styled.

LaTeX Output
============

*Note*: LaTeX output only produces the tabular environment. You probably
want to wrap it into a table environment.

.. code:: ipython3

    print(tp.as_latex())


.. parsed-literal::

    
    \begin{tabular}{ rcc }
    \toprule
    \multicolumn{ 1 }{c}{  } & a& b\\ 
    
    \midrule 
    \multirow{ 1 }{*}{1} & Top Left & Top Right\\ 
    \multirow{ 1 }{*}{2} & Bottom Left & Bottom Right\\ 
    
    \bottomrule
    \end{tabular}
    

