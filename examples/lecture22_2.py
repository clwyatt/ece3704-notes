import matplotlib.pyplot as plt
import numpy as np

wc = np.pi/2
M = 51
d = 25

k = np.linspace(0, M-1, num=M)
omega = np.linspace(0,np.pi, num=1000)

h = (1/(np.pi*(k-d)))*np.sin(wc*(k-d))
h[d] = 1

b = 0.5*h*(1-np.cos(2*np.pi*k/M))

# there must be a cleaner way to do this
H = np.zeros(len(omega)) + 1j*np.zeros(len(omega))
for i in k:
    H += b[int(i)]*np.exp(-1j*i*omega)

K = 1/H[0]
print(K)

plt.figure()
plt.subplots_adjust(hspace=0.5)
plt.subplot(2,1,1)
plt.plot(omega, 20 * np.log10(abs(K*H)))
plt.xlim(min(omega), max(omega))
#plt.ylim(-100, 20)
plt.xlabel('$\omega$ (radians/sample)')
plt.ylabel('$|H(z)|$ (dB)')
plt.grid(which='both', axis='both')
plt.title("Frequency Response for FIR Example")

plt.subplot(2,1,2)
plt.plot(omega, np.unwrap(np.angle(K*H)))
plt.xlim(min(omega), max(omega))
plt.xlabel('$\omega$ (radians/sample)')
plt.ylabel(' Phase $H(z)$ (rad)')
plt.grid(which='both', axis='both')

plt.savefig('lecture22_2.svg', format='svg', bbox_inches='tight')
plt.savefig('lecture22_2.pdf', format='pdf', bbox_inches='tight')
plt.savefig('lecture22_2.png', format='png', bbox_inches='tight')

plt.close()
