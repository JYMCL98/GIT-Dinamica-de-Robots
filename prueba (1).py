import pandas as pd
import matplotlib.pyplot as plt
import math

def configuracion_grafica():
	plt.title('Carta psicrométrica') # Nombre de la figura
	plt.xlabel('Temperatura de bulbo seco, [°C]') # Nombre del eje X
	plt.ylabel('Y') # Nombre del eje Y
	plt.xlim(0,50) # Límites del eje X
	plt.ylim(0,0.1) # Límites del eje Y

#from matplotlib.collections import LineCollection

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
data = pd.read_excel(r'C:\Users\luis_\Documents\MATLAB\Tablas ASME.xlsx') # Cambiar ruta del archivo
dT = pd.DataFrame(data, columns=['T']) # Temperature
#print(dT) # len = 13, 0-12

dPsat = pd.DataFrame(data, columns=['Psat']) # Psat
#print(dPsat) # len = 13, 0-12

# HUMEDAD RELATIVA, %

#dHR100 = pd.DataFrame(data, columns=['HR100'])
#print(dHR100) 

#dHR90 = pd.DataFrame(data, columns=['HR90'])
#dHR80 = pd.DataFrame(data, columns=['HR80'])
#dHR70 = pd.DataFrame(data, columns=['HR70'])
#dHR60 = pd.DataFrame(data, columns=['HR60'])
#dHR50 = pd.DataFrame(data, columns=['HR50'])
#dHR40 = pd.DataFrame(data, columns=['HR40'])
#dHR30 = pd.DataFrame(data, columns=['HR30'])
#dHR20 = pd.DataFrame(data, columns=['HR20'])
#dHR10 = pd.DataFrame(data, columns=['HR10'])

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


plt.plot(dT,dHA100,'k',label='Humedad absoluta',linewidth=0.7)
plt.plot(dT,dHA90,'k',label='Humedad absoluta',linewidth=0.7)
plt.plot(dT,dHA80,'k',label='Humedad absoluta',linewidth=0.7)
plt.plot(dT,dHA70,'k',label='Humedad absoluta',linewidth=0.7)
plt.plot(dT,dHA60,'k',label='Humedad absoluta',linewidth=0.7)
plt.plot(dT,dHA50,'k',label='Humedad absoluta',linewidth=0.7)
plt.plot(dT,dHA40,'k',label='Humedad absoluta',linewidth=0.7)
plt.plot(dT,dHA30,'k',label='Humedad absoluta',linewidth=0.7)
plt.plot(dT,dHA20,'k',label='Humedad absoluta',linewidth=0.7)
plt.plot(dT,dHA10,'k',label='Humedad absoluta',linewidth=0.7)

#plt.scatter(x,y)
#plt.scatter(dTwh,dYASAT,color='blue')
#plt.scatter(dTG,dYA,color='green')

# Tomar datos de uno en uno
# 
def conectar(dtwh,dtg,dyasat,dya,indice):
	dtwh_ = dtwh[indice]
	dtg_ = dtg[indice]
	dyasat_ = dyasat[indice]
	dya_ = dya[indice]
	plt.plot([dtwh_,dtg_],[dyasat_,dya_],'m-',label='line 2',linewidth=0.7)

"""
dTwh0 = dTwh[0]
dTG0 = dTG[0]
dYASAT0 = dYASAT[0]
dYA0 = dYA[0]

plt.plot([dTwh0,dTG0],[dYASAT0,dYA0],'m-')


dTwh1 = dTwh[1]
dTG1 = dTG[1]
dYASAT1 = dYASAT[1]
dYA1 = dYA[1]

plt.plot([dTwh1,dTG1],[dYASAT1,dYA1],'m-')


dTwh2 = dTwh[2]
dTG2 = dTG[2]
dYASAT2 = dYASAT[2]
dYA2 = dYA[2]

plt.plot([dTwh2,dTG2],[dYASAT2,dYA2],'m-')



dTwh3 = dTwh[3]
dTG3 = dTG[3]
dYASAT3 = dYASAT[3]
dYA3 = dYA[3]

plt.plot([dTwh3,dTG3],[dYASAT3,dYA3],'m-')


"""
conectar(dTwh,dTG,dYASAT,dYA,0)
conectar(dTwh,dTG,dYASAT,dYA,1)
conectar(dTwh,dTG,dYASAT,dYA,2)
conectar(dTwh,dTG,dYASAT,dYA,3)
conectar(dTwh,dTG,dYASAT,dYA,4)
conectar(dTwh,dTG,dYASAT,dYA,5)
conectar(dTwh,dTG,dYASAT,dYA,6)
conectar(dTwh,dTG,dYASAT,dYA,7)
conectar(dTwh,dTG,dYASAT,dYA,8)
conectar(dTwh,dTG,dYASAT,dYA,9)
conectar(dTwh,dTG,dYASAT,dYA,10)
conectar(dTwh,dTG,dYASAT,dYA,11)
conectar(dTwh,dTG,dYASAT,dYA,12)
conectar(dTwh,dTG,dYASAT,dYA,13)
conectar(dTwh,dTG,dYASAT,dYA,14)
conectar(dTwh,dTG,dYASAT,dYA,15)
conectar(dTwh,dTG,dYASAT,dYA,16)
conectar(dTwh,dTG,dYASAT,dYA,17)

#for i,j in zip(dTwh,dYASAT):
#	plt.scatter(i,j)


#for k,l in zip(dTG,dYA):
#	plt.scatter(k,l)



