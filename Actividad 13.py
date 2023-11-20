import tkinter as tk
from tkinter import ttk

def suma():
    num1 = float(ent_caja.get())
    num2 = float(ent_caja1.get())
    salida = str(num1 + num2)
    cadena.set(salida)

def multi():
    num1 = float(ent_caja.get())
    num2 = float(ent_caja1.get())
    salida = str(num1 * num2)
    cadena.set(salida)

def resta():
    num1 = float(ent_caja.get())
    num2 = float(ent_caja1.get())
    salida = str(num1 - num2)
    cadena.set(salida)

def div():
    num1 = float(ent_caja.get())
    num2 = float(ent_caja1.get())
    salida = str(num1 / num2)
    cadena.set(salida)

root = tk.Tk()
cadena = tk.StringVar()
root.geometry("700x500")
root.title("OPERADORES ARITMETICOS")

label_numero1 = tk.Label(root, text="NUMERO 1")
label_numero1.place(x=80, y=70)
label_numero2 = tk.Label(root, text="NUMERO 2")
label_numero2.place(x=230, y=70)
label_resul = tk.Label(root, text="RESULTADO")
label_resul.place(x=380, y=70)



ent_caja = tk.Entry(root)
ent_caja.place(x=50, y=100)
ent_caja1 = tk.Entry(root)
ent_caja1.place(x=200, y=100)
ent_caja2 = tk.Entry(root, textvariable=cadena)
ent_caja2.place(x=350, y=100)

btn_suma = tk.Button(root, text="SUMA", command=suma)
btn_suma.place(x=50, y=150)
btn_resta = tk.Button(root, text="RESTA", command=resta)
btn_resta.place(x=150, y=150)
btn_div = tk.Button(root, text="DIVISION", command=div)
btn_div.place(x=250, y=150)
btn_multi = tk.Button(root, text="MULTIPLICACION", command=multi)
btn_multi.place(x=350, y=150)

operaciones = ttk.LabelFrame(root, text="Operaciones")
operaciones.grid(column=0, row=0)

root.mainloop()

