# UNIVERSIDAD AUTÓNOMA CHAPINGO
# DEPARTAMENTO DE INGENIERÍA MECÁNICA AGRÍCOLA
# INGENIERÍA MECATRÓNICA AGRÍCOLA
# CINEMÁTICA DE ROBOTS
# ROBOT DELTA
# LUIS ANGEL SANCHEZ RODRIGUEZ 
# 6°7

# Importamos las librerías necesarias para el programa
import numpy as np #Importamos la librería numpy como np
import matplotlib.pyplot as plt # Importamos matplotlib como plt
from mpl_toolkits import mplot3d # Importamos mplot3d desde mplt_toolkits

# Graficación en 3d
fig, ax = plt.subplots() # Creamos una figura y sus ejes
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



# Configutación de la gráfica
def configuracion_grafica(): # función de configuración de la gráfica
    plt.title("Robot delta",x=0,y=27) # Título de la gráfica
    ax.set_xlim(-10,10) # Límites en el eje x
    ax.set_ylim(-10,10) # Límites en el eje y
    ax.set_zlim(-10,10) # Límites en el eje z

    ax.set_xlabel("x(t)") # Nombre del eje x
    ax.set_ylabel("y(t)") # Nombre del eje y
    ax.set_zlabel("z(t)") # Nombre del eje z
    ax.view_init(elev = 25, azim = 30) # # Tipo de vista de la gráfica


def sistema_coordenadas(a,b,c,a_f,b_f,c_f):
    x = [a,a_f] 
    y = [b,b_f]
    z = [c,c_f]

    ax.plot3D(x,[b,b],[c,c],color="red") # X
    ax.plot3D([a,a],y,[c,c],color="blue") # Y
    ax.plot3D([a,a],[b,b],z,color="green") # Z


# Sistema de coordenadas móvil para la matriz de rotación
def sistema_coordenadas_movil(matriz_rotacion): # definimos la matriz
    r_11 = matriz_rotacion[0,0] # Columna 0, Fila 0
    r_12 = matriz_rotacion[1,0] # Columna 1, Fila 0
    r_13 = matriz_rotacion[2,0] # Columna 2, Fila 0
    r_21 = matriz_rotacion[0,1] # Columna 0, Fila 1
    r_22 = matriz_rotacion[1,1] # Columna 1, Fila 1
    r_23 = matriz_rotacion[2,1] # Columna 2, Fila 1
    r_31 = matriz_rotacion[0,2] # Columna 0, Fila 2
    r_32 = matriz_rotacion[1,2] # Columna 1, Fila 2
    r_33 = matriz_rotacion[2,2] # Columna 2, Fila 2

    dx = matriz_rotacion[0,3] # Columna 0, Fila 3
    dy = matriz_rotacion[1,3] # Columna 1, Fila 3
    dz = matriz_rotacion[2,3] # Columna 2, Fila 3
    
    # Sistema que va a mover
    ax.plot3D([dx,dx+r_11],[dy,dy+r_12],[dz,dz+r_13], color="k") # X 
    ax.plot3D([dx,dx+r_21],[dy,dy+r_22],[dz,dz+r_23], color="brown") # Y
    ax.plot3D([dx,dx+r_31],[dy,dy+r_32],[dz,dz+r_33], color="darkviolet") # Z

# Funciones de Devanit-Hatenberg
def denavit_hatemberg(theta_i,d_i,a_i,alpha_i):
	MT = matriz_rotacion_z(theta_i)@matriz_traslacion_z(d_i)@matriz_traslacion_x(a_i)@matriz_rotacion_x(alpha_i)
	return MT
def denavit_hatemberg2(theta_i,d_i,a_i,alpha_i):
	MT = matriz_rotacion_y(theta_i)@matriz_traslacion_y(d_i)@matriz_traslacion_x(a_i)@matriz_rotacion_x(alpha_i)
	return MT
