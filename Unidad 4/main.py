import mysql.connector as db

# Conexion con base de datos, necesita un host, el usuario de la base y una contraseña
mydb = db.connect(host='35.225.17.101', user='root',
                  password='12345', database='mydatabase')

mycursor = mydb.cursor()
# Creacion de una base de datos
# mycursor.execute("CREATE DATABASE mydatabase")

# Mostrar las bases de datos creadas
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#    print(x)

# Creacion de una tabla
# mycursor.execute(
#    "CREATE TABLE IF NOT EXISTS cliente (nombre varchar(255), direccion varchar(255))")


#mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

# Insertar datos en tabla
'''
sql = "INSERT INTO cliente (nombre, direccion) VALUES (%s, %s)"
values = ("Fernando Suarez", "Ciudad de Guatemala")
values1 = ("Bryan Valdez", "Ciudad de Guatemala")
mycursor.execute(sql, values)
mycursor.execute(sql, values1)
mydb.commit()
print(mycursor.rowcount, "DATOS INSERTADOS")
'''

# Insertar varios datos en tabla
'''

sql = "INSERT INTO cliente (nombre, direccion) VALUES (%s, %s)"
values = [
    ('Nombre1', 'Direccion 1'),
    ('Nombre2', 'Direccion 2'),
    ('Nombre3', 'Direccion 3'),
    ('Nombre4', 'Direccion 4'),
    ('Nombre5', 'Direccion 5'),
    ('Nombre6', 'Direccion 6'),
    ('Nombre7', 'Direccion 7'),
    ('Nombre8', 'Direccion 8'),
    ('Nombre9', 'Direccion 9'),
    ('Nombre10', 'Direccion 10')
]

mycursor.executemany(sql, values)
mydb.commit()
print(mycursor.rowcount, "DATOS INSERTADOS")
'''

# Obtener datos de una tabla
mycursor.execute('SELECT * FROM cliente')
clientes = mycursor.fetchall()
for x in clientes:
    print(x)
