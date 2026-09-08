import tkinter as tk
def cifrado_cesar_fijo(texto):
    """Función para CIFRAR texto con un desplazamiento fijo de 3 posiciones"""
    posiciones = 3
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Identificamos si es mayúscula o minúscula
            base = ord('A') if char.isupper() else ord('a')
            # Aplicamos la fórmula del cifrado César con la posición fija (+3)
            nuevo_char = chr((ord(char) - base + posiciones) % 26 + base)
            resultado += nuevo_char
        else:
            # Los espacios y símbolos se quedan igual
            resultado += char
    return resultado

def descifrado_cesar_fijo(texto):
    """Función para DESCIFRAR texto con un desplazamiento fijo de 3 posiciones"""
    posiciones = 3
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Identificamos si es mayúscula o minúscula
            base = ord('A') if char.isupper() else ord('a')
            # Aplicamos la fórmula inversa del cifrado César (-3)
            nuevo_char = chr((ord(char) - base - posiciones) % 26 + base)
            resultado += nuevo_char
        else:
            # Los espacios y símbolos se quedan igual
            resultado += char
    return resultado

# INTERFAZ GRÁFICA 
class InterfazCesarSimple:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Cifrado César")
        self.ventana.geometry("650x500")
        self.ventana.config(bg="#f0f4f8") # Fondo azul muy clarito
        
        # Contenedor principal (Tarjeta blanca del diseño)
        main_frame = tk.Frame(ventana, bg="white")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        # Título
        title_label = tk.Label(main_frame, text="CIFRADO CÉSAR", 
                               font=("Helvetica", 20, "bold"), bg="white", fg="#0d3b66")
        title_label.pack(pady=(20, 15))
        
        # Etiqueta "Texto plano:"
        tk.Label(main_frame, text="Texto plano:", font=("Helvetica", 11, "bold"), 
                 bg="white", fg="#0d3b66").pack(pady=(10, 5))
        
        # Entrada de Texto (Una sola línea centrada, como en el diseño)
        self.entrada_texto = tk.Entry(main_frame, font=("Arial", 14), width=45, justify="center", relief="solid", bd=1)
        self.entrada_texto.pack(pady=5, ipady=5)
        
        # Frame para agrupar los botones
        button_frame = tk.Frame(main_frame, bg="white")
        button_frame.pack(pady=15)
        
        # Botón CIFRAR (Azul)
        self.btn_cifrar = tk.Button(button_frame, text="CIFRAR", font=("Helvetica", 10, "bold"), 
                                    bg="#1976D2", fg="white", width=15, cursor="hand2", relief="flat",
                                    command=self.accion_cifrar)
        self.btn_cifrar.pack(side=tk.LEFT, padx=10, ipady=5)
        
        # Botón DESCIFRAR (Verde)
        self.btn_descifrar = tk.Button(button_frame, text="DESCIFRAR", font=("Helvetica", 10, "bold"),
                                       bg="#2e7d32", fg="white", width=15, cursor="hand2", relief="flat",
                                       command=self.accion_descifrar)
        self.btn_descifrar.pack(side=tk.LEFT, padx=10, ipady=5)
        
        # Botón LIMPIAR (Gris)
        self.btn_limpiar = tk.Button(button_frame, text="LIMPIAR", font=("Helvetica", 10, "bold"), 
                                     bg="#e0e6ed", fg="#0d3b66", width=15, cursor="hand2", relief="flat",
                                     command=self.limpiar_todo)
        self.btn_limpiar.pack(side=tk.LEFT, padx=10, ipady=5)
        
        # Etiqueta "Resultado cifrado:"
        tk.Label(main_frame, text="Resultado cifrado:", font=("Helvetica", 11, "bold"), 
                 bg="white", fg="#0d3b66").pack(pady=(15, 5))
        
        # Salida de Texto (Caja de resultado)
        self.salida_texto = tk.Text(main_frame, height=5, width=50, font=("Arial", 14), 
                                    relief="solid", bd=1, wrap=tk.WORD)
        self.salida_texto.pack(pady=(0, 20))
        
        # Configurar un "tag" para poder centrar el texto en el widget Text
        self.salida_texto.tag_configure("centro", justify='center')
        
        # Mostrar el texto de ejemplo inicial
        self.mostrar_placeholder()

    def mostrar_placeholder(self):
        self.salida_texto.config(state=tk.NORMAL)
        self.salida_texto.delete("1.0", tk.END)
        # Agregamos saltos de línea para centrarlo verticalmente de forma sencilla
        self.salida_texto.insert(tk.END, "\n\nEl cifrado ")
        self.salida_texto.tag_add("centro", "1.0", "end")
        self.salida_texto.config(fg="#9ba4b5") # Color gris claro
        self.salida_texto.config(state=tk.DISABLED)

    def limpiar_todo(self):
        self.entrada_texto.delete(0, tk.END)
        self.mostrar_placeholder()

    def accion_cifrar(self):
        #Obtener el texto introducido
        texto = self.entrada_texto.get().strip()
        
        if not texto:
            self.mostrar_placeholder()
            return
            
        #Llamar a la lógica matemática
        resultado = cifrado_cesar_fijo(texto)
        
        #Mostrar el resultado en pantalla
        self.salida_texto.config(state=tk.NORMAL)
        self.salida_texto.delete("1.0", tk.END)
        self.salida_texto.insert(tk.END, f"\n\n{resultado}") # Centrado vertical simple
        self.salida_texto.tag_add("centro", "1.0", "end")
        self.salida_texto.config(fg="black") # Cambiar el texto a negro para que se lea bien
        self.salida_texto.config(state=tk.DISABLED)

    def accion_descifrar(self):
        #Obtener el texto introducido (se asume que está cifrado)
        texto = self.entrada_texto.get().strip()
        
        if not texto:
            self.mostrar_placeholder()
            return
            
        #Llamar a la lógica matemática inversa
        resultado = descifrado_cesar_fijo(texto)
        
        #Mostrar el resultado en pantalla
        self.salida_texto.config(state=tk.NORMAL)
        self.salida_texto.delete("1.0", tk.END)
        self.salida_texto.insert(tk.END, f"\n\n{resultado}") # Centrado vertical simple
        self.salida_texto.tag_add("centro", "1.0", "end")
        self.salida_texto.config(fg="black") # Cambiar el texto a negro para que se lea bien
        self.salida_texto.config(state=tk.DISABLED)

# EJECUCIÓN DEL PROGRAMA
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazCesarSimple(root)
    root.mainloop()