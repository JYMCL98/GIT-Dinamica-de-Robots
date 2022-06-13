#Nombre: José Guadalupe Sánchez Velázquez
#Grado:  6°
#Grupo:  6
#Carrera: Mecatrónica Agrícola

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm

fig, ax = plt.subplots()
ax = plt.axes(projection = "3d")
#Función para rotar la función en el eje x
def matriz_rotacion_x(grados):
	rad = grados/180*np.pi
	#Matriz de rotación
	rotacion=np.array([[1,0,0,0],
					   [0,np.cos(rad),-np.sin(rad),0],
					   [0,np.sin(rad),np.cos(rad),0],
					   [0,0,0,0]])
	return rotacion
#Función para rotar la función en el eje y
def matriz_rotacion_y(grados):
	rad = grados/180*np.pi
	#Matriz de rotacuón
	rotacion=np.array([[np.cos(rad),0,-np.sin(rad),0],
					   [          0,1,           0,0],
					   [np.sin(rad),0, np.cos(rad),0],
					   [0          ,0,           0,0]])
	return rotacion
def matriz_rotacion_z(grados):
	rad = grados/180*np.pi
	#Matriz de rotacuón
	rotacion=np.array([[np.cos(rad),-np.sin(rad),0,0],
					   [np.sin(rad), np.cos(rad),0,0],
					   [          0,           0,1,0],
					   [          0,           0,0,0]])
	return rotacion

def matriz_traslacion_x(x):
	traslacion = np.array([[1,0,0,x],
						   [0,1,0,0],
						   [0,0,1,0],
						   [0,0,0,1]])
	return traslacion

def matriz_traslacion_y(y):
	traslacion = np.array([[1,0,0,0],
						   [0,1,0,y],
						   [0,0,1,0],
						   [0,0,0,1]])
	return traslacion

def matriz_traslacion_z(z):
	traslacion = np.array([[1,0,0,0],
						   [0,1,0,0],
						   [0,0,1,z],
						   [0,0,0,1]])
	return traslacion

def configuracion_grafica():
	plt.title("MATRICES DE TRASLACION Y ROTACION\nJose Guadalupe Sanchez Velazquez 6° 6")
	ax.set_xlim(-15,15)
	ax.set_ylim(-15,15)
	ax.set_zlim(-10,10)
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_zlabel("z")
	ax.view_init(elev=25,azim=30)

def sistema_coordenadas(a,b,c,a_1,b_1,c_1):
	x = [a,a_1]
	y = [b,b_1]
	z = [c,c_1]
	ax.plot3D(x,[b,b],[c,c],color='red')
	ax.plot3D([a,a],y,[c,c],color='blue')
	ax.plot3D([b,a],[b,b],z,color='green')

def sistema_coordenadas_movil(matriz_rotacion):
	r_11 = matriz_rotacion[0,0]
	r_12 = matriz_rotacion[1,0]
	r_13 = matriz_rotacion[2,0]
	r_21 = matriz_rotacion[0,1]
	r_22 = matriz_rotacion[1,1]
	r_23 = matriz_rotacion[2,1]
	r_31 = matriz_rotacion[0,2]
	r_32 = matriz_rotacion[1,2]
	r_33 = matriz_rotacion[2,2]

	ax.plot3D([0,r_11],[0,r_22],[0,r_13], color='m')
	ax.plot3D([0,r_21],[0,r_22],[0,r_23], color='c')
	ax.plot3D([0,r_31],[0,r_32],[0,r_33], color='y')
	plt.draw()

