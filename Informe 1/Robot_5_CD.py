# Universidad Autónoma Chapingo
# Cinemática de robots 
# Jym Emmanuel Cocotle Lara
# 1710451-3
# 7° 7

# Importamos las librerías a ocupar
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
from matplotlib import cm
from matplotlib.widgets import Slider


#CONFIGURACION DE LOS PLOTS
fig, ax = plt.subplots()
plt.subplots_adjust(left = 0, bottom = 0.3, right= 0.74, top = 1)
ax = plt.axes(projection = "3d")

# MATRICES DE ROTACIÓN
# Creamos una función en la cual establecemos la matriz de rotación en x
def matriz_rotacion_x(grados):
	rad = grados/180*np.pi 
	rotacion = np.array([[1    ,0                     , 0,0],
					     [0    ,np.cos(rad), -np.sin(rad),0],
			    		 [0    ,np.sin(rad), np.cos(rad), 0],
						 [0	   ,	      0,			0,1]])
	return rotacion

# Creamos una función en la cual establecemos la matriz de rotación en y
def matriz_rotacion_y(grados):
	rad = grados/180*np.pi 
	rotacion = np.array([[np.cos(rad), 0, -np.sin(rad),0],
						 [0,           1,            0,0],
						 [np.sin(rad), 0,  np.cos(rad),0],
						 [ 0,		0,		0,			1]])
	return rotacion

# Creamos una función en la cual establecemos la matriz de rotación en z
def matriz_rotacion_z(grados):
	rad = grados/180*np.pi
	rotacion = np.array([[np.cos(rad),-np.sin(rad),0,0],
						[np.sin(rad), np.cos(rad),0,0],
						[		   0,           0,1,0],
						[0,			0,		0,		1]])
	return rotacion

#MATRICES DE TRASLACIÓN
# Creamos una función en la cual establecemos la matriz de traslación en x
def matriz_traslacion_x(x):
	traslacion = np.array([[1,0,0,x],
						  [0,1,0,0],
						  [0,0,1,0],
						  [0,0,0,1]])
	return traslacion

# Creamos una función en la cual establecemos la matriz de traslación en y
def matriz_traslacion_y(y):
	traslacion = np.array([[1,0,0,0],
						   [0,1,0,y],
						   [0,0,1,0],
						   [0,0,0,1]])
	return traslacion

# Creamos una función en la cual establecemos la matriz de traslación en z
def matriz_traslacion_z(z):
	traslacion = np.array([[1,0,0,0],
						  [0,1,0,0],
						  [0,0,1,z],
						  [0,0,0,1]])
	return traslacion

# Creamos una función en la cual establecemos las configuraciones de la gráfica
def configuracion_grafica():
	plt.title("Robot_5 RRR", x = 0, y = 27)
	ax.set_xlim(-10,10)
	ax.set_xlabel("x")
	ax.set_ylim(-10,10)
	ax.set_ylabel("y")
	ax.set_zlim(-10,10)
	ax.set_zlabel("z")
	ax.view_init(elev=25,azim=30)


	#SISTEMA MOVIL
def sistema_cordenadas_movil(matriz_rotacionz):
	# Definimos los parámetros del sistema de coordenadas
	r_11 = matriz_rotacionz[0,0]
	r_12 = matriz_rotacionz[1,0]
	r_13 = matriz_rotacionz[2,0]
	r_21 = matriz_rotacionz[0,1]
	r_22 = matriz_rotacionz[1,1]
	r_23 = matriz_rotacionz[2,1]
	r_31 = matriz_rotacionz[0,2]
	r_32 = matriz_rotacionz[1,2]
	r_33 = matriz_rotacionz[2,2]

	dx = matriz_rotacionz[0,3]
	dy = matriz_rotacionz[1,3]
	dz = matriz_rotacionz[2,3]

	ax.plot3D([dx,dx+r_11],[dy,dy+r_12],[dz,dz+r_13], color = "m")
	ax.plot3D([dx,dx+r_21],[dy,dy+r_22],[dz,dz+r_23], color = "c")
	ax.plot3D([dx,dx+ r_31],[dy,dy+r_32],[dz,dz+r_33], color = "green")

# Denavit Hatemberg
# Creamos una función para usar los parametros de Denavit Hatemberg
def dh(theta_i,d_i,a_i,alpha_i):
	MT = A1 = matriz_rotacion_z(theta_i)@matriz_traslacion_z(d_i)@matriz_traslacion_x(a_i)@matriz_rotacion_x(alpha_i)
	return MT

