
# Importamos las librerías para el programa
import numpy as np #Importamos la librería numpy como np para vectores y matrices
import matplotlib.pyplot as plt # Importamos matplotlib como plt para graficar
from mpl_toolkits import mplot3d # Importamos mplot3d desde mplt_toolkits subpaquete de la librería de graficación para 3D
from matplotlib import cm # Importamos cm desde matplotlib subpaquete para la graficación
from matplotlib.widgets import Slider # Subpaquete para agregar las barras de control del robot

# Graficación en 3d
fig, ax = plt.subplots() # Creamos una figura y sus ejes
plt.subplots_adjust(left = 0, bottom = 0.3, right =0.74, top = 1) # Ubicamos la figura
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
	plt.title("Robot 6 G.D.L. IRB 2600",x=2, y=12) # Título de la gráfica
	ax.set_xlim(-0,1200) # Límites en el eje x
	ax.set_ylim(-1200,1200) # Límites en el eje y
	ax.set_zlim(-1200,1200) # Límites en el eje z

	ax.set_xlabel("z(t)") # Nombre del eje x
	ax.set_ylabel("y(t)") # Nombre del eje y
	ax.set_zlabel("x(t)") # Nombre del eje z
	ax.view_init(elev = 134, azim = -180) # # Tipo de vista de la gráfica

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
	ax.plot3D([dz,dz+r_13],[dy,dy+r_12],[dx,dx+r_11], color="m") # X 
	ax.plot3D([dz,dz+r_23],[dy,dy+r_22],[dx,dx+r_21], color="c") # Y
	ax.plot3D([dz,dz+r_33],[dy,dy+r_32],[dx,dx+r_31], color="k") # Z


def denavit_hatemberg(theta_i,d_i,a_i,alpha_i):
	MT = matriz_rotacion_z(theta_i)@matriz_traslacion_z(d_i)@matriz_traslacion_x(a_i)@matriz_rotacion_x(alpha_i)
	return MT


def robot_abb_irb2600(theta_1,theta_2,theta_3,theta_4,theta_5,theta_6):
	A0 = np.eye(4)
	#A_0_1 = denavit_hatemberg(theta_1,d1,a1,alpha_1)
	#A_0_1 = denavit_hatemberg(theta_2,d2,a2,alpha_2)
	#A_0_1 = denavit_hatemberg(theta_3,d3,a3,alpha_3)
	#A_0_1 = denavit_hatemberg(theta_4,d4,a4,alpha_4)
	#A_0_1 = denavit_hatemberg(theta_5,d5,a5,alpha_5)
	#A_0_1 = denavit_hatemberg(theta_6,d6,a6,alpha_6)

	A_0_1 = denavit_hatemberg(theta_1,280,0,0)
	A_1_2 = denavit_hatemberg(theta_2,0,150,0)
	A_2_3 = denavit_hatemberg(theta_3,815,0,0)
	A_3_4 = denavit_hatemberg(theta_4,0,0,-90)
	A_4_5 = denavit_hatemberg(theta_5,795,0,90)
	A_5_6 = denavit_hatemberg(theta_6,0,85,0)

	A_0_2 = A_0_1@A_1_2
	A_0_3 = A_0_2@A_2_3
	A_0_4 = A_0_3@A_3_4
	A_0_5 = A_0_4@A_4_5
	A_0_6 = A_0_5@A_5_6
	
	ax.plot3D([A0[2,3],A_0_1[2,3]],[A0[1,3],A_0_1[1,3]],[A0[0,3],A_0_1[0,3]], color="red")
	ax.plot3D([A_0_1[2,3],A_0_2[2,3]],[A_0_1[1,3],A_0_2[1,3]],[A_0_1[0,3],A_0_2[0,3]], color="green")
	ax.plot3D([A_0_2[2,3],A_0_3[2,3]],[A_0_2[1,3],A_0_3[1,3]],[A_0_2[0,3],A_0_3[0,3]], color="green")
	ax.plot3D([A_0_3[2,3],A_0_4[2,3]],[A_0_3[1,3],A_0_4[1,3]],[A_0_3[0,3],A_0_4[0,3]], color="green")
	ax.plot3D([A_0_4[2,3],A_0_5[2,3]],[A_0_4[1,3],A_0_5[1,3]],[A_0_4[0,3],A_0_5[0,3]], color="green")
	ax.plot3D([A_0_5[2,3],A_0_6[2,3]],[A_0_5[1,3],A_0_6[1,3]],[A_0_5[0,3],A_0_6[0,3]], color="green")
	
	sistema_coordenadas_movil(A0) # sistema móvil de la base
	sistema_coordenadas_movil(A_0_1) # sistema móvil del eslabón 1
	sistema_coordenadas_movil(A_0_2) # sistema móvil del eslabón 2
	sistema_coordenadas_movil(A_0_3)
	sistema_coordenadas_movil(A_0_4)
	sistema_coordenadas_movil(A_0_5)
	sistema_coordenadas_movil(A_0_6)

	return A_0_6

