#ejercicio 9
def agrupar_por_categoria(lista):
    grupos = {}
    for producto, categoria in lista:
        if categoria in grupos:
            grupos[categoria].append(producto)
        else:
            grupos[categoria] = [producto]
    return grupos

productos = [
    ("Manzana",   "Frutas"),
    ("Laptop",    "Tecnología"),
    ("Banano",    "Frutas"),
    ("Celular",   "Tecnología"),
    ("Naranja",   "Frutas")
]

print(agrupar_por_categoria(productos))
