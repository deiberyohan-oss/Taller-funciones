# supermercado.py
# Archivo principal - aquí corre el programa
# Importamos todas las funciones del otro archivo
 
from Funcion import (
    mostrar_catalogo,
    agregar_producto,
    ver_carrito,
    calcular_total,
    eliminar_producto,
    vaciar_carrito
)
print("   BIENVENIDO AL SUPERMERCADO ")
 
while True:
    print("\n¿Qué deseas hacer?")
    print("  1. Ver catálogo")
    print("  2. Agregar producto al carrito")
    print("  3. Ver carrito")
    print("  4. Eliminar producto del carrito")
    print("  5. Ver total a pagar")
    print("  6. Vaciar carrito")
    print("  7. Salir")
 
    opcion = input("\nElige una opción (1-7): ")
 
    if opcion == "1":
        mostrar_catalogo()
 
    elif opcion == "2":
        mostrar_catalogo()
        nombre   = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        agregar_producto(nombre, cantidad)
 
    elif opcion == "3":
        ver_carrito()
 
    elif opcion == "4":
        ver_carrito()
        nombre = input("¿Qué producto quieres eliminar?: ")
        eliminar_producto(nombre)
 
    elif opcion == "5":
        ver_carrito()
        total = calcular_total()
        print(f"\nTOTAL A PAGAR: ${total}")
 
    elif opcion == "6":
        vaciar_carrito()
 
    elif opcion == "7":
        total = calcular_total()
        if total > 0:
            print(f"\nTu total fue: ${total}")
        print("¡Hasta luego!")
        break
 
    else:
        print("Opción no válida. Elige entre 1 y 7.")