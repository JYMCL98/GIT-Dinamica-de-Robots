# UNIVERSIDAD AUTÓNOMA CHAPINGO
# DEPARTAMENTO DE INGENIERÍA MECÁNICA AGRÍCOLA
# INGENIERÍA MECATRÓNICA AGRÍCOLA
# CINEMÁTICA DE ROBOTS
# ROTACIÓN Y TRASLACIÓN DE UN SÓLIDO EN X, Y, Z
# LUIS ANGEL SANCHEZ RODRIGUEZ 
# 6°7

# Importamos las librerías para el programa
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm

# Graficación en 3d
fig, ax = plt.subplots()
ax = plt.axes(projection = "3d")

######################  FUNCIONES DE MATRICES DE TRASLACIÓN   #########################################
def matriz_traslacion_x(x):
	traslacion_x = np.array([[1,0,0,x],
						   [0,1,0,0],
						   [0,0,1,0],	   
						   [0,0,0,1]])
	return traslacion_x

def matriz_traslacion_y(y):
	traslacion_y = np.array([[1,0,0,0],
						   [0,1,0,y],
						   [0,0,1,0],	   
						   [0,0,0,1]])
	return traslacion_y

def matriz_traslacion_z(z):
	traslacion_z = np.array([[1,0,0,0],
						   [0,1,0,0],
						   [0,0,1,z],	   
						   [0,0,0,1]])
	return traslacion_z




######################  FUNCIONES DE MATRICES DE ROTACIÓN   #########################################

# X
def matriz_rotacion_x(grados_x): #Definimos la función de rotación en x
	rad = grados_x/180*np.pi # Conversión a grados
	matriz_rotacion_x = np.array([[1, 0, 0,0], #Matriz de rotación primera fila
						  [0,  np.cos(rad), -np.sin(rad),0], #Matriz de rotación segunda fila
						  [0,np.sin(rad),np.cos(rad),0], #Matriz de rotación terca fila
						  [0,0,0,1]]) 

	return matriz_rotacion_x #Devuelvo la linea en x

# Y
def matriz_rotacion_y(grados_y): #Definimos la función de rotación en y
	rad = grados_y/180*np.pi # Conversión a grados
	matriz_rotacion_y = np.array([[np.cos(rad), 0, -np.sin(rad),0], #Matriz de rotación primera fila
						  [0,  1, 0,0], #Matriz de rotación segunda fila
						  [np.sin(rad), 0, np.cos(rad),0], #Matriz de rotación terca fila
						  [0,0,0,1]]) 

	return matriz_rotacion_y #Devuelvo la linea en y

# Z
def matriz_rotacion_z(grados_z):
	rad = grados_z/180*np.pi
	rotacion_z = np.array([[np.cos(rad),-np.sin(rad),0,0],
							[np.sin(rad),np.cos(rad),0,0],
								[0,0,1,0],
								[0,0,0,1]])
	return rotacion_z



# Configutación de la gráfica
def configuracion_grafica():
	plt.title("Matrices de traslación y rotación")
	ax.set_xlim(-20,20)
	ax.set_ylim(-20,20)
	ax.set_zlim(-20,20)

	ax.set_xlabel("x(t)")
	ax.set_ylabel("y(t)")
	ax.set_zlabel("z(t)")
	ax.view_init(elev = 25, azim = 30) # 



# Sistema de coordenadas móvil para la matriz de rotación
def sistema_coordenadas_movil(matriz_rotacion):
	r_11 = matriz_rotacion[0,0] # Columna 0, Fila 0
	r_12 = matriz_rotacion[1,0] # Columna 1, Fila 0
	r_13 = matriz_rotacion[2,0] # Columna 2, Fila 0
	r_21 = matriz_rotacion[0,1] # Columna 0, Fila 1
	r_22 = matriz_rotacion[1,1] # Columna 1, Fila 1
	r_23 = matriz_rotacion[2,1] # Columna 2, Fila 1
	r_31 = matriz_rotacion[0,2] # Columna 0, Fila 2
	r_32 = matriz_rotacion[1,2] # Columna 1, Fila 2
	r_33 = matriz_rotacion[2,2] # Columna 2, Fila 2

	# Sistema que va a mover
	ax.plot3D([0,r_11],[0,r_12],[0,r_13],color="c") # X 
	ax.plot3D([0,r_21],[0,r_22],[0,r_23],color="m") # Y
	ax.plot3D([0,r_31],[0,r_32],[0,r_33],color="y") # Z



