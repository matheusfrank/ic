#%%
"""
Author:
Matheus Frank

Description:
This code generates spectrography graphs for galaxies.

ToDos:
Generalize it for any fits input file.
"""
import matplotlib.pyplot as plt
from astropy.io import fits


#%%

with fits.open('spec-4240-55455-0240.fits') as ngc5548:
    #ngc5548.info() #Uncomment this line for info.
    header  = ngc5548['PRIMARY'].header
    data    = ngc5548['COADD'].data
    flux5548 =  data['flux']
    wl5548 = 10 ** data['loglam']
#%% 
with fits.open('spec-1068-52614-0006.fits') as ngc1068:
    #ngc1068.info()             # Uncomment this line for fits file contents.
    header  = ngc1068['PRIMARY'].header
    #print('Flux units:', ngc1068[0].header['bunit'])   #Units info.
    data    = ngc1068['COADD'].data
    #print(data.columns)        # Shows the columns in the dataset
    
    flux1068 =  data['flux']
    wl1068 = 10 ** data['loglam']
# %%
    """
    Pyplot
    """
fig, axs = plt.subplots(2, sharex=True, sharey=True)
fig.suptitle('Espectros AGN')
axs[0].grid()
axs[0].set_title(f'NGC1068')
axs[0].set_ylabel(r'Flux ($\mathrm{10^{-17} erg\,s^{-1}\,cm^{-2}\,\AA^{-1}}$)')
axs[0].plot(wl1068, flux1068)

axs[1].grid()
axs[1].set_title(f'NGC5548')
axs[1].set_xlabel(r'Wavelength ($\AA$)')
axs[1].set_ylabel(r'Flux ($\mathrm{10^{-17} erg\,s^{-1}\,cm^{-2}\,\AA^{-1}}$)')
axs[1].plot(wl5548, flux5548, 'tab:orange')

# %%
fig = plt.figure()
gs = fig.add_gridspec(2, hspace=0.1)
axs = gs.subplots(sharex=True, sharey=True)

fig.suptitle('Espectros AGN')
fig.text(0.5, 0.01, r'Wavelength ($\AA$)', ha='center')
fig.text(0.03, 0.5, r'Flux ($\mathrm{10^{-17} erg\,s^{-1}\,cm^{-2}\,\AA^{-1}}$)', va='center', rotation='vertical')

axs[0].grid()
axs[0].plot(wl1068, flux1068, label='NGC1068')
axs[0].legend()

axs[1].grid()
axs[1].plot(wl5548, flux5548, 'tab:orange', label='NGC5548')
axs[1].legend()
