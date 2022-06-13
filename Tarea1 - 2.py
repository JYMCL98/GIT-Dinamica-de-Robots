# Universidad Autónoma Chapingo
# Parámetros psicrométricos
# Luis Ángel Sánchez Rodríguez
# 1512361-8
# 7° 7


# Librerías necesarias para el funcionamiento del programa
import matplotlib.pyplot as plt  # Importamos la librería matplotlib.pyplot y la igualamos con plt
import math # Librerías para funciones matemáticas
import numpy as np  # Importamos la librería numpy y la igualamos con np
import matplotlib.animation as animation  # Importamos la librería matplotlib.animation y la igualamos con animation
from mpl_toolkits.mplot3d import Axes3D  # De mpl_toolkits.mplot3d importamos Axes3D
import tkinter as tk  # Importamos la librería tkinter y la igualamos con tk
from tkinter import ttk  # De tkinter importamos ttk
from tkinter import messagebox
from tkinter import *
from tkinter import Tk 
from tkinter import Label
from tkinter import Button
from tkinter import Frame
from tkinter import filedialog
from tkinter import Scrollbar
from tkinter import VERTICAL
from tkinter import HORIZONTAL
from tkinter import Spinbox
from tkinter import scrolledtext as st
import pandas as pd


# Configuramos la gráfica
def configuracion_grafica(): 
    plt.title('Carta psicrométrica') # Nombre de la figura
    plt.xlabel('Temperatura de bulbo seco, [°C]') # Nombre del eje X
    #plt.ylabel('Y') # Nombre del eje Y
    plt.xlim(0,50) # Límites del eje X
    plt.ylim(0,0.1) # Límites del eje Y
    plt.twinx().set_ylabel('Razón de humedad, W [kg vapor/kg aire seco]',x=-2,y=0.5) # Mover escala
    plt.twinx().set_ylim(0,50)


def calcular():
    global T_modifica,HR_modifica,p_modifica
    T_modifica = float(entrada1.get()) # °C
    HR_modifica = float(entrada2.get()) # %
    HR_modifica /= 100 # decimal
    p_modifica = float(entrada3.get()) # kPa
    calculos(T_modifica,HR_modifica,p_modifica)
    return T_modifica,HR_modifica,p_modifica



