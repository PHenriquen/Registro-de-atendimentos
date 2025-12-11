
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Fisioterapeuta(Base):
    __tablename__ = 'fisioterapeutas'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String, nullable=False)

    consultas = relationship('Consulta', back_populates='fisioterapeuta')

class Consulta(Base):
    __tablename__ = 'consultas'

    id = Column(Integer, primary_key=True)
    nome_paciente = Column(String, nullable=False)
    tipo_tratamento = Column(String, nullable=False)
    data_hora = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)

    fisioterapeuta_id = Column(Integer, ForeignKey('fisioterapeutas.id'), nullable=False)
    fisioterapeuta = relationship('Fisioterapeuta', back_populates='consultas')

    pagamento = relationship('Pagamento', back_populates='consulta', uselist=False)

class Sala(Base):
    __tablename__ = 'salas'

    id = Column(Integer, primary_key=True)
    nome_num = Column(String(120), nullable=False)
    equipamentos = Column(String(225))
    capacidade = Column(Integer)

class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True)
    nome_paciente = Column(String(120), nullable=False)
    data_nascimento = Column(Date)
    telefone = Column(String(20))
    email = Column(String(120))
    sexo = Column(String(120))
    endereco = Column(String(255))

class Pagamento(Base):
    __tablename__ = 'pagamentos'

    id = Column(Integer, primary_key=True)
    consulta_id = Column(Integer, ForeignKey('consultas.id'), nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    forma_pagamento = Column(String(50), nullable=False)
    data_pagamento = Column(DateTime)

    consulta = relationship('Consulta', back_populates='pagamento')