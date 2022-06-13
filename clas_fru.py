# Clasificación de frutas
import numpy  as np # vectores y matrices

def hardlim(n):
	if n > 0:
		value = 1
	else:
		value = 0
	return value

   	 #R, G,  B (lectura sensor de color),  W (lectura de la galga extensiométrica)
P =[[18, 33, 30, 454],# M1 
	[12, 34, 30, 775],# M2 
	[19, 40, 37, 647],# M3
	[15, 31, 32, 891],# M4
	[14, 29, 26, 923],# M5
	[10, 21, 21, 708],# M6
	[14, 27, 24, 960],# M7
	[12, 26, 24, 676],# M8
	[15, 21, 20, 189],# M9
	[12, 21, 19, 816],# M10
	[12, 18, 21,53],# P1
	[9, 15, 19, 52],# P2
	[10, 17, 22,192],# P3
	[11, 17, 23, 191],# P4
	[10, 13, 18, 264],# P5
	[8, 16, 21, 31],# P6
	[9, 15, 19, 146],# P7
	[9, 14, 18,163],# P8
	[8, 11, 13, 414],# P9
	[7, 12, 15, 210]]# P10

# Valores esperados
t = [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0] # se activa la neurona cuando hay una manzana

# Error
e = np.ones(20) 				
W = 2*np.random.rand(1,4)-1	# Matriz de pesos sinápticos
b = 2*np.random.rand(1)-1		#Vector de polarización

for epocas in range(10000):
	for q in range(20):
		a = hardlim(np.dot(W,P[q])+b) # Función de activación
		e[q] = t[q] - a
		W += np.dot(e[q],P[q]).T
		b += e[q]

print(W)
print(b)
print(e)
#####################################