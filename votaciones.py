#ejercicio 10
candidatos_validos = ["Ana", "Luis", "Sara"]

def contar_votos(votos):
    conteo = {}
    invalidos = 0
    for voto in votos:
        if voto in candidatos_validos:
            if voto in conteo:
                conteo[voto] = conteo[voto] + 1
            else:
                conteo[voto] = 1
        else:
            invalidos = invalidos + 1
    return conteo, invalidos

def ganador(conteo):
    ganador_nombre = ""
    max_votos = 0
    for candidato in conteo:
        if conteo[candidato] > max_votos:
            max_votos = conteo[candidato]
            ganador_nombre = candidato
    total = sum(conteo.values())
    porcentaje = (max_votos / total) * 100
    return ganador_nombre, round(porcentaje, 2)

votos = ["Ana", "Luis", "Ana", "Pedro", "Sara", "Ana", "xxx"]

conteo, invalidos = contar_votos(votos)
print("Conteo:", conteo)
print("Votos inválidos:", invalidos)
print("Ganador:", ganador(conteo))
