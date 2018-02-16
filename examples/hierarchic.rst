
.. code:: ipython3

    # This is only necessary to execute this notebook from the examples folder.
    import sys
    import os
    sys.path.insert(0, os.path.abspath('..'))
    
    from tableprinter import Tableprinter
    
    # For displaying the HTML output directly in the notebook
    from IPython.display import HTML

.. code:: ipython3

    # Generate hierarchic data. x1 and x2 are the two x-coordinates. y1, y2 and y3 are three levels of y-coordinates.
    data = [
        {'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, 'y3': y3, 'content': '{}/{}-{}/{}/{}'.format(x1,x2,y1,y2,y3)}
        for x1 in ['a', 'b'] for x2 in [1,2] for y1 in ['x', 'y'] for y2 in ['3', '4'] for y3 in ['i', 'j']
    ]
    
    # Not all cells have to be present
    _ = data.pop(23)

.. code:: ipython3

    tp = Tableprinter(data, x_dimensions=('x1','x2'), y_dimensions=('y1','y2','y3'))

.. code:: ipython3

    print(tp.as_unicode())


.. parsed-literal::

    ┏━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┓
    ┃      ┃           a           ┃           b           ┃
    ┃      ┃     1     ┃     2     ┃     1     ┃     2     ┃
    ┣━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━┫
    │    i │ a/1-x/3/i │ a/2-x/3/i │ b/1-x/3/i │ b/2-x/3/i │
    │  3 ──├───────────┼───────────┼───────────┼───────────┤
    │    j │ a/1-x/3/j │ a/2-x/3/j │ b/1-x/3/j │ b/2-x/3/j │
    │x ────├───────────┼───────────┼───────────┼───────────┤
    │    i │ a/1-x/4/i │ a/2-x/4/i │ b/1-x/4/i │ b/2-x/4/i │
    │  4 ──├───────────┼───────────┼───────────┼───────────┤
    │    j │ a/1-x/4/j │ a/2-x/4/j │ b/1-x/4/j │ b/2-x/4/j │
    │──────├───────────┼───────────┼───────────┼───────────┤
    │    i │ a/1-y/3/i │ a/2-y/3/i │ b/1-y/3/i │ b/2-y/3/i │
    │  3 ──├───────────┼───────────┼───────────┼───────────┤
    │    j │ a/1-y/3/j │ a/2-y/3/j │ b/1-y/3/j │ b/2-y/3/j │
    │y ────├───────────┼───────────┼───────────┼───────────┤
    │    i │ a/1-y/4/i │ a/2-y/4/i │ b/1-y/4/i │ b/2-y/4/i │
    │  4 ──├───────────┼───────────┼───────────┼───────────┤
    │    j │ a/1-y/4/j │ a/2-y/4/j │    --     │ b/2-y/4/j │
    └──────┴───────────┴───────────┴───────────┴───────────┘
    


.. code:: ipython3

    HTML(tp.as_html())




.. raw:: html

    
    <table class = "tableprinted">
            <tr> <th class="toplabel" colspan="3"></th><th colspan="2" style="padding: 0px; text-align: center;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">a</div></th><th colspan="2" style="padding: 0px; text-align: center;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">b</div></th></tr>
    <tr> <th class="toplabel" colspan="3"></th><th colspan="1" style="padding: 0px; text-align: center;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">1</div></th><th colspan="1" style="padding: 0px; text-align: center;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">2</div></th><th colspan="1" style="padding: 0px; text-align: center;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">1</div></th><th colspan="1" style="padding: 0px; text-align: center;"><div style="border-bottom: 1px solid black;margin-left: 3px; margin-right: 7px;">2</div></th></tr>
    <tr><th class="leftlabel" rowspan="4" style="">x</td><th class="leftlabel" rowspan="2" style="">3</td><th class="leftlabel" rowspan="1" style="">i</td><td class="content" style="text-align: center;">a/1-x/3/i</td><td class="content" style="text-align: center;">a/2-x/3/i</td><td class="content" style="text-align: center;">b/1-x/3/i</td><td class="content" style="text-align: center;">b/2-x/3/i</td></tr>
    <tr><th class="leftlabel" rowspan="1" style="">j</td><td class="content" style="text-align: center;">a/1-x/3/j</td><td class="content" style="text-align: center;">a/2-x/3/j</td><td class="content" style="text-align: center;">b/1-x/3/j</td><td class="content" style="text-align: center;">b/2-x/3/j</td></tr>
    <tr><th class="leftlabel" rowspan="2" style="border-top: 1px solid black;">4</td><th class="leftlabel" rowspan="1" style="border-top: 1px solid black;">i</td><td class="content" style="text-align: center;">a/1-x/4/i</td><td class="content" style="text-align: center;">a/2-x/4/i</td><td class="content" style="text-align: center;">b/1-x/4/i</td><td class="content" style="text-align: center;">b/2-x/4/i</td></tr>
    <tr><th class="leftlabel" rowspan="1" style="">j</td><td class="content" style="text-align: center;">a/1-x/4/j</td><td class="content" style="text-align: center;">a/2-x/4/j</td><td class="content" style="text-align: center;">b/1-x/4/j</td><td class="content" style="text-align: center;">b/2-x/4/j</td></tr>
    <tr><th class="leftlabel" rowspan="4" style="border-top: 1px solid black;">y</td><th class="leftlabel" rowspan="2" style="border-top: 1px solid black;">3</td><th class="leftlabel" rowspan="1" style="border-top: 1px solid black;">i</td><td class="content" style="text-align: center;">a/1-y/3/i</td><td class="content" style="text-align: center;">a/2-y/3/i</td><td class="content" style="text-align: center;">b/1-y/3/i</td><td class="content" style="text-align: center;">b/2-y/3/i</td></tr>
    <tr><th class="leftlabel" rowspan="1" style="">j</td><td class="content" style="text-align: center;">a/1-y/3/j</td><td class="content" style="text-align: center;">a/2-y/3/j</td><td class="content" style="text-align: center;">b/1-y/3/j</td><td class="content" style="text-align: center;">b/2-y/3/j</td></tr>
    <tr><th class="leftlabel" rowspan="2" style="border-top: 1px solid black;">4</td><th class="leftlabel" rowspan="1" style="border-top: 1px solid black;">i</td><td class="content" style="text-align: center;">a/1-y/4/i</td><td class="content" style="text-align: center;">a/2-y/4/i</td><td class="content" style="text-align: center;">b/1-y/4/i</td><td class="content" style="text-align: center;">b/2-y/4/i</td></tr>
    <tr><th class="leftlabel" rowspan="1" style="">j</td><td class="content" style="text-align: center;">a/1-y/4/j</td><td class="content" style="text-align: center;">a/2-y/4/j</td><td class="content empty">--</td><td class="content" style="text-align: center;">b/2-y/4/j</td></tr>
    </table>



*Note*: The produced HTML sets various ``class`` attributes and can
therefore be arbitrarily styled.

.. code:: ipython3

    print(tp.as_latex())


.. parsed-literal::

    
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
    

