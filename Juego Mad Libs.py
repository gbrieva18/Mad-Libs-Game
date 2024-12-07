import tkinter as tk
from tkinter import messagebox

def generar_historia():
    # Se obtiene las palabras ingresadas por el usuario
    nombre = entry_nombre.get()
    lugar = entry_lugar.get()
    verbo = entry_verbo.get()
    adjetivo = entry_adjetivo.get()
    sustantivo = entry_sustantivo.get()

    # Crea la historia
    historia = f"Un dia, {nombre} fue a la {lugar}, donde empezo a {verbo}, donde lo interrumpe {sustantivo}. En ese momento {nombre} quedo perplejo ante la inminente {adjetivo} de {sustantivo}."

    #Mostrar la historia en un cuadro de texto
    messagebox.showinfo("Tu Historia", historia)

#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego Mad Libs")

#Crear etiquetas y entradas para las palabras
label_nombre = tk.Label(ventana, text="Ingresa un nombre: ")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

label_lugar = tk.Label(ventana, text="Ingrese un lugar: ")
label_lugar.pack(pady=5)
entry_lugar = tk.Entry(ventana)
entry_lugar.pack(pady=5)

label_verbo = tk.Label(ventana, text="Ingrese un verbo: ")
label_verbo.pack(pady=5)
entry_verbo = tk.Entry(ventana)
entry_verbo.pack(pady=5)

label_adjetivo = tk.Label(ventana, text="Ingrese un adjetivo: ")
label_adjetivo.pack(pady=5)
entry_adjetivo = tk.Entry(ventana)
entry_adjetivo.pack(pady=5)

label_sustantivo = tk.Label(ventana, text="Ingrese un sustantivo: ")
label_sustantivo.pack(pady=5)
entry_sustantivo = tk.Entry(ventana)
entry_sustantivo.pack(pady=5)

#Crear un boton que genere la historia
boton_generar = tk.Button(ventana, text="Generar Historia", command=generar_historia)
boton_generar.pack(pady=20)

#Iniciar el bucle principal en la ventana
ventana.mainloop()