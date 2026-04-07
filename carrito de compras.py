carrito = []

def agregar_producto(nombre, precio):
    carrito.append({"nombre": nombre, "precio": precio})
    print("Producto agregado.")

def aplicar_descuento(porcentaje):
    total = 0
    for producto in carrito:
        total = total + producto["precio"]
    descuento = total * (porcentaje / 100)
    return total - descuento

def total_a_pagar():
    total = 0
    for producto in carrito:
        total = total + producto["precio"]
    return total

agregar_producto("Camisa", 80000)
agregar_producto("Pantalón", 120000)
print("Total sin descuento: $", total_a_pagar())
print("Total con 10% descuento: $", aplicar_descuento(10))