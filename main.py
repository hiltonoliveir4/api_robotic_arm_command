from flask import Flask, jsonify, request

app = Flask(__name__)

# variavel que recebe o valor a ser retornado
commands = [{"command": ""}]

# localhost/command - GET 
# (Envia todos os comandos)
@app.route("/command", methods=["GET"])
def get_command():
    return jsonify(commands)

# localhost/command - GET 
# (Envia o ultimo comando )
@app.route("/last_command", methods=["GET"])
def get_last_command():
    return jsonify(commands[-1])

# localhost/command - POST 
# (Proximo comando para ser salvo / sobrescrito)
@app.route("/command", methods=["POST"])
def post_command():
    commands.append(request.get_json())
    return jsonify(commands)

app.run(port=5000, debug=True, host="localhost")






