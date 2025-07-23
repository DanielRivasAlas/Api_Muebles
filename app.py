from flask import Flask, jsonify, request

app = Flask(__name__)

muebles = [
    {"id": 1, "nombre": "Silla", "precio": 30.0},
    {"id": 2, "nombre": "Mesa", "precio": 100.0},
    {"id": 3, "nombre": "Armario", "precio": 399.0},
    {"id": 4, "nombre": "Archivo metálico", "precio": 100.0},
    {"id": 5, "nombre": "Sala estilo americano", "precio": 460.0}
]

# Lista muebles
@app.route('/muebles', methods=['GET'])
def obtener_muebles():
    return jsonify(muebles)

# Mueble por ID
@app.route('/muebles/<int:id>', methods=['GET'])
def obtener_mueble(id):
    mueble = next((m for m in muebles if m["id"] == id), None)
    return jsonify(mueble) if mueble else ("No encontrado", 404)

# Agregar 
@app.route('/muebles', methods=['POST'])
def agregar_mueble():
    nuevo = request.get_json()
    nuevo['id'] = max(m['id'] for m in muebles) + 1 if muebles else 1
    muebles.append(nuevo)
    return jsonify(nuevo), 201

# Actualizar 
@app.route('/muebles/<int:id>', methods=['PUT'])
def actualizar_mueble(id):
    mueble = next((m for m in muebles if m["id"] == id), None)
    if mueble:
        datos = request.get_json()
        mueble.update(datos)
        return jsonify(mueble)
    return ("No encontrado", 404)

# Eliminar 
@app.route('/muebles/<int:id>', methods=['DELETE'])
def eliminar_mueble(id):
    global muebles
    muebles = [m for m in muebles if m["id"] != id]
    return ("Eliminado correctamente", 204)

if __name__ == '__main__':
    app.run(debug=True)