def tbs(dtwh,dtg,dya,dyasat,indice):
	dtwh_ = dtwh[indice]
	#dtg_ = dtg[indice]
	dya_ = dya[indice]
	dyasat_ = dyasat[indice]
	plt.plot([dtwh_,dtwh_],[dya_,dyasat_],'r-',label='line 3',linewidth=0.7)


tbs(dTwh,dTwh,dYA,dYASAT,0)
tbs(dTwh,dTwh,dYA,dYASAT,1)
tbs(dTwh,dTwh,dYA,dYASAT,2)
tbs(dTwh,dTwh,dYA,dYASAT,3)
tbs(dTwh,dTwh,dYA,dYASAT,4)
tbs(dTwh,dTwh,dYA,dYASAT,5)
tbs(dTwh,dTwh,dYA,dYASAT,6)
tbs(dTwh,dTwh,dYA,dYASAT,7)
tbs(dTwh,dTwh,dYA,dYASAT,8)
tbs(dTwh,dTwh,dYA,dYASAT,9)
tbs(dTwh,dTwh,dYA,dYASAT,10)
tbs(dTwh,dTwh,dYA,dYASAT,11)
tbs(dTwh,dTwh,dYA,dYASAT,12)
tbs(dTwh,dTwh,dYA,dYASAT,13)
tbs(dTwh,dTwh,dYA,dYASAT,14)
tbs(dTwh,dTwh,dYA,dYASAT,15)
tbs(dTwh,dTwh,dYA,dYASAT,16)
tbs(dTwh,dTwh,dYA,dYASAT,17)
tbs(dTwh,dTwh,dYA,dYASAT,18)



def W(dtwh,dtg,dya,dyasat,indice):
	dtwh_ = dtwh[indice]
	dtg_ = dtg[18]
	dya_ = dya[indice]
	dyasat_ = dyasat[indice]

	plt.plot([dtwh_,dtg_],[dyasat_,dya_],'g-',label='line 3',linewidth=0.7)

W(dTwh,dTG,dYA,dYASAT,0)
W(dTwh,dTG,dYA,dYASAT,1)
W(dTwh,dTG,dYA,dYASAT,2)
W(dTwh,dTG,dYA,dYASAT,3)
W(dTwh,dTG,dYA,dYASAT,4)
W(dTwh,dTG,dYA,dYASAT,5)
W(dTwh,dTG,dYA,dYASAT,6)
W(dTwh,dTG,dYA,dYASAT,7)
W(dTwh,dTG,dYA,dYASAT,8)
W(dTwh,dTG,dYA,dYASAT,9)
W(dTwh,dTG,dYA,dYASAT,10)
W(dTwh,dTG,dYA,dYASAT,11)
W(dTwh,dTG,dYA,dYASAT,12)
W(dTwh,dTG,dYA,dYASAT,13)
W(dTwh,dTG,dYA,dYASAT,14)
W(dTwh,dTG,dYA,dYASAT,15)
W(dTwh,dTG,dYA,dYASAT,16)
W(dTwh,dTG,dYA,dYASAT,17)
W(dTwh,dTG,dYA,dYASAT,18)

T = 20
HR = 0.5

p = 101.325 # kPa presión atmosférica a nivel del mar
Ra = 287.055 # J/kg*K, constante del gas, del aire seco



if -100<T<0:
	A1 = -5.6745359e3
	A2 = 6.3925247e0
	A3 = -9.677843e-03
	A4 = 0.6221570e-06
	A5 = 2.0747825e-09
	A6 = -0.94844024e-12
	A7 = 4.1635019e00



if 0<T<200:
	A1 = -5.8002206e3
	A2 = 1.3914993e00
	A3 = -48.640239e-03
	A4 = 41.764768e-06
	A5 = -14.452093e-09
	A6 = 0.0
	A7 = 6.5459673e00

T = T+273.15 # Kelvin
pvs = math.exp(A1/T + A2 + A3*T + A4*T**2 + A5*T**3 + A6*T**4 + A7*math.log(T))
pvs = pvs/1000 # presión parcial de vapor de agua a saturación, kPa
print(f"pvs = {pvs}")

pv = HR*pvs # presión parcial de vapor de agua, kPa
print(f"pv = {pv}")

W = 0.622*(pv/(p-pv))
W = W*1000 # razón de humedad, g de vapor de agua/kg de aire seco
print(f"W = {W}")


Ws = 0.622*(pvs/(p-pvs)) # Razón de humedad de saturación, kg vapor de agua/kg de aire seco
print(f"Ws = {Ws}")
u = (W/1000)/Ws # Grado de saturación del aire
print(f"u = {u}")


Veh = ((Ra*T)/(p*1000))*((1+1.6078*(W/1000))/(1+(W/1000))) # Volumen específico del aire húmedo, m^3/kg de aire
print(f"Veh = {Veh:.3f}")

T = T-273.15
pv=pv*1000
if 0<T<70:
	Tpr=-35.957-1.8726*math.log(pv)+1.1689*((math.log(pv))**2)
elif -60<T<0:
	Tpr = -60.45 + 7.0322*math.log(pv)+0.37*(math.log(pv)**2)
print(f"Tpr = {Tpr}") # Temperatura del punto de rocío, °C

pv=pv/1000

h = 1.006*T + (W/1000)*(2501+1.805*T) # Entalpía, kJ/kg
print(f"h = {h}")


W /=1000

print(W)
print(T)

plt.scatter(T,W,color='red',linewidth=5)
plt.plot([dTwh,dTG],[W,dYA],'r-',label='W',linewidth=5)


configuracion_grafica()
plt.show()
