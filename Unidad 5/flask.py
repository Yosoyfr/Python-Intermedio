from flask import Flask, json, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from pymongo import results

# Instancia del servidor web con Flask
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost/bookstore"


# Instancia de la conexion con MongoDB
mongo = PyMongo(app)
# Instancia de la coleccion books
dbbooks = mongo.db.books


# Middlewares
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# Rutas
@app.route("/")
def index():
    return "<h1>Server funcionando</h1>"


# Ruta para agregar libros
@app.route("/books", methods=["POST"])
def createBook():
    result = dbbooks.insert_one({
        "title": request.json["title"],
        "description": request.json["description"]
    })
    id = result.inserted_id
    return jsonify({"msg": "Book added", "id": str(ObjectId(id))})


# Ruta para recuperar todos los libros
@app.route("/books", methods=["GET"])
def getBooks():
    books = []
    for doc in dbbooks.find():
        books.append({
            "id": str(ObjectId(doc["_id"])),
            "title": doc["title"],
            "description": doc["description"]
        })
    return jsonify(books)


# Ruta para recuperar un libro
@app.route("/book/<id>", methods=["GET"])
def getBook(id):
    book = dbbooks.find_one({"_id": ObjectId(id)})
    return jsonify({
        "id": str(ObjectId(book["_id"])),
        "title": book["title"],
        "description": book["description"]
    })


# Ruta para eliminar un libro
@app.route("/books/<id>", methods=["DELETE"])
def deleteBook(id):
    dbbooks.delete_one({"_id": ObjectId(id)})
    return jsonify({
        "msg": " Book deleted"
    })


# Ruta para actualizar un libro
@app.route("/books/<id>", methods=["PUT"])
def updateBook(id):
    dbbooks.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "title": request.json["title"],
                "description": request.json["description"]
            }
        }
    )
    return jsonify({"msg": "Book updated"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
