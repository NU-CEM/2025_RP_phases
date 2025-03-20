import os
from os import walk
import ase
from ase.io import read, write
import spglib
import numpy as np
from hiphive.utilities import get_displacements
import csv
import numpy as np 


foldernames = ['000_000' ,'00Mz_00Mz' ,'00Mz_000' ,'00Mz1_00Mz2' ,'00Rz_00Rz' ,'00Rz_000' ,'00Rz1_00Rz2' ,'Rx00_0Ry0' ,'RxRy0_RxRy0' ,'Rx1Ry20_Rx2Ry10' ,'Rx00_0-Ry0' ,'RxRy0_-Rx-Ry0' ,'Rx1Ry20_-Rx2-Ry10' ,'Rx0Mz_0RyMz' ,'Rx0Rz_0RyRz' ,'Rx0Mz_0-RyMz' ,'Rx0Rz_0-RyRz' ,'Rx0Mz_0Ry0' ,'Rx0Rz_0Ry0' ,'Rx0Mz_0-Ry0' ,'Rx0Rz_0-Ry0' ,'RxRyMz_RxRyMz' ,'RxRyRz_RxRyRz' ,'RxRyMz_RxRy-Mz' ,'RxRyRz_RxRy-Rz' ,'RxRyMz_-Rx-RyMz' ,'RxRyRz_-Rx-RyRz', 'RxRyMz_-Rx-Ry-Mz' ,'RxRyRz_-Rx-Ry-Rz' ,'RxRyMz_RxRy0' ,'RxRyMz_-Rx-Ry0' ,'RxRyRz_RxRy0' ,'RxRyRz_-RxRy0']

## mode projection

atoms_ideal = read('RP_2_000_000.extxyz')
for folder in foldernames:
    print_line = []
    atoms = read(f'RP_2_{folder}.extxyz')
    # mode projection
    modes = ['Rx1','Rx2', 'Ry1','Ry2','Mz1', 'Mz2', 'Rz1', 'Rz2']
    u = get_displacements(atoms, atoms_ideal, cell_tol=0.00001)
    norm = len(atoms_ideal)  * 40 / 56 
    for mode in modes:
        Q = np.dot(u.flatten(), atoms_ideal.get_array(mode).flatten())
        Q = Q / norm  # some hard-coded normalization
        print(Q)
        print_line.append(Q)
    print(print_line)

    ##print(folder,' & '.join(print_line))
    with open(f'{folder}.csv', 'w') as file:
        wr = csv.writer(file, delimiter=',')
        wr.writerow(print_line)


### covert normal extxyz to extxyz with modes 
#modes = []
#with open('RP_1_000_000.extxyz', 'r') as f:
#        for line in f:
#                line = line.split()
#                if len(line) == 22:
#                        modes.append(line[4:22])
#modes = np.array(modes, dtype = float)
#
#foldernames = ['BaZrS3_tilt_221', 'BaZrS3_tilt_140', 'BaZrS3_tilt_127', 'BaZrS3_tilt_74', 'BaZrS3_tilt_12', 'BaZrS3_tilt_63', 'BaZrS3_tilt_139', 'BaZrS3_tilt_167', 'BaZrS3_tilt_15', 'BaZrS3_tilt_2', 'BaZrS3_tilt_139', 'BaZrS3_tilt_62', 'BaZrS3_tilt_11', 'BaZrS3_tilt_137', 'BaZrS3_tilt_204', 'BaZrS3_tilt_71']
#for folder in foldernames:
#        structure = ase.io.read(f'{folder}/relaxation/geometry.in.next_step', format = 'aims')
#        ase.io.write(f'{folder}.extxyz', structure)
#
#        atom_positions = []
#        atom_names = []
#        with open(f'{folder}.extxyz', 'r') as f:
#                for line in f:
#                        line = line.split()
#                        if len(line) == 4:
#                                atom_positions.append([line[0], float(line[1]),float(line[2]),float(line[3])])
#                        if len(line) > 4:
#                                middle_line = line
#                                middle_line[9] = middle_line[9]+ ':Mx:R:3:My:R:3:Mz:R:3:Rx:R:3:Ry:R:3:Rz:R:3'
#        atom_positions = np.array(atom_positions)
#        atom_names = np.array(atom_names)
#        atoms = np.concatenate((atom_positions, modes), axis = 1)
#        atoms = atoms.tolist()
#        with open(f'{folder}_with_modes.extxyz', 'w') as f:
#                f.write('40\n')
#                f.write(' '.join(middle_line)+ '\n')
#                for line in atoms:
#                        f.write(' '.join(line)+ '\n')
