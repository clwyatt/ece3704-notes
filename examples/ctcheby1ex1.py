# Low-pass Chebyhev analog filter example

import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np

# --- Filter Specifications ---
rp = 3             # pass-band ripple (dB)
gpass = rp         # pass-band gain + ripple (dB)
wp = 2*np.pi*8000  # cut-off frequency (pass-band edge)
gstop = 20         # negative of stop-band gain (dB)
ws = 2*np.pi*10000 # stop-band edge


# --- Design the Filter ---
N, wn = signal.cheb1ord(wp, ws, gpass, gstop, analog=True) # Filter order required and corresponding pass-band edge
b, a = signal.cheby1(N, rp, wn, btype='low', analog=True, output='ba') # Numerator and denominator coefficients 

# Compute the frequency response
w, h = signal.freqs(b, a) 

# Plot the magnitude of frequency response
plt.figure()
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Chebyshev Type I Analog Filter Frequency Response')
plt.xlabel('$\omega$ (rad/s)')
plt.ylabel('$|H(j\omega)|$ (dB)')
plt.grid(which='both', axis='both')
plt.axvline(wn, color='red', linestyle='--', label=f'Cutoff: {wn} rad/s')
plt.axhline(-rp, color='green', linestyle='--', label=f'Ripple: -{rp} dB')
plt.legend()

plt.savefig('ctcheby1ex1.svg', format='svg', bbox_inches='tight')
plt.savefig('ctcheby1ex1.pdf', format='pdf', bbox_inches='tight')
plt.savefig('ctcheby1ex1.png', format='png', bbox_inches='tight')
plt.close()

# for debugging
# print(f"Filter Order: {N}")
# print(f"Specified pass-band edge: {wp}")
# print(f"Designed pass-band edge: {wn}")
# print(f"Filter Numerator (b) coefficients: {b}")
# print(f"Filter Denominator (a) coefficients: {a}")
# plt.show()
