# Importamos las librerías
import cv2
import numpy as np
# import serial

# Configuración del puerto serial
# COM = "COM5"
# baud = 9600 # velocidad de transmisión de datos
# ser = serial.Serial(COM,baud) # Creamos una variable para la comunicación serial

video = cv2.VideoCapture(1) # Captura el video de la cámara del celular

class vision_colores():
    
    def __init__(self, cb1,cb2,cb3,ca1,ca2,ca3):
        self.colorbajo = np.array([cb1,cb2,cb3])
        self.coloralto = np.array([ca1,ca2,ca3])
    
    def deteccion(self):
        while True:
         	# Capturamos el video
         	ret,frame = video.read() 
         	# Si el video se captura correctamente, entonces:
         	if ret:
                 frame = cv2.flip(frame,0) # Volteamos la pantalla
                 frame = cv2.flip(frame,1) # Volteamos la pantalla
          		# Convertimos lo capturado a HSV (Hue, Saturation, Value)
                 frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
          		# Aplicamos una máscara pasando los valores bajos y altos del color
                 mascara = cv2.inRange(frameHSV,self.colorbajo,self.coloralto)
          		# Encontramos los contornos del objeto
                 contornos, __ = cv2.findContours(mascara,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
          		# Dibujamos los contornos
                 cv2.drawContours(frame,contornos,-1,(255,0,0),3) 
                 
                 for c in contornos:
                     area = cv2.contourArea(c)
                     if area > 600: # área del objeto
        				# Encontramos los momentos del objeto
                        M = cv2.moments(c)
                        if M["m00"] == 0:
                            M["m00"] = 1 # Igualamos a 1 ya que si dividimos entre 0 sería una indefinición
        				# Obtenemos coordenadas del objeto
                        x = int(M["m10"]/M["m00"])
                        y = int(M["m01"]/M["m00"])
                        
                        
        				# Dibujamos el círculo del centro del objeto y escribimos las coordenadas de este
                        cv2.circle(frame,(x,y),7,(0,0,255),-1) # Rellena el círculo
        				# Escribimos las coordenadas en pantalla
                        cv2.putText(frame,"{},{}".format(x,y),(x+10,y),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),2,cv2.LINE_AA)
                        nuevo_contorno = cv2.convexHull(c) # cierra los objetos para completar una figura
                        cv2.drawContours(frame,[nuevo_contorno],0,(255,0,0),3) # Dibuja los nuevos contornos
                
                 cv2.imshow("Video",frame) # Mostramos el video
                 if cv2.waitKey(1) & 0xFF == 27: # si presiona escape se sale del programa
                 			# ser.close()
                 			break
        
deteccion_azul = vision_colores(90, 100, 20, 120, 255, 255)

deteccion_azul.deteccion()

