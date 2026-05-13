from database.connection import conectar
from datetime import datetime


def CriarTarefa(titulo, descricao, prioridade, usuario):
    conn = conectar()
    cursor = conn.cursor()

    sql = """
    INSERT INTO tarefas (titulo, descricao, status, prioridade, usuario, data_criacao)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        titulo,
        descricao,
        "pendente",
        prioridade,
        usuario,
        datetime.now().strftime("%Y-%m-%d")
    )

    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()

    print("Tarefa criada com sucesso!")


def ListarTarefa():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    if not tarefas:
        print("Nenhuma tarefa")
        return

    for t in tarefas:
        print(f"ID: {t[0]} | Título: {t[1]} | Status: {t[3]}")

    cursor.close()
    conn.close()


def ConcluirTarefa():
    try:
        id_tarefa = int(input("Id Tarefa: "))
    except ValueError:
        print("Digite um número válido!")
        return

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tarefas WHERE id = %s", (id_tarefa,))
    tarefa = cursor.fetchone()

    if not tarefa:
        print("Tarefa não encontrada")
        return

    cursor.execute(
        "UPDATE tarefas SET status = %s WHERE id = %s",
        ("concluida", id_tarefa)
    )
    conn.commit()

    cursor.close()
    conn.close()

    print("Tarefa Concluída!")


def DeletarTarefa():
    try:
        id_tarefa = int(input("Id Tarefa: "))
    except ValueError:
        print("Digite um número válido!")
        return

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tarefas WHERE id = %s", (id_tarefa,))
    tarefa = cursor.fetchone()

    if not tarefa:
        print("Tarefa não encontrada")
        return

    cursor.execute("DELETE FROM tarefas WHERE id = %s", (id_tarefa,))
    conn.commit()

    cursor.close()
    conn.close()

    print("Tarefa removida com sucesso!")