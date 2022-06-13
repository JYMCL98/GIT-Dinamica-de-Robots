# Robot IRB 2400

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(left = 0, bottom = 0.3, right =1, top = 1)
ax = plt.axes(projection = "3d")

# Función para rotar en el eje x
def matriz_rotacion_x(grados):
	rad = grados/180*np.pi
	#Matriz de rotación
	rotacion=np.array([[1,0,0,0],
					   [0,np.cos(rad),-np.sin(rad),0],
					   [0,np.sin(rad),np.cos(rad),0],
					   [0,0,0,1]])
	return rotacion
# Función para rotar en el eje z
def matriz_rotacion_z(grados):
	rad = grados/180*np.pi
	#Matriz de rotacuón
	rotacion=np.array([[np.cos(rad),-np.sin(rad),0,0],
					   [np.sin(rad),np.cos(rad),0,0],
					   [0,0,1,0],
					   [0,0,0,1]])
	return rotacion

# Función para trasladar en el eje x
def matriz_traslacion_x(x):
	traslacion = np.array([[1,0,0,x],
						   [0,1,0,0],
						   [0,0,1,0],	   
						   [0,0,0,1]])
	return traslacion

# Función para trasladar en el eje z
def matriz_traslacion_z(z):
	traslacion = np.array([[1,0,0,0],
						   [0,1,0,0],
						   [0,0,1,z],	   
						   [0,0,0,1]])
	return traslacion

# Función para la configuración gráfica
def configuracion_grafica():
	# Título del gráfico
	plt.title("Robot IRB 2400", x = 0.00, y = 30)
	# Límites del gráfico
	ax.set_xlim(-3,3)
	ax.set_ylim(-3,3)
	ax.set_zlim(0,3)
	# Estiquetas para identificar los ejes
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_zlabel("z")
	# Vista

# Función para la operación de Denavit-Hartenberg
def DH(theta_i, di, ai, alpha_i):
	MT = matriz_rotacion_z(theta_i)@matriz_traslacion_z(di)@matriz_traslacion_x(ai)@matriz_rotacion_x(alpha_i)
	return MT

# Matrices de transformación homogénea
def irb(theta_1, d1, a1, alpha_1, theta_2, d2, a2, alpha_2,theta_3, d3, a3, alpha_3,theta_4, d4, a4, alpha_4,
			   theta_5, d5, a5, alpha_5,theta_6, d6, a6, alpha_6):
	
	
	A0 = np.eye(4)
	_0A1 = DH(theta_1, d1, a1, alpha_1)
	_1A2 = DH(theta_2, d2, a2, alpha_2)
	_2A3 = DH(theta_3, d3, a3, alpha_3)
	_3A4 = DH(theta_4, d4, a4, alpha_4)
	_4A5 = DH(theta_5, d5, a5, alpha_5)
	_5A6 = DH(theta_6, d6, a6, alpha_6)
	_0A2 = _0A1@_1A2
	_0A3 = _0A2@_2A3
	_0A4 = _0A3@_3A4
	_0A5 = _0A4@_4A5
	_0A6 = _0A5@_5A6

	# Se deibujan los eslabones
	ax.plot3D([A0[0,3],_0A1[0,3]],[A0[1,3],_0A1[1,3]],[A0[2,3],_0A1[2,3]], color = 'red')
	ax.plot3D([_0A1[0,3],_0A2[0,3]],[_0A1[1,3],_0A2[1,3]],[_0A1[2,3],_0A2[2,3]], color = 'green')
	ax.plot3D([_0A2[0,3],_0A3[0,3]],[_0A2[1,3],_0A3[1,3]],[_0A2[2,3],_0A3[2,3]], color = 'black')
	ax.plot3D([_0A3[0,3],_0A4[0,3]],[_0A3[1,3],_0A4[1,3]],[_0A3[2,3],_0A4[2,3]], color = 'yellow')
	ax.plot3D([_0A4[0,3],_0A5[0,3]],[_0A4[1,3],_0A5[1,3]],[_0A4[2,3],_0A5[2,3]], color = 'c')
	ax.plot3D([_0A5[0,3],_0A6[0,3]],[_0A5[1,3],_0A6[1,3]],[_0A5[2,3],_0A6[2,3]], color = 'm')

# Se actualizan las juntas cada vez que se modifica el valor de un ángulo con el slider
def actualizacion_juntas(val):
		ax.cla()
		configuracion_grafica()
		theta_1 = sld_ang_1.val
		theta_2 = sld_ang_2.val
		theta_3 = sld_ang_3.val
		theta_4 = sld_ang_4.val
		theta_5 = sld_ang_5.val
		theta_6 = sld_ang_6.val

		# Parámetros de Denavit-Hartenberg obtenidos en la tabla
		irb(theta_1, 0.2, 0, -90,theta_2, 0, 2, 0, theta_3, 0, 0, 90, theta_4, 1.4, 0, -90, 
			theta_5, 0, 0, 90, theta_6, 0.4, 0, 0)
		plt.draw()
		plt.pause(1e-3)

# Deiseño de los sliders
ax1 = plt.axes([0.2,0.20,0.65,0.026])
ax2 = plt.axes([0.2,0.18,0.65,0.026])
ax3 = plt.axes([0.2,0.16,0.65,0.026])
ax4 = plt.axes([0.2,0.14,0.65,0.026])
ax5 = plt.axes([0.2,0.12,0.65,0.026])
ax6 = plt.axes([0.2,0.10,0.65,0.026])

# Creación de los sliders
sld_ang_1 = Slider(ax1, "Theta 1",-180,180,valinit = 45)
sld_ang_2 = Slider(ax2, "Theta 2",-180,180,valinit = 0)
sld_ang_3 = Slider(ax3, "Theta 3",-180,180,valinit = 0)
sld_ang_4 = Slider(ax4, "Theta 4",-180,180,valinit = 0)
sld_ang_5 = Slider(ax5, "Theta 5",-180,180,valinit = 0)
sld_ang_6 = Slider(ax6, "Theta 6",-180,180,valinit = 0)

# Cada vez que se mueve un slider se actualizan las juntas
sld_ang_1.on_changed(actualizacion_juntas)
sld_ang_2.on_changed(actualizacion_juntas)
sld_ang_3.on_changed(actualizacion_juntas)
sld_ang_4.on_changed(actualizacion_juntas)
sld_ang_5.on_changed(actualizacion_juntas)
sld_ang_6.on_changed(actualizacion_juntas)

configuracion_grafica()
#irb(45,0,0,0,0,0)
plt.show()
