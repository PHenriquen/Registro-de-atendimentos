from database import session
from models import (
    Consulta,
    Fisioterapeuta,
    Sala,
    Paciente,
    Pagamento
)

#  FISIOTERAPEUTA
def cadastrar_fisioterapeuta(nome_fisioterapeuta, especialidade, telefone=None, email=None):
    novo = Fisioterapeuta(
        nome_fisioterapeuta=nome_fisioterapeuta,
        especialidade=especialidade,
        telefone=telefone,
        email=email
    )
    session.add(novo)
    session.commit()
    return novo


def listar_fisioterapeutas():
    return session.query(Fisioterapeuta).all()


def buscar_fisioterapeuta(id):
    return session.query(Fisioterapeuta).filter_by(id=id).first()


#  PACIENTE
def cadastrar_paciente(nome_paciente, data_nascimento=None, telefone=None, email=None, sexo=None, endereco=None):
    novo = Paciente(
        nome_paciente=nome_paciente,
        data_nascimento=data_nascimento,
        telefone=telefone,
        email=email,
        sexo=sexo,
        endereco=endereco
    )
    session.add(novo)
    session.commit()
    return novo


def listar_pacientes():
    return session.query(Paciente).all()


def buscar_paciente(id):
    return session.query(Paciente).filter_by(id=id).first()


#  SALA
def cadastrar_sala(nome_num, equipamentos=None, capacidade=None):
    nova = Sala(
        nome_num=nome_num,
        equipamentos=equipamentos,
        capacidade=capacidade
    )
    session.add(nova)
    session.commit()
    return nova


def listar_salas():
    return session.query(Sala).all()


def buscar_sala(id):
    return session.query(Sala).filter_by(id=id).first()


#  CONSULTA
def cadastrar_consulta(paciente_id, fisioterapeuta_id, tipo_tratamento, data_hora, status, sala_id=None):
    nova = Consulta(
        paciente_id=paciente_id,
        fisioterapeuta_id=fisioterapeuta_id,
        sala_id=sala_id,
        tipo_tratamento=tipo_tratamento,
        data_hora=data_hora,
        status=status
    )
    session.add(nova)
    session.commit()
    return nova


def listar_consultas():
    return session.query(Consulta).all()


def buscar_consulta(id):
    return session.query(Consulta).filter_by(id=id).first()


#  PAGAMENTO
def cadastrar_pagamento(consulta_id, valor, forma_pagamento, data_pagamento=None):
    novo = Pagamento(
        consulta_id=consulta_id,
        valor=valor,
        forma_pagamento=forma_pagamento,
        data_pagamento=data_pagamento
    )
    session.add(novo)
    session.commit()
    return novo


def listar_pagamentos():
    return session.query(Pagamento).all()


def buscar_pagamento(id):
    return session.query(Pagamento).filter_by(id=id).first()

