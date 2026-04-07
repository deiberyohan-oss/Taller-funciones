def analizar_ciudades(temperaturas):#ºanaliza las temperaturas de las ciudades
    ciudad_cal = ""
    ciudad_fri = ""
    
    temp_max = float('-inf') # temperatura máxima
    temp_min = float('inf') # temperatura mínima
    
    for ciudad, lista in temperaturas.items():
        if len(lista) == 0:#si la lista de temperaturas está vacía, se salta esa ciudad
            continue        
        promedio = sum(lista) / len(lista)

        if promedio > temp_max:
            temp_max = promedio #actualiza la temperatura máxima y la ciudad más caliente
            ciudad_cal = ciudad 
        
        if promedio < temp_min:
            temp_min = promedio#actualiza la temperatura mínima y la ciudad más fría
            ciudad_fri = ciudad
    
    return ciudad_cal, temp_max, ciudad_fri, temp_min

temperaturas = {
    "Bogotá":   [14, 15, 13, 16, 14, 15, 13],
    "Cali":     [28, 29, 27, 30, 28, 31, 29],
    "Medellín": [22, 33, 21, 24, 22, 23, 22]
}

resultado = analizar_ciudades(temperaturas)

print("Más caliente:", resultado[0], resultado[1])
print("Más fría:", resultado[2], resultado[3])
