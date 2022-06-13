import tkinter as tk
import matplotlib.pyplot as plt
import math
import pandas as pd
import numpy as np

from mpl_toolkits import mplot3d # Importamos mplot3d desde mplt_toolkits subpaquete de la librería de graficación para 3D
from matplotlib import cm # Importamos cm desde matplotlib subpaquete para la graficación
from matplotlib.widgets import Slider # Subpaquete para agregar las barras de control del robot

from tkinter import *
from tkinter import Tk, Label, Button, Frame,  messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
from tkinter import scrolledtext as st

fig, ax = plt.subplots() # Creamos una figura y sus ejes
plt.subplots_adjust(left = 0, bottom = 0.3, right =0.74, top = 1) # Ubicamos la figura
ax = plt.axes(projection = "3d") # Establecemos los ejes como 3 dimensiones

# FUNCIONES DE MATRICES DE TRASLACIÓN
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

# FUNCIONES DE MATRICES DE ROTACIÓN

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
	return rotacion_z # devolvemos la matriz de rotación en 

# Cinemática inversa
def cinematica_inversa(x,y,a1,a2):
	# Le damos posición y obtenemos ángulo
    theta_2 = math.acos((x**2+y**2-a1**2-a2**2)/(2*a1*a2))
    theta_1 = math.atan2(y,x)-math.atan2((a2*math.sin(theta_2)),(a1+a2*math.cos(theta_2)))

    theta_1 = round((theta_1*180/np.pi),1)
    theta_2 = round((theta_2*180/np.pi),1)
    print('\u03B8\u2081: ',theta_1)
    print('\u03B8\u2082: ',theta_2)
    print()
    return theta_1,theta_2


# Configutación de la gráfica
def configuracion_grafica(): # función de configuración de la gráfica
	plt.title("Robot 2 G.D.L. RR",x=3, y=12) # Título de la gráfica
	ax.set_xlim(-17,17) # Límites en el eje x
	ax.set_ylim(0,17) # Límites en el eje y
	ax.set_zlim(-0,5) # Límites en el eje z

	ax.set_xlabel("x(t)") # Nombre del eje x
	ax.set_ylabel("y(t)") # Nombre del eje y
	ax.set_zlabel("z(t)") # Nombre del eje z
	ax.view_init(elev = 83, azim = -90) # # Tipo de vista de la gráfica

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
	ax.plot3D([dx,dx+r_11],[dy,dy+r_12],[dz,dz+r_13], color="m") # X 
	ax.plot3D([dx,dx+r_21],[dy,dy+r_22],[dz,dz+r_23], color="c") # Y
	ax.plot3D([dx,dx+r_31],[dy,dy+r_32],[dz,dz+r_33], color="k") # Z

def denavit_hatemberg(theta_i,d_i,a_i,alpha_i):
	MT = matriz_rotacion_z(theta_i)@matriz_traslacion_z(d_i)@matriz_traslacion_x(a_i)@matriz_rotacion_x(alpha_i)
	return MT

def robot_RR(theta_1,d1,a1,alpha_1,theta_2,d2,a2,alpha_2):
	A0 = np.eye(4) # Matriz identidad de 4x4
	A_0_1 = denavit_hatemberg(theta_1,d1,a1,alpha_1)
	A_1_2 = denavit_hatemberg(theta_2,d2,a2,alpha_2)
	A_0_2 = A_0_1 @ A_1_2

	sistema_coordenadas_movil(A0) # sistema móvil de la base
	sistema_coordenadas_movil(A_0_1) # sistema móvil del eslabón 1
	sistema_coordenadas_movil(A_0_2) # sistema móvil del eslabón 2

	ax.plot3D([A0[0,3],A_0_1[0,3]],[A0[1,3],A_0_1[1,3]],[A0[2,3],A_0_1[2,3]], color="blue") # Eslabón 1
	ax.plot3D([A_0_1[0,3],A_0_2[0,3]],[A_0_1[1,3],A_0_2[1,3]],[A_0_1[2,3],A_0_2[2,3]], color="green") # Eslabón 2
	return A_0_2


