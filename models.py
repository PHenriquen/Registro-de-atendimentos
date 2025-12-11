from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Fisioterapeuta(Base):
    __tablename__ = 'fisioterapeutas'

    id = Column(Integer, primary_key=True)
    nome_fisioterapeuta = Column(String(120), nullable=False)
    especialidade = Column(String(120), nullable=False)
    telefone = Column(String(20))
    email = Column(String(120))

    consultas = relationship('Consulta', back_populates='fisioterapeuta')


class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True)
    nome_paciente = Column(String(120), nullable=False)
    data_nascimento = Column(Date)
    telefone = Column(String(20))
    email = Column(String(120))
    sexo = Column(String(10))
    endereco = Column(String(255))

    consultas = relationship('Consulta', back_populates='paciente')


class Sala(Base):
    __tablename__ = 'salas'

    id = Column(Integer, primary_key=True)
    nome_num = Column(String(120), nullable=False)
    equipamentos = Column(String(225))
    capacidade = Column(Integer)

    consultas = relationship('Consulta', back_populates='sala')


class Consulta(Base):
    __tablename__ = 'consultas'

    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'), nullable=False)
    fisioterapeuta_id = Column(Integer, ForeignKey('fisioterapeutas.id'), nullable=False)
    sala_id = Column(Integer, ForeignKey('salas.id'), nullable=True)

    tipo_tratamento = Column(String(120), nullable=False)
    data_hora = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)

    paciente = relationship('Paciente', back_populates='consultas')
    fisioterapeuta = relationship('Fisioterapeuta', back_populates='consultas')
    sala = relationship('Sala', back_populates='consultas')

    pagamento = relationship('Pagamento', back_populates='consulta', uselist=False)


class Pagamento(Base):
    __tablename__ = 'pagamentos'

    id = Column(Integer, primary_key=True)
    consulta_id = Column(Integer, ForeignKey('consultas.id'), nullable=False)

    valor = Column(DECIMAL(10, 2), nullable=False)
    forma_pagamento = Column(String(50), nullable=False)
    data_pagamento = Column(DateTime)

    consulta = relationship('Consulta', back_populates='pagamento')
