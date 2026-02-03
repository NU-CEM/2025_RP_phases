from calorine.gpumd import read_thermo
from dynasor.tools.acfs import smoothing_function
import numpy as np
from scipy import constants
from ase.io import read
import matplotlib as mpl
import mplpub
mplpub.setup(template='acs')
mpl.rcParams['ytick.labelsize'] = 9
mpl.rcParams['xtick.labelsize'] = 9

# parameters
n_vals = [1, 2, 4, 5, 6, 3]

# plot setup
xlim = [0, 1000]
ylim = [0.9, 2.0]
alpha = 0.3

fig, axes = plt.subplots(figsize=(4.0, 6.0), nrows=3,sharex=True, dpi=120)
n = 6
colors = plt.cm.coolwarm(np.linspace(0,1,n))
n1 = 0
n2 = 0
n3 = 0
count = 0
files = ['1','2','3','4','5','6', 'inf']
for i in files:
    if i == 'inf':
        ## note that the data for n*_thermo.out files can be found here: https://doi.org/10.5281/zenodo.18386067. Please download these before running the script. 
        df = read_thermo(f'/Users/prakriti/2025_RP_phases_data/n{i}_thermo.out')
        atoms = read(f'data/n{i}_model.xyz')
    else:
        df = read_thermo(f'/Users/prakriti/2025_RP_phases_data/n{i}_thermo.out')
        atoms = read(f'data/n{i}_model.xyz')
    k_B = constants.physical_constants["Boltzmann constant in eV/K"][0]
    if i == 'inf':
        window_average = 200
    else:
        window_average = 5000
    df['potential_energy'] = df['potential_energy']/atoms.get_global_number_of_atoms()
    print(i, round(df['potential_energy'].iloc[0],5))
    df['potential_energy'] = df['potential_energy']-df['potential_energy'].iloc[0]

    df['potential_energy'] = df['potential_energy'] - (1.5*k_B*df['temperature'])
    # process data
    df['temp_lin'] = df['temperature']
    
    df['Epot'] = 1000 * df['potential_energy']

    df['temperature'] = smoothing_function(df['temperature'], window_average)
    df['potential_energy'] = smoothing_function(df['potential_energy'], window_average)

    # heat capacity
    p = 200
    window_size1 = 2000
    window_size2 = 4 * window_size1
    
    df['heat_capacity'] = df.Epot.diff(periods=p) / df.temp_lin.diff(periods=p) / k_B / 1.5 / 1000
    df['heat_capacity'] = smoothing_function(df['heat_capacity'] + 1.0, window_size2)
    
    
    if i == '1': 
        n1,n2,n3 = 10,10,10
    elif i == '2':
        n1,n2,n3 = 8,8,8
    elif i == '3':
        n1,n2,n3 = 8,8,6
    elif i == '4':
        n1,n2,n3 = 6,6,8
    elif i == '5':
        n1,n2,n3 = 6,6,7
    elif i == '6':
        n1,n2,n3 = 6,6,6
    elif i == '7':
        n1,n2,n3 = 6,6,5
    elif i == '8':
        n1,n2,n3 = 6,6,4
    elif i == 'inf':
        n1,n2,n3 = 7,7,7
    a = np.sqrt(df['cell_xx']**2+df['cell_xy']**2+df['cell_xz']**2)/(n1*2)
    a = smoothing_function(a, window_average)
    b = np.sqrt(df['cell_yx']**2+df['cell_yy']**2+df['cell_yz']**2)/(n2*2)
    b = smoothing_function(b, window_average)
    c = np.sqrt(df['cell_zx']**2+df['cell_zy']**2+df['cell_zz']**2)/(n2*2)
    c = smoothing_function(c, window_average)
    temp  = df['temperature']
    energy = df['potential_energy']
    
    ax = axes[0]
    ax.text(-0.20, 1, 'a)', transform=ax.transAxes, fontsize = 10)
    if i == 'inf':
        #ax.plot(df['temperature'],a/np.sqrt(2), label = r'perov a', color = 'k')
        #ax.plot(df['temperature'],b/2, label = r'perov b', color = 'red')
        ax.plot(df['temperature'],c/np.sqrt(2), label = r'perov', color = 'k')
    else:
        ax.plot(df['temperature'],a, color = colors[count], label = f'$n={i}$')
    ax.set_ylim([4.95,5.1])
    ax.legend(frameon=True,facecolor='white', fontsize = 8)
    ax.set_ylabel(r'Lattice parameter (\AA)', fontsize = 10)
    ax = axes[2]
    if i == 'inf':
        data = np.load(f'data/heat_capacity_data_perovskite.npy', allow_pickle=True).item()
        ax.plot(data['temperature_fit'], data['heatcapacity_fit'], '-', color='k', label=f'', zorder = 6)
    elif i == '1':
        data = np.load(f'data/heat_capacity_data_RP_n{i}.npy', allow_pickle=True).item()
        ax.plot(data['temperature_fit'], data['heatcapacity_fit'], '-', color=colors[0], label=f'RP n{n}', zorder = 1)
    elif i == '2':
        data = np.load(f'data/heat_capacity_data_RP_n{i}.npy', allow_pickle=True).item()
        ax.plot(data['temperature_fit'], data['heatcapacity_fit'], '-', color=colors[1], label=f'RP n{n}', zorder = 2)
    elif i == '3':
        data = np.load(f'data/heat_capacity_data_RP_n{i}.npy', allow_pickle=True).item()
        ax.plot(data['temperature_fit'], data['heatcapacity_fit'], '-', color=colors[2], label=f'RP n{n}', zorder = 7)
    elif i == '4':
        data = np.load(f'data/heat_capacity_data_RP_n{i}.npy', allow_pickle=True).item()
        ax.plot(data['temperature_fit'], data['heatcapacity_fit'], '-', color=colors[3], label=f'RP n{n}', zorder = 3)
    elif i == '5':
        data = np.load(f'data/heat_capacity_data_RP_n{i}.npy', allow_pickle=True).item()
        ax.plot(data['temperature_fit'], data['heatcapacity_fit'], '-', color=colors[4], label=f'RP n{n}', zorder = 4)
    elif i == '6':
        data = np.load(f'data/heat_capacity_data_RP_n{i}.npy', allow_pickle=True).item()
        ax.plot(data['temperature_fit'], data['heatcapacity_fit'], '-', color=colors[5], label=f'RP n{n}', zorder = 5)
    ax.set_ylim([0.95,2])
    ax.set_ylabel(r'Heat capacity (k$_B$)', fontsize = 10)
    ax.set_xlabel('Temperature (K)', fontsize = 10)
    ax.text(-0.20, 1, 'c)', transform=ax.transAxes, fontsize = 10)
    ax = axes[1]
    if i == 'inf':
        ax.plot(df['temperature'],df['potential_energy']*100, label = r'\infty', color = 'k')
    elif i == '1' or '2' or '3':
        ax.plot(df['temperature'],df['potential_energy']*100, label = f'{i}', color = colors[count])
    else:
        ax.plot(df['temperature'],df['potential_energy']*100, color = colors[count])
      
    ax.set_ylabel('Energy (meV/atom)', fontsize = 10)
    ax.set_xlabel('Temperature (K)', fontsize=10)
    ax.text(-0.20, 1, 'b)', transform=ax.transAxes, fontsize = 10)
    ax.set_ylim([-0.12,1.62])
    #ax.legend()
    count = count + 1
#plt.tick_params(labelsize = 10)
plt.xlim([0,1000])
plt.tight_layout()
plt.subplots_adjust(hspace=0)
plt.savefig('figs/plot_heating.png')

