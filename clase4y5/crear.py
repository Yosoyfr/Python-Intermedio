# Modo lectura viene predeterminadamente, lanza error si el archivo no existe
# archivo = open("file.txt", "r")
# archivo.close()


# Modo escritura, si el archivo no existe lo crea
# archivo = open("file.txt", "w")
# archivo.close()


# Modo agregar, si el archivo no existe lo crea
# archivo = open("file.txt", "a")
# archivo.close()

# Modo crear, si el archivo existe lanza un error
# archivo = open("file.txt", "x")
# archivo.close()


archivo = open("file.txt", "w+")
archivo.close()
