import tkinter as tk
from tkinter import messagebox

registros_docentes = []

def guardar_docente():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    materia = entry_materia.get()
    carrera = entry_carrera.get()
    genero = entry_genero.get()
    celular = entry_celular.get()
    año = entry_año.get()

    if not (nombre and apellido and edad and materia and carrera and genero and celular and año):
        messagebox.showwarning("Campos incompletos", "Por favor completa todos los campos.")
        return

    try:
        edad = int(edad)
        año = int(año)
    except ValueError:
        messagebox.showerror("Error de formato", "Edad y año deben ser números.")
        return

    docente = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Materia": materia,
        "Carrera": carrera,
        "Género": genero,
        "Celular": celular,
        "Año_Ingreso": año
    }

    registros_docentes.append(docente)

    if len(registros_docentes) >= 5:
        messagebox.showinfo("Registros completos", f"Se han registrado {len(registros_docentes)} docentes.")
        boton_guardar.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Docente registrado", f"Docente {nombre} {apellido} registrado con éxito.\nTotal: {len(registros_docentes)}")

    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_materia.delete(0, tk.END)
    entry_carrera.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_celular.delete(0, tk.END)
    entry_año.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Registro de Docentes")
ventana.geometry("400x500")

tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Apellido:").pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Materia:").pack()
entry_materia = tk.Entry(ventana)
entry_materia.pack()

tk.Label(ventana, text="Carrera:").pack()
entry_carrera = tk.Entry(ventana)
entry_carrera.pack()

tk.Label(ventana, text="Género:").pack()
entry_genero = tk.Entry(ventana)
entry_genero.pack()

tk.Label(ventana, text="Número de celular:").pack()
entry_celular = tk.Entry(ventana)
entry_celular.pack()

tk.Label(ventana, text="Año de ingreso a la universidad:").pack()
entry_año = tk.Entry(ventana)
entry_año.pack()

boton_guardar = tk.Button(ventana, text="Guardar Docente", command=guardar_docente)
boton_guardar.pack(pady=20)

ventana.mainloop()