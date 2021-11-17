'''
SINTAXIS DE UN METODO O FUNCION EN PYTHON
def nombre_de_funcion():
    BLOQUES DE CODIGO NECESARIOS
'''


# Funcion vacia - METODO
def sumar(num1, num2) -> None:
    res = num1 + num2
    print("El resultado es:", res)


# Llamada de una funcion
# sumar(2, 10)


# Funcion normal - Funcion que retorna un valor
def sumar(num1, num2) -> int:
    res = num1 + num2
    return res


# Llamada de una funcion
restultado = sumar(5.1, 1)
# print("El resultado es:", restultado)

# ARGUMENTOS O PARAMETROS ARBITRARIOS


# Tipo CLAVE : VALOR
def resta(num1, num2):
    res = num2-num1
    return res


restultado = resta(num2=10, num1=18)
# print("El resultado es:", restultado)

# Parametro arbitrario de tipo *
# Se utiliza cuando una funcion espera recibir un numero arbitrario (desconocido) de argumentos, estos argumentos llegan a la funcion en forma de una tupla, para definir que esperamos, este tipo de parametro se antecede con un * (asterisco)


def sumar(*nums):
    res = 0
    # La funcion len(params) -> retorna la cantidad de items de la secuencia
    print("Longitud de la tupla:", len(nums))
    for x in nums:
        res += x
    return res


#restultado = sumar(1, 2, 3, 4, 10)
#print("El resultado es:", restultado)

def calcular_iva(iva, descuento, *productos):
    res = 0
    print(productos)
    for x in productos:
        res += x
    return res*iva-descuento


total = calcular_iva(1.12, 10, 50, 100, 200)
# print("El total es:", total)

# PARAMETROS POR OMISION


def saludar(nombre, _mensaje="Hola, como estas", _despedida="Adios"):
    print(_mensaje, nombre + ",", _despedida)


# saludar("Jaime")
