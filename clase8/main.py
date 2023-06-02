import os
from dotenv import load_dotenv
import mysql.connector as db

load_dotenv()

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")

# CREACION DE UNA CONEXION
mydb = db.connect(host=MYSQL_HOST, user=MYSQL_USER,
                  password=MYSQL_PASSWORD, database=MYSQL_DATABASE)

# CREACION DE UN CURSOR
mycursor = mydb.cursor()


# CREACION DE UNA BASE DE DATOS
# mycursor.execute('CREATE DATABASE python')

# MOSTRAR LAS BASES DE DATOS CREADAS
# mycursor.execute('SHOW DATABASES')
# for database in mycursor:
#    print(database)


# CREACION DE UNA TABLA
mycursor.execute(
    'CREATE TABLE IF NOT EXISTS cliente (nombre VARCHAR(255), direccion VARCHAR(255))')

# MOSTRAR LAS TABLAS DE UNA BASE DE DATOS
# mycursor.execute('SHOW TABLES')
# for table in mycursor:
#     print(table)

# INSERCION DE DATOS EN UNA TABLA - UNA FILA A LA VEZ
'''
query = 'INSERT INTO cliente (nombre, direccion) VALUES (%s, %s)'
values = ('Jose Rosales', 'Ciudad de Guatemala')
mycursor.execute(query, values)
mydb.commit() # De forma obligatoria
print(mycursor.rowcount, 'DATOS INSERTADOS')
'''

# INSERCION DE VARIOS DATOS EN UNA TABLA - VARIAS FILAS
'''
query = 'INSERT INTO cliente (nombre, direccion) VALUES (%s, %s)'
values = [('Nombre1', 'Direccion1'),
          ('Nombre2', 'Direccion2'),
          ('Nombre3', 'Direccion3'),
          ('Nombre4', 'Direccion4'),
          ('Nombre5', 'Direccion5'),
          ('Nombre6', 'Direccion6'),
          ('Nombre7', 'Direccion7'),
          ('Nombre8', 'Direccion8')]
mycursor.executemany(query, values)
mydb.commit() # De forma obligatoria
print(mycursor.rowcount, 'DATOS INSERTADOS')
'''

# OBTENER DATOS DE UNA TABLA
'''
mycursor.execute('SELECT direccion, nombre FROM cliente')
mycursor.execute('SELECT * FROM cliente')
myresult = mycursor.fetchall()  # Lo que hara es traer todos las filas de la tabla
for cliente in myresult:
   print(cliente)
'''


# ACTUALIZACION DE DATOS EN UNA TABLA
'''
query = 'UPDATE cliente SET nombre=%s, direccion=%s WHERE direccion=%s AND nombre=%s'
values = ('Nombre aleatorio', 'Direccion aleatoria', 'Direccion6', 'Nombre6')
mycursor.execute(query, values)
mydb.commit()
'''

# ELIMINACION DE DATOS EN UNA TABLA
'''
query = 'DELETE FROM cliente WHERE direccion=%s AND nombre=%s'
values = ('Direccion8', 'Nombre8')
mycursor.execute(query, values)
mydb.commit()
'''

mycursor.execute('SELECT * FROM cliente')
myresult = mycursor.fetchall()  # Lo que hara es traer todos las filas de la tabla
for cliente in myresult:
    print(cliente)
