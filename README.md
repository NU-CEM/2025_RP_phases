### Repository for `Diverse Polymorphism in Ruddelsden-Popper Chalcogenides`

This repository contains the data and Python code required to reproduce plots in the paper [Diverse polymorphism in Ruddelsden-Popper chalcogenides](https://arxiv.org/pdf/2507.11300).

Note that the thermodynamic data, NEP model, and training set data are too large for version control and are collected [here](https://doi.org/10.5281/zenodo.18386067). 

 - `data`: Data for plotting, please see the additional README in the sub-folder.
 - `figs`: Figures which are produced.
 - `model`: MLIP (specifically [NEP](https://gpumd.org/index.html)) trained using the HSE06 functional.
 - `relaxed_structures`: NEP-relaxed, kinetically stable structures for the n=1 to 6 RP phases.
 - `tilt_structures`: Unrelaxed RP phases with the 33 unique tilt patterns defined by Aleksandrov.
 - `FigX_xxx.py` and `FigX_xxx.ipynb`: Python scripts to plot the figures in the main text.
 - `SI_fig_xxx.py` and `SI_fig_xxx.ipynb`: Additional python scripts and Jupyter notebooks to plot figures in the supplementary information.
 - `BaZrS3_cubic_2x2x2_with_modes.extxyz` and `construct_Aleksandrov_RP.ipynb`: Geometry and Jupyter notebooks to create the tilt structures. 

Software versions used to run the above scripts/notebooks:

- [ase](https://wiki.fysik.dtu.dk/ase/)       3.22.1
- [phonopy](https://phonopy.github.io/phonopy)   2.21.0
- [spglib](https://spglib.readthedocs.io/en/stable/)    2.2.0
- [hiphive](https://hiphive.materialsmodeling.org/)   1.3.1
- [calorine](https://calorine.materialsmodeling.org/)  2.2.1
- [GPUMD](https://gpumd.org/)     3.9.5

To install via conda, navigate into the repository root folder adn run the following terminal command: `conda env create -f environment.yml`

