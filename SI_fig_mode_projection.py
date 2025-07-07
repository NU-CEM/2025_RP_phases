from ase.io import read,write
import os
import spglib
import numpy as np
from hiphive.utilities import get_displacements
import csv
from calorine.gpumd.io import write_xyz
from calorine.gpumd import read_thermo
from dynasor.tools.acfs import smoothing_function
import matplotlib.pyplot as plt
from scipy import constants
import pandas as pd
import mplpub 
mplpub.setup('acs')

#for i in range(1,9):
#    columns = ['Rx1','Rx2', 'Ry1','Ry2','Rz1','Rz2','Mz1','Mz2']
#    fig = plt.figure(figsize = (6,4), dpi = 200)
#    ax1 = fig.add_subplot(111)
#    df = pd.read_csv(f'data/modes_RP_{i}_heating.csv')
#    x = np.linspace(0,1000,199)
#    print(df.iloc[:, 0])
#    ax1.plot(x, df.iloc[:,0], label = r'$\phi_{x_1}$', color = 'tab:blue', linestyle = 'solid')
#    ax1.plot(x, df.iloc[:,1], label = r'$\phi_{x_2}$', color = 'tab:blue', linestyle = 'solid', lw = 3.0, alpha = 0.3)
#    ax1.plot(x, df.iloc[:,2], label = r'$\phi_{y_1}$', color = 'tab:orange', linestyle = 'solid')
#    ax1.plot(x, df.iloc[:,3], label = r'$\phi_{y_2}$', color = 'tab:orange', linestyle = 'solid', lw = 3.0, alpha = 0.3)
#    ax1.plot(x, df.iloc[:,4], label = r'$\phi_{z_1}$', color = 'tab:green', linestyle = 'solid')
#    ax1.plot(x, df.iloc[:,5], label = r'$\phi_{z_2}$', color = 'tab:green', linestyle = 'solid', lw = 3.0, alpha = 0.3)
#    ax1.plot(x, df.iloc[:,6], label = r'$\psi_{z_1}$', color = 'tab:red', linestyle = 'solid')
#    ax1.plot(x, df.iloc[:,7], label = r'$\psi_{z_2}$', color = 'tab:red', linestyle = 'solid', lw = 3.0, alpha = 0.3)
#    ax1.set_xlabel('Temperature (K)')
#    ax1.set_ylabel('Q')
#    ax1.set_xlim([0,1000])
#    plt.legend(loc=1, fontsize = 7)
#    plt.savefig(f'figs/plot_mode_project_n_{i}_heating.png')

for i in range(1,9):
    columns = ['Rx1','Rx2', 'Ry1','Ry2','Rz1','Rz2','Mz1','Mz2']
    fig = plt.figure(figsize = (6,4), dpi = 200)
    ax1 = fig.add_subplot(111)
    df = pd.read_csv(f'data/modes_RP_{i}_cooling.csv')
    x = np.linspace(0,1000,199)
    print(df.iloc[:, 0])
    ax1.plot(x, df.iloc[:,0], label = r'$\phi_{x_1}$', color = 'tab:blue', linestyle = 'solid')
    ax1.plot(x, df.iloc[:,1], label = r'$\phi_{x_2}$', color = 'tab:blue', linestyle = 'solid', lw = 3.0, alpha = 0.3)
    ax1.plot(x, df.iloc[:,2], label = r'$\phi_{y_1}$', color = 'tab:orange', linestyle = 'solid')
    ax1.plot(x, df.iloc[:,3], label = r'$\phi_{y_2}$', color = 'tab:orange', linestyle = 'solid', lw = 3.0, alpha = 0.3)
    ax1.plot(x, df.iloc[:,4], label = r'$\phi_{z_1}$', color = 'tab:green', linestyle = 'solid')
    ax1.plot(x, df.iloc[:,5], label = r'$\phi_{z_2}$', color = 'tab:green', linestyle = 'solid', lw = 3.0, alpha = 0.3)
    ax1.plot(x, df.iloc[:,6], label = r'$\psi_{z_1}$', color = 'tab:red', linestyle = 'solid')
    ax1.plot(x, df.iloc[:,7], label = r'$\psi_{z_2}$', color = 'tab:red', linestyle = 'solid', lw = 3.0, alpha = 0.3)
    ax1.set_xlabel('Temperature (K)')
    ax1.set_ylabel('Q')
    ax1.set_xlim([0,1000])
    plt.legend(loc=1, fontsize = 7)
    plt.savefig(f'figs/plot_mode_project_n_{i}_cooling.png')
