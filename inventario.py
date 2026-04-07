#ejercicio 4
def valor_total(inventario):
    total = 0
    for producto in inventario:
        total = total + producto["precio"] * producto["cantidad"]
    return total

inventario = [
    {"nombre": "Laptop",   "precio": 2500000, "cantidad": 3},
    {"nombre": "Mouse",    "precio":   50000, "cantidad": 10},
    {"nombre": "Teclado",  "precio":   80000, "cantidad": 7}
]

print("Valor total: $", valor_total(inventario))    
