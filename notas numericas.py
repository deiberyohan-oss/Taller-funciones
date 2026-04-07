rangos = (
    (4.5, 5.0, "A"),
    (4.0, 4.4, "B"),
    (3.0, 3.9, "C"),
    (2.0, 2.9, "D"),
    (0.0, 1.9, "F")
)
def nota_a_letra(nota):
    for minimo, maximo, letra in rangos:
        if minimo <= nota <= maximo:
            return letra
    return "Nota inválida"

def reporte(estudiantes):
    for nombre, nota in estudiantes:
        print(nombre, "->", nota, "->", nota_a_letra(nota))

estudiantes = [("Ana", 4.7), ("Luis", 3.2), ("Sara", 1.5)]
reporte(estudiantes)