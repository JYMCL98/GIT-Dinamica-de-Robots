import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig,ax=plt.subplots()
ax=plt.axes(projection = "3d")

#  Funciones para rotaciones
def matriz_rotacion_z(grados):
	rad = grados/180*np.pi
	rotacion = np.array([[np.cos(rad),-np.sin(rad),0,0],
						[np.sin(rad), np.cos(rad),0,0],
						[		   0,           0,1,0],
						[          0,           0,0,1]])
	return rotacion
def matriz_rotacion_x(grados):
	rad = grados/180*np.pi 
	rotacion = np.array([[1    ,0          ,           0,0],
						[0    ,np.cos(rad), -np.sin(rad),0],
						[0    ,np.sin(rad),  np.cos(rad),0],
						[0    ,          0,            0,1]])
	return rotacion

def matriz_rotacion_y(grados):
	rad = grados/180*np.pi 
	rotacion = np.array([[np.cos(rad), 0, -np.sin(rad),0],
						 [0,           1,            0,0],
						 [np.sin(rad), 0,  np.cos(rad),0],
						 [0,           0,            0,1]])
	return rotacion

 #  Funciones de traslación
def matriz_traslacion_X(x):
	traslacion=np.array([[1,0,0,x],
						 [0,1,0,0],
						 [0,0,1,0],
						 [0,0,0,1]])
	return traslacion

def matriz_traslacion_Y(y):
	traslacion=np.array([[1,0,0,0],
						 [0,1,0,y],
						 [0,0,1,0],
						 [0,0,0,1]])
	return traslacion

def matriz_traslacion_Z(z):
	traslacion=np.array([[1,0,0,0],
						 [0,1,0,0],
						 [0,0,1,z],
						 [0,0,0,1]])
	return traslacion

def configuracion_grafica():
	ax.set_xlim(-10,10)
	ax.set_ylim(-10,10)
	ax.set_zlim(-10,10)
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_zlabel("z")
	ax.view_init(elev=25, azim=30)

def sistema_coordenada(a,b,c,a_f,b_f,c_f):
	x = [a,a_f]
	y = [b,b_f]
	z = [c,b_f]
	ax.plot3D(x,[b,b],[c,c],color= 'red')
	ax.plot3D([a,a],y, [c,c],color= 'blue')
	ax.plot3D([a,a],[b,b],z,color= 'green')

def sistema_coordenada_movil(matriz_rotacion):
	r_11 = matriz_rotacion[0,0]
	r_12 = matriz_rotacion[1,0]
	r_13 = matriz_rotacion[2,0]
	r_21 = matriz_rotacion[0,1]
	r_22 = matriz_rotacion[1,1]
	r_23 = matriz_rotacion[2,1]
	r_31 = matriz_rotacion[0,2]
	r_32 = matriz_rotacion[1,2]
	r_33 = matriz_rotacion[2,2]
	dx= matriz_rotacion[0,3]
	dy= matriz_rotacion[1,3]
	dz= matriz_rotacion[2,3]

	ax.plot3D([dx,dx+r_11],[dy,dy+r_12],[dz,dz+r_13],color='m')
	ax.plot3D([dx,dx+r_21],[dy,dy+r_22],[dz,dz+r_23],color='c')
	ax.plot3D([dx,dx+r_31],[dy,dy+r_32],[dz,dz+r_33],color='y')

def denavit_hatemberg(theta_i,d_i,a_i,alpha_i):
	MT = matriz_rotacion_z(theta_i)@matriz_traslacion_Z(d_i)@matriz_traslacion_X(a_i)@matriz_rotacion_x(alpha_i)
	return MT
def denavit_hatemberg2(theta_i,d_i,a_i,alpha_i):
	MT = matriz_rotacion_y(theta_i)@matriz_traslacion_Y(d_i)@matriz_traslacion_X(a_i)@matriz_rotacion_x(alpha_i)
	return MT
def denavit_hatemberg3(theta_i,d_i,a_i,alpha_i):
	MT = matriz_rotacion_z(theta_i)@matriz_traslacion_Z(d_i)@matriz_traslacion_X(a_i)@matriz_rotacion_y(alpha_i)
	return MT

