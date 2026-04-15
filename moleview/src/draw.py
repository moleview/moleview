"""
MIT License

Copyright (c) 2020-2021 Rangsiman Ketkaew

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

from matplotlib import pyplot as plt
import numpy as np
import plotly.graph_objects as go
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from .atom import check_atom, check_radii, check_color, find_bonds


class DrawComplex_matplotlib:
    """
    Display 3D structure of octahedral complex with label for each atoms using Matplotlib.

    Parameters
    ----------
    atom : list, None
        Atomic symbols of octahedral structure.
    coord : list, array, tuple, bool, None
        Atomic coordinates of octahedral structure.
    cutoff_global : int or float
        Global cutoff for screening bonds.
        Default value is 2.0.
    cutoff_hydrogen : int or float
        Cutoff for screening hydrogen bonds.
        Default value is 1.2.

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
    >>> test =  DrawComplex_matplotlib(atom=atom, coord=coord)
    >>> test.add_atom()
    >>> test.add_bond()
    >>> test.add_legend()
    >>> test.config_plot(show_title=True, show_axis=True, show_grid=True)
    >>> test.show_plot()

    """

    def __init__(self, atom=None, coord=None, cutoff_global=2.0, cutoff_hydrogen=1.2):
        self.atom = atom
        self.coord = coord
        self.cutoff_global = cutoff_global
        self.cutoff_hydrogen = cutoff_hydrogen
        self.sphere_resolution = 20

        if self.atom is None:
            raise TypeError("atom is not specified")
        if self.coord is None:
            raise TypeError("coord is not specified")

        self.title_name = "Display Complex"
        self.title_size = "12"
        self.label_size = "10"
        self.show_title = True
        self.show_axis = True
        self.show_grid = True

        self.atoms_pair = []
        self.bond_list = None

        self.start_plot()

    def start_plot(self):
        """
        Introduce figure to plot.

        """
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection="3d")

        self.ax.set_title("Full complex", fontsize="12")
        # ax = fig.add_subplot(111, projection='3d')

    def add_atom(self):
        """
        Add all atoms to show in figure.

        """
        for i in range(len(self.coord)):
            # Determine atomic number
            n = check_atom(self.atom[i])
            self.ax.scatter(
                self.coord[i][0],
                self.coord[i][1],
                self.coord[i][2],
                marker="o",
                linewidths=0.5,
                edgecolors="black",
                color=check_color(n),
                label=f"{self.atom[i]}",
                s=check_radii(n) * 300,
            )

    def add_symbol(self):
        """
        Add symbol of atoms to show in figure.

        """
        for j in range(len(self.atom)):
            self.ax.text(
                self.coord[j][0] + 0.1,
                self.coord[j][1] + 0.1,
                self.coord[j][2] + 0.1,
                f"{self.atom[j]},{j}",
                fontsize=9,
            )

    def add_bond(self):
        """
        Calculate bond distance, screen bond, and add them to show in figure.

        See Also
        --------
        octadist.src.util.find_bonds : Find atomic bonds.

        """
        _, self.bond_list = find_bonds(
            self.atom, self.coord, self.cutoff_global, self.cutoff_hydrogen
        )

        for i in range(len(self.bond_list)):
            get_atoms = self.bond_list[i]
            x, y, z = zip(*get_atoms)
            atoms = list(zip(x, y, z))
            self.atoms_pair.append(atoms)

        for i in range(len(self.atoms_pair)):
            merge = list(zip(self.atoms_pair[i][0], self.atoms_pair[i][1]))
            x, y, z = merge
            self.ax.plot(x, y, z, color="black", linewidth=2)

    def add_legend(self):
        """
        Add atoms legend to show in figure.

        References
        ----------
        1. Remove duplicate labels in legend.
            Ref: https://stackoverflow.com/a/26550501/6596684.

        2. Fix size of point in legend.
            Ref: https://stackoverflow.com/a/24707567/6596684.

        """
        # remove duplicate labels
        handles, labels = self.ax.get_legend_handles_labels()
        handle_list, label_list = [], []

        for handle, label in zip(handles, labels):
            if label not in label_list:
                handle_list.append(handle)
                label_list.append(label)
        leg = plt.legend(
            handle_list,
            label_list,
            loc="lower left",
            bbox_to_anchor=(-0.2, 0),
            scatterpoints=1,
            fontsize=12,
        )

        # fix size of point in legend
        for i in range(len(leg.legend_handles)):
            leg.legend_handles[i]._sizes = [90]

    def config_plot(self, show_title=True, show_axis=True, show_grid=True, **kwargs):
        """
        Setting configuration for figure.

        Parameters
        ----------
        show_title : bool
            If True, show title of figure.
            If False, not show title of figure.
        show_axis : bool
            If True, show axis of figure.
            If False, not show axis of figure.
        show_grid : bool
            If True, show grid of figure.
            If False, not show grid of figure.
        kwargs : dict (optional)
            title_name : title name of figure.
            title_size : text size of title.
            label_size : text size of axis labels.

        """
        title_name_user = kwargs.get("title_name")
        self.title_size = kwargs.get("title_size")
        self.label_size = kwargs.get("label_size")
        self.show_title = show_title
        self.show_axis = show_axis
        self.show_grid = show_grid

        if title_name_user is not None:
            self.ax.set_title(title_name_user)

        if self.title_size is not None:
            if title_name_user is None:
                title_name_user = self.title_name
            self.ax.set_title(title_name_user, fontsize=self.title_size)

        if self.label_size is not None:
            self.ax.set_xlabel(r"X", fontsize=self.label_size)
            self.ax.set_ylabel(r"Y", fontsize=self.label_size)
            self.ax.set_zlabel(r"Z", fontsize=self.label_size)

        if not self.show_title:
            self.ax.set_title("")
        if not self.show_axis:
            plt.axis("off")
        if not self.show_grid:
            self.ax.grid(False)

    def save_img(self, save="Complex_saved_by_OctaDist", file="png"):
        """
        Save figure as an image.

        Parameters
        ----------
        save : str
            Name of image file.
            Default value is "Complex_saved_by_OctaDist".
        file : file
            Image type.
            Default value is "png".

        """
        plt.savefig(f"{save}.{file}")

    def show_plot(self):
        """
        Show plot.

        """
        plt.show()


class DrawComplex_plotly:
    """
    Display 3D structure of octahedral complex using Plotly.

    Parameters
    ----------
    atom : list, None
        Atomic symbols of octahedral structure.
    coord : list, array, tuple, bool, None
        Atomic coordinates of octahedral structure.
    cutoff_global : int or float
        Global cutoff for screening bonds.
        Default value is 2.0.
    cutoff_hydrogen : int or float
        Cutoff for screening hydrogen bonds.
        Default value is 1.2.

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
    >>> test =  DrawComplex_plotly(atom=atom, coord=coord)
    >>> test.add_atom()
    >>> test.add_bond()
    >>> test.add_legend()
    >>> test.config_plot(show_title=True, show_axis=True, show_grid=True)
    >>> test.show_plot()

    """

    def __init__(self, atom=None, coord=None, cutoff_global=2.0, cutoff_hydrogen=1.2):
        self.atom = atom
        self.coord = coord
        self.cutoff_global = cutoff_global
        self.cutoff_hydrogen = cutoff_hydrogen
        self.sphere_resolution = 20

        if self.atom is None:
            raise TypeError("atom is not specified")
        if self.coord is None:
            raise TypeError("coord is not specified")

        self.bond_list = []
        self.start_plot()

    def start_plot(self):
        """
        Introduce figure to plot.
        """
        self.fig = go.Figure()
        self.fig.update_layout(title="Full complex")

    def _generate_sphere_surface(self, center, radius):
        """Generate Cartesian coordinates for a sphere surface."""
        u = np.linspace(0, 2 * np.pi, self.sphere_resolution)
        v = np.linspace(0, np.pi, self.sphere_resolution)

        x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
        y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
        z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))
        return x, y, z

    def add_atom(self):
        """
        Add all atoms to show in figure.
        """
        # Group atoms by element to create single trace per element type
        atoms_data = {}
        for i, symbol in enumerate(self.atom):
            if symbol not in atoms_data:
                atoms_data[symbol] = {"x": [], "y": [], "z": []}
            atoms_data[symbol]["x"].append(self.coord[i][0])
            atoms_data[symbol]["y"].append(self.coord[i][1])
            atoms_data[symbol]["z"].append(self.coord[i][2])

        for symbol, data in atoms_data.items():
            n = check_atom(symbol)
            radius = check_radii(n)
            color = check_color(n)

            self.fig.add_trace(
                go.Scatter3d(
                    x=[data["x"][0]],
                    y=[data["y"][0]],
                    z=[data["z"][0]],
                    mode="markers",
                    name=symbol,
                    legendgroup=symbol,
                    visible="legendonly",
                    marker=dict(size=10, color=color),
                    hoverinfo="skip",
                )
            )

            for x_coord, y_coord, z_coord in zip(data["x"], data["y"], data["z"]):
                x_sphere, y_sphere, z_sphere = self._generate_sphere_surface(
                    (x_coord, y_coord, z_coord), radius
                )

                self.fig.add_trace(
                    go.Surface(
                        x=x_sphere,
                        y=y_sphere,
                        z=z_sphere,
                        surfacecolor=np.ones_like(x_sphere),
                        colorscale=[[0, color], [1, color]],
                        cmin=0,
                        cmax=1,
                        showscale=False,
                        name=symbol,
                        legendgroup=symbol,
                        showlegend=False,
                        hovertemplate=f"{symbol}<extra></extra>",
                        lighting=dict(ambient=0.55, diffuse=0.8, specular=0.25),
                    )
                )

    def add_bond(self):
        """
        Calculate bond distance, screen bond, and add them to show in figure.
        """
        _, self.bond_list = find_bonds(
            self.atom, self.coord, self.cutoff_global, self.cutoff_hydrogen
        )

        x_lines = []
        y_lines = []
        z_lines = []

        for bond in self.bond_list:
            start_atom, end_atom = bond
            x_lines.extend([start_atom[0], end_atom[0], None])
            y_lines.extend([start_atom[1], end_atom[1], None])
            z_lines.extend([start_atom[2], end_atom[2], None])

        self.fig.add_trace(
            go.Scatter3d(
                x=x_lines,
                y=y_lines,
                z=z_lines,
                mode="lines",
                name="Bond",
                line=dict(color="black", width=3),
                showlegend=False,
            )
        )

    def add_legend(self):
        """
        Add atoms legend to show in figure.
        Plotly handles legend automatically based on trace names.
        """
        self.fig.update_layout(showlegend=True, legend=dict(itemsizing="constant"))

    def config_plot(self, show_title=True, show_axis=True, show_grid=True, **kwargs):
        """
        Setting configuration for figure.
        """
        title_text = kwargs.get("title_name", "Full complex")

        layout_update = {}

        if show_title:
            layout_update["title"] = title_text
        else:
            layout_update["title"] = ""

        scene = dict(
            aspectmode="data",
            xaxis=dict(visible=show_axis, showgrid=show_grid, title="X"),
            yaxis=dict(visible=show_axis, showgrid=show_grid, title="Y"),
            zaxis=dict(visible=show_axis, showgrid=show_grid, title="Z"),
        )

        layout_update["scene"] = scene
        self.fig.update_layout(**layout_update)

    def show_plot(self):
        """
        Show plot.
        """
        self.fig.show()
