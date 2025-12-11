from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base

DB_URL = "mysql+pymysql://root:@localhost:5506/consulta_fisioterapia?charset=utf8mb4"

engine = create_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

def criar_banco():
    Base.metadata.create_all(engine)

# Teste de conexão
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("O Banco está conectado com sucesso!")
except Exception as e:
    print("Erro ao conectar:", e)
