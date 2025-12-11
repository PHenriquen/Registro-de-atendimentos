ef menu():
    inicializar_banco()

    while True:
        print("\n===== Sistema de Agendamento – Clínica de Fisioterapia =====")
        print("1 - Cadastrar Fisioterapeuta")
        print("2 - Listar Fisioterapeutas")
        print("3 - Agendar Consulta")
        print("4 - Listar Consultas")
        print("5 - Atualizar Status de Consulta")
        print("6 - Remover Consulta")
        print("7 - Sair")

        op = input("Escolha: ")

        if op == "1": criar_fisioterapeuta()
        elif op == "2": listar_fisioterapeutas()
        elif op == "3": criar_consulta()
        elif op == "4": listar_consultas()
        elif op == "5": atualizar_status_consulta()
        elif op == "6": remover_consulta()
        elif op == "7":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()