import datetime


class Producto:
    pass  # Instruccion que puede ser utilizada cuando se requiera una sentencia sintacticamente real pero en realidad no hace nada


# Creacion de un objeto = Instancia de una clase
p1 = Producto()


class Producto:
    codigo = '0161'
    nombre = 'Laptop Dell'
    precio = 5000
    marca = 'Dell'


# Creacion de un objeto = Instancia de una clase
p1 = Producto()

# print(p1.nombre)
p1.nombre = 'Tablet Dell'
# print(p1.nombre)


class Producto():
    def __init__(self, codigo, nombre, precio, marca, _modelo=None):
        self.codigo = codigo  # Atributo
        self.nombre = nombre  # Atributo
        self.precio = precio  # Atributo
        self.marca = marca  # Atributo
        self.iva = precio * 0.12  # Atributo
        self.fecha_creacion = datetime.date.today()  # Atributo
        self.modelo = _modelo  # Atributo

    def presentacion(self, _lema=''):
        print(self.nombre, _lema)

    def calcular_total(self, unidades):
        resultado = self.precio * unidades
        return resultado


p1 = Producto('0161', 'Laptop Dell', 12, 'Dell', 'Negro')
p1.presentacion()
#unidades = int(input("Cuantas unidades de " + p1.nombre + " va a llevar:"))
#total = p1.calcular_total(unidades)
# print('El total de la compra es: ', total)
# print('IVA:', total * 0.12)