def calculos(T_,HR_,p_):
    global pvs,pv,w,Ws,u,Veh,Tpr,H,Tw,T,HR,p,T_1,pvs_1,Ws_1
    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry("380x620")
    win.configure(background="#190972")
    win.title("Cálculos")
    e3=tk.Label(win,text="Parámetros psicrométricos",bg="red",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    
    T = T_
    HR = HR_
    p = p_

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

    w = 0.622*(pv/(p-pv))
    w = w*1000 # razón de humedad, g de vapor de agua/kg de aire seco
    print(f"W = {w}")


    Ws = 0.622*(pvs/(p-pvs)) # Razón de humedad de saturación, kg vapor de agua/kg de aire seco
    print(f"Ws = {Ws}")
    u = (w/1000)/Ws # Grado de saturación del aire
    print(f"u = {u}")

    Veh = ((Ra*T)/(p*1000))*((1+1.6078*(w/1000))/(1+(w/1000))) # Volumen específico del aire húmedo, m^3/kg de aire
    print(f"Veh = {Veh:.3f}") 

    T = T-273.15
    pv=pv*1000
    if 0<T<70:
        Tpr=-35.957-1.8726*math.log(pv)+1.1689*((math.log(pv))**2)
    elif -60<T<0:
        Tpr = -60.45 + 7.0322*math.log(pv)+0.37*(math.log(pv)**2)
    print(f"Tpr = {Tpr}") # Temperatura del punto de rocío, °C

    pv=pv/1000

    H = 1.006*T + (w/1000)*(2501+1.805*T) # Entalpía, kJ/kg
    print(f"h = {H}")

    Tw = T * math.atan(0.151977*((HR*100)+8.313659)**0.5)+math.atan(T+(HR*100))-math.atan((HR*100)-1.676331)+(0.00391838*((HR*100)**1.5))*math.atan(0.023101*(HR*100))-4.686035
    print(f"Tw = {Tw}")
    
    w/=1000
    T_1 = Tw+273.15
    pvs_1 = math.exp(A1/T_1 + A2 + A3*T_1 + A4*T_1**2 + A5*T_1**3 + A6*T_1**4 + A7*math.log(T_1))
    pvs_1 /=1000
    Ws_1 = 0.622*(pvs_1/(p-pvs_1))

    e3 = tk.Label(win,text= f"pvs = {pvs:.3f} kPa",bg="#0B2769",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=6,fill=tk.X)

    e3 = tk.Label(win,text= f"pv = {pv:.3f} kPa",bg="#0B2769",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=7,fill=tk.X)

    e3 = tk.Label(win,text= f"W = {w:.2f} g/kg",bg="#0B2769",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=8,fill=tk.X)

    e3 = tk.Label(win,text= f"Ws = {Ws:.4f} kg/kg",bg="#0B2769",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=9,fill=tk.X)

    e3 = tk.Label(win,text= f"u = {u:.3f}",bg="#0B2769",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=10,fill=tk.X)

    e3 = tk.Label(win,text= f"Veh = {Veh:.3f} m^3/kg",bg="#0B2769",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=11,fill=tk.X)

    e3 = tk.Label(win,text= f"Tpr = {Tpr:.2f} °C",bg="#0B2769",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=12,fill=tk.X)

    e3 = tk.Label(win,text= f"h = {H:.1f} kJ/kg",bg="#0B2769",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=13,fill=tk.X)

    e3 = tk.Label(win,text= f"Tw = {Tw:.1f} °C",bg="#0B2769",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=14,fill=tk.X)


    # Hacer
    #boton2=tk.Button(win,text="Ok",command=ventana.deiconify())
    #boton2.pack(side=tk.TOP)

    return pvs,pv,w,Ws,u,Veh,Tpr,H,Tw,T,HR,p


def grafica():
    ventana.withdraw()
    #win2 = tk.Toplevel()
    #win2.geometry("1080x720")
    #win2.configure(background="#190972")
    #win2.title("Gráfica")
    #e5=tk.Label(win2,text="Carta Pscicrométrica",bg="red",fg="white")
    #e5.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)

    calcular()
    p = p_modifica
    p *=7.501 # mmHg
    rango_2 = np.arange(0, 55, 5)
    rango_3 = np.arange(55, 91, 5)

    # Fórmula para obtener psat por rangos de temperatura
    #psat_1 = (0.00016*(rango_1**3))+(0.01047*(rango_1**2))+(0.33266*(rango_1))+4.58407
    psat_2 = (0.0000046*(rango_2**4))+(0.0000891*(rango_2**3))+(0.0127959*(rango_2**2))+(0.3183402*(rango_2))+4.58407
    psat_3 = (0.00217*(rango_3**3))-(0.27038*(rango_3**2))+(16.05426*(rango_3))-308.4337

    #array_psat = np.concatenate((psat_1, psat_2, psat_3), axis=0)
    array_psat = np.concatenate((psat_2, psat_3), axis=0)
    array_temperatura = np.arange(0.01,91,5)

    array_calor = [597.729,594.905,592.06,589.249,586.42,583.571,580.748,577.906,575.038,572.194,569.302,566.41,563.492,560.569,557.62,554.644,551.637,548.602,545.538]


    # Humedad relativa
    dHR_100 = (array_psat*100)/100
    dHR_90 = (array_psat*90)/100
    dHR_80 = (array_psat*80)/100
    dHR_70 = (array_psat*70)/100
    dHR_60 = (array_psat*60)/100
    dHR_50 = (array_psat*50)/100
    dHR_40 = (array_psat*40)/100
    dHR_30 = (array_psat*30)/100
    dHR_20 = (array_psat*20)/100
    dHR_10 = (array_psat*10)/100


    # Humedad absoluta, Kg vapor/Kg aire seco
    dHA100 = (dHR_100*0.622)/(p-dHR_100)
    dHA90 = (dHR_90*0.622)/(p-dHR_90)
    dHA80 = (dHR_80*0.622)/(p-dHR_80)
    dHA70 = (dHR_70*0.622)/(p-dHR_70)
    dHA60 = (dHR_60*0.622)/(p-dHR_60)
    dHA50 = (dHR_50*0.622)/(p-dHR_50)
    dHA40 = (dHR_40*0.622)/(p-dHR_40)
    dHA30 = (dHR_30*0.622)/(p-dHR_30)
    dHA20 = (dHR_20*0.622)/(p-dHR_20)
    dHA10 = (dHR_10*0.622)/(p-dHR_10)


    # Creación de arreglos para las variables a utilizar
    array_dTwh = np.arange(0.01,91,5)
    array_dYASAT = dHA100
    array_dYA = np.zeros(19)
    array_dTG = array_dYASAT*array_calor/0.227+array_dTwh
    array_dh = 1.006*array_dTwh + array_dYASAT*(2501+1.805*array_dTwh)



    # Graficación de las líneas de Humedad
    plt.plot(array_temperatura,dHA100,'k',linewidth=1)
    plt.plot(array_temperatura,dHA90,'k',linewidth=1)
    plt.plot(array_temperatura,dHA80,'k',linewidth=1)
    plt.plot(array_temperatura,dHA70,'k',linewidth=1)
    plt.plot(array_temperatura,dHA60,'k',linewidth=1)
    plt.plot(array_temperatura,dHA50,'k',linewidth=1)
    plt.plot(array_temperatura,dHA40,'k',linewidth=1)
    plt.plot(array_temperatura,dHA30,'k',linewidth=1)
    plt.plot(array_temperatura,dHA20,'k',linewidth=1)
    plt.plot(array_temperatura,dHA10,'k',linewidth=1)

    # líneas para Twh
    def l_tw(dtwh,dtg,dyasat,dya):
        for i in range(19): 
            dtwh_ = dtwh[i]
            dtg_ = dtg[i]
            dyasat_ = dyasat[i]
            dya_ = dya[i]
            plt.plot([dtwh_,dtg_],[dyasat_,dya_],'k',linewidth=0.7)


    # Graficación de líneas de temperatura de bulbo húmedo
    l_tw(array_dTwh,array_dTG,array_dYASAT,array_dYA)


    # Función para graficar temperatura de bulbo seco
    def tbs(dtwh,dtg,dya,dyasat):
        for i in range(19):
            dtwh_ = dtwh[i]
            #dtg_ = dtg[indice]
            dya_ = dya[i]
            dyasat_ = dyasat[i]
            plt.plot([dtwh_,dtwh_],[dya_,dyasat_],'r-',linewidth=0.7)

    # Graficación de líneas de temperatura de bulbo húmedo
    tbs(array_dTwh,array_dTwh,array_dYA,array_dYASAT)


    # Función para razón de humedad
    def W(dtwh,dtg,dya,dyasat):
        for i in range(19): 
            dtwh_ = dtwh[i]
            dtg_ = dtg[18]
            dya_ = dya[i]
            dyasat_ = dyasat[i]

            plt.plot([dtwh_,dtg_],[dyasat_,dya_],'g-',linewidth=0.7)

    # Graficación de las líneas de razón de humedad
    W(array_dTwh,array_dTG,array_dYA,array_dYASAT)

    # Función para líneas de entalía
    def h(dtwh,dh,dya,dyasat):
        for i in range(19): 
            dtwh_ = dtwh[i]
            dh_ = dh[i]
            dya_ = dya[i]
            dyasat_ = dyasat[i]
            plt.plot([dtwh_,dh_],[dya_,dyasat_],'#1C2F5E',linewidth=0.7)

    # Graficación de las líneas de entalpía
    h(array_dTwh,array_dh,array_dYASAT,array_dYA)

    # Graficación del punto de interés
    plt.scatter(T,w,color='red',linewidth=3) # Punto
    plt.plot([T,T],[w,0],'r-',linewidth=3) # T (baja)
    plt.plot([T,100],[w,w],'#E967E6',label='W',linewidth=3) # W (derecha) 
    plt.plot([T,Tpr],[w,w],'r-',linewidth=3) # Tpr (izquierda)
    plt.plot([Tpr,Tpr],[w,0],'#3623CE',label='Tpr',linewidth=3) # Tpr (baja)
    plt.plot([T,Tw],[w,Ws_1],'r-',linewidth=3) # Tw (sube) y_punto rocío = Es la W al 100% de humedad
    plt.plot([Tw,Tw],[0,Ws_1],'#0EB8DC',label='Tw',linewidth=3) # Tw (baja) 
    plt.plot([T,T],[Ws,w],'r-',linewidth=3) # Ws (sube) 
    plt.plot([T,100],[Ws,Ws],'#6AE932',label='Ws',linewidth=3) # Ws (derecha) 
    plt.plot([H,0],[0,Ws],'g-',label='h',linewidth=3) # h 
    plt.legend()


    configuracion_grafica()
    plt.show()


ventana=Tk()
ventana.title("Interfaz Carta Pscicrométrica")
ventana.geometry("720x620")
ventana.configure(background="#1F0202")

e1=tk.Label(ventana,text="Valor de Temperatura (°C): ",bg="red",fg="white")
e1.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e2=tk.Label(ventana,text="Valor de HR (%): ",bg="#0B2769",fg="white")
e2.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada2=tk.Entry(ventana)
entrada2.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e4=tk.Label(ventana,text="Presión (kPa): ",bg="#0B2769",fg="white")
e4.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada3=tk.Entry(ventana)
entrada3.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

#boton=tk.Button(ventana,text="Calcular",fg="blue",command=calcular)
#boton.pack(side=tk.TOP)

grafica=tk.Button(ventana,text="Ventana gráfica",fg="blue",command=grafica)
grafica.pack(side=tk.TOP)


tab_control = ttk.Notebook(ventana)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='File')
tab_control.pack(expand=1, fill='both')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Cálculos')
tab_control.pack(expand=1, fill='both')

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Plot')
tab_control.pack(expand=1, fill='both')


