#!/usr/bin/env python
"""
Write a dot file from a networkx graph for further processing with graphviz.

You need to have either pygraphviz or pydotplus for this example.

See https://networkx.org/documentation/latest/reference/drawing.html
for more info.

"""
# Author: Aric Hagberg (hagberg@lanl.gov)

#    Copyright (C) 2004-2016 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

import networkx as nx

# and the following code block is not needed
# but we want to see which module is used and
# if and why it fails
try:
    import pygraphviz
    from networkx.drawing.nx_agraph import write_dot
    print("using package pygraphviz")
except ImportError:
    try:
        import pydotplus
        from networkx.drawing.nx_pydot import write_dot
        print("using package pydotplus")
    except ImportError:
        print()
        print("Both pygraphviz and pydotplus were not found ")
        print("see https://networkx.org/documentation"
              "/latest/reference/drawing.html for info")
        print()
        raise

G=nx.grid_2d_graph(5,5)  # 5x5 grid
write_dot(G,"grid.dot")
print("Now run: neato -Tps grid.dot >grid.ps")
