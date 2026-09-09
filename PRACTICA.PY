DICCIONARIO_FRANCMASON = {
    'A': '_|', 'B': '|_|', 'C': '|_',
    'D': '-|', 'E': '|-|', 'F': '|-',
    'G': '^|', 'H': '|^|', 'I': '|^',
    'J': '_|.', 'K': '|_|.', 'L': '|_.',
    'M': '-|.', 'N': '|-|.', 'O': '|-.',
    'P': '^|.', 'Q': '|^|.', 'R': '|^.',
    'S': '\\/', 'T': '>', 'U': '<', 'V': '/\\',
    'W': '\\/.', 'X': '>.', 'Y': '<.', 'Z': '/\\.'
}


def cifrar_texto(texto):
    resultado = []

    for char in texto.upper():
        if char in DICCIONARIO_FRANCMASON:
            resultado.append(DICCIONARIO_FRANCMASON[char])
        elif char == ' ':
            resultado.append('/')
        else:
            resultado.append(char)

    return " ".join(resultado)


# ===== PRUEBA =====

texto = input("Ingrese el mensaje: ")

resultado = cifrar_texto(texto)

print("Mensaje cifrado:")
print(resultado)