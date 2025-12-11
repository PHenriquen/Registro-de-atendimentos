from sqlalchemy import create_engine, text

# Conexão com o servidor:
DB_URL = "mysql+pymysql://root:@localhost:3308/taskflow_db?charset=utf8mb4"
engine = create_engine(DB_URL, echo=True)

# Testar conexão de verdade
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("O Banco está conectado com sucesso!")
except Exception as e:
    print("Erro ao conectar:", e)