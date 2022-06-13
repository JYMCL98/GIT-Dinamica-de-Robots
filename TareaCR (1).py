
import numpy as np  # Importamos la librería numpy
import matplotlib.pyplot as plt  #Importamos la librería matplotlib como plt
import matplotlib.animation as animation  # Importamos la librería matplotlib como animation
from mpl_toolkits.mplot3d import Axes3D #Importamos la librería Axes3D
import tkinter as tk  # Importamos la librería tkinter como tk
from tkinter import ttk  # Importamos ttk

#Declaramos los datos de la función
z = np.linspace(0,30,100) #Genera una línea del 0 al 30
x = np.sin(z) # Función seno (z)
y = np.cos(z) # Función cos (z)




# Z
def rotacion_z(grados_z,datos_z,line_z): #Definimos la función de rotación en z
	rad = grados_z/180*np.pi # Conversión a grados
	matriz_rotacion_z = np.array([[np.cos(rad), -np.sin(rad), 0], #Matriz de rotación primera columna
						  [np.sin(rad),  np.cos(rad), 0], #Matriz de rotación segunda fila
						  [          0,            0, 1]]) #Matriz de rotación terca fila

	datos_z = matriz_rotacion_z @ datos_z #Multiplicación de matrices
	#Actualizo la posición de los datos de la línea
	line_z.set_data(datos_z[0],datos_z[1])# Datos en x,y
	line_z.set_3d_properties(datos_z[2])#Datos en z
	return line_z #Devuelvo la linea en z


# X
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

# Y
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



# Funciones de los botones
def boton1():  # Definimos una función la cual sera mandada a llamar posteriormente
    # Agregar figura
    fig_z = plt.figure()  # Declaramos una figura
    ax_z = Axes3D(fig_z)  # Establecemos que la figura es en 3D
    datos_z = np.array(
        [x, y, z]
    )  # Asiganos una matriz con los valores de la función para cada variable
    grados_z = 360  # Establecemos que gira 360 grados
    line_z = plt.plot(datos_z[0], datos_z[1], datos_z[2])[
        0
    ]  # Definimos el "resorte" que se graficará en los ejes x, y, z

    # Propiedades de los ejes
    ax_z.set_xlim(-1, 1)  # Establecemos los limites del eje x
    ax_z.set_ylim(-1, 1)  # Establecemos los limites del eje y
    ax_z.set_zlim(0, 30)  # Establecemos los limites del eje z
    
    ax_z.set_xlabel("x(t)")  # Establecemos el nombre del eje x
    ax_z.set_ylabel("y(t)")  # Establecemos el nombre del eje y
    ax_z.set_zlabel("z(t)")  # Establecemos el nombre del eje z

    line_ani_z = animation.FuncAnimation(  # Definimos la animacion en el eje x
        fig_z,  # La figura a animar
        rotacion_z,  # La función de rotación a seguir
        frames=grados_z,  # Los grados a rotar
        fargs=(datos_z, line_z),  # Los datos para graficar
        interval=50,  # El intervalo de animación (tiempo)
        repeat=True,  # La repetición
        blit=False,  # La posición
    )
    plt.show()  # Mostramos la gráfica animada


