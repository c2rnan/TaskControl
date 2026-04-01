from services.sistema import *

def menu():
    CarregarDados()

    while True:
        print("""
        ===================
           TASK CONTROL    
        ===================
        1 - Criar Tarefas
        2 - Listar Tarefas
        3 - Concluir Tarefas
        4 - Deletar Tarefas
        0 - Sair
        """)

        opcao = input("Escolha:")

        if opcao == "1":
            titulo = input("Titulo: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade: (Baixa/Medía/Alta)")
            usuario = input("Usuário: ")

            CriarTarefa(titulo, descricao, prioridade, usuario)
        elif opcao == "2":
            ListarTarefa()
        elif opcao == "3":
            ConcluirTarefa()
        elif opcao == "4":
            DeletarTarefa()
        elif opcao == "0":
            print("Encerrando Sistema...")
            break
        else:
            print("Opção inválida!")

menu()
