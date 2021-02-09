import tkinter
from tkinter import ttk
import re
import string

# ----------------------------------------------- Creación e implementación de Widgets ---------------------------------------------------
main_Window = tkinter.Tk()
main_Window.geometry("480x720")
main_Window.resizable(False, False)

background = tkinter.Canvas(main_Window, width = 480, height = 720, bd = '0')
img = tkinter.PhotoImage(file = "Background_image.png")
background.create_image(240, 355, image = img)
background.place(x = 0, y = 0)

tabla = tkinter.Canvas(main_Window, width = 470, height = 400)
tabla.columnconfigure(0, weight = 1)

lista = ["                   ", "    Decimal     ", "    Binario     ", "Hexadecimal"]
entrada_var = tkinter.StringVar(tabla)
entrada_var.set(lista[0])
entrada = ttk.OptionMenu(tabla, entrada_var, *lista)
entrada.grid(row = 1, column = 0)

numero = ttk.Entry(tabla, justify = 'center')
numero.grid(row = 1, column = 1)

salida_var = tkinter.StringVar(tabla)
salida_var.set(lista[0])
salida = ttk.OptionMenu(tabla, salida_var, *lista)
salida.grid(row = 1, column = 3)
tabla.place(x = 75, y = 380)

resultado = tkinter.Frame(main_Window)
resultado.place(x = 45, y = 600)
conversion_text = ttk.Label(resultado, text = "Resultado → ")
conversion_text.grid(row = 0, column = 0)
conversion_final = ttk.Label(resultado, text = "")
conversion_final.grid(row = 0, column = 1)

start = ttk.Button(main_Window, text = "Convertir", command = lambda: startFunction())
start.place(x = 200, y = 420)


# ------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------- Creación e implementación de funciones ---------------------------------------------

# Convertidor de decimal a otro sistema
def decimal (numero, tipo):
    resultado = None
    if(re.search('[a-zA-z]', numero)):
        print("ERROR - caracteres invalidos para un número Decimal")
        return 
    numero = int(numero)
    if(tipo == "Bin"):
        resultado = bin(numero)
    elif(tipo == "Hex"):
        resultado = hex(numero)
    return resultado

# Convertidor de binario a otro sistema
def binario (numero, tipo):
    a = 0
    try:
        decimal = int(numero, 2)
    except:
        print("ERROR - caracteres invalidos para un número Binario")
        return
    #Convertir el número a binario
    numero = int(numero, 2)
    if(tipo == "Dec"):
        resultado = numero
    elif(tipo == "Hex"):
        resultado = hex(numero)
    return resultado

# Convertidor de hexadecimal a otro sistema
def hexadecimal (numero, tipo):
    if(all(c in string.hexdigits for c in numero)):
        numero = int(numero, 16)
        if(tipo == "Dec"):
            resultado = numero
        elif(tipo == "Bin"):
            resultado = bin(numero)
        return resultado
    else:
        print("ERROR - caracteres invalidos para un número Hexadecimal")
        return

# Lectura de parámetros y número a convertir
def startFunction ():
    global numero, entrada_var, salida_var, conversion_final
    numeromandar = numero.get()
    regreso = ""
    if(entrada_var.get() == salida_var.get() or not numero.get()):
        conversion_final.configure(text = "ERROR")

        return

    if(numero.get()):
        if(entrada_var.get() == "    Decimal     "):
            if(salida_var.get() == "    Binario     "):
                tipo = "Bin"
            elif(salida_var.get() == "Hexadecimal"):
                tipo = "Hex"
            regreso = decimal(numeromandar, tipo)

        elif(entrada_var.get() == "    Binario     "):
            if(salida_var.get() == "    Decimal     "):
                tipo = "Dec"
            elif(salida_var.get() == "Hexadecimal"):
                tipo = "Hex"
            regreso = binario(numeromandar, tipo)

        elif(entrada_var.get() == "Hexadecimal"):
            if(salida_var.get() == "    Decimal     "):
                tipo = "Dec"
            elif(salida_var.get() == "    Binario     "):
                tipo = "Bin"
            regreso = hexadecimal(numeromandar, tipo)
        if(regreso):
            conversion_final.configure(text = regreso)
        else:
            conversion_final.configure(text = "ERROR")

# ------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------- Inicio de loop principal para GUI --------------------------------------------------

main_Window.mainloop()

# ------------------------------------------------------------------------------------------------------------------------------------