def boton2():  # Definimos una función la cual sera mandada a llamar posteriormente
    # Agregar figura
    fig_x = plt.figure()  # Declaramos una figura
    ax_x = Axes3D(fig_x)  # Establecemos que la figura es en 3D
    datos_x = np.array(
        [x, y, z]
    )  # Asiganos una matriz con los valores de la función para cada variable
    grados_x = 360  # Establecemos que gira 360 grados
    line_x = plt.plot(datos_x[0], datos_x[1], datos_x[2])[
        0
    ]  # Definimos el "resorte" que se graficará en los ejes x, y, z

    # Propiedades de los ejes
    ax_x.set_xlim(-30, 30)  # Establecemos los limites del eje x
    ax_x.set_ylim(-30, 30)  # Establecemos los limites del eje y
    ax_x.set_zlim(-30, 30)  # Establecemos los limites del eje z
    
    ax_x.set_xlabel("x(t)")  # Establecemos el nombre del eje x
    ax_x.set_ylabel("y(t)")  # Establecemos el nombre del eje y
    ax_x.set_zlabel("z(t)")  # Establecemos el nombre del eje z

    line_ani_x = animation.FuncAnimation(  # Definimos la animacion en el eje y
        fig_x,  # La figura a animar
        rotacion_x,  # La función de rotación a seguir
        frames=grados_x,  # Los grados a rotar
        fargs=(datos_x, line_x),  # Los datos para graficar
        interval=50,  # El intervalo de animación (tiempo)
        repeat=True,  # La repetición
        blit=False,  # La posición
    )
    plt.show()  # Mostramos la gráfica animada


def boton3():  # Definimos una función la cual sera mandada a llamar posteriormente
    fig_y = plt.figure()  # Declaramos una figura
    ax_y = Axes3D(fig_y)  # Establecemos que la figura es en 3D
    datos_y = np.array(
        [x, y, z]
    )  # Asiganos una matriz con los valores de la función para cada variable
    grados_y = 360  # Establecemos que gira 360 grados
    line_y = plt.plot(datos_y[0], datos_y[1], datos_y[2])[
        0
    ]  # Definimos el "resorte" que se graficará en los ejes x, y, z

    # Propiedades de los ejes
    ax_y.set_xlim(-30, 30)  # Establecemos los limites del eje x
    ax_y.set_ylim(-30, 30)  # Establecemos los limites del eje y
    ax_y.set_zlim(-30, 30)  # Establecemos los limites del eje z
    
    ax_y.set_xlabel("x(t)")  # Establecemos el nombre del eje x
    ax_y.set_ylabel("y(t)")  # Establecemos el nombre del eje y
    ax_y.set_zlabel("z(t)")  # Establecemos el nombre del eje z

    line_ani_y = animation.FuncAnimation(  # Definimos la animacion en el eje z
        fig_y,  # La figura a animar
        rotacion_y,  # La función de rotación a seguir
        frames=grados_y,  # Los grados a rotar
        fargs=(datos_y, line_y),  # Los datos para graficar
        interval=50,  # El intervalo de animación (tiempo)
        repeat=False,  # La repetición
        blit=False,  # La posición
    )
    plt.show()  # Mostramos la gráfica animada


def cerrar():  # Definimos una función la cual sera mandada a llamar posteriormente
    ventana.quit()  # Salimos de la ventana
    ventana.destroy()  # Cerramos cualquier otra ventana abierta


# Formato de la ventana
ventana = tk.Tk()  # Definimos una nueva ventana con ayuda de tkinter
ventana.geometry("700x250")  # Establecemos las dimensiones de la ventana
ventana.title("Cinemática de robots")  # Establecemos el nombre de la ventana
ventana["bg"] = "#3AF71B"  # Establecemos el color de fondo de la ventana