def animacion_sistema_coordenadas(grados_x,grados_y,grados_z,gx,gy,gz):
	if grados_x>0:
		min=1
		max=grados_x+1
		step=1
	else:
		min=-1
		max=grados_x-1
		step = -1
	for i in range(min,max,step):
		ax.cla()#Limpia la gráfica
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25)# el metodo meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z
		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)# Grafico surface en 3D
		W = np.ones(len(Z))
		index = 0

		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
			traslacion = matriz_traslacion_x(i)	#Rotación en el eje x
			resultado = traslacion @ coordenadas_funcion #Aquí se hace la rotación del sólido, en el eje x
			X[index] = resultado[0]
			Y[index] = resultado[1]
			Z[index] = resultado[2]
			index+=1
		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(1e-9)
	
	if grados_y>0:
		min=1
		max=grados_y+1
		step=1
	else:
		min=-1
		max=grados_y-1
		step = -1

	for j in range(min,max,step):
		ax.cla()#Limpia la gráfica
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25)# el metodo meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z
		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)# Grafico surface en 3D
		W = np.ones(len(Z))
		index = 0

		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
			traslacion = matriz_traslacion_y(j)@matriz_traslacion_x(i)	#Rotación en el eje x
			resultado = traslacion @ coordenadas_funcion #Aquí se hace la rotación del sólido, en el eje x
			X[index] = resultado[0]
			Y[index] = resultado[1]
			Z[index] = resultado[2]
			index+=1
		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(1e-9)

	if grados_z>0:
		min=1
		max=grados_z+1
		step=1
	else:
		min=-1
		max=grados_z-1
		step = -1

	for k in range(min,max,step):
		ax.cla()#Limpia la gráfica
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25)# el metodo meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z
		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)# Grafico surface en 3D
		W = np.ones(len(Z))
		index = 0

		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
			traslacion = matriz_traslacion_z(k)@matriz_traslacion_y(j)@matriz_traslacion_x(i)	#Rotación en el eje x
			resultado = traslacion @ coordenadas_funcion #Aquí se hace la rotación del sólido, en el eje x
			X[index] = resultado[0]
			Y[index] = resultado[1]
			Z[index] = resultado[2]
			index+=1
		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(1e-9)

	if gx>0:
		min=1
		max=gx+1
		step=1
	else:
		min=-1
		max=gx-1
		step = -1

	for l in range(min,max,step):
		ax.cla()#Limpia la gráfica
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25)# el metodo meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z
		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)# Grafico surface en 3D
		W = np.ones(len(Z))
		index = 0

		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
			traslacion = matriz_rotacion_x(l)@matriz_traslacion_z(k)@matriz_traslacion_y(j)@matriz_traslacion_x(i)	#Rotación en el eje x
			resultado = traslacion @ coordenadas_funcion #Aquí se hace la rotación del sólido, en el eje x
			X[index] = resultado[0]
			Y[index] = resultado[1]
			Z[index] = resultado[2]
			index+=1
		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(1e-9)

	if gy>0:
		min=1
		max=gy+1
		step=1
	else:
		min=-1
		max=gy-1
		step = -1

	for m in range(min,max,step):
		ax.cla()#Limpia la gráfica
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25)# el metodo meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z
		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)# Grafico surface en 3D
		W = np.ones(len(Z))
		print(W)
		index = 0

		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
			traslacion = matriz_rotacion_y(m)@matriz_rotacion_x(l)@matriz_traslacion_z(k)@matriz_traslacion_y(j)@matriz_traslacion_x(i)	#Rotación en el eje x
			resultado = traslacion @ coordenadas_funcion #Aquí se hace la rotación del sólido, en el eje x
			X[index] = resultado[0]
			Y[index] = resultado[1]
			Z[index] = resultado[2]
			index+=1
		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(1e-9)

	if gz>0:
		min=1
		max=gz+1
		step=1
	else:
		min=-1
		max=gz-1
		step = -1

	for n in range(min,max,step):
		ax.cla()#Limpia la gráfica
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25)# el metodo meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z
		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)# Grafico surface en 3D
		W = np.ones(len(Z))
		print(W)
		index = 0

		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
			traslacion = matriz_rotacion_z(n)@matriz_rotacion_y(m)@matriz_rotacion_x(l)@matriz_traslacion_z(k)@matriz_traslacion_y(j)@matriz_traslacion_x(i)	#Rotación en el eje x
			resultado = traslacion @ coordenadas_funcion #Aquí se hace la rotación del sólido, en el eje x
			X[index] = resultado[0]
			Y[index] = resultado[1]
			Z[index] = resultado[2]
			index+=1
		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(1e-9)


animacion_sistema_coordenadas(-5,-10,-15,-90,1,1)
plt.show()