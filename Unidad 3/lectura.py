'''
MODES
"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing.  The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist.
'''

# Lectura de archivos
ruta = "lectura.txt"
# Apertura del archivo
archivo = open(ruta)
# Lectura de todo el contenido del archivo
# print(archivo.read())

# Lectura de linea por lina
#linea1 = archivo.readline()
#linea2 = archivo.readline()

#linea3 = archivo.readline(6)
# print(linea1)
# print(linea2)
# print(linea3)

# Leer el archivo completo
linea = archivo.readline().strip()
while linea != "":
    print(linea)
    if linea == "Francisco":
        break
    linea = archivo.readline().strip()


# Cierre del archivo
archivo.close()
print("Fin de la lectura")
