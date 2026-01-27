### Repository for `Diverse Polymorphism in Ruddelsden-Popper Chalcogenides`

This repository contains the data and Python code required to reproduce plots in the paper [Diverse polymorphism in Ruddelsden-Popper chalcogenides]():

 - `FigX_xxx.py` or `FigX_xxx.ipynb`: Code to plot the figures in the main text.
 - `data`: Data for plotting, please see the additional README in the sub-folder.
 - `figs`: Figures which are produced
 - `model`: MLIP (specifically [NEP](https://gpumd.org/index.html)) trained using the HSE06 functional.
 - `tilt_structures`: Unrelaxed RP phases with the 33 unique tilt patterns defined by Aleksandrov applied, collected in the FHI-aims `geometry.in` format. They are generated with `construct_Aleksandrov_RP.ipynb` and `BaZrS3_cubic_2x2x2_with_modes.extxyz`.
 - `ground_states`: NEP-relaxed ground state structures for the n=1 to 6 RP phases, collected in the FHI-aims `geometry.in` format.
 - `SI_fig_xxx.py` or `SI_fig_xxx.ipynb`: Additional python scripts and Jupyter notebooks to plot figures in the supplementary information.

The `n*_thermo.out` for figure plotting, NEP model, and training set data are collected in [here](https://doi.org/10.5281/zenodo.17539815) and [here](https://doi.org/10.5281/zenodo.17539815)

Software versions used to run the above scripts/notebooks:

- [ase](https://wiki.fysik.dtu.dk/ase/)       3.22.1
- [phonopy](https://phonopy.github.io/phonopy)   2.21.0
- [spglib](https://spglib.readthedocs.io/en/stable/)    2.2.0
- [hiphive](https://hiphive.materialsmodeling.org/)   1.3.1
- [calorine](https://calorine.materialsmodeling.org/)  2.3.1
- [GPUMD](https://gpumd.org/)     3.9.5
- [mplpub](https://gitlab.com/materials-modeling/mplpub) 1.1

