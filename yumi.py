import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
from matplotlib.widgets import Slider

fig,ax = plt.subplots()
plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
ax = plt.axes(projection="3d")

def matriz_rotacion_z(grados):
    rad = grados/180*np.pi
    rotacion = np.array([[np.cos(rad),-np.sin(rad), 0, 0],
                        [np.sin(rad),np.cos(rad), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])
    return rotacion
    
def matriz_rotacion_y(grados):
    rad = grados/180*np.pi
    rotacion = np.array([[np.cos(rad), 0, -np.sin(rad), 0],
                        [0, 1, 0, 0],
                        [np.sin(rad), 0, np.cos(rad),0 ],
                        [0, 0, 0,1]])
    return rotacion

def matriz_rotacion_x(grados):
    rad = grados/180*np.pi
    rotacion = np.array([[1, 0, 0,0],
                        [0, np.cos(rad), -np.sin(rad),0],
                        [0, np.sin(rad), np.cos(rad),0],
                        [0, 0, 0,1]])
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
    plt.title("Robot 14 g.d.l YUMI", x = 0, y = 27)
    ax.set_xlim(-30,30)
    ax.set_ylim(-30,30)
    ax.set_zlim(-30,30)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.view_init(elev=25,azim=30) #Vista

def sistema_coordenadas(a,b,c,a_f,b_f,c_f):
    x = [a,a_f]
    y = [b,b_f]
    z = [c,c_f]

    ax.plot3D(x,[b,b],[c,c],color="red")
    ax.plot3D([a,a],y,[c,c],color="blue")
    ax.plot3D([a,a],[b,b],z,color="green")

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

    dx = matriz_rotacion[0,3]
    dy = matriz_rotacion[1,3]
    dz = matriz_rotacion[2,3]

    ax.plot3D([dx,dx+r_11],[dy,dy+r_12],[dz,dz+r_13],color="c")
    ax.plot3D([dx,dx+r_21],[dy,dy+r_22],[dz,dz+r_23],color="m")
    ax.plot3D([dx,dx+r_31],[dy,dy+r_32],[dz,dz+r_33],color="y")

def robotyumi(theta1,d1,a1,alpha1, theta2,d2,a2,alpha2, theta3,d3,a3,alpha3, theta4,d4,a4,alpha4,
            theta5,d5,a5,alpha5, theta6,d6,a6,alpha6, theta7,d7,a7,alpha7):
    A0 = np.eye(4)
    A_0_1 = denavit_hartenberg(theta1,d1,a1,alpha1)    
    A_1_2 = denavit_hartenberg(theta2,d2,a2,alpha2)
    A_2_3 = denavit_hartenberg(theta3,d3,a3,alpha3)
    A_3_4 = denavit_hartenberg(theta4,d4,a4,alpha4)   
    A_4_5 = denavit_hartenberg(theta5,d5,a5,alpha5)
    A_5_6 = denavit_hartenberg(theta6,d6,a6,alpha6)
    A_6_7 = denavit_hartenberg(theta7,d7,a7,alpha7)

    A_0_2 = A_0_1 @ A_1_2
    A_0_3 = A_0_2 @ A_2_3
    A_0_4 = A_0_3 @ A_3_4
    A_0_5 = A_0_4 @ A_4_5
    A_0_6 = A_0_5 @ A_5_6
    A_0_7 = A_0_6 @ A_6_7

    sistema_coordenadas_movil(A0)
    sistema_coordenadas_movil(A_0_1)
    sistema_coordenadas_movil(A_0_2)
    sistema_coordenadas_movil(A_0_3)
    sistema_coordenadas_movil(A_0_4)
    sistema_coordenadas_movil(A_0_5)
    sistema_coordenadas_movil(A_0_6)
    sistema_coordenadas_movil(A_0_7)

    ax.plot3D([A0[0,3],A_0_1[0,3]],[A0[1,3],A_0_1[1,3]],[A0[2,3],A_0_1[2,3]], color='red')
    ax.plot3D([A_0_1[0,3],A_0_2[0,3]],[A_0_1[1,3],A_0_2[1,3]],[A_0_1[2,3],A_0_2[2,3]], color='red')
    ax.plot3D([A_0_2[0,3],A_0_3[0,3]],[A_0_2[1,3],A_0_3[1,3]],[A_0_2[2,3],A_0_3[2,3]], color='red')
    ax.plot3D([A_0_3[0,3],A_0_4[0,3]],[A_0_3[1,3],A_0_4[1,3]],[A_0_3[2,3],A_0_4[2,3]], color='red')
    ax.plot3D([A_0_4[0,3],A_0_5[0,3]],[A_0_4[1,3],A_0_5[1,3]],[A_0_4[2,3],A_0_5[2,3]], color='red')
    ax.plot3D([A_0_5[0,3],A_0_6[0,3]],[A_0_5[1,3],A_0_6[1,3]],[A_0_5[2,3],A_0_6[2,3]], color='red')
    ax.plot3D([A_0_6[0,3],A_0_7[0,3]],[A_0_6[1,3],A_0_7[1,3]],[A_0_6[2,3],A_0_7[2,3]], color='red')

def denavit_hartenberg(theta,d,a,alpha):  # Denavit–Hartenberg
    MT = matriz_rotacion_z(theta)@matriz_traslacion_z(d)@matriz_traslacion_x(a)@matriz_rotacion_x(alpha)
    #MT = matriz_rotacion_x(theta)@matriz_traslacion_x(d)@matriz_traslacion_y(a)@matriz_rotacion_y(alpha)
    return(MT)

def actualizacion_juntas(val):
    plt.figure(1)
    ax.cla()
    configuracion_grafica()
    #robotyumi(sld_ang1.val, 0, 10, 0, sld_ang2.val, 0, 7, 0)
    robotyumi(sld_ang1.val,16.6,0,0, sld_ang2.val,0,3,0, sld_ang3.val,25.15,-3,-90, sld_ang4.val,0,4.05,90,
            sld_ang5.val,26.5,-4.05,-90, sld_ang6.val,0,2.7,90, sld_ang7.val,3.6,-2.7,-90)

    plt.draw()
    plt.pause(1e-9)

plt.figure(2,figsize=([6,4]))
ax1 = plt.axes([0.2, 0.92, 0.65, 0.05])
ax2 = plt.axes([0.2, 0.77, 0.65, 0.05])
ax3 = plt.axes([0.2, 0.62, 0.65, 0.05])
ax4 = plt.axes([0.2, 0.47, 0.65, 0.05])
ax5 = plt.axes([0.2, 0.32, 0.65, 0.05])
ax6 = plt.axes([0.2, 0.17, 0.65, 0.05])
ax7 = plt.axes([0.2, 0.02, 0.65, 0.05])

sld_ang1 = Slider(ax1, "Theta 1", -180, 180, valinit=15)
sld_ang2 = Slider(ax2, "Theta 2", -180, 180, valinit=15)
sld_ang3 = Slider(ax3, "Theta 3", -180, 180, valinit=15)
sld_ang4 = Slider(ax4, "Theta 4", -180, 180, valinit=15)
sld_ang5 = Slider(ax5, "Theta 5", -180, 180, valinit=15)
sld_ang6 = Slider(ax6, "Theta 6", -180, 180, valinit=15)
sld_ang7 = Slider(ax7, "Theta 7", -180, 180, valinit=15)


plt.figure(1)
sistema_coordenadas(0,0,0,1,1,1)
#robotyumi(0,166,-30,-90, 0,0,30,90)


sld_ang1.on_changed(actualizacion_juntas)
sld_ang2.on_changed(actualizacion_juntas)
sld_ang3.on_changed(actualizacion_juntas)
sld_ang4.on_changed(actualizacion_juntas)
sld_ang5.on_changed(actualizacion_juntas)
sld_ang6.on_changed(actualizacion_juntas)
sld_ang7.on_changed(actualizacion_juntas)

# robot_yumi_animado(90,0,10,0, 45,0,7,0)

configuracion_grafica()
robotyumi(0,166,-30,-90, 0,0,30,90, 180,251,40.5,-90, 0,100,0,90, 180,250,27,-90, 0,0,30,90, 180,251,40.5,-90)

plt.show()
