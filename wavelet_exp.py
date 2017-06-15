from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# These are experiments with using wavelet transformations to extract transient rather than stationary (as in FFT) waveforms from EMG data. 

sig = singles['talented']['voltage']
widths = np.linspace(0.001,10,100)
wt_out = signal.cwt(sig, signal.ricker, widths)
print (wt_out, wt_out.shape)
plt.imshow(wt_out, extent=[0, 1, 1, 10],cmap='PRGn',aspect='auto',vmax=abs(wt_out).max(), vmin=-abs(wt_out).max())
plt.show()
wt_out_frame = pandas.DataFrame(wt_out).T
print(wt_out_frame.head())

sig2 = singles['stereotyped']['voltage']
# widths = np.linspace(0.005,10)
wt_out2 = signal.cwt(sig2, signal.ricker, widths)
print (wt_out2, wt_out2.shape, sig2.shape)
plt.imshow(wt_out2, extent=[0, 1, 1, 10],cmap='PRGn',aspect='auto',vmax=abs(wt_out2).max(), vmin=-abs(wt_out2).max())
plt.show()

sig3 = singles['weather']['voltage']
# widths = np.linspace(0.005,10)
wt_out3 = signal.cwt(sig3, signal.ricker, widths)
print (wt_out3, wt_out3.shape, sig3.shape)
plt.imshow(wt_out3, extent=[0, 1, 1, 10],cmap='PRGn',aspect='auto',vmax=abs(wt_out3).max(), vmin=-abs(wt_out3).max())
plt.show()
