materias = {}


# Insertar valores en el diccionario
materias["Lunes"] = ["Bases 2"]
materias["Martes"] = ["Analisis 2", "Gerenciales 2"]
materias["Miercoles"] = ["Modela 2", "Bases 2"]
materias["Jueves"] = ["Redes 2", "Analisis 2", "Gerenciales 2"]
materias["Viernes"] = ["Modela 2"]
materias["Sabado"] = ["Redes 2"]


# print(materias["Domingo"])
# print(materias.get("Domingo", []))
# Recorrer un diccionario
'''
for dia, clases in materias.items():
    print('El dia', dia, 'tengo:', clases)
for dia in materias:
    print('El dia', dia, 'tengo:', materias.get(dia))
'''


# Declarar diccionario de capitales

capitales = {'Chile': 'Santiago', 'Guatemala': 'Guatemala',
             'España': 'Madrid', 'Francia': 'Paris', 'Alemania': 'Berlin'}

pais = 'Islandia'
# print('La capital de', pais, 'es:', capitales.get(pais, "No hay registro"))

# Recorrer un diccionario
'''
for pais in capitales:
    print('La capital de', pais, 'es:', capitales.get(pais))
'''

# Verificar si existe una clave
x = 'Islandia'
'''
if x in capitales:
    print(capitales[x])
'''

# Como eliminar un registro de un diccionario
del capitales["Guatemala"]

# Agregar datos a diccionario
capitales["Portugal"] = 'Lisboa'

# Otra forma de declarar diccionario
# A partir de una tupla
alumnos = dict(((201807190, "Francisco"), (202004796, "Benjamin")))

# A partir de una cadenas
estudiantes = dict(FRANCISCO=201807190, BENJAMIN=202004796)

# Algunos metodos de los diccionarios
# Obtiene una lista de tuplas de la forma clave : valor
print(capitales.items())
# Obtiene una lista de las claves
print(capitales.keys())
# Obtiene una lista de los valores del diccionario
print(capitales.values())
