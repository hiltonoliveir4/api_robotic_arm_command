from flask import Flask, jsonify, request, g
import sqlite3

app = Flask(__name__)
DB_URL = "robotic-arm.db"

# variavel que recebe o valor a ser retornado

@app.before_request
def before_request():
    print("CONECTANDO AO BANCO")
    conn = sqlite3.connect(DB_URL)
    g.conn = conn

@app.teardown_request
def teardown_request(exception):
    if(g.conn is not None):
        g.conn.close()
        print("DESCONECTANDO DO BANCO")

# localhost/command - GET 
# (Envia todos os comandos)
@app.route("/command", methods=["GET"])
def get_commands():
    commands = get_all_commands()
    return jsonify(commands)

# localhost/command - GET 
# (Envia o ultimo comando )
@app.route("/last_command", methods=["GET"])
def get_last_command():
    query = "SELECT id, command from commands order by id desc limit 1;"
    cursor = g.conn.execute(query)
    command = [{"command": row[1]} for row in cursor.fetchall()]
    return jsonify(command)

# localhost/command - POST 
# (Proximo comando para ser salvo / sobrescrito)
@app.route("/command", methods=["POST"])
def post_command():
    body = request.get_json()
    insert = g.conn.execute("""
            INSERT INTO commands(command) 
            VALUES (?)
        """, (body['command'],))
    g.conn.commit()
    commands = get_all_commands()
    return jsonify(commands)


# funcao que retorna todos os comandos do banco de dados
def get_all_commands():
    query = "SELECT id, command from commands order by id;"
    cursor = g.conn.execute(query)
    commands = [{"command": row[1]} for row in cursor.fetchall()]
    return commands   





