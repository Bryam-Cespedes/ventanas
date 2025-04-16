import tkinter as tk
from tkinter import messagebox

VALID_USER = "0101"
VALID_PASSWORD = "23456781"

def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    if usuario == VALID_USER and contraseña == VALID_PASSWORD:
        messagebox.showinfo("Login correcto", "¡Bienvenido!")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("300x200")

label_usuario = tk.Label(ventana, text="Usuario (4 dígitos):")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

label_contraseña = tk.Label(ventana, text="Contraseña (8 dígitos):")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack()

boton_login = tk.Button(ventana, text="Iniciar sesión", command=verificar_login)
boton_login.pack(pady=20)

ventana.mainloop()