# Etiquetas
etiqueta = ttk.Label(  # Creamos una nueva etiqueta
    ventana,  # La colocamos en la ventana creada anteriormente
    text=" ",  # Establecemos el texto de la etiqueta
    background="#3AF71B",  # Establecemos el color de fondo de la etiqueta
    font=("Arial", 15),  # Establecemos el tipo y tamaño de letra
)
etiqueta.grid(row=0, column=1)  # Ubicamos la etiqueta en base a filas y columnas
etiqueta = ttk.Label(  # Creamos una nueva etiqueta
    ventana,  # La colocamos en la ventana creada anteriormente
    text="Luis Ángel Sánchez Rodríguez",  # Establecemos el texto de la etiqueta
    background="#3AF71B",  # Establecemos el color de fondo de la etiqueta
    font=("Arial", 15),  # Establecemos el tipo y tamaño de letra
)
etiqueta.grid(row=1, column=0)  # Ubicamos la etiqueta en base a filas y columnas
etiqueta = ttk.Label(  # Creamos una nueva etiqueta
    ventana,  # La colocamos en la ventana creada anteriormente
    text="6°7 Mecatrónica",  # Establecemos el texto de la etiqueta
    background="#3AF71B",  # Establecemos el color de fondo de la etiqueta
    font=("Arial", 15),  # Establecemos el tipo y tamaño de letra
)
etiqueta.grid(row=1, column=1)  # Ubicamos la etiqueta en base a filas y columnas
etiqueta = ttk.Label(  # Creamos una nueva etiqueta
    ventana,  # La colocamos en la ventana creada anteriormente
    text="Matrícula:",  # Establecemos el texto de la etiqueta
    background="#3AF71B",  # Establecemos el color de fondo de la etiqueta
    font=("Arial", 15),  # Establecemos el tipo y tamaño de letra
)
etiqueta.grid(row=2, column=0)  # Ubicamos la etiqueta en base a filas y columnas
etiqueta = ttk.Label(  # Creamos una nueva etiqueta
    ventana,  # La colocamos en la ventana creada anteriormente
    text="1512361-8",  # Establecemos el texto de la etiqueta
    background="#3AF71B",  # Establecemos el color de fondo de la etiqueta
    font=("Arial", 15),  # Establecemos el tipo y tamaño de letra
)
etiqueta.grid(row=2, column=1)  # Ubicamos la etiqueta en base a filas y columnas


# Botones
boton1 = tk.Button(  # Declaramos un nuevo botón
    ventana,  # Lo colocamos en la ventana creada
    text="Rotación en el eje z",  # Establecemos el texto del botón
    width=20,  # Establecemos el ancho del botón
    height=3,  # Establecemos la altura del botón
    bg="#0FA075",  # Establecemos el color de fondo del botón
    font=("Arial", 12),  # Establecemos el tipo y tamaño de letra
    command=boton1,  # Configuramos la función a ejecutar cuando el botón sea presionado
)
boton1.grid(row=3, column=0)  # Ubicamos el botón en base a filas y columnas


boton2 = tk.Button(  # Declaramos un nuevo botón
    ventana,  # Lo colocamos en la ventana creada
    text="Rotación en el eje x",  # Establecemos el texto del botón
    width=20,  # Establecemos el ancho del botón
    height=3,  # Establecemos la altura del botón
    bg="#0FA075",  # Establecemos el color de fondo del botón
    font=("Arial", 12),  # Establecemos el tipo y tamaño de letra
    command=boton2,  # Configuramos la función a ejecutar cuando el botón sea presionado
)
boton2.grid(row=3, column=1)  # Ubicamos el botón en base a filas y columnas

boton3 = tk.Button(  # Declaramos un nuevo botón
    ventana,  # Lo colocamos en la ventana creada
    text="Rotación en el eje y",  # Establecemos el texto del botón
    width=20,  # Establecemos el ancho del botón
    height=3,  # Establecemos la altura del botón
    bg="#0FA075",  # Establecemos el color de fondo del botón
    font=("Arial", 12),  # Establecemos el tipo y tamaño de letra
    command=boton3,  # Configuramos la función a ejecutar cuando el botón sea presionado
)
boton3.grid(row=3, column=2)  # Ubicamos el botón en base a filas y columnas


cerrar = tk.Button(  # Declaramos un nuevo botón
    ventana,  # Lo colocamos en la ventana creada
    text="Cerrar",  # Establecemos el texto del botón
    width=20,  # Establecemos el ancho del botón
    height=3,  # Establecemos la altura del botón
    bg="#0FA075",  # Establecemos el color de fondo del botón
    font=("Arial", 12),  # Establecemos el tipo y tamaño de letra
    command=cerrar,  # Configuramos la función a ejecutar cuando el botón sea presionado
)
cerrar.grid(row=4, column=1)  # Ubicamos el botón en base a filas y columnas


ventana.mainloop()  # Indica a la interfaz que debe quedarse esperando a que el usuario haga algo