# Creamos una función la cual contenga los parametros para el robot que ocuparemos
def Robot_CSV(theta1,d1,a1,alpha1,theta2,d2,a2,alpha2,theta3,d3,a3,alpha3):
	# Establecemos la posición de los eslabones y establecemos su sentido de giro según sea el caso
	A0 = np.eye(4)
	A_0_1 = dh(theta1,d1,a1,alpha1)
	A_1_2= dh(theta2,d2,a2,alpha2)
	A_1_3= dh(theta3,d3,a3,alpha3)

	A_0_2 = A_0_1@A_1_2
	A_0_3 = A_0_2@A_1_3


	sistema_cordenadas_movil(A0)  # Colocamos un sitema de coordenadas en el punto A0
	sistema_cordenadas_movil(A_0_1)  # Colocamos un sitema de coordenadas en el punto 0A1
	sistema_cordenadas_movil(A_0_2)  # Colocamos un sitema de coordenadas en el punto 0A2
	sistema_cordenadas_movil(A_0_3)  # Colocamos un sitema de coordenadas en el punto 0A3

	ax.plot3D([A0[0,3],A_0_1[0,3]],[A0[1,3],A_0_1[1,3]],[A0[2,3],A_0_1[2,3]], color="red")
	ax.plot3D([A_0_1[0,3],A_0_2[0,3]],[A_0_1[1,3],A_0_2[1,3]],[A_0_1[2,3],A_0_2[2,3]], color="blue")
	ax.plot3D([A_0_2[0,3],A_0_3[0,3]],[A_0_2[1,3],A_0_3[1,3]],[A_0_2[2,3],A_0_3[2,3]], color="green")

	return A_0_3


#DIBUJO DE ROBOT CON SLIDERS
def actualizacion_juntas(val):
		
		ax.cla()
		configuracion_grafica()
		#DECLARAMOS QUE LOS VALORES DE LOS ANGULOS o distancias TOMEN LOS VALORES DE LAS TRACKBARS
		theta_1 = sld_ang_1.val
		theta_2 = sld_ang_2.val
		theta_3 = sld_ang_3.val
		
		#PARAMETROS PARA PASARLE AL ROBOT
		#theta1,d1,a1,alpha1,theta2,d2,a2,alpha2,theta3,d3,a3,alpha3
		Matriz_TH=Robot_CSV(theta_1,2,0,90,theta_2,0,3,0,theta_3,0,3,90)
		x=0
		y=0
		while x<4:
			while y<4:
				tabla._cells[(x,y)]._text.set_text(np.round(Matriz_TH[x,y],3))
				y=y+1
			y=0
			x=x+1

#Configuración de los sliders
ax1 = plt.axes([0.2,0.20,0.65,0.03])
ax2 = plt.axes([0.2,0.15,0.65,0.03])
ax3 = plt.axes([0.2,0.1,0.65,0.03])
ax4 = plt.axes([0.2,0.05,0.65,0.03])

axT = plt.axes([0.63,0.3,0.07,0.03])

# Definimos el nombre de los sliders así como sus límites y su valor inicial
sld_ang_1 = Slider(ax1, r'$\theta_1$',-180,180,valinit = 90)
sld_ang_2 = Slider(ax2, r'$\theta_2$',-180,180,valinit = 90)
sld_ang_3 = Slider(ax3, r'$\theta_3$',-180,180,valinit = 0)

# Llamamos a la función del brazo del robot para que se muestre con sus valores iniciales
configuracion_grafica()
#theta1,d1,a1,alpha1,theta2,d2,a2,alpha2,theta3,d3,a3,alpha3
Matriz_TH=Robot_CSV(90,2,0,90,90,0,3,0,0,0,3,90)
tabla=plt.table(cellText=np.round(Matriz_TH,3),bbox=[0,0,5,5],loc='center')
tabla.auto_set_font_size(False)
tabla.set_fontsize(8)
axT.axis('off')

# Llammamos a la funcion de actualización de juntas en base a los valores de los sliders
configuracion_grafica()
sld_ang_1.on_changed(actualizacion_juntas)
sld_ang_2.on_changed(actualizacion_juntas)
sld_ang_3.on_changed(actualizacion_juntas)


plt.show()
