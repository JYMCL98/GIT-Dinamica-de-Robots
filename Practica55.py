"""
import cv2
import numpy as np

video = cv2.VideoCapture(1)
cm_por_pixel_x = 13.1/640.0 # entre pixeles de largo
cm_por_pixel_y = 9.7/480.0

while True:
	_,frame = video.read()
	img_grises = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow("background",img_grises)

	k = cv2.waitKey(5)
	if k == 27:
		break


while True:
	_,frame = video.read()
	img_grises2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	cv2.imshow("foreground",img_grises2)

	diferencia = np.absolute(np.matrix(np.int16(img_grises))-np.matrix(np.int16(img_grises2)))
	diferencia[diferencia>255]=255
	diferencia=np.uint8(diferencia)
	cv2.imshow("Diferencia imagenes",diferencia)

	Diff = diferencia
	Diff[Diff<=100]=0
	Diff[Diff>100]=1

# Localización en x
	suma_columnas = np.matrix(np.sum(Diff,0)) # se suman las comlumnas
# enumero cada uno de los elementos de la matriz
	columna_numeracion = np.matrix(np.arange(640)) # resolución de la cámara
	columna_multiplicacion = np.multiply(suma_columnas,columna_numeracion)
	total = np.sum(columna_multiplicacion)
	total_total = np.sum(np.sum(Diff))
	localizacion_columna = total/total_total

	x_localizacion = localizacion_columna*cm_por_pixel_x

	print(f"Localizacion x: {x_localizacion}")


	# Localización en y
	suma_filas = np.matrix(np.sum(Diff,1)) # se suman las comlumnas
	suma_filas=suma_filas.transpose()
	# enumero cada uno de los elementos de la matriz
	fila_numeracion = np.matrix(np.arange(640)) # resolución de la cámara
	fila_multiplicacion = np.multiply(suma_columnas,columna_numeracion)
	total = np.sum(fila_multiplicacion)
	total_total = np.sum(np.sum(Diff))
	localizacion_fila = total/total_total

	y_localizacion = localizacion_fila*cm_por_pixel_y

	print(f"Localizacion y: {y_localizacion}")




	k = cv2.waitKey(5)
	if k == 27:
		break

cv2.destroyAllWindows()

"""
############################################################################
import cv2
import numpy as np

video = cv2.VideoCapture(1)
ancho = 640 #x
alto = 802 #y

cm_por_pixel_x = 19/ancho # cm/pixeles largo
cm_por_pixel_y = 14/alto # ancho

while True:
    __,frame = video.read()
    imagen_grises = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Background",imagen_grises)

    
    if cv2.waitKey(1) == 27:
        break

while True:
    __,frame = video.read()
    imagen_grises2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Foreground",imagen_grises2)

    diferencia_imagenes = np.absolute(np.matrix(np.int16(imagen_grises))-np.matrix(np.int16(imagen_grises2)))
    diferencia_imagenes[diferencia_imagenes>255]=255
    diferencia_imagenes=np.uint8(diferencia_imagenes)
    cv2.imshow("diferencia_imagenes",diferencia_imagenes)    
    
    
    Diff = diferencia_imagenes
    Diff[Diff<=100]=0
    Diff[Diff>100]=1

    columnaSuma=np.matrix(np.sum(Diff,0))
    #ENUMERAR CADA UNO DE LOS ELEMENTOS
    columnaNum=np.matrix(np.arange(ancho))
    columnaMult=np.multiply(columnaSuma,columnaNum)
    total=np.sum(columnaMult)
    totalTotal=np.sum(np.sum(Diff))
    columnaLocal=total/totalTotal
    print(f"columna: {columnaLocal}")

    x_localizacion = columnaLocal*cm_por_pixel_x

    filaSuma=np.matrix(np.sum(Diff,1))
    filaSuma = filaSuma.transpose()
    #ENUMERAR CADA UNO DE LOS ELEMENTOS
    filaNum=np.matrix(np.arange(480))
    filaMult=np.multiply(filaSuma,filaNum)
    total=np.sum(filaMult)
    totalTotal=np.sum(np.sum(Diff))
    filaLocal=total/totalTotal
    print(f"fila: {filaLocal}")

    y_localizacion = filaLocal*cm_por_pixel_y
    print("       x                  y")
    print(x_localizacion,y_localizacion)

    
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

#print("Fin del programa escrito por Luis Ángel Sánchez Rodríguez 6°7 Mecatrónica")