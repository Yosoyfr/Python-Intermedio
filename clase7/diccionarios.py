# Diccionarios

# Diccionario vacio
materias = {}

# Insertar valores en el diccionario
materias["Lunes"] = ["Ciencias Sociales", "Ciencias Naturales"]
materias["Martes"] = ["Lenguaje", "Ingles"]
materias["Miercoles"] = ["Ciencias Sociales", "Ciencias Naturales", "Fisica"]
materias["Jueves"] = []
materias["Viernes"] = ["Matematicas"]


# Accediendo al valor de un diccionario
# print(materias.get("Lunes", []))


# Recorrido de un diccionario
# for aux in materias: # Cuando recorro un diccionario estoy iterando sus llaves
#    print(aux)


# Recorrido de un diccionario
# for dia in materias:
#    print('El dia:', dia, 'tengo las clases de:', materias.get(dia))


# Recorrido de un diccionario (llave, valor)
# for llave, valor in materias.items():
#    print('El dia:', llave, 'tengo las clases de:', valor)


llave = "Sabado"

if llave in materias:
    print('Tengo las clases de:', materias.get(llave))
else:
    print("Esta clave no existe en mi diccionario")
