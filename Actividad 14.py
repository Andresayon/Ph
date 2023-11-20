import tkinter as tk

def clic_en_numero(numero):
    actual = escribir.get()
    escribir.delete(0, tk.END)
    escribir.insert(0, str(actual) + str(numero))

def clic_en_operacion(operacion):
    actual = escribir.get()
    escribir.delete(0, tk.END)
    escribir.insert(0, str(actual) + str(operacion))

def calcular():
    try:
        expresion = escribir.get()
        resultado = eval(expresion)
        escribir.delete(0, tk.END)
        escribir.insert(0, str(resultado))
    except Exception as e:
        escribir.delete(0, tk.END)
        escribir.insert(0, "Error")

def btn_mc_click():
    pass

def btn_mr_click():
    pass

def btn_ms_click():
    pass

def btn_mmass_click():
    pass

def btn_sqr_click():
    actual = float(escribir.get())
    resultado = actual ** 0.5
    escribir.delete(0, tk.END)
    escribir.insert(0, str(resultado))

def btn_porcentaje_click():
    actual = float(escribir.get())
    resultado = actual / 100
    escribir.delete(0, tk.END)
    escribir.insert(0, str(resultado))

def btn_invertir_click():
    actual = float(escribir.get())
    if actual != 0:
        resultado = 1 / actual
        escribir.delete(0, tk.END)
        escribir.insert(0, str(resultado))
    else:
        escribir.delete(0, tk.END)
        escribir.insert(0, "Error")

root = tk.Tk()
cadena = tk.StringVar()
root.geometry("450x600")
root.title("CALCULADORA BASICA")

escribir = tk.Entry(root, width=50, borderwidth=5)
escribir.place(x=65, y=60)

btn_mc = tk.Button(root, width=5, height=2, text="MC", command=btn_mc_click)
btn_mc.place(x=65, y=150)

btn_mr = tk.Button(root, width=5, height=2, text="MR", command=btn_mr_click)
btn_mr.place(x=125, y=150)

btn_ms = tk.Button(root, width=5, height=2, text="MS", command=btn_ms_click)
btn_ms.place(x=195, y=150)

btn_mmass = tk.Button(root, width=5, height=2, text="M+", command=btn_mmass_click)
btn_mmass.place(x=265, y=150)

btn_sqr = tk.Button(root, width=5, height=2, text="sqr", command=btn_sqr_click)
btn_sqr.place(x=335, y=150)

btn_uno = tk.Button(root, width=5, height=2, text="1", command=lambda: clic_en_numero(1))
btn_uno.place(x=65, y=300)

btn_dos = tk.Button(root, width=5, height=2, text="2", command=lambda: clic_en_numero(2))
btn_dos.place(x=125, y=300)

btn_tres = tk.Button(root, width=5, height=2, text="3", command=lambda: clic_en_numero(3))
btn_tres.place(x=195, y=300)

btn_cuatro = tk.Button(root, width=5, height=2, text="4", command=lambda: clic_en_numero(4))
btn_cuatro.place(x=65, y=250)

btn_cinco = tk.Button(root, width=5, height=2, text="5", command=lambda: clic_en_numero(5))
btn_cinco.place(x=125, y=250)

btn_seis = tk.Button(root, width=5, height=2, text="6", command=lambda: clic_en_numero(6))
btn_seis.place(x=195, y=250)

btn_siete = tk.Button(root, width=5, height=2, text="7", command=lambda: clic_en_numero(7))
btn_siete.place(x=65, y=200)

btn_ocho = tk.Button(root, width=5, height=2, text="8", command=lambda: clic_en_numero(8))
btn_ocho.place(x=125, y=200)

btn_nueve = tk.Button(root, width=5, height=2, text="9", command=lambda: clic_en_numero(9))
btn_nueve.place(x=195, y=200)

btn_cero = tk.Button(root, width=13, height=2, text="0", command=lambda: clic_en_numero(0))
btn_cero.place(x=65, y=350)

# Botones de operación
btn_mas = tk.Button(root, width=5, height=2, text="+", command=lambda: clic_en_operacion("+"))
btn_mas.place(x=265, y=350)

btn_menos = tk.Button(root, width=5, height=2, text="-", command=lambda: clic_en_operacion("-"))
btn_menos.place(x=265, y=300)

btn_por = tk.Button(root, width=5, height=2, text="*", command=lambda: clic_en_operacion("*"))
btn_por.place(x=265, y=250)

btn_div = tk.Button(root, width=5, height=2, text="/", command=lambda: clic_en_operacion("/"))
btn_div.place(x=265, y=200)

btn_punto = tk.Button(root, width=5, height=2, text=".", command=lambda: clic_en_numero("."))
btn_punto.place(x=195, y=350)

btn_igual = tk.Button(root, width=5, height=6, text="=", command=calcular)
btn_igual.place(x=335, y=300)

btn_porcentaje = tk.Button(root, width=5, height=2, text="%", command=btn_porcentaje_click)
btn_porcentaje.place(x=335, y=200)

btn_uno_sobre_x = tk.Button(root, width=5, height=2, text="1/x", command=btn_invertir_click)
btn_uno_sobre_x.place(x=335, y=250)

root.mainloop()