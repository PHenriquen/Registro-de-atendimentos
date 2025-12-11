from services import (
    cadastrar_fisioterapeuta,
    listar_fisioterapeutas,
    buscar_fisioterapeuta,

    cadastrar_paciente,
    listar_pacientes,
    buscar_paciente,

    cadastrar_sala,
    listar_salas,
    buscar_sala,

    cadastrar_consulta,
    listar_consultas,
    buscar_consulta,

    cadastrar_pagamento,
    listar_pagamentos,
    buscar_pagamento
)

from database import criar_banco
from datetime import datetime


def menu():
    criar_banco()

    while True:
        print("\n===== Sistema de Agendamento – Clínica de Fisioterapia =====")
        print("1 - Cadastrar Fisioterapeuta")
        print("2 - Listar Fisioterapeutas")

        print("3 - Cadastrar Paciente")
        print("4 - Listar Pacientes")

        print("5 - Cadastrar Sala")
        print("6 - Listar Salas")

        print("7 - Agendar Consulta")
        print("8 - Listar Consultas")

        print("9 - Registrar Pagamento")
        print("10 - Listar Pagamentos")

        print("11 - Sair")

        op = input("Escolha: ")

        if op == "1":
            criar_fisioterapeuta_input()

        elif op == "2":
            mostrar_fisioterapeutas()

        elif op == "3":
            criar_paciente_input()

        elif op == "4":
            mostrar_pacientes()

        elif op == "5":
            criar_sala_input()

        elif op == "6":
            mostrar_salas()

        elif op == "7":
            criar_consulta_input()

        elif op == "8":
            mostrar_consultas()

        elif op == "9":
            criar_pagamento_input()

        elif op == "10":
            mostrar_pagamentos()

        elif op == "11":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")


# ---------------------------------------------------------
# FISIOTERAPEUTA
# ---------------------------------------------------------

def criar_fisioterapeuta_input():
    print("\n--- Cadastro de Fisioterapeuta ---")
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    cadastrar_fisioterapeuta(nome, especialidade, telefone, email)
    print("Fisioterapeuta cadastrado.")


def mostrar_fisioterapeutas():
    print("\n--- Fisioterapeutas Cadastrados ---")
    fisios = listar_fisioterapeutas()

    if not fisios:
        print("Nenhum cadastrado.")
        return

    for f in fisios:
        print(f"{f.id} | {f.nome_fisioterapeuta} | {f.especialidade} | {f.telefone} | {f.email}")


# ---------------------------------------------------------
# PACIENTE
# ---------------------------------------------------------

def criar_paciente_input():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome: ")
    nasc = input("Data nascimento (YYYY-MM-DD): ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    sexo = input("Sexo: ")
    endereco = input("Endereço: ")

    nasc = datetime.strptime(nasc, "%Y-%m-%d")

    cadastrar_paciente(nome, nasc, telefone, email, sexo, endereco)
    print("Paciente cadastrado.")


def mostrar_pacientes():
    print("\n--- Pacientes Cadastrados ---")
    pacs = listar_pacientes()

    if not pacs:
        print("Nenhum cadastrado.")
        return

    for p in pacs:
        print(f"{p.id} | {p.nome_paciente} | {p.telefone} | {p.email}")


# ---------------------------------------------------------
# SALA
# ---------------------------------------------------------

def criar_sala_input():
    print("\n--- Cadastro de Sala ---")
    nome = input("Nome ou número da sala: ")
    equipamentos = input("Equipamentos (opcional): ")
    capacidade = input("Capacidade (opcional): ")

    capacidade = int(capacidade) if capacidade else None

    cadastrar_sala(nome, equipamentos, capacidade)
    print("Sala cadastrada.")


def mostrar_salas():
    print("\n--- Salas Cadastradas ---")
    salas = listar_salas()

    if not salas:
        print("Nenhuma sala cadastrada.")
        return

    for s in salas:
        print(f"{s.id} | {s.nome_num} | Equip.: {s.equipamentos} | Cap.: {s.capacidade}")


# ---------------------------------------------------------
# CONSULTA
# ---------------------------------------------------------

def criar_consulta_input():
    print("\n--- Agendamento de Consulta ---")

    paciente_id = int(input("ID do paciente: "))
    fisioterapeuta_id = int(input("ID do fisioterapeuta: "))

    sala_id = input("ID da sala (opcional): ")
    sala_id = int(sala_id) if sala_id else None

    tipo = input("Tipo de tratamento: ")

    data_hora = input("Data e hora (YYYY-MM-DD HH:MM): ")
    data_hora = datetime.strptime(data_hora, "%Y-%m-%d %H:%M")

    status = input("Status inicial: ")

    cadastrar_consulta(paciente_id, fisioterapeuta_id, tipo, data_hora, status, sala_id)
    print("Consulta agendada.")


def mostrar_consultas():
    print("\n--- Consultas Cadastradas ---")
    cons = listar_consultas()

    if not cons:
        print("Nenhuma consulta.")
        return

    for c in cons:
        print(
            f"{c.id} | Pac.: {c.paciente.nome_paciente} | "
            f"Fisio: {c.fisioterapeuta.nome_fisioterapeuta} | "
            f"Tratamento: {c.tipo_tratamento} | {c.data_hora} | Status: {c.status}"
        )


# ---------------------------------------------------------
# PAGAMENTO
# ---------------------------------------------------------

def criar_pagamento_input():
    print("\n--- Registrar Pagamento ---")

    consulta_id = int(input("ID da consulta: "))
    valor = float(input("Valor: "))
    forma = input("Forma de pagamento: ")

    data_p = input("Data do pagamento (YYYY-MM-DD HH:MM) (opcional): ")
    data_p = datetime.strptime(data_p, "%Y-%m-%d %H:%M") if data_p else None

    cadastrar_pagamento(consulta_id, valor, forma, data_p)
    print("Pagamento registrado.")


def mostrar_pagamentos():
    print("\n--- Pagamentos Registrados ---")
    pags = listar_pagamentos()

    if not pags:
        print("Nenhum pagamento registrado.")
        return

    for p in pags:
        print(
            f"{p.id} | Consulta {p.consulta_id} | R${p.valor} | "
            f"{p.forma_pagamento} | {p.data_pagamento}"
        )


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

if __name__ == "__main__":
    menu()
