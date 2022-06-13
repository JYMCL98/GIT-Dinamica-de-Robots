# UNIVERSIDAD AUTÓNOMA CHAPINGO
# DEPARTAMENTO DE INGENIERÍA MECÁNICA AGRÍCOLA
# INGENIERÍA MECATRÓNICA AGRÍCOLA
# DINÁMICA Y CONTROL DE ROBOTS
# ROBOT RR 2 GDL con sliders
# LUIS ANGEL SANCHEZ RODRIGUEZ 
# 7°7

# Importamos las librerías para el programa
import numpy as np #Importamos la librería numpy como np para vectores y matrices
import matplotlib.pyplot as plt # Importamos matplotlib como plt para graficar
from mpl_toolkits import mplot3d # Importamos mplot3d desde mplt_toolkits subpaquete de la librería de graficación para 3D
from matplotlib import cm # Importamos cm desde matplotlib subpaquete para la graficación
from matplotlib.widgets import Slider # Subpaquete para agregar las barras de control del robot
import math

# Graficación en 3d
fig, ax = plt.subplots() # Creamos una figura y sus ejes
plt.subplots_adjust(left = 0, bottom = 0.3, right =1, top = 1) # Ubicamos la figura
ax = plt.axes(projection = "3d") # Establecemos los ejes como 3 dimensiones


######################  FUNCIONES DE MATRICES DE TRASLACIÓN   #########################################

# X
def matriz_traslacion_x(x): # Definimos la matriz de traslación en x
	traslacion_x = np.array([[1,0,0,x], # Primera fila de la matriz de traslación
						   [0,1,0,0], # Segunda fila de la matriz de traslación
						   [0,0,1,0], # Tercera fila de la matriz de traslación	   
						   [0,0,0,1]]) # Cuarta fila de la matriz de traslación
	return traslacion_x # Devolvemos la matriz de traslación en x

# Y
def matriz_traslacion_y(y):  # Definimos la matriz de traslación en y
	traslacion_y = np.array([[1,0,0,0], # Primera fila de la matriz de traslación
						   [0,1,0,y], # Segunda fila de la matriz de traslación
						   [0,0,1,0], # Tercera fila de la matriz de traslación	   
						   [0,0,0,1]]) # Cuarta fila de la matriz de traslación
	return traslacion_y # Devolvemos la matriz de traslación en y

# Z
def matriz_traslacion_z(z):  # Definimos la matriz de traslación en z
	traslacion_z = np.array([[1,0,0,0], # Primera fila de la matriz de traslación
						   [0,1,0,0], # Segunda fila de la matriz de traslación
						   [0,0,1,z], # Tercera fila de la matriz de traslación	   
						   [0,0,0,1]]) # Cuarta fila de la matriz de traslación
	return traslacion_z # Devolvemos la matriz de traslación en z

######################  FUNCIONES DE MATRICES DE ROTACIÓN   #########################################

# X
def matriz_rotacion_x(grados_x): #Definimos la función de rotación en x
	rad = grados_x/180*np.pi # Conversión a grados
	matriz_rotacion_x = np.array([[1, 0, 0,0], #Matriz de rotación primera fila
						  [0,  np.cos(rad), -np.sin(rad),0], #Matriz de rotación segunda fila
						  [0,np.sin(rad),np.cos(rad),0], #Matriz de rotación terca fila
						  [0,0,0,1]]) # Cuarta fila de la matriz

	return matriz_rotacion_x #Devuelvo la matriz de rotación en x

# Y
def matriz_rotacion_y(grados_y): #Definimos la función de rotación en y
	rad = grados_y/180*np.pi # Conversión a grados
	matriz_rotacion_y = np.array([[np.cos(rad), 0, -np.sin(rad),0], #Matriz de rotación primera fila
						  [0,  1, 0,0], #Matriz de rotación segunda fila
						  [np.sin(rad), 0, np.cos(rad),0], #Matriz de rotación terca fila
						  [0,0,0,1]]) # Cuarta fila de la matriz

	return matriz_rotacion_y #Devuelvo la matriz de rotación en y

