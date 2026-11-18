import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

#import seaborn as sns
# if using a Jupyter notebook, include:

####  Reading data from external files

data1 = np.loadtxt("B-eform.dat",float)
data2 = np.loadtxt("C-eform.dat",float)
data3 = np.loadtxt("N-eform.dat",float)

#### Setting of the plot arrangement in Figure

fig, axs =plt.subplots(nrows=3,ncols=1,sharex=True,gridspec_kw={'width_ratios':[18],'height_ratios':[2,2,2]})


#####  Plotting data and setting graph appearance for subplot 1 i.e ax[0]

axs[0].imshow( data1 , cmap = 'seismic' , interpolation = 'nearest', vmin=-4 , vmax=5.5)
axs[0].xaxis.set_ticks(np.arange(0,16,1))
axs[0].yaxis.set_ticks(np.arange(0,5,1))
axs[0].set_yticklabels(['Mo', 'Tc', 'Ru', 'Rh', 'Os'], fontsize=9)

fig.suptitle('Formataion Energy ($E_{form}$ eV)', fontsize=10)

#####  Plotting data and setting graph appearance for subplot 2 i.e ax[1]

axs[1].imshow( data2 , cmap = 'seismic' , interpolation = 'nearest', vmin=-4 , vmax=5.5)
axs[1].xaxis.set_ticks(np.arange(0,16,1))
axs[1].yaxis.set_ticks(np.arange(0,5,1))
axs[1].set_yticklabels(['Mo', 'Tc', 'Ru', 'Rh', 'Os'], fontsize=9)

#####  Plotting data and setting graph appearance for sublots 3 i.e ax[2]

pcm=axs[2].imshow( data3 , cmap = 'seismic' , interpolation = 'nearest', vmin=-4 , vmax=5.5)
axs[2].xaxis.set_ticks(np.arange(0,16,1))
axs[2].yaxis.set_ticks(np.arange(0,5,1))
axs[2].set_yticklabels(['Mo', 'Tc', 'Ru', 'Rh', 'Os'], fontsize=9)
axs[2].set_xticklabels(['R3m', 'R$\overline{3}$m', 'P$\overline{3}$m1', 'P$\overline{3}$1m', 'P6$_3$/mmc', 'Pnma', 'Pbcn', 'Fmmm', 'P4/mmm', 'I4/mmm', 'P$\overline{6}$m2', 'P6/mmm', 'Fm$\overline{3}$m', 'C2/m', 'I4$_1$/amd', 'I4/mcm'], rotation=90, fontsize=9)
#ax3.plt.grid(True)
#axs[2].colorbar(location='bottom')


#### Combining the subplots into one figure and saving

plt.tight_layout()
fig.colorbar(pcm,ax=axs[:], shrink=0.8)
plt.savefig("Eform.jpg",dpi=300,orientation='landscape', bbox_inches="tight")

plt.show()
