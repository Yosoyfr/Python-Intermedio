# TUPLAS
# Operaciones con tuplas
tupla1 = (1, 2, 3)  # Declaracion de una tupla
tupla2 = 1, 2, 3, 4  # Misma declaracion pero sin parentesis
tupla3 = (1,)  # Si es solo un elemnto finalizamos con una ","
tupla4 = tupla1, 4, 5, 6, 7, 8  # Anidación de tuplas
tupla5 = ()  # Declaracion de tupla vacia

# print(tupla5)


# Longitud de una tupla
# print('Numero de elementos:', len(tupla5))

# print(tupla1[1])
# tupla1[1] = 100 NO SE PUEDE ASIGNAR O MODIFICAR UN VALOR DE UNA TUPLA

# Rangos
# print(tupla2[:2])


# LISTAS
# Operaciones con listas
lista1 = [1, 2, 3, 4, 5, 6]  # LIsta homogenea (numerica)
lista2 = ['uno', 2, True, (), []]  # Lista heterogenea

# Anidacion de listas
lista3 = ["nombre", lista1]
lista4 = [54, 25, 65, 10, 15, 2, 4, 1]

# print('Lista 1 homogenea: ',lista1)
# print('Lista 2 heterogenea: ',lista1)

# Imprimir el ultimo elemnto de una lista
# print(lista1[-1])
# Para recorrer la lista de adelante para atras solo es de enviar la posicion con un signo negativo

# Impmir un elemento especifico de la lista
# print(lista2[2])

# Acceder a la lista anidad e imprimir un elemento de esta
# print(lista3[1][4])

# Como invertir en orden de la lista
# print(lista4[::-1])

# Cambiar o mutar el valor de un elemento en una posicion de la lista
#lista1[2] = 100
# print(lista1)

# Eliminar el ultimo elemento de una lista
# lista1.pop()
# print(lista1)

# Elimina el primer elemento que coincida
# lista2.remove(True)
# print(lista2)

# Otra forma de eliminar
del lista2[1]
# print(lista2)

# Eliminar elementos [desde:hasta]
lista1 = [1, 2, 3, 4, 5, 6]
del lista1[2:5]
# print(lista1)

# Como borrar todos los elementos de una lista
lista1 = [1, 2, 3, 4, 5, 6]
lista1[:] = []
lista1 = []
# print(lista1)

lista1 = [1, 2, 3, 4, 5, 6]
# Añadir un elemento al final de la lista
#lista1 = lista1 + [7, 8, 9]
# print(lista1)


# Añadir elementos con la funcion append
# lista1.append(10)
# print(lista1)

# Añadir o extender los elemeentos una lista con la funcion extend
#lista1.extend([7, 8, 9])
# print(lista1)

# Contar el numero de veces que aparece un elemento
lista5 = [1, 11, 2, 2, 10, 3, 4, 5, 6, 7, 8, 8, 2, 9]
# print(lista5.count(10))

# Obtener la posicion que ocupa un elemento
# print(lista5.index(9))

# Tambien podemos ordenar listas de forma ascendente por default
# lista5.sort()
# print(lista5)

# Tambien podemos ordenar listas de forma descendente
# lista5.sort(reverse=True)
# print(lista5)

# Podemos ordenar una lista y guardarla en otra
lista6 = sorted(lista5)
print(lista5)
print(lista6)