# Z
def matriz_rotacion_z(grados_z): #Definimos la función de rotación en z
	rad = grados_z/180*np.pi # Conversión a grados
	rotacion_z = np.array([[np.cos(rad),-np.sin(rad),0,0],  #Matriz de rotación primera fila
							[np.sin(rad),np.cos(rad),0,0], #Matriz de rotación segunda fila
								[0,0,1,0], #Matriz de rotación terca fila
								[0,0,0,1]]) # Cuarta fila de la matriz
	return rotacion_z # devolvemos la matriz de rotación en z

def cinematica_inversa(x,y,z,d1,d4):
	theta_1 = math.atan2(y,x)
	d2 = z
	d3 = math.cos(theta_1)*x + math.sin(theta_1)*y - d4
	theta_1 = round((theta_1*180/np.pi),1)
	return theta_1, d2, d3

# Configutación de la gráfica
def configuracion_grafica(): # función de configuración de la gráfica
	plt.title("Robot 4 G.D.L. RPPR",x=-0.03, y=30) # Título de la gráfica
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

def DH(theta_i,d_i,a_i,alpha_i):
	MT = matriz_rotacion_z(theta_i)@matriz_traslacion_z(d_i)@matriz_traslacion_x(a_i)@matriz_rotacion_x(alpha_i)
	print(MT)
	return MT

def robot_RR(theta_1, d1, a1, alpha_1, 
		 	 theta_2, d2, a2, alpha_2,
			 theta_3, d3, a3, alpha_3,
			 theta_4, d4, a4, alpha_4):
	
	# Pata 1 Frente derecha
	A0 = np.eye(4)
	_0A1 = DH(theta_1, d1, a1, alpha_1)
	_1A2 = DH(theta_2, d2, a2, alpha_2)
	_2A3 = DH(theta_3, d3, a3, alpha_3)
	_3A4 = DH(theta_4, d4, a4, alpha_4)
	_0A2 = _0A1@_1A2
	_0A3 = _0A2@_2A3
	_0A4 = _0A3@_3A4

	# Se deibujan los eslabones
	ax.plot3D([A0[0,3],_0A1[0,3]],[A0[1,3],_0A1[1,3]],[A0[2,3],_0A1[2,3]], color = 'red')
	ax.plot3D([_0A1[0,3],_0A2[0,3]],[_0A1[1,3],_0A2[1,3]],[_0A1[2,3],_0A2[2,3]], color = 'green')
	ax.plot3D([_0A2[0,3],_0A3[0,3]],[_0A2[1,3],_0A3[1,3]],[_0A2[2,3],_0A3[2,3]], color = 'red')
	ax.plot3D([_0A3[0,3],_0A4[0,3]],[_0A3[1,3],_0A4[1,3]],[_0A3[2,3],_0A4[2,3]], color = 'green')

def actualizacion_juntas2(val):
	
	ax.cla() # Limpia la gráfica
	configuracion_grafica()
	x = sld_angulo_1.val
	y = sld_angulo_2.val
	z = sld_angulo_3.val
	theta_1,d2,d3 = cinematica_inversa(x,y,z,1,1)
	Matriz_TH = robot_RR(theta_1,1,0,0,
						 90,d2,0,90,
						 0,d3,0,0,
						 0,1,0,0) #theta_1, d1=0, a1=10, alpha_1=0, theta_2, d2=0, a2=7, alpha_2=0
	

ax1 = plt.axes([0.2,0.15,0.65,0.03])
ax2 = plt.axes([0.2,0.1,0.65,0.03])
ax3 = plt.axes([0.2,0.05,0.65,0.03])	

sld_angulo_1 = Slider(ax1,r"$X$",-3,3,valinit=1)	
sld_angulo_2 = Slider(ax2,r"$Y$",-3,3,valinit=1)
sld_angulo_3 = Slider(ax3,r"$z$",0,3,valinit=1)	


configuracion_grafica()
Matriz_TH = robot_RR(0,1,0,0,
				   	 90,1,0,90,
				   	 0,1,0,0,
				   	 0,1,0,0)

sld_angulo_1.on_changed(actualizacion_juntas2)
sld_angulo_2.on_changed(actualizacion_juntas2)
sld_angulo_3.on_changed(actualizacion_juntas2)

plt.show()