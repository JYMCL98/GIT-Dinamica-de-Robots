#Librerías 
import numpy as np # librería para manejo de vectores y arreglos

# Función escalón
def hardlim(n): 
	if n>0:
		value = 1
	else:
		value = 0

	return value

# Entradas
#     a,b,c,d,e,f,g
P = [[1,1,1,1,1,1,0],  #0
	 [0,1,1,0,0,0,0],  #1
	 [1,1,0,1,1,0,1],  #2
	 [1,1,1,1,0,0,1],  #3
	 [0,1,1,0,0,1,1],  #4
	 [1,0,1,1,0,1,1],  #5
	 [1,0,1,1,1,1,1],  #6
	 [1,1,1,0,0,0,0],  #7
	 [1,1,1,1,1,1,1],  #8
	 [1,1,1,1,0,1,1]]  #9

# Valores esperados
t_pares = [1,0,1,0,1,0,1,0,1,0]
t_mayores_5 = [0,0,0,0,0,0,1,1,1,1]
t_numeros_p = [0,0,1,1,0,1,0,1,0,0]
t_impares = [0,1,0,1,0,1,0,1,0,1]

t = t_pares
#t = t_impares
#t = t_mayores_5
#t = t_numeros_p

# Error
e = np.ones(10) 

# inicializamos de manera aleatoria 
# random entrega un valor aleatorio entre 0 y 1, se multiplica por 2 para que dé valores aleatorios de 0 a 2
# como se quiere valores de -1 a 1, por eso se le resta uno, y el 7 es el número de valores aleatorios

W = 2*np.random.rand(1,7)-1 # Matriz de pesos sinápticos
b = 2*np.random.rand(1)-1  # Vector de polarización

for epocas in range(500):
	for q in range(10):
		a = hardlim(np.dot(W,P[q])+b) # neurona perceptrón (salida)
		e[q] = t[q]-a
		W += np.dot(e[q],P[q]).T # Transpuesta
		b += e[q]

print(W)
print(b)
print(e)
###########################################################