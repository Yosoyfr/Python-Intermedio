# Tuplas
# Las tuplas en su interior pueden tener cualquier tipo de dato

# Operaciones con tuplas
tupla1 = (1, 2, 3, 4, 5)  # Declaracion de una tupla
# Misma declaracion pero sin utilizar parentesis (empaquetado)
tupla2 = 6, 7, 8, 9, 10
# Si es solo un elemento finalizamos con una ','
tupla3 = (1,)  # Tupla de un elemento
tupla4 = tupla1, tupla2, True, "Texto"  # Anidacion de tuplas
tupla5 = ()  # Tupla vacia

# Longitud de una tupla
size = len(tupla5)
# print(size)

# Obtener elementos de una tupla
# print(tupla2[0])
# Las tuplas son un tipo de dato inmutable
# tupla2[0] = 100

# Utilizacion de rangos
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
sub_tupla = tupla[4:6]
# print(sub_tupla)

print(tupla4)
print(tupla4[0])
print(tupla4[0][1])
