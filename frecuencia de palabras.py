#ejercicio 5
def contar_palabras(palabras):
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] = frecuencia[palabra] + 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

palabras = ["hola", "mundo", "hola", "python", "hola", "saludos", "python", "amor"]

print(contar_palabras(palabras))
