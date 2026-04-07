def analizar_notas(notas):
    promedio = sum(notas) / len(notas)
    mayor = max(notas)
    menor = min(notas)
    
    return promedio, mayor, menor


notas = [3.5, 4.0, 2.8, 4.5]
resultado = analizar_notas(notas)

print("Promedio:", resultado[0])
print("Mayor:", resultado[1])
print("Menor:", resultado[2])