def denavit_hatemberg3(theta_i,d_i,a_i,alpha_i):
	MT = matriz_rotacion_z(theta_i)@matriz_traslacion_z(d_i)@matriz_traslacion_x(a_i)@matriz_rotacion_y(alpha_i)
	return MT

def robot_delta(theta_1,d1,a1,alpha_1,theta_2,d2,a2,alpha_2,theta_3,d3,a3,alpha_3): #
	A0 = np.eye(4)

	A_0_1 = denavit_hatemberg2(theta_1,d1,a1,alpha_1)
	A_1_2 = denavit_hatemberg(theta_2,d2,a2,alpha_2)
	A_2_3 = denavit_hatemberg(theta_3,d2,a2,alpha_3)
	A_0_2 = A_0_1@A_1_2
	A_0_3 = A_0_2@A_2_3

	sistema_coordenadas_movil(A0)
	sistema_coordenadas_movil(A_0_1)
	sistema_coordenadas_movil(A_0_2)
	sistema_coordenadas_movil(A_0_3)

	ax.plot3D([A0[0,3],A_0_1[0,3]],[A0[1,3],A_0_1[1,3]],[A0[2,3],A_0_1[2,3]], color = 'red')
	ax.plot3D([A_0_1[0,3],A_0_2[0,3]],[A_0_1[1,3],A_0_2[1,3]],[A_0_1[2,3],A_0_2[2,3]], color = 'red')
	ax.plot3D([A_0_2[0,3],A_0_3[0,3]],[A_0_2[1,3],A_0_3[1,3]],[A_0_2[2,3],A_0_3[2,3]], color = 'red')

def robot_delta3(theta_1,d1,a1,alpha_1,theta_2,d2,a2,alpha_2,theta_3,d3,a3,alpha_3): #
	A0 = np.eye(4)
	
	A_0_1 = denavit_hatemberg2(theta_1,d1,a1,alpha_1)
	A_1_2 = denavit_hatemberg3(theta_2,d2,a2,alpha_2)
	A_2_3 = denavit_hatemberg(theta_3,d2,a2,alpha_3)
	A_0_2 = A_0_1@A_1_2
	A_0_3 = A_0_2@A_2_3

	sistema_coordenadas_movil(A0)
	sistema_coordenadas_movil(A_0_1)
	sistema_coordenadas_movil(A_0_2)
	sistema_coordenadas_movil(A_0_3)

	ax.plot3D([A0[0,3],A_0_1[0,3]],[A0[1,3],A_0_1[1,3]],[A0[2,3],A_0_1[2,3]], color = 'blue')
	ax.plot3D([A_0_1[0,3],A_0_2[0,3]],[A_0_1[1,3],A_0_2[1,3]],[A_0_1[2,3],A_0_2[2,3]], color = 'blue')
	ax.plot3D([A_0_2[0,3],A_0_3[0,3]],[A_0_2[1,3],A_0_3[1,3]],[A_0_2[2,3],A_0_3[2,3]], color = 'blue')

def robot_delta_animado(theta_1,d1,a1,alpha_1,theta_2,d2,a2,alpha_2):
	if theta_1 > 90:
		min = 90
		max = theta_1+1
		step = 1
	else:
		min = 90
		max = theta_1-1
		step = -1
	j = 45
	k = 70
	a = 90
	b = 0
	c = 65
	for i in range(min,max,step):
		f = i + 20
		ax.cla()
		configuracion_grafica()
		robot_delta(90,0,4,0,i,0,3,0,c,0,3,0)
		robot_delta3(210,0,4,0,k,0,3,-b,a,0,0,0)
		robot_delta3(330-i,0,4,0,k,0,3,b,a,0,0,0)
		j = j + 1
		k = k + 1
		a = a - 1
		b = b + 0.5
		c = c + 1
		plt.draw()
		plt.pause(1e-9)

robot_delta_animado(0,0,8,0,90,8,10,0)
configuracion_grafica()
plt.show() # Mostramos la gráfica