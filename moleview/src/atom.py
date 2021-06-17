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

import numpy as np
from scipy.spatial import distance


def check_atom(x):
    """
    Convert atomic number to symbol and vice versa for atom 1-109.

    Parameters
    ----------
    x : str or int
        symbol or atomic number.

    Returns
    -------
    atom[x] : str
        If x is atomic number, return symbol.

    atom.index(i) : int
        If x is symbol, return atomic number.

    Examples
    --------
    >>> check_atom('He')
    2

    >>> check_atom(2)
    'He'

    """
    atoms = [
        "0",
        "H",
        "He",
        "Li",
        "Be",
        "B",
        "C",
        "N",
        "O",
        "F",
        "Ne",
        "Na",
        "Mg",
        "Al",
        "Si",
        "P",
        "S",
        "Cl",
        "Ar",
        "K",
        "Ca",
        "Sc",
        "Ti",
        "V",
        "Cr",
        "Mn",
        "Fe",
        "Co",
        "Ni",
        "Cu",
        "Zn",
        "Ga",
        "Ge",
        "As",
        "Se",
        "Br",
        "Kr",
        "Rb",
        "Sr",
        "Y",
        "Zr",
        "Nb",
        "Mo",
        "Tc",
        "Ru",
        "Rh",
        "Pd",
        "Ag",
        "Cd",
        "In",
        "Sn",
        "Sb",
        "Te",
        "I",
        "Xe",
        "Cs",
        "Ba",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Pm",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Hf",
        "Ta",
        "W",
        "Re",
        "Os",
        "Ir",
        "Pt",
        "Au",
        "Hg",
        "Tl",
        "Pb",
        "Bi",
        "Po",
        "At",
        "Rn",
        "Fr",
        "Ra",
        "Ac",
        "Th",
        "Pa",
        "U",
        "Np",
        "Pu",
        "Am",
        "Cm",
        "Bk",
        "Cf",
        "Es",
        "Fm",
        "Md",
        "No",
        "Lr",
        "Rf",
        "Db",
        "Sg",
        "Bh",
        "Hs",
        "Mt",
    ]

    if isinstance(x, int):
        return atoms[x]
    else:
        for i in atoms:
            if x == i:
                return atoms.index(i)


def check_radii(x):
    """
    Convert atomic number (index) to atom radii in Angstroms: 1-119.

    Parameters
    ----------
    x : int
        Atomic number.

    Returns
    -------
    atom_radii[x] : int
        Atomic radius.

    Examples
    --------
    >>> check_radii(2) # He
    0.93

    """
    atom_radii = (
        np.array(
            [
                0,
                230,
                930,
                680,
                350,
                830,
                680,
                680,
                680,
                640,
                1120,
                970,
                1100,
                1350,
                1200,
                750,
                1020,
                990,
                1570,
                1330,
                990,
                1440,
                1470,
                1330,
                1350,
                1350,
                1340,
                1330,
                1500,
                1520,
                1450,
                1220,
                1170,
                1210,
                1220,
                1210,
                1910,
                1470,
                1120,
                1780,
                1560,
                1480,
                1470,
                1350,
                1400,
                1450,
                1500,
                1590,
                1690,
                1630,
                1460,
                1460,
                1470,
                1400,
                1980,
                1670,
                1340,
                1870,
                1830,
                1820,
                1810,
                1800,
                1800,
                1990,
                1790,
                1760,
                1750,
                1740,
                1730,
                1720,
                1940,
                1720,
                1570,
                1430,
                1370,
                1350,
                1370,
                1320,
                1500,
                1500,
                1700,
                1550,
                1540,
                1540,
                1680,
                1700,
                2400,
                2000,
                1900,
                1880,
                1790,
                1610,
                1580,
                1550,
                1530,
                1510,
                1500,
                1500,
                1500,
                1500,
                1500,
                1500,
                1500,
                1500,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
                1600,
            ],
            dtype=np.float32,
        )
        / 1000.0
    )

    return atom_radii[x]


