from banco import (
    adicionar_transacao,
    listar_transacoes,
    calcular_saldo
)

def menu():
    while True:
        print("\n==== CONTROLE FINANCEIRO ====")
        print("1 - Adicionar Receita")
        print("2 - Adicionar Despesa")
        print("3 - Listar Transações")
        print("4 - Ver Saldo")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da receita: ")
            valor = float(input("Valor: R$ "))

            adicionar_transacao("receita", descricao, valor)
            print("Receita adicionada com sucesso!")

        elif opcao == "2":
            descricao = input("Descrição da despesa: ")
            valor = float(input("Valor: R$ "))

            adicionar_transacao("despesa", descricao, valor)
            print("Despesa adicionada com sucesso!")

        elif opcao == "3":
            transacoes = listar_transacoes()

            print("\n==== TRANSAÇÕES ====")
            for transacao in transacoes:
                  print(transacao)

        elif opcao == "4":
            saldo = calcular_saldo()
            print(f"\nSaldo atual: R$ {saldo:.2f}")

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


menu()