# Escritura de archivos
archivo = open("saludo.py", "w")
archivo.write('print("Hola a todos") \n')
archivo.close()

contenidoNuevo = 'print("Nueva linea") \n'
archivo = open("saludo.py", "a")
archivo.write(contenidoNuevo)
archivo.close()
