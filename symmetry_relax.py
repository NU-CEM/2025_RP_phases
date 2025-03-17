import os 
import numpy as np
from ase.io import read, write
from calorine.calculators import CPUNEP
from calorine.tools import get_force_constants, relax_structure
from matplotlib import pyplot as plt
from pandas import DataFrame
from phonopy.units import THzToCm
from seekpath import get_explicit_k_path
import spglib
from ase.spacegroup.symmetrize import FixSymmetry
from ase.constraints import UnitCellFilter
from ase.optimize import BFGS
import ase.spacegroup
import pandas as pd 

phonons = ['000_000', '00Rz_00Rz', '00Rz_000', '00Rz1_00Rz2', '00Mz_00Mz', '00Mz_000', '00Mz1_00Mz2', 'Rx00_0Ry0', 'RxRy0_RxRy0', 'Rx1Ry20_Rx2Ry10', 'Rx00_0-Ry0', 'RxRy0_-Rx-Ry0', 'Rx1Ry20_-Rx2-Ry10']
phonons = ['000_000', '00Rz_00Rz', '00Rz_000', '00Rz1_00Rz2', '00Mz_00Mz', '00Mz_000', '00Mz1_00Mz2', 'Rx00_0Ry0', 'RxRy0_RxRy0', 'Rx1Ry20_Rx2Ry10', 'Rx00_0-Ry0', 'RxRy0_-Rx-Ry0']
phonons = ['000_000' ,'00Mz_00Mz' ,'00Mz_000' ,'00Mz1_00Mz2' ,'00Rz_00Rz' ,'00Rz_000' ,'00Rz1_00Rz2' ,'Rx00_0Ry0' ,'RxRy0_RxRy0' ,'Rx1Ry20_Rx2Ry10' ,'Rx00_0-Ry0' ,'RxRy0_-Rx-Ry0' ,'Rx1Ry20_-Rx2-Ry10' ,'Rx0Mz_0RyMz' ,'Rx0Rz_0RyRz' ,'Rx0Mz_0-RyMz' ,'Rx0Rz_0-RyRz' ,'Rx0Mz_0Ry0' ,'Rx0Mz_0-Ry0' ,'Rx0Rz_0Ry0' ,'RxRyMz_RxRyMz' ,'RxRyRz_RxRyRz' ,'RxRyRz_RxRy-Rz' ,'RxRyMz_RxRy-Mz' ,'RxRyRz_-Rx-RyRz' ,'RxRyMz_-Rx-Ry-Mz' ,'RxRyRz_-Rx-Ry-Rz' ,'RxRyMz_RxRy0' ,'RxRyMz_-Rx-Ry0' ,'RxRyRz_RxRy0']
phonons = ['000_000' ,'00Mz_00Mz' ,'00Mz_000' ,'00Mz1_00Mz2' ,'00Rz_00Rz' ,'00Rz_000' ,'00Rz1_00Rz2' ,'Rx00_0Ry0' ,'RxRy0_RxRy0' ,'Rx1Ry20_Rx2Ry10' ,'Rx00_0-Ry0' ,'RxRy0_-Rx-Ry0' ,'Rx1Ry20_-Rx2-Ry10' ,'Rx0Mz_0RyMz' ,'Rx0Rz_0RyRz' ,'Rx0Mz_0-RyMz' ,'Rx0Rz_0-RyRz' ,'Rx0Mz_0Ry0' ,'Rx0Rz_0Ry0' ,'Rx0Mz_0-Ry0' ,'Rx0Rz_0-Ry0' ,'RxRyMz_RxRyMz' ,'RxRyRz_RxRyRz' ,'RxRyMz_RxRy-Mz' ,'RxRyRz_RxRy-Rz' ,'RxRyMz_-Rx-RyMz' ,'RxRyRz_-Rx-RyRz', 'RxRyMz_-Rx-Ry-Mz' ,'RxRyRz_-Rx-Ry-Rz' ,'RxRyMz_RxRy0' ,'RxRyMz_-Rx-Ry0' ,'RxRyRz_RxRy0' ,'RxRyRz_-RxRy0']
materials = next(os.walk('.'))[2]
count = 1

for i in range(1,9):
     space_group = []
     symbol = []
     energy = []
     phonon_mode = []
    
     for phonon in phonons:
          structure = read(f'RP_{i}_{phonon}.in', format = 'aims')
          #print("structure " + spglib.get_spacegroup(structure,symprec=0.000000001))
          atoms = read(f'RP_{i}_{phonon}.in', format = 'aims')
          #print("atoms " + spglib.get_spacegroup(atoms,symprec=0.000000001))
          calc = CPUNEP('nep.txt')
          fs = FixSymmetry(structure, symprec=0.000000001)
          structure.set_constraint(fs)
          structure.calc = calc
          ucf = UnitCellFilter(structure)
          dyn = BFGS(ucf, logfile='log.out', trajectory='test.traj')
          dyn.run(fmax=0.0001, steps=1000)
          symm = spglib.get_spacegroup(structure,symprec=0.000000001) 
          space_group.append(symm)
          symbol.append(spglib.get_spacegroup(structure,symprec=0.000000001))
          energy.append(round(structure.get_potential_energy()/structure.get_global_number_of_atoms(),5))
          write(f'sym_relax/sym_relax_RP_{i}_{phonon}.in', structure, format = 'aims')
          phonon_mode.append(phonon)
     test = pd.DataFrame(list(zip(phonon_mode, space_group, energy)))
     print(i, test[2].min())
     test[2] = test[2]-test[2].min()
     print(test)
     #res = list(zip(space_group,symbol,energy,phonon_mode))
     #sg = min(res, key=lambda p:p[2])[1]
     #E = min(res, key=lambda p:p[2])[2]
     #for j in res:
     #   print(i, j[1], j[3], round(j[2] - E,5))
