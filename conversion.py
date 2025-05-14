print ("hola mundo")
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

USUARIO_VALIDO = "admin"
CONTRASENA_VALIDA = "1234"

def mostrar_login():
    ventana_login = tk.Tk()
    ventana_login.title("Login")
    ventana_login.geometry("350x250")
    ventana_login.configure(bg="turquoise")

    titulo = tk.Label(ventana_login, text="Bienvenido", bg="#f0f8ff", fg="black",
                      font=("Helvetica", 16, "bold"))
    titulo.pack(pady=10)

    tk.Label(ventana_login, text="Usuario:", bg="#f0f8ff", fg="#000000",
             font=("Helvetica", 10)).pack(pady=5)
    entrada_usuario = tk.Entry(ventana_login, font=("Helvetica", 10))
    entrada_usuario.pack()

    tk.Label(ventana_login, text="Contraseña:", bg="#f0f8ff", fg="#000000",
             font=("Helvetica", 10)).pack(pady=5)
    entrada_contra = tk.Entry(ventana_login, show="*", font=("Helvetica", 10))
    entrada_contra.pack()

    def verificar():
        if entrada_usuario.get() == USUARIO_VALIDO and entrada_contra.get() == CONTRASENA_VALIDA:
            ventana_login.destroy()
            mostrar_selector()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(ventana_login, text="Ingresar", command=verificar,
              bg="#5cb85c", fg="white", font=("Helvetica", 10, "bold"),
              relief="raised", padx=10, pady=5).pack(pady=15)

    ventana_login.mainloop()

def mostrar_selector():
    ventana = tk.Tk()
    ventana.title("Selector de imágenes")
    ventana.geometry("500x400")
    ventana.configure(bg="violet")

    tk.Label(ventana, text="Selecciona una imagen:", bg="violet", font=("Arial", 12)).pack(pady=10)

    opciones = {
        "Longitud" 
        "Masa" 
        "Tiempo"
    }

    combo = ttk.Combobox(ventana, values=list(opciones.keys()))
    combo.pack(pady=10)

    label_imagen = tk.Label(ventana, bg="violet")
    label_imagen.pack()

    def mostrar_imagen(event):
        seleccion = combo.get()
        ruta = opciones.get(seleccion)
        if ruta:
            try:
                respuesta = requests.get(ruta)
                respuesta.raise_for_status()  # Lanza un error si la respuesta es un error
                imagen = Image.open(BytesIO(respuesta.content))
                imagen = imagen.resize((300, 200))
                img = ImageTk.PhotoImage(imagen)
                label_imagen.config(image=img)
                label_imagen.image = img
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar la imagen:\n{e}")

    combo.bind("<<ComboboxSelected>>", mostrar_imagen)

    ventana.mainloop()

mostrar_login()
