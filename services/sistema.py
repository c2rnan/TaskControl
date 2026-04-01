import json
import os
from models.tarefa import Tarefa

tarefas = []

ARQUIVO = "database/dados.json"

def CriarTarefa(titulo, descricao, prioridade, usuario):
    id_tarefa = max([t.id for t in tarefas], default=0) + 1

    t = Tarefa(id_tarefa, titulo, descricao, prioridade, usuario)
    tarefas.append(t)

    SalvarDados()
    print("Tarefa criada com sucesso!")

def ListarTarefa():
    if not tarefas:
        print("Nenhuma tarefa")
        return

    for t in tarefas:
        print(f"ID: {t.id} | Título: {t.titulo} | Status: {t.status}")

def ConcluirTarefa():
    try:
        id_tarefa = int(input("Id Tarefa: "))
    except ValueError:
        print("Digite um número válido!")
        return
    encontrado = False

    for t in tarefas:
        if t.id == id_tarefa:
            t.concluir()
            SalvarDados()
            print("Tarefa Concluída!")
            encontrado = True
            break

    if not encontrado:
        print("Tarefa não encontrada")

def DeletarTarefa():
    try:
        id_tarefa = int(input("Id Tarefa: "))
    except ValueError:
        print("Digite um número válido!")
        return
    encontrado = False

    for t in tarefas:
        if t.id == id_tarefa:
            tarefas.remove(t)
            SalvarDados()
            print("Tarefa removida com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print("Tarefa não encontrada")

def SalvarDados():
    lista_dict = []

    for t in tarefas:
        lista_dict.append(t.to_dict())

    with open("database/dados.json", "w") as f:
        json.dump(lista_dict, f, indent=4)

def CarregarDados():
    if not os.path.exists("database/dados.json"):
        return

    with open("database/dados.json", "r") as f:
        dados = json.load(f)

    tarefas.clear()

    for d in dados:
        t = Tarefa(
            d["id"],
            d["titulo"],
            d["descricao"],
            d["prioridade"],
            d["usuario"]
        )
        t.status = d["status"]
        t.data_criacao = d["data_criacao"]

        tarefas.append(t)