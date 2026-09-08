import tkinter as tk
# LÓGICA DEL CIFRADO (Totalmente separada)
def cifrado_cesar(texto, n_posiciones):
    """Función exclusiva para CIFRAR texto desplazando 'n' posiciones"""
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Identificamos si es mayúscula o minúscula para no deformar el texto
            base = ord('A') if char.isupper() else ord('a')
            # Aplicamos la fórmula del cifrado César
            nuevo_char = chr((ord(char) - base + n_posiciones) % 26 + base)
            resultado += nuevo_char
        else:
            # Los espacios y números se quedan igual
            resultado += char
    return resultado
# LÓGICA PARA DESCIFRAR
def descifrado_cesar(texto, n_posiciones):
    """Función exclusiva para DESCIFRAR texto"""
    return cifrado_cesar(texto, -n_posiciones)
#INTERFAZ GRÁFICA 
class InterfazCesarSoloCifrar:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Cifrado César (Posiciones n)")
        self.ventana.geometry("650x550") # Ajusté un poco el alto para el selector
        self.ventana.config(bg="#f0f4f8") # Fondo azul muy clarito

        # Contenedor principal (Tarjeta blanca del diseño)
        main_frame = tk.Frame(ventana, bg="white")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)

        # Título
        title_label = tk.Label(main_frame, text="CIFRADO CÉSAR CON POSICION", 
                               font=("Helvetica", 20, "bold"), bg="white", fg="#0d3b66")
        title_label.pack(pady=(20, 10))

        # Selector de posiciones 'n' (Inicia en 3) adaptado al diseño
        frame_posiciones = tk.Frame(main_frame, bg="white")
        frame_posiciones.pack(pady=5)
        
        tk.Label(frame_posiciones, text="Posiciones a desplazar (n):", font=("Helvetica", 11, "bold"), 
                 bg="white", fg="#0d3b66").pack(side=tk.LEFT, padx=5)

        self.var_n = tk.IntVar(value=3) # Posición 3 por defecto

        self.selector_n = tk.Spinbox(frame_posiciones, from_=1, to=100, textvariable=self.var_n, 
                                     width=5, font=("Arial", 12), justify="center", relief="solid", bd=1)

        self.selector_n.pack(side=tk.LEFT, padx=5)

        # Etiqueta "Texto plano:"
        tk.Label(main_frame, text="Texto plano:", font=("Helvetica", 11, "bold"), 
                 bg="white", fg="#0d3b66").pack(pady=(15, 5))
        
        # Entrada de Texto
        self.entrada_texto = tk.Entry(main_frame, font=("Arial", 14), width=45, justify="center", relief="solid", bd=1)
        self.entrada_texto.pack(pady=5, ipady=5)
        
        # Frame para agrupar los botones
        button_frame = tk.Frame(main_frame, bg="white")
        button_frame.pack(pady=15)
        
        # Botón CIFRAR (Azul)
        self.btn_cifrar = tk.Button(button_frame, text=" CIFRAR", font=("Helvetica", 10, "bold"), 
                                    bg="#1976D2", fg="white", width=15, cursor="hand2", relief="flat",
                                    command=self.accion_cifrar)
        self.btn_cifrar.pack(side=tk.LEFT, padx=10, ipady=5)


        # ====================================================
        # NUEVO: BOTÓN DESCIFRAR
        # ====================================================

        self.btn_descifrar = tk.Button(button_frame, text="DESCIFRAR", font=("Helvetica", 10, "bold"), 
                                       bg="#388E3C", fg="white", width=15, cursor="hand2", relief="flat",
                                       command=self.accion_descifrar)
        self.btn_descifrar.pack(side=tk.LEFT, padx=10, ipady=5)


        # Botón LIMPIAR (Gris) - Añadido para mantener tu diseño original
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
        
        # Configurar un "tag" para poder centrar el texto
        self.salida_texto.tag_configure("centro", justify='center')
        
        # Mostrar el texto de ejemplo inicial
        self.mostrar_placeholder()

    def mostrar_placeholder(self):
        self.salida_texto.config(state=tk.NORMAL)
        self.salida_texto.delete("1.0", tk.END)
        self.salida_texto.insert(tk.END, "\n\nEl cifrado aparecerá aquí")
        self.salida_texto.tag_add("centro", "1.0", "end")
        self.salida_texto.config(fg="#9ba4b5") # Color gris claro
        self.salida_texto.config(state=tk.DISABLED)

    def limpiar_todo(self):
        """Limpia el texto, resetea el valor 'n' y pone el placeholder"""
        self.entrada_texto.delete(0, tk.END)
        self.var_n.set(3) # Vuelve al valor por defecto
        self.mostrar_placeholder()

    # Acción del botón Cifrar
    def accion_cifrar(self):
        #Obtener el texto y el número 'n'
        texto = self.entrada_texto.get().strip()

        if not texto:
            self.mostrar_placeholder()
            return

        n = self.var_n.get()

        #Llamar a la lógica matemática separada
        resultado = cifrado_cesar(texto, n)
        
        #Mostrar el resultado en pantalla
        self.salida_texto.config(state=tk.NORMAL)
        self.salida_texto.delete("1.0", tk.END)
        self.salida_texto.insert(tk.END, f"\n\n{resultado}") # Centrado vertical simple
        self.salida_texto.tag_add("centro", "1.0", "end")
        self.salida_texto.config(fg="black") # Texto a negro para lectura
        self.salida_texto.config(state=tk.DISABLED)
    # NUEVO: ACCIÓN DEL BOTÓN DESCIFRAR
    def accion_descifrar(self):
        # Obtener el resultado cifrado
        texto = self.salida_texto.get("1.0", tk.END).strip()

        # Si no hay resultado, no hacer nada
        if not texto or texto == "El cifrado aparecerá aquí":
            return

        n = self.var_n.get()

        # Descifrar el resultado
        resultado = descifrado_cesar(texto, n)

        # Mostrar el texto descifrado
        self.salida_texto.config(state=tk.NORMAL)
        self.salida_texto.delete("1.0", tk.END)
        self.salida_texto.insert(tk.END, f"\n\n{resultado}")
        self.salida_texto.tag_add("centro", "1.0", "end")
        self.salida_texto.config(fg="black")
        self.salida_texto.config(state=tk.DISABLED)
#EJECUCIÓN DEL PROGRAMA
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazCesarSoloCifrar(root)
    root.mainloop()