import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

def configuracion_grafica():
	plt.title('Carta psicrométrica') # Nombre de la figura
	plt.xlabel('Temperatura de bulbo seco, [°C]') # Nombre del eje X
	plt.ylabel('Y') # Nombre del eje Y
	plt.xlim(0,50) # Límites del eje X
	plt.ylim(0,0.1) # Límites del eje Y
	plt.twinx().set_ylabel('Razón de humedad, W [kg vapor/kg aire seco]',x=0,y=0.5) # Mover escala
	#plt.twinx().set_ylim(0,50)

data = pd.read_excel(r'C:/Users/jymcl/Downloads/Tablas ASME - Copy.xlsx') #C:\Users\luis_\Downloads\

dT = pd.DataFrame(data, columns=['T']) # Temperature

dPsat = pd.DataFrame(data, columns=['Psat']) # Psat

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
dh = pd.DataFrame(data,columns=['h']).to_numpy() # Entalpía

print(dh)
results = list(map(float, dh))
results_2 = np.array(results)
print(results_2)

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


def conectar(dtwh,dtg,dyasat,dya,indice):
	dtwh_ = dtwh[indice]
	dtg_ = dtg[indice]
	dyasat_ = dyasat[indice]
	dya_ = dya[indice]
	plt.plot([dtwh_,dtg_],[dyasat_,dya_],'k',label='line 2',linewidth=0.7)

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


def tbs(dtwh,dtg,dya,dyasat,indice):
	dtwh_ = dtwh[indice]
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

def h(dtwh,dh,dya,dyasat,indice):
	dtwh_ = dtwh[indice]
	dh_ = dh[indice]
	dya_ = dya[indice]
	dyasat_ = dyasat[indice]
	plt.plot([dtwh_,dh_],[dya_,dyasat_],'#1C2F5E',label='line 3',linewidth=0.7)

h(dTwh,dh,dYASAT,dYA,0)
h(dTwh,dh,dYASAT,dYA,1)
h(dTwh,dh,dYASAT,dYA,2)
h(dTwh,dh,dYASAT,dYA,3)
h(dTwh,dh,dYASAT,dYA,4)
h(dTwh,dh,dYASAT,dYA,5)
h(dTwh,dh,dYASAT,dYA,6)
h(dTwh,dh,dYASAT,dYA,7)
h(dTwh,dh,dYASAT,dYA,8)
h(dTwh,dh,dYASAT,dYA,9)
h(dTwh,dh,dYASAT,dYA,10)
h(dTwh,dh,dYASAT,dYA,11)
h(dTwh,dh,dYASAT,dYA,12)
h(dTwh,dh,dYASAT,dYA,13)
h(dTwh,dh,dYASAT,dYA,14)
h(dTwh,dh,dYASAT,dYA,15)
h(dTwh,dh,dYASAT,dYA,16)
h(dTwh,dh,dYASAT,dYA,17)
h(dTwh,dh,dYASAT,dYA,18)


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

Tw = T * math.atan(0.151977*((HR*100)+8.313659)**0.5)+math.atan(T+(HR*100))-math.atan((HR*100)-1.676331)+(0.00391838*((HR*100)**1.5))*math.atan(0.023101*(HR*100))-4.686035
print(Tw)

W /=1000

T_1 = Tw+273.15
pvs_1 = math.exp(A1/T_1 + A2 + A3*T_1 + A4*T_1**2 + A5*T_1**3 + A6*T_1**4 + A7*math.log(T_1))
pvs_1 /=1000
Ws_1 = 0.622*(pvs_1/(p-pvs_1))
print(Ws_1)

plt.scatter(T,W,color='red',linewidth=3) # Punto
plt.plot([T,T],[W,0],'r-',label='Tw',linewidth=3) # T (baja)
plt.plot([T,100],[W,W],'r-',label='W',linewidth=3) # W (derecha) 
plt.plot([T,Tpr],[W,W],'r-',label='W',linewidth=3) # Tpr (izquierda)
plt.plot([Tpr,Tpr],[W,0],'r-',label='W',linewidth=3) # Tpr (baja)
plt.plot([T,Tw],[W,Ws_1],'r-',label='W',linewidth=3) # Tw (sube) y_punto rocío = Es la W al 100% de humedad
plt.plot([Tw,Tw],[0,Ws_1],'r-',label='Tw',linewidth=3) # Tw (baja) y_punto rocío = Es la W al 100% de humedad
plt.plot([T,T],[Ws,W],'r-',label='Ws',linewidth=3) # Ws (sube) 
plt.plot([T,100],[Ws,Ws],'r-',label='Ws',linewidth=3) # Ws (derecha) 
plt.plot([h,0],[0,Ws],'g-',label='h',linewidth=3) # h 

configuracion_grafica()
plt.show()