def actualizacion_juntas(val):
	
	ax.cla() # Limpia la gráfica
	configuracion_grafica()
	theta_1 = sld_angulo_1.val
	theta_2 = sld_angulo_2.val
	Matriz_TH = robot_RR(theta_1,0,10,0,theta_2,0,7,0) #theta_1, d1=0, a1=10, alpha_1=0, theta_2, d2=0, a2=7, alpha_2=0
    
	plt.draw()
	plt.pause(1e-3)

def actualizacion_juntas2(val):
	
	ax.cla() # Limpia la gráfica
	configuracion_grafica()
	x = sld_angulo_1.val
	y = sld_angulo_2.val
	theta_1,theta_2 = cinematica_inversa(x,y,10,7)
	Matriz_TH = robot_RR(theta_1,0,10,0,theta_2,0,7,0) #theta_1, d1=0, a1=10, alpha_1=0, theta_2, d2=0, a2=7, alpha_2=0
	
	sld_angulo_2.eventson = False
	sld_angulo_2.set_val(Matriz_TH[1,3])
	sld_angulo_2.eventson = True
    
	"""
	x = 0
	y = 0
	while x<4:
		while y<4:
			tabla._cells[(x,y)]._text.set_text(np.round(Matriz_TH[x,y],3))
			y=y+1
		y=0
		x= x+1
    """
	plt.draw()
	plt.pause(1e-3)

def actualizacion_juntas3(val):
	
	ax.cla() # Limpia la gráfica
	configuracion_grafica()
	x = sld_angulo_1.val
	y = sld_angulo_2.val
	theta_1,theta_2 = cinematica_inversa(x,y,10,7)
	Matriz_TH = robot_RR(theta_1,0,10,0,theta_2,0,7,0) #theta_1, d1=0, a1=10, alpha_1=0, theta_2, d2=0, a2=7, alpha_2=0
	
	sld_angulo_1.eventson = False
	sld_angulo_1.set_val(Matriz_TH[0,3])
	sld_angulo_1.eventson = TRUE
    
"""
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
    """

ventana = Tk()
ventana.minsize(width=900, height=700)
ventana.title('Carta')
ventana["bg"] = "#6DBFD3"