def check_color(x):
    """
    Convert atomic number to color: 1-109.

    Parameters
    ----------
    x : int
        Atomic number.

    Returns
    -------
    atomic color[x] : str
        Atomic color.

    References
    ----------
    http://jmol.sourceforge.net/jscolors/

    Examples
    --------
    >>> check_color(2) # He
    '#D9FFFF'

    """
    atom_color = [
        "0",
        "#FFFFFF",
        "#D9FFFF",
        "#CC80FF",
        "#C2FF00",
        "#FFB5B5",
        "#909090",
        "#3050F8",
        "#FF0D0D",
        "#90E050",
        "#B3E3F5",
        "#AB5CF2",
        "#8AFF00",
        "#BFA6A6",
        "#F0C8A0",
        "#FF8000",
        "#FFFF30",
        "#1FF01F",
        "#80D1E3",
        "#8F40D4",
        "#3DFF00",
        "#E6E6E6",
        "#BFC2C7",
        "#A6A6AB",
        "#8A99C7",
        "#9C7AC7",
        "#E06633",
        "#F090A0",
        "#50D050",
        "#C88033",
        "#7D80B0",
        "#C28F8F",
        "#668F8F",
        "#BD80E3",
        "#FFA100",
        "#A62929",
        "#5CB8D1",
        "#702EB0",
        "#00FF00",
        "#94FFFF",
        "#94E0E0",
        "#73C2C9",
        "#54B5B5",
        "#3B9E9E",
        "#248F8F",
        "#0A7D8C",
        "#006985",
        "#C0C0C0",
        "#FFD98F",
        "#A67573",
        "#668080",
        "#9E63B5",
        "#D47A00",
        "#940094",
        "#429EB0",
        "#57178F",
        "#00C900",
        "#70D4FF",
        "#FFFFC7",
        "#D9FFC7",
        "#C7FFC7",
        "#A3FFC7",
        "#8FFFC7",
        "#61FFC7",
        "#45FFC7",
        "#30FFC7",
        "#1FFFC7",
        "#00FF9C",
        "#00E675",
        "#00D452",
        "#00BF38",
        "#00AB24",
        "#4DC2FF",
        "#4DA6FF",
        "#2194D6",
        "#267DAB",
        "#266696",
        "#175487",
        "#D0D0E0",
        "#FFD123",
        "#B8B8D0",
        "#A6544D",
        "#575961",
        "#9E4FB5",
        "#AB5C00",
        "#754F45",
        "#428296",
        "#420066",
        "#007D00",
        "#70ABFA",
        "#00BAFF",
        "#00A1FF",
        "#008FFF",
        "#0080FF",
        "#006BFF",
        "#545CF2",
        "#785CE3",
        "#8A4FE3",
        "#A136D4",
        "#B31FD4",
        "#B31FBA",
        "#B30DA6",
        "#BD0D87",
        "#C70066",
        "#CC0059",
        "#D1004F",
        "#D90045",
        "#E00038",
        "#E6002E",
        "#EB0026",
    ]

    return atom_color[x]


def find_bonds(atom, coord, cutoff_global=2.0, cutoff_hydrogen=1.2):
    """
    Find all bond distance and filter the possible bonds.

    - Compute distance of all bonds
    - Screen bonds out based on global cutoff distance
    - Screen H bonds out based on local cutoff distance

    Parameters
    ----------
    atom : list
        List of atomic labels of molecule.
    coord : list
        List of atomic coordinates of molecule.
    cutoff_global : int or float
        Global cutoff for screening bonds.
        Default value is 2.0.
    cutoff_hydrogen : int or float
        Cutoff for screening hydrogen bonds.
        Default value is 1.2.

    Returns
    -------
    filtered_bond_2 : list
        Selected bonds in molecule after screening.

    Examples
    --------
    >>> atom = ['Fe', 'N', 'N', 'N', 'O', 'O', 'O']
    >>> coord = [[2.298354000, 5.161785000, 7.971898000],
                 [1.885657000, 4.804777000, 6.183726000],
                 [1.747515000, 6.960963000, 7.932784000],
                 [4.094380000, 5.807257000, 7.588689000],
                 [0.539005000, 4.482809000, 8.460004000],
                 [2.812425000, 3.266553000, 8.131637000],
                 [2.886404000, 5.392925000, 9.848966000]]
    >>> pair_bond, bond_dist = find_bonds(atom, coord)
    >>> pair_bond
    [['Fe', 'N'],
     ['Fe', 'N'],
     ['Fe', 'N'],
     ['Fe', 'O'],
     ['Fe', 'O'],
     ['Fe', 'O']]
    >>> bond_dist
    [[[2.298354, 5.161785, 7.971898], [1.885657, 4.804777, 6.183726]],
     [[2.298354, 5.161785, 7.971898], [1.747515, 6.960963, 7.932784]],
     [[2.298354, 5.161785, 7.971898], [4.094380, 5.807257, 7.588689]],
     [[2.298354, 5.161785, 7.971898], [0.539005, 4.482809, 8.460004]],
     [[2.298354, 5.161785, 7.971898], [2.812425, 3.266553, 8.131637]],
     [[2.298354, 5.161785, 7.971898], [2.886404, 5.392925, 9.848966]]]

    """
    all_pair = []
    all_bond = []

    for i in range(len(coord)):
        for j in range(i + 1, len(coord)):
            if i == 0:
                dist = distance.euclidean(coord[i], coord[j])
            else:
                dist = distance.euclidean(coord[i], coord[j])

            all_pair.append([atom[i], atom[j]])
            all_bond.append([coord[i], coord[j], dist])

    filtered_pair_1 = []
    filtered_bond_1 = []

    for i in range(len(all_bond)):
        if all_bond[i][2] <= cutoff_global:
            filtered_pair_1.append([all_pair[i][0], all_pair[i][1]])

            filtered_bond_1.append([all_bond[i][0], all_bond[i][1], all_bond[i][2]])

    filtered_pair_2 = []
    filtered_bond_2 = []

    for i in range(len(filtered_bond_1)):
        if filtered_pair_1[i][0] == "H" or filtered_pair_1[i][1] == "H":
            if filtered_bond_1[i][2] <= cutoff_hydrogen:
                filtered_pair_2.append([filtered_pair_1[i][0], filtered_pair_1[i][1]])
                filtered_bond_2.append([filtered_bond_1[i][0], filtered_bond_1[i][1]])
        else:
            filtered_pair_2.append([filtered_pair_1[i][0], filtered_pair_1[i][1]])
            filtered_bond_2.append([filtered_bond_1[i][0], filtered_bond_1[i][1]])

    return filtered_pair_2, filtered_bond_2
