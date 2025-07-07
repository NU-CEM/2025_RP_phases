### Repository for `Diverse polymorphism in Ruddelsden-Popper chalcogenides`

This repository contains the data and Python code required to reproduce plots in the paper [Diverse polymorphism in Ruddelsden-Popper chalcogenides]():

 - `Fig_xxx.py` or `Fig_xxx.ipynb`: Code to plot the figures in the main text.
 - `data`: Data for plotting, please see the additional README in the sub-folder.
 - `figs`: Figures which are produced
 - `model`: MLIP (specifically [NEPs](https://gpumd.org/index.html)) trained using the HSE06 functional.
 - `structures`: Atomic structures of the tilts.
 - `SI_fig_xxx.py` or `SI_fig_xxx.py`: Additional Jupyter notebooks to plot figures in the supplementary information.

Software versions used to run the above scripts/notebooks:

- [ase](https://wiki.fysik.dtu.dk/ase/)       3.22.1
- [phonopy](https://phonopy.github.io/phonopy)   2.21.0
- [spglib](https://spglib.readthedocs.io/en/stable/)    2.2.0
- [hiphive](https://hiphive.materialsmodeling.org/)   1.3.1
- [calorine](https://calorine.materialsmodeling.org/)  2.3.1
- [GPUMD](https://gpumd.org/)     3.9.4
- [mplpub](https://gitlab.com/materials-modeling/mplpub) 1.1

