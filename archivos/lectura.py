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
ruta = "file.txt"
# Apertura del archivo
archivo = open(ruta)
# Lectura de todo el contenido del archivo
# contenido = archivo.read()


# Lectura en partes del archivo
#contenido = archivo.read(12)


# Lectura linea por linea
# linea1 = archivo.readline().strip()
# linea2 = archivo.readline().strip()
# linea3 = archivo.readline().strip()
# linea4 = archivo.readline().strip()
# print(linea4)

linea = archivo.readline().strip()
while linea != '':
    print(linea)
    if linea == 'Mauricio':
        break
    linea = archivo.readline().strip()

# Cierre del archivo
archivo.close()
print('Fin de la lectura')
