import tkinter as tk

def sumar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor ingrese números válidos.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Suma de dos números")

# Etiqueta para indicar qué hacer
label_instruccion = tk.Label(ventana, text="Ingresar número:")
label_instruccion.grid(row=0, column=0, columnspan=2, pady=5)

# Entradas de texto
entry1 = tk.Entry(ventana)
entry1.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(ventana)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Botón para sumar
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.grid(row=2, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

# Ejecutar la aplicación
ventana.mainloop()
