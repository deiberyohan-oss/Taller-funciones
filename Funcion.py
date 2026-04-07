# funciones.py
# Aquí van todas las funciones que usa el supermercado

carrito = []

catalogo = {
    "manzana":  1500,
    "leche":    3200,
    "pan":      2500,
    "arroz":    4000,
    "huevos":   8500,
    "jugo":     3500,
    "cafe":     6000,
    "agua":     1200
}

def mostrar_catalogo():
    print("\n====== PRODUCTOS DISPONIBLES ======")
    for producto, precio in catalogo.items():
        print(f"  {producto:<12} -> ${precio}")
    print("===================================")

def agregar_producto(nombre, cantidad):
    nombre = nombre.lower()
    if nombre in catalogo:
        precio = catalogo[nombre]
        # Busca si ya está en el carrito para sumar cantidad
        for item in carrito:
            if item["nombre"] == nombre:
                item["cantidad"] += cantidad
                print(f"Se agregaron {cantidad} {nombre}(s) al carrito.")
                return
        # Si no estaba, lo agrega nuevo
        carrito.append({
            "nombre":   nombre,
            "precio":   precio,
            "cantidad": cantidad
        })
        print(f"Se agregaron {cantidad} {nombre}(s) al carrito.")
    else:
        print(f"El producto '{nombre}' no existe en el catálogo.")

def ver_carrito():
    if len(carrito) == 0:
        print("\nEl carrito está vacío.")
        return
    print("\n========== TU CARRITO ==========")
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        print(f"  {item['nombre']:<12} x{item['cantidad']}  -> ${subtotal}")
    print("=================================")

def calcular_total():
    total = 0
    for item in carrito:
        total += item["precio"] * item["cantidad"]
    return total

def eliminar_producto(nombre):
    nombre = nombre.lower()
    for item in carrito:
        if item["nombre"] == nombre:
            carrito.remove(item)
            print(f"'{nombre}' eliminado del carrito.")
            return
    print(f"'{nombre}' no está en el carrito.")

def vaciar_carrito():
    carrito.clear()
    print("Carrito vaciado.")