def actualizacion_juntas(val):
	
	ax.cla() # Limpia la gráfica
	configuracion_grafica()
	theta_1 = sld_angulo_1.val
	theta_2 = sld_angulo_2.val
	theta_3 = sld_angulo_3.val
	theta_4 = sld_angulo_4.val
	theta_5 = sld_angulo_5.val
	theta_6 = sld_angulo_6.val
	Matriz_TH = robot_abb_irb2600(theta_1,theta_2,theta_3,theta_4,theta_5,theta_6) #theta_1, d1=0, a1=10, alpha_1=0, theta_2, d2=0, a2=7, alpha_2=0
	x = 0
	y = 0
	while x<4:
		while y<4:
			tabla._cells[(x,y)]._text.set_text(np.round(Matriz_TH[x,y],3))
			y=y+1
		y=0
		x= x+1
	plt.draw()
	plt.pause(1e-3)


ax1 = plt.axes([0.15,0.15,0.3,0.03])
ax2 = plt.axes([0.15,0.1,0.3,0.03])
ax3 = plt.axes([0.15,0.05,0.3,0.03])
ax4 = plt.axes([0.6,0.15,0.07,0.03])
ax5 = plt.axes([0.6,0.1,0.07,0.03])
ax6 = plt.axes([0.6,0.05,0.07,0.03])

ax_table = plt.axes([0.63,0.3,0.07,0.03])

sld_angulo_1 = Slider(ax1,r'$\theta_1$',-180,180,valinit=0)	
sld_angulo_2 = Slider(ax2,r'$\theta_2$',-180,180,valinit=0)	
sld_angulo_3 = Slider(ax3,r'$\theta_3$',-180,180,valinit=0)	
sld_angulo_4 = Slider(ax4,r'$\theta_4$',-180,180,valinit=0)	
sld_angulo_5 = Slider(ax5,r'$\theta_5$',-180,180,valinit=0)	
sld_angulo_6 = Slider(ax6,r'$\theta_6$',-180,180,valinit=0)	


configuracion_grafica()
#Matriz_TH = robot_RR(45,0,10,0,45,0,7,0)
Matriz_TH = robot_abb_irb2600(0,0,0,0,0,0)

tabla = plt.table(cellText=np.round(Matriz_TH,3),bbox=[0,0,5,5],loc='center')
tabla.auto_set_font_size(False)
tabla.set_fontsize(8)
ax_table.axis('off')


sld_angulo_1.on_changed(actualizacion_juntas)
sld_angulo_2.on_changed(actualizacion_juntas)
sld_angulo_3.on_changed(actualizacion_juntas)
sld_angulo_4.on_changed(actualizacion_juntas)
sld_angulo_5.on_changed(actualizacion_juntas)
sld_angulo_6.on_changed(actualizacion_juntas)


plt.show()

