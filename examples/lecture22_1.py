import matplotlib.pyplot as plt
import numpy as np

wc = 100

p1 = wc*np.exp(1j*2*np.pi/3)
p2 = -wc
p3 = wc*np.exp(-1j*2*np.pi/3)

ctomega = np.linspace(0.01,1000, num=1000)
s = 1j*ctomega

H1 = (wc**3)/((s-p1)*(s-p2)*(s-p3))

nyquist = 2*500
T = (2*np.pi)/nyquist

print(2*np.atan2(wc*T,2))

dtomega = np.linspace(0,np.pi, num=1000)
z = np.exp(1j*dtomega)

# another computationally direct approach
# s = (2*(z-1))/(T*(z+1))
# H2 = (wc**3)/((s-p1)*(s-p2)*(s-p3))

# DT tf/frequency response
K = ((T*wc/2)**3)/((1-p1*T/2)*(1-p2*T/2)*(1-p3*T/2))
alpha1 = (1+p1*T/2)/(1-p1*T/2)
alpha2 = (1+p2*T/2)/(1-p2*T/2)
alpha3 = (1+p3*T/2)/(1-p3*T/2)

H2 = K*((z+1)**3)/((z-alpha1)*(z-alpha2)*(z-alpha3))

# pole locations
# print(np.abs(alpha1))
# print(np.abs(alpha2))
# print(np.abs(alpha3))

plt.figure()
plt.subplots_adjust(hspace=0.5)
plt.subplot(2,1,1)
plt.semilogx(ctomega, 20 * np.log10(abs(H1)))
plt.xlim(min(ctomega), max(ctomega))
plt.ylim(-100, 20)
plt.title('Analog Filter and DT Filter Frequency Response')
plt.xlabel('$\omega$ (rad/s)')
plt.ylabel('$|H(s)|$ (dB)')
plt.grid(which='both', axis='both')

plt.subplot(2,1,2)
plt.plot(dtomega, 20 * np.log10(abs(H2)))
plt.xlim(min(dtomega), max(dtomega))
plt.ylim(-100, 20)
plt.xlabel('$\omega$ (radians/sample)')
plt.ylabel('$|H(z)|$ (dB)')
plt.grid(which='both', axis='both')


plt.savefig('lecture22_1.svg', format='svg', bbox_inches='tight')
plt.savefig('lecture22_1.pdf', format='pdf', bbox_inches='tight')
plt.savefig('lecture22_1.png', format='png', bbox_inches='tight')

# just check phase is nonlinear
# plt.figure()
# plt.plot(dtomega, np.unwrap(np.angle(H2)))
# plt.xlim(min(dtomega), max(dtomega))
# plt.xlabel('$\omega$ (radians/sample)')
# plt.show()

plt.close()




