# Espericueta Fonseca Fernando Simón. Mecatrónoca 6to 6.
# Cinemática de robots

# Importación de libreráis
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import tkinter

print("Programado por: Fernando Espericueta")
# Definimos las función de rotación sobre el eje z
def rotacion_z(grados, datos, line):
	# Conversión de grados a radianes
	rad = grados/180*np.pi

	# Definimos la matriz de rotación correspndiente para el eje z 
	matriz_rotacion_z = np.array([[np.cos(rad), -np.sin(rad), 0],
								  [np.sin(rad),  np.cos(rad), 0],
								  [    0      ,      0      , 1]])

	# Se actualiza la posición de los datos de la línea
	datos = matriz_rotacion_z @ datos
	
	# Toma los datos en x e y para graficarlos
	line.set_data(datos[0], datos[1])
	# Toma los datos en z para graficarlos
	line.set_3d_properties(datos[2])
	# devuleve los valores de la variable line
	return line

# Definimos la función de rotación sobre el eje y
def rotacion_y(grados, datos, line):
	# Converaión de grados a radianes
	rad = grados/180*np.pi

	# Definimos la matriz de rotación correspondiente para el eje y
	matriz_rotacion_y = np.array([[np.cos(rad),     0, -np.sin(rad)],
								  [    0      ,     1,      0      ],
								  [np.sin(rad),     0,  np.cos(rad)]])

	# Se actualizan la posición de los datos de la linea
	datos = matriz_rotacion_y @ datos
	# Toma los datos en x e y para graficarlos
	line.set_data(datos[0], datos[1])
	# Toma los datos en z para graficarlos
	line.set_3d_properties(datos[2])
	# Devuelve los valores de la variable line
	return line

# Definimos la función de rotación sobre el eje x
def rotacion_x(grados, datos, line):
	# Conversión de grados a radianes
	rad = grados/180*np.pi

	# Definimos la matriz de rotación correspondiente para el je x
	matriz_rotacion_x = np.array([[    1,     0,            0      ],
								  [    0, np.cos(rad), -np.sin(rad)],
								  [    0, np.sin(rad),  np.cos(rad)]])

	# Se actualiza la posición de los datos de la línea
	datos = matriz_rotacion_x @ datos
	# Toma los datos en x e y para graficarlos
	line.set_data(datos[0], datos[1])
	# Toma los datos en z para graficarlos
	line.set_3d_properties(datos[2])
	# Devuelve los valores de la variable line
	return line

# Se define la función para generar las figuras
def figuras(a):

	plt.close()
	# Declaramos la figura
	fig = plt.figure()
	ax = Axes3D(fig)

	# Declaramos los datos de la función 
	z = np.linspace(0,30,100)
	x = np.sin(z)*30
	y = np.cos(z)*30

	# Se declara el vector que contiene los datos en x, y y z
	datos = np.array([x,y,z])
	grados = 360
	# Se grafica la línea
	line = plt.plot(datos[0],datos[1],datos[2])[0]
	# Propiedades de los ejes
	ax.set_xlim(-30,30)
	ax.set_ylim(-30,30)
	ax.set_zlim(0,30)

	ax.set_xlabel("x(t)")
	ax.set_ylabel("y(t)")
	ax.set_zlabel("z(t)")

	# Sentencia if para la selección del la rotación en el eje deseado
	if a == 1:
		line_ani = animation.FuncAnimation(fig, rotacion_z, frames = grados, fargs = (datos,line), interval = 1, repeat = False, blit = False)
	elif a == 2:
		line_ani = animation.FuncAnimation(fig, rotacion_y, frames = grados, fargs = (datos,line), interval = 1, repeat = False, blit = False)
	else:
		line_ani = animation.FuncAnimation(fig, rotacion_x, frames = grados, fargs = (datos,line), interval = 1, repeat = False, blit = False)
	# Se muestra la animación
	plt.show()

# Se crea una ventana
ventana = tkinter.Tk()
# Se le dan medidas a la ventana
ventana.geometry("120x200")
# De le da color a la ventana
ventana.config(bg = "#256")

# Se crea el botón 1
boton1 = tkinter.Button(ventana, text = "Rotación z", command = lambda:figuras(1))
# Se coloca el botón en la posición deseada
boton1.place(x=30, y=30)
# Se le da color al botón
boton1.config(bg = "blue")

# Se crea el botón 2
boton2 = tkinter.Button(ventana, text = "Rotación y", command = lambda:figuras(2))
# Se coloca el botón 2 en la posición deseada
boton2.place(x=30, y=80)
# Se de la color al botón 2
boton2.config(bg = "red")

# Se crea el botón 3
boton3 = tkinter.Button(ventana, text = "Rotación x", command = lambda:figuras(3))
# Se coloca el botón 3 en la posoción deseada
boton3.place(x=30, y=130)
# Se le da color al botón 3
boton3.config(bg = "green")

# Se muestra le ventana creada todo el tiempo
ventana.mainloop()

print("Programado por: Fernando Espericueta")