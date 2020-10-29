# MoleView: A Fast and lightweight plug-in for 3D molecular visualization

Molecule + Viewer = MoleView <br/>
View your molecule anywhere and anytime!

## Installation

```sh
pip install moleview
```

**Requirements**
- Python 3
- NumPy
- SciPy
- Matplotlib

## Usage

```sh
moleview benzene.xyz
```

## Gallery

Screenshots of program:

| ![][ss_1]     | ![][ss_2]          | ![][ss_3]     |
|:-------------:|:------------------:|:-------------:|
| Aspirin       | Alanine tripeptide |      C180     |

[ss_1]: https://raw.githubusercontent.com/moleview/moleview/master/img/aspirin.png
[ss_2]: https://raw.githubusercontent.com/moleview/moleview/master/img/alanine-tripeptide.png
[ss_3]: https://raw.githubusercontent.com/moleview/moleview/master/img/c180.png

## Development

What you can help improve MoleView :)

- Visualization of a large molecule in matplotlib is still slow. It would be great if we can make it faster.
- Is it possible to make MoleView displays animation of a trajectory file that contains a number of structures? 
- Is it possible to speed up the performance using GPU? 
- It would be very great if MoleView can provide analysis functions such as molecular orbitals, density, ...

All pull requests, issues, comments and suggestions are welcome.

## Support and Citation
```
@software{Moleview2020,
    author = "Rangsiman Ketkaew",
    title  = "MoleView: A fast and lightweight plug-in for 3D molecular visualization",
    month  = "oct",
    year   = "2020",
    url   = "https://github.com/moleview/moleview"
}
```

## Author

Rangsiman Ketkaew : rangsiman1993@gmail.com
