import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
from openpyxl import load_workbook

#load excel file
workbook = load_workbook(filename="C:/Users/luis_/Documents/MATLAB/Tablas ASME.xlsx")

#open workbook
sheet = workbook.active

#modify the desired cell
p_atm = int(input("Presión atmosférica: ")) # multiplicar por 7.50062 para obtener mmHg
sheet["A2"] = p_atm

#save the file
workbook.save(filename="C:/Users/luis_/Documents/MATLAB/Tablas ASME.xlsx")
"""

# 
data = pd.read_excel(r'C:\Users\jymcl\Downloads\Tablas ASME.xlsx')
dT = pd.DataFrame(data, columns=['T']) # Temperature
#print(dT) # len = 13, 0-12

dPsat = pd.DataFrame(data, columns=['Psat']) # Psat
#print(dPsat) # len = 13, 0-12

# HUMEDAD RELATIVA, %

dHR100 = pd.DataFrame(data, columns=['HR100'])
#print(dHR100) 

dHR90 = pd.DataFrame(data, columns=['HR90'])
dHR80 = pd.DataFrame(data, columns=['HR80'])
dHR70 = pd.DataFrame(data, columns=['HR70'])
dHR60 = pd.DataFrame(data, columns=['HR60'])
dHR50 = pd.DataFrame(data, columns=['HR50'])
dHR40 = pd.DataFrame(data, columns=['HR40'])
dHR30 = pd.DataFrame(data, columns=['HR30'])
dHR20 = pd.DataFrame(data, columns=['HR20'])
dHR10 = pd.DataFrame(data, columns=['HR10'])

# Humedad absoluta, Kg vapor/Kg aire seco

dHA100 = pd.DataFrame(data, columns=['HA100'])
dHA90 = pd.DataFrame(data, columns=['HA90'])
dHA80 = pd.DataFrame(data, columns=['HA80'])
dHA70 = pd.DataFrame(data, columns=['HA70'])
dHA60 = pd.DataFrame(data, columns=['HA60'])
dHA50 = pd.DataFrame(data, columns=['HA50'])
dHA40 = pd.DataFrame(data, columns=['HA40'])
dHA30 = pd.DataFrame(data, columns=['HA30'])
dHA20 = pd.DataFrame(data, columns=['HA20'])
dHA10 = pd.DataFrame(data, columns=['HA10'])


dTwh = pd.DataFrame(data, columns=['Twh']).to_numpy()
#dcalor_latente = pd.DataFrame(data, columns=['calor'])
dYASAT = pd.DataFrame(data, columns=['YASAT']).to_numpy()
dYA = pd.DataFrame(data, columns=['YA']).to_numpy()
dTG = pd.DataFrame(data, columns=['TG']).to_numpy()


plt.plot(dT,dHA100,'k')
plt.plot(dT,dHA90,'k')
plt.plot(dT,dHA80,'k')
plt.plot(dT,dHA70,'k')
plt.plot(dT,dHA60,'k')
plt.plot(dT,dHA50,'k')
plt.plot(dT,dHA40,'k')
plt.plot(dT,dHA30,'k')
plt.plot(dT,dHA20,'k')
plt.plot(dT,dHA10,'k')

x1, y1 = [-1, 12], [1, 4]
x2, y2 = [1, 10], [3, 2]
plt.plot(70, 0.3, 80, 0, marker = "o")

#x = [80,70] # Las coordenadas de los dos puntos a conectar
#y = [0,0.3]

#for i in range(len(x)):

 #   plt.plot(x[i], y[i], color='r')
  #  plt.scatter(x[i], y[i], color='b')
   # print(x,y)


#for i in range(len(x)):

#    plt.plot(x[i], y[i], color='r')
#    plt.scatter(x[i], y[i], color='b')

#plt.scatter(dTwh,dYASAT, color = 'Blue')
#plt.scatter(dTG,dYA, color = 'Red')

# tomar datos de uno en uno
#x1_values = [dTwh[1],dYASAT[1]]
#y1_values = [dTG[1],dYA[1]]



#plt.plot(a,b,'blue')


#dTwh,dTG
#dYASAT,dYA


plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0,90)
plt.ylim(0,1.5)

plt.show()