frame1 = Frame(tab1, bg='#0B2769')
frame1.grid(column=0,row=0,sticky='nsew')
frame2 = Frame(tab1, bg='#0B2769')
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

def read_file():
    file = filedialog.askopenfilename(initialdir ='/',title='Select a file',filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
    ubicacion['text'] = file

def data():
    data_open = ubicacion['text']
    try:
        excel_file = r'{}'.format(data_open)
        df = pd.read_excel(excel_file)
    except ValueError:
        messagebox.showerror('Información', 'Invalid format')
        return None
    except FileNotFoundError:
        messagebox.showerror('Información', 'Invalid file')
        return None
    clc()

    tabla['column'] = list(df.columns)
    tabla['show'] = "headings"
    for columna in tabla['column']:
        tabla.heading(columna, text= columna)
    
    df_fila = df.to_numpy().tolist()
    for fila in df_fila:
        tabla.insert('', 'end', values =fila)

def clc():
    tabla.delete(*tabla.get_children())


tabla = ttk.Treeview(frame1 , height=10)
tabla.grid(column=0, row=0, sticky='nsew')

ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
ladox.grid(column=0, row = 1, sticky='ew') 

ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
ladoy.grid(column = 1, row = 0, sticky='ns')

tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

estilo = ttk.Style(frame1)
estilo.theme_use('clam') 
estilo.configure(".",font= ('Times New Roman', 12), foreground='red2')
estilo.configure("Treeview", font= ('Times New Roman', 12), foreground='black',  background='white')
estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

boton1 = Button(frame2, text= 'Open file', command= read_file)
boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

boton2 = Button(frame2, text= 'Show content', command= data)
boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

boton3 = Button(frame2, text= 'Clear input',  command= clc)
boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

ubicacion = Label(frame2, fg= 'white', bg='gray26', text= 'Location: ', font= ('Times New Roman',10,'bold') )
ubicacion.grid(column=3, row = 0)


ventana.mainloop()