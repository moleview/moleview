#!/usr/bin/env python3

"""
MIT License

Copyright (c) 2020 Rangsiman Ketkaew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

######### USAGE ##########
# $ moleview.py YOUR.xyz #
##########################

import sys
import re
import pprint
from octadist import DrawComplex

# Read xyz file

f = open(sys.argv[1], 'r')
lines = f.read().split("\n")
f.close()

num_atoms = int(lines[0])
atoms = []
coords = []

# Compile regex
coord_patt = re.compile(
    r"(\w+)\s+([0-9\-\+\.*^eEdD]+)\s+([0-9\-\+\.*^eEdD]+)\s+"
    r"([0-9\-\+\.*^eEdD]+)")
# Extract xyz
for i in range(2, 2 + num_atoms):
    m = coord_patt.search(lines[i])
    if m:
        atoms.append(m.group(1))
        xyz = [val.lower().replace("d", "e").replace('*^', 'e') for val
               in m.groups()[1:4]]
        coords.append([float(val) for val in xyz])

# pprint.pprint(atoms)
# pprint.pprint(coords)

mol = DrawComplex(atom=atoms, coord=coords)
mol.add_atom()
mol.add_bond()
mol.add_legend()
mol.config_plot(
    show_title=True,
    show_axis=True,
    show_grid=True,
)
mol.show_plot()
