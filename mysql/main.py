import mysql.connector as db

mydb = db.connect(host='3.144.239.128', user='root',
                  password='12345', database='pythonda')

mycursor = mydb.cursor()


# CREACION DE UNA BASE DE DATOS
# mycursor.execute('CREATE DATABASE pythonda')

# MOSTRAR LAS BASES DE DATOS CREADAS
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#    print(x)


# CREACION DE UNA TABLA
mycursor.execute(
    'CREATE TABLE IF NOT EXISTS cliente (nombre VARCHAR(255), direccion VARCHAR(255))')

# MOSTRAR LAS TABLAS DE UNA BASE DE DATOS
#mycursor.execute('SHOW TABLES')
# for x in mycursor:
#    print(x)

# INSERCION DE DATOS EN UNA TABLA
'''
query = 'INSERT INTO cliente (nombre, direccion) VALUES (%s, %s)'
values = ('Jose Rosales', 'Ciudad de Guatemala')
mycursor.execute(query, values)
mydb.commit()
print(mycursor.rowcount, 'DATOS INSERTADOS')
'''

# INSERCION DE VARIOS DATOS EN UNA TABLA
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
mydb.commit()
print(mycursor.rowcount, 'DATOS INSERTADOS')
'''

# OBTENER DATOS DE UNA TABLA
mycursor.execute('SELECT * FROM cliente')
clientes = mycursor.fetchall()
for x in clientes:
    print(x)
