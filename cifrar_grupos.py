import tkinter as tk
from tkinter import messagebox


def vigenere(texto, clave, cifrar=True):
    clave = clave.upper()
    resultado = ""
    j = 0

    for c in texto.upper():
        if 'A' <= c <= 'Z':
            k = ord(clave[j % len(clave)]) - 65
            desplazamiento = k if cifrar else -k
            resultado += chr((ord(c) - 65 + desplazamiento) % 26 + 65)
            j += 1
        else:
            resultado += c

    return resultado


def cifrar():
    texto = entrada_texto.get("1.0", tk.END).strip()
    clave = entrada_clave.get().strip()

    if not texto or not clave:
        messagebox.showwarning("Advertencia", "Ingrese el texto y la clave.")
        return

    if not clave.isalpha():
        messagebox.showwarning("Advertencia", "La clave debe contener solo letras.")
        return

    resultado = vigenere(texto, clave, True)

    salida.delete("1.0", tk.END)
    salida.insert("1.0", resultado)


def descifrar():
    texto = entrada_texto.get("1.0", tk.END).strip()
    clave = entrada_clave.get().strip()

    if not texto or not clave:
        messagebox.showwarning("Advertencia", "Ingrese el texto y la clave.")
        return

    if not clave.isalpha():
        messagebox.showwarning("Advertencia", "La clave debe contener solo letras.")
        return

    resultado = vigenere(texto, clave, False)

    salida.delete("1.0", tk.END)
    salida.insert("1.0", resultado)


def limpiar():
    entrada_texto.delete("1.0", tk.END)
    entrada_clave.delete(0, tk.END)
    salida.delete("1.0", tk.END)


# Ventana principal
ventana = tk.Tk()
ventana.title("Cifrado de Vigenére")
ventana.geometry("650x550")
ventana.resizable(False, False)

# Título
titulo = tk.Label(
    ventana,
    text="CIFRADO DE VIGENÉRE",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=15)

# Texto
tk.Label(
    ventana,
    text="Texto:",
    font=("Arial", 12, "bold")
).pack(anchor="w", padx=30)

entrada_texto = tk.Text(
    ventana,
    height=7,
    width=70,
    font=("Arial", 11)
)
entrada_texto.pack(padx=30, pady=5)

# Clave
tk.Label(
    ventana,
    text="Clave:",
    font=("Arial", 12, "bold")
).pack(anchor="w", padx=30, pady=(10, 0))

entrada_clave = tk.Entry(
    ventana,
    width=40,
    font=("Arial", 12)
)
entrada_clave.pack(padx=30, pady=5)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

tk.Button(
    frame_botones,
    text="CIFRAR",
    width=15,
    command=cifrar
).grid(row=0, column=0, padx=5)

tk.Button(
    frame_botones,
    text="DESCIFRAR",
    width=15,
    command=descifrar
).grid(row=0, column=1, padx=5)

tk.Button(
    frame_botones,
    text="LIMPIAR",
    width=15,
    command=limpiar
).grid(row=0, column=2, padx=5)

# Resultado
tk.Label(
    ventana,
    text="Resultado:",
    font=("Arial", 12, "bold")
).pack(anchor="w", padx=30)

salida = tk.Text(
    ventana,
    height=7,
    width=70,
    font=("Arial", 11)
)
salida.pack(padx=30, pady=5)

ventana.mainloop()

def vigenere(texto, clave, cifrar=True):
    clave = clave.upper()
    resultado = ""
    j = 0

    for c in texto.upper():
        if 'A' <= c <= 'Z':
            k = ord(clave[j % len(clave)]) - 65
            desplazamiento = k if cifrar else -k
            resultado += chr((ord(c) - 65 + desplazamiento) % 26 + 65)
            j += 1
        else:
            resultado += c

    return resultado
