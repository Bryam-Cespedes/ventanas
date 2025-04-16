import tkinter as tk
from tkinter import messagebox

registros = []

def guardar_registro():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    semestre = entry_semestre.get()
    carrera = entry_carrera.get()
    genero = entry_genero.get()
    celular = entry_celular.get()

    if not (nombre and apellido and edad and semestre and carrera and genero and celular):
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        return

    try:
        edad = int(edad)
        semestre = int(semestre)
        celular = str(celular)
    except ValueError:
        messagebox.showerror("Error de formato", "Edad y semestre deben ser números.")
        return

    registro = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Semestre": semestre,
        "Carrera": carrera,
        "Género": genero,
        "Celular": celular
    }
    
    registros.append(registro)

    if len(registros) >= 5:
        messagebox.showinfo("Registros completos", f"Se han registrado {len(registros)} estudiantes.")
        boton_guardar.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Estudiante registrado", f"Estudiante {nombre} {apellido} registrado con éxito.\nTotal: {len(registros)}")

    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_semestre.delete(0, tk.END)
    entry_carrera.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_celular.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Registro de Estudiantes")
ventana.geometry("400x450")

tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Apellido:").pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Semestre:").pack()
entry_semestre = tk.Entry(ventana)
entry_semestre.pack()

tk.Label(ventana, text="Carrera:").pack()
entry_carrera = tk.Entry(ventana)
entry_carrera.pack()

tk.Label(ventana, text="Género:").pack()
entry_genero = tk.Entry(ventana)
entry_genero.pack()

tk.Label(ventana, text="Número de celular:").pack()
entry_celular = tk.Entry(ventana)
entry_celular.pack()

boton_guardar = tk.Button(ventana, text="Guardar Estudiante", command=guardar_registro)
boton_guardar.pack(pady=20)

ventana.mainloop()