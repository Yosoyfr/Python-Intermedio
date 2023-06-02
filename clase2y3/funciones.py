'''
SINTAXIS DE UNA FUNCION EN PYTHON
def nombre_de_la_funcion([parametros_opcionales]):
    # BLOQUES DE CODIGO QUE PERTENECEN A LA FUNCION
'''


# Funcion vacia -> METODO
def sumar(num1, num2) -> None:
    res = num1 + num2
    print("El resultado es:", res)


# Llamada de una funcion
# sumar(3, 2)
# sumar(9, 5)
# sumar(2, 3)


# Funcion normal -> Funcion que retorna una valor [int]
# La utilizacion de argumentos por referencia
def restar(num1, num2) -> int:
    res = num2 - num1
    return res


# Llamada de una funcion que retorna valor
# resultado = restar(1, 10)
# resultado = restar(10, 1)
# print("El resultado es:", resultado)
# resultado = restar(num2=10, num1=1)
# print("El resultado es:", resultado)


# Funcion normal -> Funcion que retorna una valor [int]
# Utilizacion de la asignacion de parametros en la forma CLAVE=VALOR
def multiplicar(num1, _num2=5) -> int:
    res = _num2 * num1
    return res


# resultado = multiplicar()
# print("El resultado es:", resultado)


# Funcion normal -> Funcion que retorna una valor [list]
# Utilizacion de la asignacion de parametros arbitrarios ->
# Se utiliza cuando una funcion espera recibir un numero arbitrario (desconocido)
# de argumentos, estos argumentos llegan a la funcion en forma de una tupla,
# para definir que esperamos, este tipo de parametro se antecede con un * (asterisco)
def lista_utiles(*utiles) -> list:
    # La funcion len(params) -> retorna la cantida de items en una secuencia
    print('Longitud de la tupla (lista de utiles):', len(utiles))
    lista = []
    for util in utiles:
        lista.append(util)
    return lista


lista = lista_utiles("Cuaderno", "lapicero rojo", "lapicero negro", "lapiz")
print("La lista de utiles es:", lista)
