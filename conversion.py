import tkinter as tk
from tkinter import ttk, messagebox

def convertir(valor, tipo):
    conversiones = {
        "Metros a Kilómetros": (valor / 1000, "km"),
        "Pulgadas a Metros": (valor * 0.0254, "m"),
        "Kilogramos a Gramos": (valor * 1000, "g"),
        "Libras a Kilogramos": (valor * 0.453592, "kg"),
        "Segundos a Minutos": (valor / 60, "min"),
        "Horas a Días": (valor / 24, "días"),
        
    }
    resultado, unidad = conversiones.get(tipo, (None, ""))
    return resultado, unidad

def validar_entrada(valor):
    try:
        return float(valor)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return None

def abrir_ventana_conversion(categoria):
    ventana = tk.Toplevel()
    ventana.title(f"Conversión de {categoria}")
    ventana.geometry("350x300")
    ventana.configure(bg="#f9f9f9")

    opciones = {
        "Longitud": ["Metros a Kilómetros", "Pulgadas a Metros"],
        "Masa": ["Kilogramos a Gramos", "Libras a Kilogramos"],
        "Tiempo": ["Segundos a Minutos", "Horas a Días"]
    }
        

    tk.Label(ventana, text="Seleccione tipo de conversión:", bg="#f9f9f9", font=("Arial", 10, "bold")).pack(pady=5)
    seleccion = ttk.Combobox(ventana, values=opciones[categoria], state="readonly")
    seleccion.current(0)
    seleccion.pack(pady=5)

    tk.Label(ventana, text="Ingrese valor:", bg="#f9f9f9").pack(pady=5)
    entrada = tk.Entry(ventana)
    entrada.pack(pady=5)

    resultado_label = tk.Label(ventana, text="", bg="#f9f9f9", font=("Arial", 10))
    resultado_label.pack(pady=10)

    def ejecutar_conversion():
        valor = validar_entrada(entrada.get())
        if valor is not None:
            tipo = seleccion.get()
            resultado, unidad = convertir(valor, tipo)
            if resultado is not None:
                resultado_label.config(text=f"Resultado: {resultado} {unidad}")
            else:
                resultado_label.config(text="Conversión no válida")

    tk.Button(ventana, text="Convertir", command=ejecutar_conversion).pack(pady=10)


ventana_principal = tk.Tk()
ventana_principal.title("Conversores de Unidades")
ventana_principal.geometry("300x300")
ventana_principal.configure(bg="pink")

tk.Label(ventana_principal, text="Escoja su opción", bg="#aef7a2", font=("Arial", 12, "bold")).pack(pady=15)

def crear_boton(texto, categoria):
    return tk.Button( ventana_principal,  text=texto,  bg="red",  fg="white", font=("Arial", 12), width=15,height=2, command=lambda: abrir_ventana_conversion(categoria) ).pack(pady=5)

crear_boton("Longitud", "Longitud")
crear_boton("Masa", "Masa")
crear_boton("Tiempo", "Tiempo")

ventana_principal.mainloop()
