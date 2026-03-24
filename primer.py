"""""
def saludar():
    """"Funcion que saluda al usuario""""
    print("Hola mundo")


#funcion sumar
def suma(a, b):
    #suma dos numeros
    resultado = a + b
    return resultado

total= suma(5, 3)
print(total)
#resta
def resta(a, b):
    #resta dos numeros
    resultado = a - b
    return resultado

total= resta(5, 3)
print(total)
#multiplicacion
def multiplicacion(a, b):
    #multiplica dos numeros
    resultado = a * b
    return resultado
total= multiplicacion(5, 3)
print(total)
#division
def division(a, b):
    #divide dos numeros
    resultado = a / b
    return resultado    
total= division(5, 3)
print(total)
#parametros por defecto
def potencia(base, exponente=2):
   #calcula la potencia de un numero
    return  base ** exponente
print(potencia(5))
print(potencia(2, 3))
#tabla de multiplicar
def tabla_multiplicar(numero):
    #imprime la tabla de multiplicar de un numero
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
tabla_multiplicar(11)
#argumentos con nombre
def pelis(nombre,director,año):
    #pelicula
    return f"¨{nombre}, dirigido por {director} en el año {año}"
print(pelis(nombre="El Padrino", director="Francis Ford Coppola", año=1972))
"""""
#retorno multiple
def operaciones(a, b):
    #realiza varias operaciones con dos numeros
    suma = a + b
    promedio = (a + b) / 2
    num_mayor = max(a, b)
    return f"la suma es {suma},\n el promedio es {promedio}\n y el número mayor es {num_mayor}"
resultado=operaciones(10, 2)
print(resultado)
#argumentos variables
def sumas(*args):    
    #suma culaquier cantidad de numeros
    total = 0
    for numero in args:
        total += numero
    return total
print(sumas(1, 2, 3,))
print(sumas(1,2,3,4,5,6))
