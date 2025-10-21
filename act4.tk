import tkinter as tk
from tkinter import ttk

# Función para realizar las operaciones matemáticas
def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = combo_operacion.get()
        
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División por cero"
        else:
            resultado = "Operación no válida"
        
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Error: Ingresa números válidos")

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora Básica")
root.geometry("300x200")

# Crear y posicionar los elementos de la interfaz
label_num1 = tk.Label(root, text="Primer número:")
label_num1.pack(pady=5)

entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Segundo número:")
label_num2.pack(pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

label_operacion = tk.Label(root, text="Operación:")
label_operacion.pack(pady=5)

# Combobox para seleccionar la operación
combo_operacion = ttk.Combobox(root, values=["+", "-", "*", "/"])
combo_operacion.current(0)  # Selecciona "+" por defecto
combo_operacion.pack(pady=5)

# Botón para calcular
boton_calcular = tk.Button(root, text="Calcular", command=calcular)
boton_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
