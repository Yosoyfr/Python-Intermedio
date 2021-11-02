class Persona:
    pass  # Instruccion que puede ser utilizada cuando querras una sentencia sintacticamente pero en realidad no hace nada


# Creacion de un objeto = Instancia de una clase
p1 = Persona()


class Persona:
    nombre = ""
    apellido = ""
    dpi = ""


p1 = Persona()
p1.nombre = "Francisco"
p1.apellido = "Suarez"
p1.dpi = 1

p2 = Persona()
p2.nombre = "Benjamin"
p2.apellido = "Ardon"
p2.dpi = 2

#print("Persona 1 - Nombre:", p1.nombre, "Apellido:", p1.apellido)
#print("Persona 2 - Nombre:", p2.nombre, "Apellido:", p2.apellido)


class Persona:  # Clase
    nombre = ""  # Atributos
    apellido = ""  # Atributos
    dpi = ""  # Atributos

    # Metodos o funciones
    def presentacion(self):
        print("Persona", self.dpi, "- Nombre:",
              self.nombre, "Apellido:", self.apellido)


p1 = Persona()
p1.nombre = "Francisco"
p1.apellido = "Suarez"
p1.dpi = 1

p2 = Persona()
p2.nombre = "Benjamin"
p2.apellido = "Ardon"
p2.dpi = 2

# p1.presentacion()
# p2.presentacion()


class Persona:  # Clase

    def __init__(self, nombre, apellido, dpi):
        self.nombre = nombre  # Atributos
        self.apellido = apellido  # Atributos
        self.dpi = dpi  # Atributos

    # Metodos o funciones
    def presentacion(self):
        print("Persona", self.dpi, "- Nombre:",
              self.nombre, "Apellido:", self.apellido)

    def print_dpi(self):
        print("DPI:", self.dpi)


p1 = Persona("Francisco", "Suarez", 1)
# p1.presentacion()
# p1.print_dpi()


'''
SINTAXIS DE UN METODO O FUNCION
def nombreDeFuncion():
    BLOQUES DE CODIGO
'''

# Funcion vacia - METODO


def sumar(num1, num2):
    res = num1 + num2
    print("El resultado es:", res)


# Llamada de una funcion o metodo
#sumar(1, 2)


# Funcion con retorno - Funcion
def sumar(num1, num2):
    res = num1 + num2
    return res


res = sumar(5, 1)
#print("El resultado es:", res)


# ARGUMENTOS O PARAMETROS ARBITRARIOS
# Por tipo clave: valor
def resta(num1, num2):
    res = num2 - num1
    return res


#res = resta(num2=20, num1=10)
# print(res)

# Funcion que espera recibir un numero arbitrario (desconocido) de argumentos, estos argumentos
# llegan a la funcion en forma de tupla, para definir que esperamos este tipo de parametro se antecede al parametro un * (asterisco)

def suma(*nums):
    res = 0
    for x in nums:
        res += x
    return res


#res = suma(1, 2)
# print(res)


def iva(i, *totales, y):
    res = 0
    for x in totales:
        res += x
    return res*i-y


#res = iva(i=0.12, y=10, totales=(50, 100, 200))
# print(res)

# Parametros por omision
def saludar(nombre, mensaje="Hola", despedida="Adios"):
    print(mensaje, nombre + ",", despedida)


saludar("Benjamin", despedida="Orale")
