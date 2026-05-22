from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. Dizemos onde o banco vai existir (criará um arquivo na raiz do projeto)
ENGINE = create_engine("sqlite:///benchmarks.db")

# 2. Criamos a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

# 3. Criamos o 'db' abrindo uma sessão real com o banco
db = SessionLocal()

# --- AQUI COMEÇA O SEU CÓDIGO ---
# Agora o 'db' existe! O VS Code vai reconhecer e o vermelho vai sumir.
gpus_for_registration = [
    # Suas GPUs aqui...
]

db.add_all(gpus_for_registration)
db.commit()
db.close() # Boa prática: fechar a sessão quando terminar