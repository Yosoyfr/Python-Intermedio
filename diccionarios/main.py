materias = {}

# Insertar valores en un diccionario
materias["Lunes"] = ['Bases 2']
materias["Martes"] = ["Analisis 2", "Gerenciales 2"]
materias["Miercoles"] = ["Modela 2", "Bases 2"]
materias["Jueves"] = ["Redes 2", "Analisis 2", "Gerenciales 2"]
materias["Viernes"] = ["Modela 2"]
materias["Sabado"] = ["Redes 2"]

# Accediendo al valor de un diccionario
'''
dia = materias.get('Domingo', ['Este dia no tengo clases'])
for x in dia:
    print(x)
'''

# Recorrido de un diccionario
'''
for dia in materias:
    print('El dia:', dia, 'tengo las clases de:', materias.get(dia))
'''

dia = 'Lunes'
if dia in materias:
    print(materias.get(dia))
else:
    print('Esta clave no existe')
