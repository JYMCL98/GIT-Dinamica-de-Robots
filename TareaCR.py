import numpy as np # Importamos la librería numpy
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

#Declaramos los datos de la función
z = np.linspace(0,30,100) #Genera una línea del 0 al 30
x = np.sin(z) #
y = np.cos(z) #


#rotar en z,x,y
#tkinter
# tkinter y matplotlib

#Definimos la función de animación
def rotacion_z(grados_z,datos_z,line_z):
	rad = grados_z/180*np.pi
	matriz_rotacion_z = np.array([[np.cos(rad), -np.sin(rad), 0],
						  [np.sin(rad),  np.cos(rad), 0],
						  [          0,            0, 1]])

	datos_z = matriz_rotacion_z @ datos_z #multiplicación de matrices
	#Actualizo la posición de los datos de la línea
	line_z.set_data(datos_z[0],datos_z[1])#x,y
	line_z.set_3d_properties(datos_z[2])#z
	return line_z

#Declaramos la figura
fig = plt.figure()
ax = Axes3D(fig)

#Graficación en 3d
datos_z = np.array([x,y,z])
grados_z = 360
line_z = plt.plot(datos_z[0],datos_z[1],datos_z[2])[0] #Toma los primeros datos de la línea 0

#Propiedades de los ejes
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(0,30)

ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")
ax.set_zlabel("z(t)")

line_ani_z = animation.FuncAnimation(fig,rotacion_z,frames=grados_z,
												fargs=(datos_z,line_z),interval=50,
												repeat=False,blit=False)
plt.show()



########################################################################################
#Definimos la función de animación en x
def rotacion_x(grados_x,datos_x,line_x):
	rad = grados_x/180*np.pi
	matriz_rotacion_x = np.array([[1, 0, 0],
						  [0,  np.cos(rad), -np.sin(rad)],
						  [0,np.sin(rad),np.cos(rad)]])

	datos_x = matriz_rotacion_x @ datos_x #multiplicación de matrices
	#Actualizo la posición de los datos de la línea
	line_x.set_data(datos_x[0],datos_x[1])#x,y
	line_x.set_3d_properties(datos_x[2])#z
	return line_x


#Declaramos la figura
fig_2 = plt.figure()
ax = Axes3D(fig_2)

#Graficación en 3d
datos_x = np.array([x,y,z])
grados_x = 360
line_x = plt.plot(datos_x[0],datos_x[1],datos_x[2])[0] #Toma los primeros datos de la línea 0

#Propiedades de los ejes
ax.set_xlim(-10,10)
ax.set_ylim(-20,20)
ax.set_zlim(0,30)

ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")
ax.set_zlabel("z(t)")

line_ani_x = animation.FuncAnimation(fig_2,rotacion_x,frames=grados_x,
												fargs=(datos_x,line_x),interval=50,
												repeat=True,blit=False)
plt.show()

#####################################################################################
#Definimos la función de animación en y
def rotacion_y(grados_y,datos_y,line_y):
	rad = grados_y/180*np.pi
	matriz_rotacion_y = np.array([[np.cos(rad), 0, -np.sin(rad)],
						  [0,  1, 0],
						  [np.sin(rad), 0, np.cos(rad)]])

	datos_y = matriz_rotacion_y @ datos_y #multiplicación de matrices
	#Actualizo la posición de los datos de la línea
	line_y.set_data(datos_y[0],datos_y[1])#x,y
	line_y.set_3d_properties(datos_y[2])#z
	return line_y


#Declaramos la figura
fig_3 = plt.figure()
ax = Axes3D(fig_3)

#Graficación en 3d
datos_y = np.array([x,y,z])
grados_y = 360
line_y = plt.plot(datos_y[0],datos_y[1],datos_y[2])[0] #Toma los primeros datos de la línea 0

#Propiedades de los ejes
ax.set_xlim(-10,10)
ax.set_ylim(-20,20)
ax.set_zlim(0,30)

ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")
ax.set_zlabel("z(t)")

line_ani_y = animation.FuncAnimation(fig_3,rotacion_y,frames=grados_y,
												fargs=(datos_y,line_y),interval=50,
												repeat=True,blit=False)
plt.show()
