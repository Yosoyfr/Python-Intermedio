from flask import Flask, request, json, jsonify
from flask_pymongo import PyMongo, ObjectId
from pymongo import results
from flask_cors import CORS

# Instancia del servior web con FLASK
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/bookstore'


# Instancia de la conexion con MONGO DB
mongo = PyMongo(app)
# Instancia con la coleccion books
dbbooks = mongo.db.books


# Middlewares
cors = CORS(app, resources={r"/*": {'origins': '*'}})


# Rutas
@app.route('/')
def index():
    return '<h1>Server Funcionando</h1>'


# Ruta para agregar libros
@app.route('/books', methods=['POST'])
def insertBook():
    result = dbbooks.insert_one({
        'title': request.json['title'],
        'description': request.json['description']
    })
    id = result.inserted_id
    return jsonify({'message': 'Book added', 'id': str(ObjectId(id))})


# Ruta para recuperar todos los libros
@app.route('/books', methods=['GET'])
def getBooks():
    id_ = request.args.get('id')
    if id_:
        book = dbbooks.find_one({'_id': ObjectId(id_)})
        return jsonify({
            'id': str(ObjectId(book['_id'])),
            'title': book['title'],
            'description': book['description']
        })
    title = request.args.get('title')
    filt = {'title': title}
    if title:
        books = []
        for doc in dbbooks.find(filt):
            books.append({
                'id': str(ObjectId(doc['_id'])),
                'title': doc['title'],
                'description': doc['description']
            })
        return jsonify(books)
    books = []
    for doc in dbbooks.find():
        books.append({
            'id': str(ObjectId(doc['_id'])),
            'title': doc['title'],
            'description': doc['description']
        })
    return jsonify(books)


# Ruta para eliminar un libro
@app.route('/books/<id>', methods=['DELETE'])
def deleteBook(id):
    dbbooks.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Book deleted'})


# Ruta para actualizar un libro
@app.route('/books/<id>', methods=['PUT'])
def updateBook(id):
    dbbooks.update_one({'_id': ObjectId(id)}, {
        "$set": {
            "title": request.json["title"],
            "description": request.json["description"]
        }
    })
    return jsonify({'message': 'Book updated'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
