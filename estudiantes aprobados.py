def estudiantes_aprobados(lista):
    aprobados = []
    for nombre, nota in lista:
        if nota >= 3.0:
            aprobados.append((nombre, nota))
    return aprobados

estudiantes = [
    ("Maria", 3.5),
    ("Samuel", 2.0),
    ("Sarah", 4.2),
    ("Juan", 1.8),
    ("Yoan", 5.0)
]

print(estudiantes_aprobados(estudiantes))