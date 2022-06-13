# Universidad Autónoma Chapingo
# Cinemática de robots 
# Jym Emmanuel Cocotle Lara
# 1710451-3
# 7° 7

# Importamos las librerías para el programa
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
from matplotlib import cm
from matplotlib.widgets import Slider
import math

# Graficación en 3d
fig, ax = plt.subplots() # Creamos una figura y sus ejes
plt.subplots_adjust(left = 0, bottom = 0.3, right =1, top = 1) # Ubicamos la figura
ax = plt.axes(projection = "3d") # Establecemos los ejes como 3 dimensiones

# MATRICES DE ROTACIÓN
# Creamos una función en la cual establecemos la matriz de rotación en x
def matriz_rotacion_x(grados):
	rad = grados/180*np.pi 
	rotacion_x = np.array([[1    ,0                     , 0,0],
					     [0    ,np.cos(rad), -np.sin(rad),0],
			    		 [0    ,np.sin(rad), np.cos(rad), 0],
						 [0	   ,	      0,			0,1]])
	return rotacion_x

# Creamos una función en la cual establecemos la matriz de rotación en y
def matriz_rotacion_y(grados):
	rad = grados/180*np.pi 
	rotacion_y = np.array([[np.cos(rad), 0, -np.sin(rad),0],
						 [0,           1,            0,0],
						 [np.sin(rad), 0,  np.cos(rad),0],
						 [ 0,		0,		0,			1]])
	return rotacion_y

# Creamos una función en la cual establecemos la matriz de rotación en z
def matriz_rotacion_z(grados):
	rad = grados/180*np.pi
	rotacion_z = np.array([[np.cos(rad),-np.sin(rad),0,0],
						[np.sin(rad), np.cos(rad),0,0],
						[		   0,           0,1,0],
						[0,			0,		0,		1]])
	return rotacion_z

#MATRICES DE TRASLACIÓN
# Creamos una función en la cual establecemos la matriz de traslación en x
def matriz_traslacion_x(x):
	traslacion_x = np.array([[1,0,0,x],
						  [0,1,0,0],
						  [0,0,1,0],
						  [0,0,0,1]])
	return traslacion_x

# Creamos una función en la cual establecemos la matriz de traslación en y
def matriz_traslacion_y(y):
	traslacion_y = np.array([[1,0,0,0],
						   [0,1,0,y],
						   [0,0,1,0],
						   [0,0,0,1]])
	return traslacion_y

# Creamos una función en la cual establecemos la matriz de traslación en z
def matriz_traslacion_z(z):
	traslacion_z = np.array([[1,0,0,0],
						  [0,1,0,0],
						  [0,0,1,z],
						  [0,0,0,1]])
	return traslacion_z

def cinematica_inversa(x,y,z,d1,d4):
	theta_1 = math.atan2(y,x)
	d2 = z
	d3 = math.cos(theta_1)*x + math.sin(theta_1)*y - d4
	theta_1 = round((theta_1*180/np.pi),1)
	return theta_1, d2, d3

# Configutación de la gráfica
def configuracion_grafica(): # función de configuración de la gráfica
	plt.title("Robot_1 RPPR",x=-0.03, y=27) # Título de la gráfica
	ax.set_xlim(-3,3)
	ax.set_ylim(-3,3)
	ax.set_zlim(0,3) 

	ax.set_xlabel("x(t)") # Nombre del eje x
	ax.set_ylabel("y(t)") # Nombre del eje y
	ax.set_zlabel("z(t)") # Nombre del eje z

def sistema_coordenadas(a,b,c,a_f,b_f,c_f):
	x = [a,a_f] 
	y = [b,b_f]
	z = [c,c_f]

	ax.plot3D(x,[b,b],[c,c],color="red") # X
	ax.plot3D([a,a],y,[c,c],color="blue") # Y
	ax.plot3D([a,a],[b,b],z,color="green") # Z

def dh(theta_i,d_i,a_i,alpha_i):
	MT = matriz_rotacion_z(theta_i)@matriz_traslacion_z(d_i)@matriz_traslacion_x(a_i)@matriz_rotacion_x(alpha_i)
	print(MT)
	return MT

def robot_RR(theta_1, d1, a1, alpha_1, 
		 	 theta_2, d2, a2, alpha_2,
			 theta_3, d3, a3, alpha_3,
			 theta_4, d4, a4, alpha_4):
	

	A0 = np.eye(4)
	A_0_1 = dh(theta_1, d1, a1, alpha_1)
	A_1_2 = dh(theta_2, d2, a2, alpha_2)
	A_2_3 = dh(theta_3, d3, a3, alpha_3)
	A_3_4 = dh(theta_4, d4, a4, alpha_4)


	A_0_2 = A_0_1@A_1_2
	A_0_3 = A_0_2@A_2_3
	A_0_4 = A_0_3@A_3_4

	# Se deibujan los eslabones
	ax.plot3D([A0[0,3],A_0_1[0,3]],[A0[1,3],A_0_1[1,3]],[A0[2,3],A_0_1[2,3]], color = 'red')
	ax.plot3D([A_0_1[0,3],A_0_2[0,3]],[A_0_1[1,3],A_0_2[1,3]],[A_0_1[2,3],A_0_2[2,3]], color = 'green')
	ax.plot3D([A_0_2[0,3],A_0_3[0,3]],[A_0_2[1,3],A_0_3[1,3]],[A_0_2[2,3],A_0_3[2,3]], color = 'red')
	ax.plot3D([A_0_3[0,3],A_0_4[0,3]],[A_0_3[1,3],A_0_4[1,3]],[A_0_3[2,3],A_0_4[2,3]], color = 'green')

def actualizacion_juntas2(val):
	
	ax.cla() # Limpia la gráfica
	configuracion_grafica()
	x = sld_angulo_1.val
	y = sld_angulo_2.val
	z = sld_angulo_3.val
	theta_1,d2,d3 = cinematica_inversa(x,y,z,1,1)
	Matriz_TH = robot_RR(theta_1,1,0,0,90,d2,0,90,0,d3,0,0,0,1,0,0)
	
ax1 = plt.axes([0.2,0.15,0.65,0.03])
ax2 = plt.axes([0.2,0.1,0.65,0.03])
ax3 = plt.axes([0.2,0.05,0.65,0.03])	

sld_angulo_1 = Slider(ax1,r"$X$",-3,3,valinit=1)	
sld_angulo_2 = Slider(ax2,r"$Y$",-3,3,valinit=1)
sld_angulo_3 = Slider(ax3,r"$z$",0,3,valinit=1)	


configuracion_grafica()
Matriz_TH = robot_RR(0,1,0,0,90,1,0,90,0,1,0,0,0,1,0,0)

sld_angulo_1.on_changed(actualizacion_juntas2)
sld_angulo_2.on_changed(actualizacion_juntas2)
sld_angulo_3.on_changed(actualizacion_juntas2)

plt.show()