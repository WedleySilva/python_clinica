from conexao import conectar
from funcionario_crud import FuncionarioCRUD

def menu():
    connection = conectar()

    if connection is None:
        return

    funcionario_crud = FuncionarioCRUD(connection)

    while True:
        print("====== MENU ======")
        print("1 - Adicionar Funcionário")
        print("2 - Visualizar Funcionários")
        print("3 - Editar Funcionário")
        print("4 - Deletar Funcionário")
        print("-----------------------------------------")
        print("5 - Adicionar Procedimento")
        print("6 - Visualizar Procedimentos")
        print("7 - Editar Procedimento")
        print("8 - Deletar Procedimento")
        print("-----------------------------------------")
        print("9 - Visualizar Disponibilidades")
        print("0 - Sair")
        print("-----------------------------------------")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            funcionario_crud.adicionar_funcionario()
        elif opcao == 2:
            funcionario_crud.visualizar_funcionarios()
        elif opcao == 3:
            funcionario_crud.editar_funcionario()
        elif opcao == 4:
            funcionario_crud.deletar_funcionario()
        elif opcao == 5:
            funcionario_crud.adicionar_procedimento()
        elif opcao == 6:
            funcionario_crud.visualizar_procedimentos()
        elif opcao == 7:
            funcionario_crud.editar_procedimento()
        elif opcao == 8:
            funcionario_crud.deletar_procedimento()
        elif opcao == 9:
            funcionario_crud.visualizar_disponibilidades()
        elif opcao == 0:
            print("Saindo...")
            connection.close()
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
