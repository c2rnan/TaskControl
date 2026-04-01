from datetime import datetime

class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade, usuario):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = "pendente"
        self.prioridade = prioridade
        self.usuario = usuario
        self.data_criacao = datetime.now().strftime("%Y-%m-%d")

    def concluir(self):
        self.status = "concluida"

    def to_dict(self):
        return self.__dict__