def animacion_coordenadas(dx,dy,dz,grados_x,grados_y,grados_z):
	# Traslade en x,y,z
	# Rote grados x,y,z

	#########################   TRASLACIÓN   ####################
	# X
	if dx > 0:
		min = 1
		max = dx+1
		step = 1
	else:
		min = -1#dx-1 
		max = gx-1 #0
		step = -1

	for i in range(min, max, step):
		ax.cla() # Limpia la gráfica
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25) # el método meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z
		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R) # Gráfico surface en 3D
		W = np.ones(len(Z))

		index = 0
		for dato in zip(X,Y,Z,W): # recorre arrays al mismo tiempo
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2], dato[3]], dtype = object)
			traslacion_x = matriz_traslacion_x(i)	# Traslación en el eje x
			resultado_x = traslacion_x @ coordenadas_funcion # Aquí se hace la rotación del sólido, en el eje x
			X[index] = resultado_x[0]
			Y[index] = resultado_x[1]
			Z[index] = resultado_x[2]
			index+=1
		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(1e-9)

	# Y
	if dy > 0:
		min = 1
		max = dy+1
		step = 1
	else:
		min = -1 #dy-1
		max = gy-1 #0
		step = -1

	for j in range(min, max, step):
		ax.cla() 
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25) # el método meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z
		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)# Gráfico surface en 3D
		W = np.ones(len(Z))

		index = 0
		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2], dato[3]], dtype = object)
			traslacion_y = matriz_traslacion_y(j) @ matriz_traslacion_x(i)	# Traslación en el eje y
			resultado_y = traslacion_y @ coordenadas_funcion # Aquí se hace la rotación del sólido, en el eje y
			X[index] = resultado_y[0]
			Y[index] = resultado_y[1]
			Z[index] = resultado_y[2]
			index+=1

		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(1e-9)

	
	# Z
	if dz > 0:
		min = 1
		max = dz+1
		step = 1
	else:
		min = -1 #dz-1
		max = dz-1 #0
		step = -1

	for k in range(min, max, step):
		ax.cla()
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25) # el método meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z
		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)# Gráfico surface en 3D
		W = np.ones(len(Z))

		index = 0
		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2], dato[3]], dtype = object)
			# traslacion_z = matriz_traslacion_z(k) @ matriz_traslacion_y(j) @ matriz_traslacion_x(i)	# Traslación en el eje z
			traslacion_z = matriz_traslacion_z(k) @ matriz_traslacion_y(j)	# Traslación en el eje z
			traslacion_z = traslacion_z @ matriz_traslacion_x(i)
			resultado_z = traslacion_z @ coordenadas_funcion # Aquí se hace la rotación del sólido, en el eje z
			X[index] = resultado_z[0]
			Y[index] = resultado_z[1]
			Z[index] = resultado_z[2]
			index+=1

		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(1e-9)


		###################   ROTACIÓN    #############
		# Rotación en X

	# X
	if grados_x > 0:
		min = 1
		max = grados_x+1
		step = 1
	else:
		min = grados_x-1
		max = 0
		step = -1

	for l in range(min, max, step):
		ax.cla() # Limpia la gráfica
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25) # el método meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z
		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R) # Grafico surface en 3D
		W = np.ones(len(Z))

		index = 0
		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
			rotacion_x = matriz_rotacion_x(l)@matriz_traslacion_z(k)@matriz_traslacion_y(j)@matriz_traslacion_x(i) 	#Rotación en el eje x
			resultado_x = rotacion_x @ coordenadas_funcion #Aquí se hace la rotación del sólido, en el eje x
			X[index] = resultado_x[0]
			Y[index] = resultado_x[1]
			Z[index] = resultado_x[2]
			index+=1
		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(0.001)

	# Y
	if grados_y > 0:
		min = 1
		max = grados_y+1
		step = 1
	else:
		min = grados_y-1
		max = 0
		step = -1
	for m in range(min,max,step):
		ax.cla()
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25)# el método meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z

		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)# Grafico surface en 3D
		W = np.ones(len(Z))

		index = 0
		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
			rotacion_y = matriz_rotacion_y(m)@matriz_rotacion_x(l)	#Rotación en el eje x
			resultado_y = rotacion_y @ coordenadas_funcion #Aquí se hace la rotación del sólido, en el eje x
			X[index] = resultado_y[0]
			Y[index] = resultado_y[1]
			Z[index] = resultado_y[2]
			index+=1
		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(0.001)

	# Z
	if grados_z > 0:
		min = 1
		max = grados_z+1
		step = 1
	else:
		min = grados_z-1
		max = 0
		step = -1
	for n in range(min,max,step):
		ax.cla() 
		configuracion_grafica()
		
		X = np.arange(-5, 5, 0.25)
		Y = np.arange(-5, 5, 0.25)# el método meshgrid devuelve una matriz de coordenadas
		# a partir de vectores de coordendas, que usamos para
		# los datos del eje Z

		X, Y = np.meshgrid(X, Y)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)# Grafico surface en 3D
		W = np.ones(len(Z))

		index = 0
		for dato in zip(X,Y,Z,W):
			coordenadas_funcion = np.array([dato[0],dato[1],dato[2],dato[3]],dtype=object)
			rotacion_z = matriz_rotacion_z(n)@matriz_rotacion_y(m)@matriz_rotacion_x(l)	#Rotación en el eje x
			resultado_z = rotacion_z @ coordenadas_funcion #Aquí se hace la rotación del sólido, en el eje x
			X[index] = resultado_z[0]
			Y[index] = resultado_z[1]
			Z[index] = resultado_z[2]
			index+=1
		surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		plt.draw()
		plt.pause(0.001)


animacion_coordenadas(10,10,10,10,10,10)
plt.show()