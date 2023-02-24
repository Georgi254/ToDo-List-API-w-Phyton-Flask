from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "Ir al super", "done": False },
    { "label": "Hacer ejercicio", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    todos_answer = jsonify(todos)
    return todos_answer

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop((position-1))
    return jsonify(todos)

# Estas dos líneas siempre deben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)