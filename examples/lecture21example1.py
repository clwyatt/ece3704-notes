import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(-3,15, 19)

D = 11/8
E = -1/16
a = -1/8
absgamma = np.sqrt(1/8)
r = np.sqrt(((D**2)*(absgamma**2) + (E**2)-2*D*a*E)/((absgamma**2) - a*a))
w0 = np.acos(-a/absgamma)
theta = np.atan((D * a - E) / (D * np.sqrt(absgamma**2 - a**2)))
y1 = -(3/8)*(( 3/4)**n)*(n >= 0) + r*(absgamma**n)*np.cos(w0*n + theta)*(n >= 0)

F = 11/8
G = 7/(8*np.sqrt(7))
y2 = -(3/8)*(( 3/4)**n)*(n >= 0) + F*(absgamma**n)*np.cos(w0*n)*(n >= 0) +  G*(absgamma**n)*np.sin(w0*n)*(n >= 0)

p1 = 1/8 + 1j*(np.sqrt(7)/8)
p2 = 1/8 - 1j*(np.sqrt(7)/8)
#H = 11/16 - 1j*0.165359
#I = 11/16 + 1j*0.165359
H = (7+3*np.sqrt(7)*1j)/(7+5*np.sqrt(7)*1j)
I = (-7+3*np.sqrt(7)*1j)/(-7+5*np.sqrt(7)*1j)
y3 = -(3/8)*(( 3/4)**n)*(n >= 0) + H*((p1)**n)*(n >= 0) + I*((p2)**n)*(n >= 0)

print(H)
print(I)

plt.figure()
#plt.stem(n,y1)
#plt.stem(n,y2)
plt.stem(n,y3)
plt.xticks(n)
plt.title('Example Response')
plt.xlabel('$n$')
plt.ylabel('$y_1[n]$')
plt.grid(which='both', axis='both')


plt.savefig('lecture21example1.svg', format='svg', bbox_inches='tight')
plt.savefig('lecture21example1.pdf', format='pdf', bbox_inches='tight')
plt.savefig('lecture21example1.png', format='png', bbox_inches='tight')
