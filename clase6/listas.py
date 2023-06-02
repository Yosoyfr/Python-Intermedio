# Listas
# Operaciones con listas
lista1 = [1, 2, 3, 4, 5]  # Lista homogenea (numerico)
lista2 = ['uno', 2, True, (), [1, 2, 3]]  # Lista heterogenea

# print('Lista 1 homogenea:', lista1)
# print('Lista 2 heterogene:', lista2)

# Anidacion de listas
lista3 = [lista1, lista2]
# print(lista3)


lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Indices 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Negat -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# Obtener elementos de una lista - utilizando el indice
indice = 10
# valor = lista4[indice]
# print(valor)
# print(lista4[2])

# Obtener elementos de una lista - utilizando el indice negativo
indice = -3
valor = lista4[indice]
# print(valor)

# Accediendo a valores de una lista anidada
indice_exterior = 1
indice_interior = -1
valor = lista3[indice_exterior][indice_interior][1]
# print(valor)


# Utilizacion de rangos
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Indices 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
sub_lista4 = lista4[:]
# print(sub_lista4)

# Cambiar o mutar el valor de un elemento en una posicion de una lista
# print(lista4)
lista4[-1] = 100
# print(lista4)

# Agregando elementos con la funcion append
lista5 = [1, 2, 3, 4]
# print(lista5)
lista5.append(5)
lista5.append(6)
lista5.append(7)
# print(lista5)

# Agregando elementos con la funcion insert
lista5 = [1, 2, 3, 4]
# print(lista5)
lista5.insert(1, 6)
lista5.insert(4, 10)
lista5.insert(100, 200)
# print(lista5)

# Eliminar el primer elemento que coincida
lista5 = [1, 1, 3, 1, 2, 2, 3, 2, 4, 4]
# print(lista5)
lista5.remove(3)
lista5.remove(3)
# print(lista5)

# Eliminar el ultimo elemento/por indice de una lista
lista5 = [1, 2, 3, 4]
print(lista5)
valor = lista5.pop()  # Ultimo elemento
# valor = lista5.pop(1) # por indice
print(lista5)
