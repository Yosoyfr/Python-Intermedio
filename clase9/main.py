import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()
URI_MONGODB = os.environ.get("URI_MONGODB")
client = MongoClient(URI_MONGODB)

db = client.pythonda
collec = db.seccionda

# INSERCION DE UN DATO EN UNA COLECCION
'''
result = collec.insert_one(
    {'nombre': 'Francisco Suarez', 'direccion': 'Ciudad de Guatemala', 'edad': 22})
print(result.inserted_id)
'''

# INSERCION DE VARIOS DATOS EN UNA COLECCION
'''
values = [
    {'nombre': 'Luis Lopez', 'direccion': 'Ciudad de Guatemala', 'edad': 22},
    {'nombre': 'Emma Alegria', 'direccion': 'Ciudad de Guatemala', 'edad': 22},
    {'nombre': 'Patricia Garcia', 'direccion': 'Ciudad de Guatemala', 'edad': 22}
]
result = collec.insert_many(values)
print(result.inserted_ids)
'''

# ACTUALIZACION DE UN DATOS EN UNA COLECCION
# filt = {'edad': 20}
# upd = {'$set': {'nombre': 'Kevin Juarez'}}
# result = collec.update_one(filt, upd)


# ACTUALIZACION DE VARIOS DATOS EN UNA COLECCION
# filt = {'direccion': 'Ciudad de Guatemala'}
# upd = {'$set': {'direccion': 'Mixco'}}
# result = collec.update_many(filt, upd)


# LECTURA DE TODOS LOS DATOS EN UNA COLECCION
# result = collec.find()
# for x in result:
#    print(x)


# LECTURA DE LOS DATOS EN UNA COLECCION DE FIRMA FILTRADA
# filt = {'edad': 20}
# result = collec.find(filter=filt)
# for x in result:
#    print(x)


# LECTURA DE UN DATO EN UNA COLECCION DE FIRMA FILTRADA
# filt = {'edad': 22}
# result = collec.find_one(filter=filt)
# print(result)


# ELIMINACION DE UN DATO EN UNA COLECCION DE FIRMA FILTRADA
# filt = {'edad': 22}
# result = collec.delete_one(filt)


# ELIMINACION DE VARIOS DATOS EN UNA COLECCION DE FIRMA FILTRADA
# filt = {'edad': 22}
# result = collec.delete_many(filt)
