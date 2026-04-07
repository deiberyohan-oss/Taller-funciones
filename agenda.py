#ejercicio 3
agenda = {}
def agregar_contacto(nombre, telefono):#agrega el contacto 
    agenda[nombre] = telefono
    print("Contacto agregado.")

def buscar_contacto(nombre): #busca el contacto
    if nombre in agenda:
        print(nombre, "->", agenda[nombre])
    else:
        print("No encontrado.")

def eliminar_contacto(nombre):#elimina el contacto
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado.") #si el contacto existe, lo elimina
    else:
        print("No encontrado.")

agregar_contacto("Petro", "321-8338487")
buscar_contacto("Petro")
eliminar_contacto("Petro")
