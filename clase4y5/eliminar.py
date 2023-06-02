import os

archivo = 'file.txt'
if os.path.exists(archivo):
    os.remove(archivo)
else:
    print('El archivo no existe')