def robot_RR(theta_1,d1,a1,alpha_1,theta_2,d2,a2,alpha_2,theta_3,d3,a3,alpha_3): #
	A0 = np.eye(4)
	A_0_1 = denavit_hatemberg2(theta_1,d1,a1,alpha_1)
	A_1_2 = denavit_hatemberg(theta_2,d2,a2,alpha_2)
	A_2_3 = denavit_hatemberg(theta_3,d2,a2,alpha_3)
	A_0_2 = A_0_1@A_1_2
	A_0_3 = A_0_2@A_2_3

	sistema_coordenada_movil(A0)
	sistema_coordenada_movil(A_0_1)
	sistema_coordenada_movil(A_0_2)
	sistema_coordenada_movil(A_0_3)

	ax.plot3D([A0[0,3],A_0_1[0,3]],[A0[1,3],A_0_1[1,3]],[A0[2,3],A_0_1[2,3]], color = 'red')
	ax.plot3D([A_0_1[0,3],A_0_2[0,3]],[A_0_1[1,3],A_0_2[1,3]],[A_0_1[2,3],A_0_2[2,3]], color = 'red')
	ax.plot3D([A_0_2[0,3],A_0_3[0,3]],[A_0_2[1,3],A_0_3[1,3]],[A_0_2[2,3],A_0_3[2,3]], color = 'red')

def robot_RR3(theta_1,d1,a1,alpha_1,theta_2,d2,a2,alpha_2,theta_3,d3,a3,alpha_3): #
	A0 = np.eye(4)
	A_0_1 = denavit_hatemberg2(theta_1,d1,a1,alpha_1)
	A_1_2 = denavit_hatemberg3(theta_2,d2,a2,alpha_2)
	A_2_3 = denavit_hatemberg(theta_3,d2,a2,alpha_3)
	A_0_2 = A_0_1@A_1_2
	A_0_3 = A_0_2@A_2_3

	sistema_coordenada_movil(A0)
	sistema_coordenada_movil(A_0_1)
	sistema_coordenada_movil(A_0_2)
	sistema_coordenada_movil(A_0_3)

	ax.plot3D([A0[0,3],A_0_1[0,3]],[A0[1,3],A_0_1[1,3]],[A0[2,3],A_0_1[2,3]], color = 'red')
	ax.plot3D([A_0_1[0,3],A_0_2[0,3]],[A_0_1[1,3],A_0_2[1,3]],[A_0_1[2,3],A_0_2[2,3]], color = 'red')
	ax.plot3D([A_0_2[0,3],A_0_3[0,3]],[A_0_2[1,3],A_0_3[1,3]],[A_0_2[2,3],A_0_3[2,3]], color = 'red')
def robot_RR_animado(theta_1,d1,a1,alpha_1,theta_2,d2,a2,alpha_2):
	if theta_1>90:
		min = 90
		max = theta_1+1
		step = 1
	else:
		min = 90
		max = theta_1-1
		step = -1
	j=45
	k=70
	a=90
	b=0
	c=65
	for i in range(min,max,step):
		f=i+20
		ax.cla()
		configuracion_grafica()
		robot_RR(90,0,4,0,i,0,3,0,c,0,3,0)
		robot_RR3(210,0,4,0,k,0,3,-b,a,0,0,0)
		robot_RR3(330-i,0,4,0,k,0,3,b,a,0,0,0)
		j=j+1
		k=k+1
		a=a-1
		b=b+0.5
		c=c+1
		plt.draw()
		plt.pause(1e-3)

	"""if theta_2>0:
		min = 1
		max = theta_2+1
		step = 1
	else:
		min = -1
		max = theta_2-1
		step = -1
	for f in range(min,max,step):
		ax.cla()
		configuracion_grafica()
		robot_RR(i,0,10,0,f,0,7,0)
		plt.draw()
		plt.pause(1e-3)"""

robot_RR_animado(0,0,10,0,90,10,10,0)

#sistema_coordenada(0,0,0,1,1,1)
configuracion_grafica()
plt.show()