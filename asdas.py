from tkinter import *
import pandas as pd
from tkinter import ttk

ventana = Tk()

ventana.title("Welcome to LikeGeeks app")

ventana.geometry("900x650")
ventana.title("Universidad Autónoma Chapingo")
ventana["bg"] = "#6DBFD3"


tab_control = ttk.Notebook(ventana)

tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Datos')

tab_control.pack(expand=1, fill='both')


tab2 = ttk.Frame(tab_control)

tab_control.add(tab2, text='Datos obtenidos de excel')

tab_control.pack(expand=1, fill='both')


tab3 = ttk.Frame(tab_control)

tab_control.add(tab3, text='Graficas')

tab_control.pack(expand=1, fill='both')


data = pd.read_excel(r'C:/Users/jymcl/Downloads/Tablas ASME - Copy.xlsx')
dHA100 = pd.DataFrame(data, columns=['HA100']).to_numpy()
dHA90 = pd.DataFrame(data, columns=['HA90']).to_numpy()
dHA80 = pd.DataFrame(data, columns=['HA80']).to_numpy()
datt = len(dHA100)
dat_1 = datt-1
print(datt)

for r in range(0, datt):
    for c in range(0, 1):
        cell = Entry(tab2, width=10)
        cell.grid(row=r, column=c)
        cell.insert(r, dHA100[r])

    for c in range(1, 2):
        cell = Entry(tab2, width=10)
        cell.grid(row=r, column=c)
        cell.insert(r, dHA90[r])

    for c in range(2, 3):
        cell = Entry(tab2, width=10)
        cell.grid(row=r, column=c)
        cell.insert(r, dHA80[r])


ventana.mainloop()





'''
for r in range(0, datt):
    for c in range(0, 3):
        cell = Entry(ventana, width=10)
        cell.grid(row=r, column=c)
        cell.insert(0, ''.format(r, c))

ventana.mainloop()
'''