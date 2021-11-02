import os

if os.path.exists("archivo.txt"):
    os.remove("archivo.txt")
else:
    print("El archivo no existe")
