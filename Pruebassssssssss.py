import tkinter as tk
import matplotlib.pyplot as plt
import math
import pandas as pd
import numpy as np

from tkinter import *
from tkinter import ttk, Tk, Label, Button, Frame,  messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL, Spinbox
from tkinter import scrolledtext as st


ventana = Tk()
ventana.minsize(width=900, height=700)
ventana.title('Carta')
ventana["bg"] = "#6DBFD3"


def abrir_archivo():

    global Pres,Temp,Hu_Re,canti,Pres_2,Temp_2,Hu_Re_2

    archivo = filedialog.askopenfilename(initialdir ='/', 
                                            title='Selecione archivo', 
                                            filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
    indica['text'] = archivo

    data = pd.read_excel(archivo)
    Pres = pd.DataFrame(data, columns=['Presión']).to_numpy()
    Temp = pd.DataFrame(data, columns=['Temperatura']).to_numpy()
    Hu_Re = pd.DataFrame(data, columns=['Humedad Relativa']).to_numpy()

    conv = list(map(float, Pres))
    conv_2 = np.array(conv)

    conv_3 = list(map(float, Temp))
    conv_4 = np.array(conv_3)

    conv_5 = list(map(float, Hu_Re))
    conv_6 = np.array(conv_5)


    print(conv_2)

    Pres_2 = conv_2
    Temp_2 = conv_4
    Hu_Re_2 = conv_6
    Hu_Re_2 = Hu_Re_2/100

    canti = len(Pres_2)

    print(Temp[1])



def oper():
    global canti,Pres_2,Temp_2,Hu_Re_2
    T = float(entrada1.get()) # °C
    Temp_2 = [T]
    HR = float(entrada2.get()) # %
    Hu_Re_2 = [HR]
    P = float(entrada3.get()) # kPa
    Pres_2 = [P]
    canti = 1
    return Temp_2,Hu_Re_2,Pres_2,canti





tab_control = ttk.Notebook(ventana)

tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Datos de excel')

tab_control.pack(expand=1, fill='both')


tab2 = ttk.Frame(tab_control)

tab_control.add(tab2, text='Operaciones')

tab_control.pack(expand=1, fill='both')


tab3 = ttk.Frame(tab_control)

tab_control.add(tab3, text='Graficas')

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




e1=tk.Label(frame1,text="Temperatura (°C): ",bg="#2DE0AE",fg="#2F3257")
e1.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e2=tk.Label(frame1,text="HR (decimales): ",bg="#2DE0AE",fg="#2F3257")
e2.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada2=tk.Entry(ventana)
entrada2.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e3=tk.Label(frame1,text="Presión (mmHg): ",bg="#2DE0AE",fg="#2F3257")
e3.pack(padx=5,pady=5,ipadx=5,ipady=5)
entrada3=tk.Entry(ventana)
entrada3.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

calc=tk.Button(frame1,text="Calcular",fg="#2F3257",command=oper)
calc.pack(side=tk.TOP)




def operaciones(T_2,HR_1,P_1):

    global pvs,pv,W,Ws,u,Veh,Tpr,h_1,Tw,T_1,pvs_1,Ws_1,y

    T = T_2
    HR = HR_1
    p=P_1

    p=p/7.501
    

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

    h_1 = 1.006*T + (W/1000)*(2501+1.805*T) # Entalpía, kJ/kg
    print(f"h = {h_1}")


    # Bulbo humedo
    Tw = T * math.atan(0.151977*((HR*100)+8.313659)**0.5)+math.atan(T+(HR*100))-math.atan((HR*100)-1.676331)+(0.00391838*((HR*100)**1.5))*math.atan(0.023101*(HR*100))-4.686035
    print(Tw)

    W /=1000

    T_1 = Tw+273.15
    pvs_1 = math.exp(A1/T_1 + A2 + A3*T_1 + A4*T_1**2 + A5*T_1**3 + A6*T_1**4 + A7*math.log(T_1))
    pvs_1 /=1000
    Ws_1 = 0.622*(pvs_1/(p-pvs_1))


    m=(0-W)/(h_1-T)

    y = (m*T)+Ws

    print(m)

    return pvs,pv,W,Ws,u,Veh,Tpr,h_1,Tw,T_1,pvs_1,Ws_1,y

def configuracion_grafica():
    plt.title('Carta psicrométrica') # Nombre de la figura
    plt.xlabel('Temperatura de bulbo seco, [°C]') # Nombre del eje X
    plt.ylabel('Y') # Nombre del eje Y
    plt.xlim(0,60) # Límites del eje X
    plt.ylim(0,0.03) # Límites del eje Y
    plt.twinx().set_ylabel('Razón de humedad, W [kg vapor/kg aire seco]',x=0,y=0.5) # Mover escala


def graficacion():

    patm = Pres_2[0]
    a = np.arange(-10, 0, 1) # inicio, final (excluido), paso
    b = np.arange(0, 55,1)
    c = np.arange(55, 91, 1)
    Twh = np.arange(0, 91, 1)

    psat_1 = (0.00016*(a**3))+(0.01047*(a**2))+(0.33266*(a))+4.58407
    psat_2 = (0.0000046*(b**4))+(0.0000891*(b**3))+(0.0127959*(b**2))+(0.3183402*(b))+4.58407
    psat_3 = (0.00217*(c**3))-(0.27038*(c**2))+(16.05426*(c))-308.4337

    calor = [597.452,596.883,596.315,595.747,595.18,594.614,594.047,593.481,592.915,592.35,
             591.784,591.219,590.654,590.089,589.523,588.958,588.393,587.828,587.263,586.698,
             586.132,585.567,585.001,584.435,583.869,583.303,582.736,582.17,581.603,581.035,
             580.468,579.9,579.332,578.763,578.195,577.625,577.056,576.486,575.915,575.345,
             574.773,574.202,573.63,573.057,572.484,571.91,571.336,570.761,570.186,569.61,
             569.033,568.456,567.879,567.3,566.721,566.142,565.561,564.98,564.398,563.816,
             563.232,562.648,562.063,561.478,560.891,560.304,559.715,559.126,558.536,557.945,
             557.353,556.76,556.166,555.572,554.976,554.379,553.781,553.181,552.581,551.98,
             551.377,550.774,550.169,549.563,548.955,548.347,547.737,547.126,546.513,545.9,
             545.284]

    psat = np.concatenate((psat_2, psat_3), axis=0)

    HR_100 = (psat*100)/100
    HR_90 = (psat*90)/100
    HR_80 = (psat*80)/100
    HR_70 = (psat*70)/100
    HR_60 = (psat*60)/100
    HR_50 = (psat*50)/100
    HR_40 = (psat*40)/100
    HR_30 = (psat*30)/100
    HR_20 = (psat*20)/100
    HR_10 = (psat*10)/100

    HA_100 = (HR_100*0.622)/(patm-HR_100)
    HA_90 = (HR_90*0.622)/(patm-HR_90)
    HA_80 = (HR_80*0.622)/(patm-HR_80)
    HA_70 = (HR_70*0.622)/(patm-HR_70)
    HA_60 = (HR_60*0.622)/(patm-HR_60)
    HA_50 = (HR_50*0.622)/(patm-HR_50)
    HA_40 = (HR_40*0.622)/(patm-HR_40)
    HA_30 = (HR_30*0.622)/(patm-HR_30)
    HA_20 = (HR_20*0.622)/(patm-HR_20)
    HA_10 = (HR_10*0.622)/(patm-HR_10)

    YASAT = HA_100
    YA = np.zeros(91, dtype=int)
    TG = (YASAT*calor)/0.227+Twh
    Veh =(287.055*(Twh+273.15)/(patm*133.322))*((1+1.6078*YASAT)/(1+YASAT))
    h_2 = (1.006*Twh)+(YASAT*(2501+(1.805*Twh)))


    plt.plot(Twh,HA_100,'k',label='Humedad absoluta',linewidth=0.7)
    plt.plot(Twh,HA_90,'k',label='Humedad absoluta',linewidth=0.7)
    plt.plot(Twh,HA_80,'k',label='Humedad absoluta',linewidth=0.7)
    plt.plot(Twh,HA_70,'k',label='Humedad absoluta',linewidth=0.7)
    plt.plot(Twh,HA_60,'k',label='Humedad absoluta',linewidth=0.7)
    plt.plot(Twh,HA_50,'k',label='Humedad absoluta',linewidth=0.7)
    plt.plot(Twh,HA_40,'k',label='Humedad absoluta',linewidth=0.7)
    plt.plot(Twh,HA_30,'k',label='Humedad absoluta',linewidth=0.7)
    plt.plot(Twh,HA_20,'k',label='Humedad absoluta',linewidth=0.7)
    plt.plot(Twh,HA_10,'k',label='Humedad absoluta',linewidth=0.7)


    def conectar(twh,tg,yasat,ya):
        for i in range(0,90):
            twh_ = twh[i]
            tg_ = tg[i]
            yasat_ = yasat[i]
            ya_ = ya[i]
            plt.plot([twh_,tg_],[yasat_,ya_],'k',label='line 2',linewidth=0.7)
            
    def tbs(twh,tg,ya,yasat):
        for i in range(0,90):
            twh_ = twh[i]
            ya_ = ya[i]
            yasat_ = yasat[i]
            plt.plot([twh_,twh_],[ya_,yasat_],'k-',label='line 3',linewidth=0.7)

    def W(twh,tg,ya,yasat):
        for i in range(0,90):
            twh_ = twh[i]
            tg_ = tg[90]
            ya_ = ya[i]
            yasat_ = yasat[i]
            plt.plot([twh_,tg_],[yasat_,ya_],'k-',label='line 3',linewidth=0.7)

    def h(twh,h_1,ya,yasat):
        for i in range(0,90):
            twh_ = twh[i]
            h_ = h_2[i]
            ya_ = ya[i]
            yasat_ = yasat[i]
            plt.plot([twh_,h_],[ya_,yasat_],'k-',label='line 3',linewidth=0.7)

    conectar(Twh,TG,YASAT,YA)
    tbs(Twh,Twh,YA,YASAT)
    W(Twh,TG,YA,YASAT)
    h(Twh,h_2,YASAT,YA)


    #configuracion_grafica()
    #plt.show()


def B1():
    resultado.delete('1.0', tk.END)
    for i in range(0,canti):
            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            print("\nPvs: ",pvs)
            resultado.insert(tk.INSERT,
            f"Pvs = {pvs:.4f} kPa \n")

def B2():
    resultado.delete('1.0', tk.END)
    for i in range(0,canti):
            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            print("Pv: ",pv)
            resultado.insert(tk.INSERT,
            f"Pv = {pv:.4f} kPa \n")

def B3():
    resultado.delete('1.0', tk.END)
    for i in range(0,canti):
            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            print("W: ",W)
            resultado.insert(tk.INSERT,
            f"W = {W:.4f} g/Kg \n")
    
def B4():
    resultado.delete('1.0', tk.END)
    for i in range(0,canti):
            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            print("Ws: ",Ws)
            resultado.insert(tk.INSERT,
            f"Ws = {Ws:.4f} Kg/Kg \n")


def B5():
    resultado.delete('1.0', tk.END)
    for i in range(0,canti):
            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            print("u: ",u)
            resultado.insert(tk.INSERT,
            f"u = {u:.4f} \n")

def B6():
    resultado.delete('1.0', tk.END)
    for i in range(0,canti):
            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            print("Veh: ",Veh)
            resultado.insert(tk.INSERT,
            f"Veh = {Veh:.4f} m^3/Kg \n")

def B10():
    resultado.delete('1.0', tk.END)
    for i in range(0,canti):
            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            print("Tpr: ",Veh)
            resultado.insert(tk.INSERT,
            f"Tpr = {Tpr:.4f} °C \n")

def B7():

    resultado.delete('1.0', tk.END)
    for i in range(0,canti):
            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            print("h: ",h)
            resultado.insert(tk.INSERT,
            f"h = {h:.4f} kJ/Kg \n")
    

def B8():

    resultado.delete('1.0', tk.END)
    for i in range(0,canti):
            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            print("Pvs: ",pvs)
            print("Pv: ",pv)
            print("W: ",W)
            print("Ws: ",Ws)
            print("u: ",u)
            print("Veh: ",Veh)
            print("h: ",h)
            resultado.insert(tk.INSERT,
            f"Pvs = {pvs:.4f} \nPv = {pv:.4f} \nW = {W:.4f} \nWs = {Ws:.4f} \nu = {u:.4f} \nVeh = {Veh:.4f} \nTpr = {Tpr:.4f} °C \n h = {h:.4f}") 

def B9():
    ventana.quit()
    ventana.destroy() 



################ BOTONES PARA GRAFICAR #########################

def B11():
    plt.clf()
    #configuracion_grafica()
    graficacion()
    for i in range(0,canti):

            operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
            plt.scatter(Temp_2[i],W,color='red',linewidth=3)
    configuracion_grafica()
    plt.show()


def B13():
    plt.clf()


    graficacion()


def B14():
    plt.clf()
    graficacion()


def B19():
    plt.clf()
    graficacion()
    for i in range(0,canti):
        operaciones(Temp_2[i],Hu_Re_2[i],Pres_2[i])
        plt.scatter(Temp_2[i],W,color='red',linewidth=3)
        plt.plot([Temp_2[i],Temp_2[i]],[W,0],'b-',label='Tw',linewidth=3)
        plt.plot([Temp_2[i],100],[W,W],'m-',label='W',linewidth=3)
        plt.plot([Temp_2[i],Tpr],[W,W],'g-',label='W',linewidth=3) # Tpr (izquierda)
        plt.plot([Tpr,Tpr],[W,0],'m-',label='W',linewidth=3) # Tpr (baja)
        plt.plot([Temp_2[i],Tw],[W,Ws_1],'g-',label='W',linewidth=3) # Tw (sube) y_punto rocío = Es la W al 100% de humedad
        plt.plot([Tw,Tw],[0,Ws_1],'k-',label='Tw',linewidth=3) # Tw (baja) y_punto rocío = Es la W al 100% de humedad
        plt.plot([Temp_2[i],Temp_2[i]],[Ws,W],'y-',label='Ws',linewidth=3) # Ws (sube) 
        plt.plot([Temp_2[i],100],[Ws,Ws],'b-',label='Ws',linewidth=3) # Ws (derecha) 
        plt.plot([h_1,0],[0,Ws],'g-',label='h',linewidth=3) # h

    configuracion_grafica()
    plt.show()
    

def B20():
    ventana.quit()
    ventana.destroy()

def B21():
    plt.clf()
    graficacion()



B1 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="Pws", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B1, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B1.grid(row=5, column=0) # Ubicamos el botón en base a filas y columnas

B2 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="Pw", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B2, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B2.grid(row=5, column=1) # Ubicamos el botón en base a filas y columnas


B3 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="W", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B3, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B3.grid(row=5, column=2) # Ubicamos el botón en base a filas y columnas


B4 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="Ws", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B4, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B4.grid(row=5, column=3) # Ubicamos el botón en base a filas y columnas


B5 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="u", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B5, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B5.grid(row=6, column=0) # Ubicamos el botón en base a filas y columnas


B6 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="Veh", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B6, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B6.grid(row=6, column=1) # Ubicamos el botón en base a filas y columnas 


B10 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="Tpr", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B10, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B10.grid(row=6, column=2) # Ubicamos el botón en base a filas y columnas 


B7 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="h", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B7, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B7.grid(row=6, column=3) # Ubicamos el botón en base a filas y columnas 


B8 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="Todo", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#283746", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B8, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B8.grid(row=7, column=2) # Ubicamos el botón en base a filas y columnas 


B9 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="Cerrar", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#283746", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B9, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B9.grid(row=7, column=3) # Ubicamos el botón en base a filas y columnas





B11 = tk.Button( # Declaramos un nuevo botón
tab3, # Lo colocamos en la ventana creada
text="Graficar puntos", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B11, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B11.grid(row=5, column=0) # Ubicamos el botón en base a filas y columnas


B13 = tk.Button( # Declaramos un nuevo botón
tab3, # Lo colocamos en la ventana creada
text="Unir puntos", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B13, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B13.grid(row=5, column=2) # Ubicamos el botón en base a filas y columnas


B14 = tk.Button( # Declaramos un nuevo botón
tab3, # Lo colocamos en la ventana creada
text="Graficar promedio diario", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B14, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B14.grid(row=5, column=3) # Ubicamos el botón en base a filas y columnas


B19 = tk.Button( # Declaramos un nuevo botón
tab3, # Lo colocamos en la ventana creada
text="Todo", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#283746", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B19, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B19.grid(row=7, column=2) # Ubicamos el botón en base a filas y columnas 


B20 = tk.Button( # Declaramos un nuevo botón
tab3, # Lo colocamos en la ventana creada
text="Cerrar", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#283746", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B20, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B20.grid(row=7, column=3) # Ubicamos el botón en base a filas y columnas

B21 = tk.Button( # Declaramos un nuevo botón
tab2, # Lo colocamos en la ventana creada
text="Tbh", # Establecemos el texto del botón
width=20, # Establecemos el ancho del botón
height=3, # Establecemos la altura del botón
bg="#3C5A78", # Establecemos el color de fondo del botón
font=("Sylfaen", 12), # Establecemos el tipo y tamaño de letra
command=B21, # Configuramos la función a ejecutar cuando el botón sea presionado
)
B21.grid(row=7, column=0) # Ubicamos el botón en base a filas y columnas



resultado = st.ScrolledText(tab2,
wrap = tk.WORD,
width = 20,
height = 15,
font = ("Sylfaen",
15)) 

resultado.grid(row = 0, column = 5, columnspan = 5, rowspan = 8, padx = 5, pady = 5)


ventana.mainloop()