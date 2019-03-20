%matplotlib inline

from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
import math as math
import numpy as numpy

##################### 5.1 #####################

x = input("Gib die dB-Anzahl des ersten Summanden an: ")
y = input("Gib die dB-Anzahl des zweiten Summanden an: ")
dB1 = int(x)
dB2 = int(y)

sum = 10 * math.log(math.pow(10,(dB1/10))+math.pow(10,(dB2/10)), 10)

print("Die Summe aus %d dB und %d dB beträgt %0.3f dB." % (dB1, dB2 ,sum))


##################### 5.2 #####################

# Hierbei wird das Abtasttheorem verwendet. Der Sinn eines Tiefpassfilter besteht darin, dass dieser verhindert das Aliasing 
# zustande kommt. Dabei beschränkt man sich auf eine geeignete Bandbreite,
# welche verhindert, dass bei der Abtastung das Originalsignal verfälscht wird.


##################### 5.3 #####################

wav_filename = "speech_clean.wav"

# read the WAV file
samplerate, data = wavfile.read(wav_filename)

# get the total number of samples
total_samples = len(data)

# half of the array is enough; the symmetrical negative counterpart can be omitted
lmt = int((total_samples / 2) - 1)

# compute the fast fourier transformation and convert the imaginary values into abolute values
fft_abs = abs(fft(data))        

# compute the frequency bin centers for the plot's correct axis
freqs = fftfreq(totalnum_samples, 1 / samplerate)

l = 300/freqs[1]
x = math.ceil(l)


for ATM in range(0, x):
    fft_abs[ATM] = 0
    
y = math.ceil(3400/freqs[1])
z = math.ceil(8000/freqs[1])

# for ATM in range(y, z):
#     fft_abs[ATM] = 0
    
    
# plot the frequencies
plt.plot(frequency[0:lmt], fft_abs[0:lmt])
plt.title("Frequenzspektrum der Datei: %s" % wav_filename)
plt.xlabel('Frequenz in Hz')
plt.ylabel('Amplitude')
# plt.xscale('log') # use a logarithmic x axis
plt.show()
