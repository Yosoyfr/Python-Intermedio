# LISTAS
# Operaciones con listas
lista1 = [1, 2, 3, 4, 5]  # Lista homogenea (numerica)
lista2 = ['uno', 2, True, (), []]  # Lista heterogenea

#print('Lista 1 homogenea:', lista1)
#print('Lista 2 heterogenea:', lista2)

# Anidacion de listas
lista3 = ['nombre', lista1]
lista4 = [54, 25, 65, 10, 15, 2, 4, 1]


# Obtener elementos de una lista
# print(lista4[5])

# Imprimir el ultimo elemento de una lista
# print(lista4[-3])
# Para recorrer la lista de adelante para atras solo es de enviar la posicion con un signo negativo

# Acceder a la lista anidada e imprimir un elemento de esta
# print(lista3[1][2])

lista4 = [54, 25, 65, 10, 15, 2, 4, 1]

# Como invertir el orden de una lista
# print(lista4[::-1])

# Cambiar o mutar el valor de un elemento en una posicion de una lista
# print(lista4)
# lista4[0] = 100
# print(lista4)

# Añadir elementos con la funcion append
lista5 = [1, 2, 3, 4]
# lista5.append(5)
# lista5.append(6)
# print(lista5)


# Añadir elementos con la funcion insert
lista5 = [1, 2, 3, 4]
#lista5.insert(1, 0)
#lista5.insert(4, 10)
# print(lista5)


# Eliminar el primer elemento que coincida
lista5 = [1, 2, 3, 4, 4, 5, 6, 6, 7]
# lista5.remove(4)
# print(lista5)


# Eliminar el ultimo elemento de una lista
lista5 = [1, 2, 3, 4]
# lista5.pop()
# print(lista5)


# Otra forma de eliminar elementos de una lista
lista5 = [1, 2, 3, 4, [1, 2, 3]]
del lista5[4][0]
print(lista5)
