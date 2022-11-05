#%%
"""
Author:
Matheus Frank

Description:
This code generates spectrography graphs for galaxies.

ToDos:
Make it a class object and add zoom methods. Add spectral lines.
"""
import matplotlib.pyplot as plt
from numpy import arange
from numpy import append
from numpy import loadtxt
from astropy.io import fits

#%%
with fits.open('spec-2127-53859-0085.fits') as ngc5548:
    #ngc5548.info() #Uncomment this line for info.
    header  = ngc5548['PRIMARY'].header
    #print(header)
    #print('Flux units:', ngc1068[0].header['bunit'])   #Units info.
    data    = ngc5548['COADD'].data
    #print(data.columns)        # Shows the columns in the dataset
    
    #print(data['flux'])
    flux5548 =  data['flux']
    wl5548 = 10 ** data['loglam']
    
#%%  
with fits.open('spec-1068-52614-0006.fits') as ngc1068:
    #ngc1068.info()             # Uncomment this line for fits file contents.
    header  = ngc1068['PRIMARY'].header
    #print(header)
    #print('Flux units:', ngc1068[0].header['bunit'])   #Units info.
    data    = ngc1068['COADD'].data
    #print(data.columns)        # Shows the columns in the dataset
    
    #print(data['flux'])
    flux1068 =  data['flux']*1e2
    wl1068 = 10 ** data['loglam']
#%%

emissionLines =  loadtxt('emissionLines.txt', dtype=('str','str'), skiprows=1, usecols=(0,3), unpack=True)
emissionLinesArr1 = []
emissionLinesArr2 = []
for i in range(0,len(emissionLines[0])):
    a, b = emissionLines[0][i], emissionLines[1][i]
    emissionLinesArr1.append(float(a)), emissionLinesArr2.append(b)

absorptionLines = loadtxt('absorptionLines.txt', dtype=('str','str'), skiprows=1, usecols=(0,3), unpack=True)
absorptionLinesArr1 = []
absorptionLinesArr2 = []
for i in range(0,len(absorptionLines[0])):
    a, b = absorptionLines[0][i], absorptionLines[1][i]
    absorptionLinesArr1.append(float(a)), absorptionLinesArr2.append(b)

skyLines = loadtxt('skyLines.txt',dtype=('str','str'), skiprows=1, usecols=(0,3), unpack=True)
skyLinesArr1 = []
skyLinesArr2 = []
for i in range(0,len(skyLines[0])):
    a, b = skyLines[0][i], skyLines[1][i]
    skyLinesArr1.append(float(a)), skyLinesArr2.append(b)

spectralLines = [[emissionLinesArr1,    emissionLinesArr2],
                 [absorptionLinesArr1,  absorptionLinesArr2],
                 [skyLinesArr1,         skyLinesArr2]]

#print(f"Printa os elementos das linhas de emissao:\n{spectralLines[0][1]}")

# %%

y_bottomLimit = -2e3
y_topLimit = 6e3
y_step = 1e3

x_bottomLimit = 3.5e3
x_topLimit = 9.5e3
x_step = 5e2

fig = plt.figure(dpi=1000)
gs = fig.add_gridspec(2, hspace=0.2)
axs = gs.subplots(sharex=True, sharey=True)

fig.suptitle('Espectros AGN')
fig.text(0.5, -0.02, r'Wavelength ($\AA$)', ha='center')
fig.text(0.0, 0.5, r'Flux ($\mathrm{10^{-17} erg\,s^{-1}\,cm^{-2}\,\AA^{-1}}$)', va='center', rotation='vertical')

axs[0].grid()
axs[0].plot(wl1068, flux1068, 'tab:blue', label='NGC1068', linewidth=1)
axs[0].vlines(x = spectralLines[0][0], ymin=-2000, ymax=6000, color="#606060", linestyle ="dotted", linewidth=0.25)#, label="Emission Lines")
axs[0].vlines(x = spectralLines[1][0], ymin=-2000, ymax=6000, color="#606060", linestyle ="dotted",linewidth=0.25)#, label="Absorption Lines")
axs[0].vlines(x = spectralLines[2][0], ymin=-2000, ymax=6000, color="#606060", linestyle ="dotted", linewidth=0.25)#, label="Sky Lines")
axs[0].legend()

axs[1].grid()
axs[1].plot(wl5548, flux5548, 'tab:orange', label='NGC5548', linewidth=1)
axs[1].vlines(x = spectralLines[0][0], ymin=-2000, ymax=6000, color="#606060", linestyle ="dotted", linewidth=0.25) #label="Emission Lines")
axs[1].vlines(x = spectralLines[1][0], ymin=-2000, ymax=6000, color="#606060", linestyle ="dotted", linewidth=0.25) #label="Absorption Lines")
axs[1].vlines(x = spectralLines[2][0], ymin=-2000, ymax=6000, color="#606060", linestyle ="dotted", linewidth=0.25) #label="Sky Lines")
axs[1].legend()


for g in [0,1]:
    for h in [0,1,2]:
        arr = arange(0,len(spectralLines[h][1]))*120
        for i in range(0,len(spectralLines[h][1])):
            if spectralLines[h][0][i] >= x_bottomLimit:
                axs[g].text(spectralLines[h][0][i], arr[i], spectralLines[0][1][i], rotation = 0, verticalalignment='center', fontsize=1.75)
            else:
                pass

fig = plt.ylim(y_bottomLimit, y_topLimit) 
fig = plt.xlim(x_bottomLimit,x_topLimit)
fig = plt.yticks(arange(y_bottomLimit, y_topLimit+1, y_step))
fig = plt.xticks(arange(x_bottomLimit,x_topLimit+1 ,x_step),rotation=35)
fig = plt.savefig('spectres.jpeg')
# %%
"""
Intetionally in Blank
"""
# %%
"""
LEGACY

arr = arange(0,len(spectralLines[0][1]))*10
print(arr)

emissionLines =  loadtxt('emissionLines.txt', dtype=('str','str'), skiprows=1, usecols=(0,3), unpack=True)
emissionLinesList = []
for i in range(0,len(emissionLines[0])):
    tuple = (float(emissionLines[0][i]),emissionLines[1][i])
    emissionLinesList.append(tuple)

absorptionLines = loadtxt('absorptionLines.txt', dtype=('str','str'), skiprows=1, usecols=(0,3), unpack=True)
absorptionLinesList = []
for i in range(0,len(absorptionLines[0])):
    tuple = (float(absorptionLines[0][i]),absorptionLines[1][i])
    absorptionLinesList.append(tuple)

skyLines = loadtxt('skyLines.txt',dtype=('str','str'), skiprows=1, usecols=(0,3), unpack=True)
skyLinesList = []
for i in range(0,len(skyLines[0])):
    tuple = (float(skyLines[0][i]),skyLines[1][i])
    skyLinesList.append(tuple)

spectralLines = [emissionLinesList, absorptionLinesList, skyLinesList]

print(skyLines[0])
#print(spectralLines[0][0][0], spectralLines[0][0][1])
#print(len(spectralLines[0]))
"""