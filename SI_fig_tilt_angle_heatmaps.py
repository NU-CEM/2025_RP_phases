from ase.io import read
import numpy as np
import matplotlib.pyplot as plt

# parameters
n = 1

n_snapshots = 10000
T_start = 1
T_stop = 1000

t_average = 10
temperatures = np.linspace(T_start, T_stop, n_snapshots)

# bins
n_ave = 150
theta_index = 2
max_angle = 25
n_bins = 84
bins = np.linspace(-max_angle, max_angle, n_bins)
# fig setup
fig, axes = plt.subplots(figsize=(20, 6), nrows=3, ncols=12, sharex=True, sharey=True)

# plot params
xlim = [0, 1000]
ylim = [-14, 14]
vmax = 0.14
cmap = 'Blues'

for i in range(1,13):
    # read data
    ## Note: these are layer-by-layer xyz trajectory files from the heating runs. These are too large to upload somewhere. Please contact us if you need this file to reproduce this work/for your own research. 
    dump_fname = f'text_{i}.extxyz'
    print('reading traj')
    traj = read(dump_fname, index=':')
    print('done reading traj')
    
    angles = np.array([atoms.get_array('euler_xyz') for atoms in traj])
    del traj
    print('angles shape', angles.shape)
    
    # collect histograms
    theta_ref = None
    hist_traj = []
    T_traj = []
    for it in range(t_average, n_snapshots-t_average, 1):
        T = temperatures[it]
        print(it, T)
        
        # time average
        data_x = angles[it-t_average:it+t_average, :, 0].flatten()
        data_y = angles[it-t_average:it+t_average, :, 1].flatten()
        data_z = angles[it-t_average:it+t_average, :, 2].flatten()
    
        # get angles histogram
        histogram_x, bin_edges = np.histogram(data_x, bins=bins, density=True)
        histogram_y, bin_edges = np.histogram(data_y, bins=bins, density=True)
        histogram_z, bin_edges = np.histogram(data_z, bins=bins, density=True)
    
        theta_bins = bin_edges[:-1] + 0.5 * (bin_edges[1] - bin_edges[0])
        if theta_ref is None:
            theta_ref = theta_bins
        else:
            assert np.allclose(theta_ref, theta_bins)
    
        hist_traj.append([histogram_x, histogram_y, histogram_z])
        T_traj.append(T)
    
    hist_traj = np.array(hist_traj)
    
    # plotting
    for it, ax in enumerate(axes[:, i-1]):
        im = ax.pcolormesh(T_traj, theta_ref, hist_traj[:, it, :].T, vmin=0.0, vmax=vmax, cmap=cmap)
        print(it, 'min max P', np.min(hist_traj), np.max(hist_traj))
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
    
        label = r'$\theta_' + 'xyz'[it] + '$'
        ax.text(0.47, 0.84, label, transform=ax.transAxes, fontsize=12)
axes[0,0].set_title('Slab I Layer I')
axes[0,1].set_title('Slab I Layer II')
axes[0,2].set_title('Slab I Layer III')
axes[0,3].set_title('Slab I Layer IV')
axes[0,4].set_title('Slab I Layer V')
axes[0,5].set_title('Slab I Layer VI')
axes[0,6].set_title('Slab II Layer I')
axes[0,7].set_title('Slab II Layer II')
axes[0,8].set_title('Slab II Layer III')
axes[0,9].set_title('Slab II Layer IV')
axes[0,10].set_title('Slab II Layer V')
axes[0,11].set_title('Slab II Layer VI')
fig.supxlabel('Temperature (K)')
plt.subplots_adjust(wspace=0.1, hspace=0)
fig.tight_layout()
plt.savefig('n6_tilts.png')
