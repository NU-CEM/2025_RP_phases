import os 
import numpy as np
from ase.io import read
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

materials = next(os.walk('.'))[2]
count = 1
for i in range(1,9):
     space_group = []
     symbol = []
     energy = []
     for mater in materials:
       if f"RP_{i}" in mater:
        structure = read('%s'%mater, format = 'aims')
        atoms = read('%s'%mater, format = 'aims')
        calc = CPUNEP('nep.txt')
        fs = FixSymmetry(structure, symprec=0.00001)
        structure.set_constraint(fs)
        structure.calc = calc
        
        ucf = UnitCellFilter(structure)
        dyn = BFGS(ucf, logfile='log.out', trajectory='test.traj')
        dyn.run(fmax=0.0001, steps=100)
        symm = ase.spacegroup.get_spacegroup(structure, symprec=0.00001)
        space_group.append(symm.no)
        symbol.append(spglib.get_spacegroup(atoms,symprec=0.0000001))
        energy.append(structure.get_potential_energy()/structure.get_global_number_of_atoms())
     res = list(zip(space_group,symbol,energy))
     print(res) 
     sg = min(res, key=lambda p:p[2])[1]
     E = min(res, key=lambda p:p[2])[2]
     print(i, sg , E)
     for j in res:
        print(j[1], E - j[2])
