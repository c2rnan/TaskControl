from flask import Flask
from database.connection import conectar
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app, resources={r"/tarefas*": {"origins": "*"}})


print("RODANDO APP CERTO")

@app.route("/")
def home():
    return "API rodando!"

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()

    titulo = dados.get("titulo")
    descricao = dados.get("descricao")
    prioridade = dados.get("prioridade")
    usuario = dados.get("usuario")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tarefas (titulo, descricao, status, prioridade, usuario, data_criacao) VALUES (%s, %s, %s, %s, %s, NOW())",
        (titulo, descricao, "pendente", prioridade, usuario)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"mensagem": "Tarefa criada com sucesso!"}, 201

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tarefas")
    dados = cursor.fetchall()

    tarefas = []

    for t in dados:
        tarefas.append({
            "id": t[0],
            "titulo": t[1],
            "descricao": t[2],
            "status": t[3],
            "prioridade": t[4],
            "usuario": t[5],
            "data_criacao": str(t[6])
        })

    cursor.close()
    conn.close()

    return tarefas


@app.route("/tarefas/<int:id>", methods=["PUT"])
def concluir_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tarefas WHERE id = %s", (id,))
    tarefa = cursor.fetchone()

    if not tarefa:
        return {"erro": "Tarefa não encontrada"}, 404

    cursor.execute(
        "UPDATE tarefas SET status = %s WHERE id = %s",
        ("concluida", id)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return {"mensagem": "Tarefa concluída!"}


@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tarefas WHERE id = %s", (id,))
    tarefa = cursor.fetchone()

    if not tarefa:
        return {"erro": "Tarefa não encontrada"}, 404

    cursor.execute("DELETE FROM tarefas WHERE id = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"mensagem": "Tarefa removida!"}


@app.route("/debug")
def debug():
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)