def abrir_archivo():

    global X_1,Y_1,Z_1,X_2,Y_2,Z_2

    archivo = filedialog.askopenfilename(initialdir ='/', 
                                            title='Selecione archivo', 
                                            filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
    indica['text'] = archivo

    data = pd.read_excel(archivo)
    X_1 = pd.DataFrame(data, columns=['X']).to_numpy()
    Y_1 = pd.DataFrame(data, columns=['Y']).to_numpy()
    Z_1 = pd.DataFrame(data, columns=['Z']).to_numpy()

    conv = list(map(float, X_1))
    conv_2 = np.array(conv)

    conv_3 = list(map(float, Y_1))
    conv_4 = np.array(conv_3)

    conv_5 = list(map(float, Z_1))
    conv_6 = np.array(conv_5)

    X_2 = conv_2
    Y_2 = conv_4
    Z_2 = conv_6

def oper():
    
    #plt.clf()
    global X_3,Y_3,Z_3,sld_angulo_1,sld_angulo_2
    
    X_3 = float(entrada1.get()) # X
    Y_3 = float(entrada1.get()) # Y
    Z_3 = float(entrada1.get()) # Z
    
    ax1 = plt.axes([0.2,0.15,0.65,0.03])
    ax2 = plt.axes([0.2,0.1,0.65,0.03])
    ax3 = plt.axes([0.63,0.3,0.07,0.03])
    
    
    #sld_angulo_1 = Slider(ax1,"Theta 1",0,180,valinit=45)	
    #sld_angulo_2 = Slider(ax2,"Theta 2",-180,180,valinit=45)	
    
    sld_angulo_1 = Slider(ax1,r"$X$",-10,10,valinit=X_3)	
    sld_angulo_2 = Slider(ax2,r"$Y$",0,14,valinit=Y_3)
    
    thet_1,thet_2 = cinematica_inversa(X_3,Y_3,10,7)
    configuracion_grafica()
    Matriz_TH = robot_RR(thet_1,0,10,0,thet_2,0,7,0)  # theta_1,d1,a1,alpha_1,theta_2,d2,a2,alpha_2
    
    tabla = plt.table(cellText=np.round(Matriz_TH,3),bbox=[0,0,5,5],loc='center')
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(8)
    ax3.axis('off')
    
    
    sld_angulo_1.on_changed(actualizacion_juntas2)
    sld_angulo_2.on_changed(actualizacion_juntas3)
    
    plt.show()

    return X_3,Y_3,Z_3,sld_angulo_1,sld_angulo_2


e1=tk.Label(ventana,text="Coordenada en X: ",bg="#2DE0AE",fg="#2F3257")
e1.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e2=tk.Label(ventana,text="Coordenada en Y: ",bg="#2DE0AE",fg="#2F3257")
e2.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada2=tk.Entry(ventana)
entrada2.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e3=tk.Label(ventana,text="Coordenada en Z: ",bg="#2DE0AE",fg="#2F3257")
e3.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada3=tk.Entry(ventana)
entrada3.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

calc=tk.Button(ventana,text="Calcular",fg="#2F3257",command=oper)
calc.pack(side=tk.TOP)


tab_control = ttk.Notebook(ventana)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Datos de excel')
tab_control.pack(expand=1, fill='both')


frame1 = Frame(tab1, bg='#6DBFD3')
frame1.grid(column=0,row=0,sticky='nsew')
frame2 = Frame(tab1, bg='#6DBFD3')
frame2.grid(column=0,row=1,sticky='nsew')

frame1.columnconfigure(0, weight = 1)
frame1.rowconfigure(0, weight= 1)

frame2.columnconfigure(0, weight = 1)
frame2.rowconfigure(0, weight= 1)
frame2.columnconfigure(1, weight = 1)
frame2.rowconfigure(0, weight= 1)

frame2.columnconfigure(2, weight = 1)
frame2.rowconfigure(0, weight= 1)

frame2.columnconfigure(3, weight = 2)
frame2.rowconfigure(0, weight= 1)

tabla = ttk.Treeview(frame1 , height=10)
tabla.grid(column=0, row=0, sticky='nsew')

ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
ladox.grid(column=0, row = 1, sticky='ew') 

ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
ladoy.grid(column = 1, row = 0, sticky='ns')

tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

estilo = ttk.Style(frame1)
estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
estilo.configure(".",font= ('Sylfaen', 14), foreground='blue')
estilo.configure("Treeview", font= ('Helvetica', 12), foreground='black',  background='white')
estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

def datos_excel():
    datos_obtenidos = indica['text']
    try:
        archivoexcel = r'{}'.format(datos_obtenidos)
        df = pd.read_excel(archivoexcel)

    except ValueError:
        messagebox.showerror('Informacion', 'Formato incorrecto')
        return None

    except FileNotFoundError:
        messagebox.showerror('Informacion', 'Archivo corrupto')
        return None

    Limpiar()

    tabla['column'] = list(df.columns)
    tabla['show'] = "headings"  #encabezado
    
    for columna in tabla['column']:
        tabla.heading(columna, text= columna)

    df_fila = df.to_numpy().tolist()
    for fila in df_fila:
        tabla.insert('', 'end', values =fila)

def Limpiar():
    tabla.delete(*tabla.get_children())

boton1 = Button(frame2, text= 'Abrir', command= abrir_archivo)
boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

boton2 = Button(frame2, text= 'Mostrar', command= datos_excel)
boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

boton3 = Button(frame2, text= 'Limpiar',  command= Limpiar)
boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)


indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Sylfaen',10,'bold') )
indica.grid(column=3, row = 0)

def operaciones(T_2,HR_1,P_1):

    global pvs,pv,W,Ws,u,Veh,Tpr,h_1,Tw,T_1,pvs_1,Ws_1,y
    
    return pv


def graficacion():
    a = np.arange(-10, 0, 1) # inicio, final (excluido), paso
    

"""
def B1():
    resultado.delete('1.0', tk.END)
    for i in range(0,canti):
            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            print("\nPvs: ",pvs)
            resultado.insert(tk.INSERT,
            f"Pvs = {pvs:.4f} kPa \n")
"""
def B9():
    ventana.quit()
    ventana.destroy() 

def B11():
    plt.clf()


def B20():
    ventana.quit()
    ventana.destroy()

ventana.mainloop()