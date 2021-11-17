# Escritura de archivos
#archivo = open('saludar.py', 'w')
#archivo.write('print("Hola a todos desde la ejecucion 1") \n')
# archivo.close()

# Modo de agregar
#archivo = open('saludar.py', 'a')
#archivo.write('print("Nueva linea")  \n')
# archivo.close()

estudiante = ['Francisco', 'Emma', 'Manuel', 'Americo', 'Jose']
archivo = open('estudiantes.py', 'w')
contenido = 'print("Nombres de estudiantes")  \n'
archivo.write(contenido)
for nombre in estudiante:
    contenido = 'print("' + nombre + '")  \n'
    archivo.write(contenido)
