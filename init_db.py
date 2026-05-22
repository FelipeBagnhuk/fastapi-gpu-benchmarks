"""Inicializa o banco de dados e popula com dados se estiver vazio."""
from app.database.connection import engine, Base, SessionLocal
from app.database.models import GpuBenchmark
from seed import seed_db


def init_database():
    """Cria tabelas e popula com dados se estiver vazia."""
    # Criar tabelas
    Base.metadata.create_all(bind=engine)
    
    # Verificar se já tem dados
    session = SessionLocal()
    try:
        count = session.query(GpuBenchmark).count()
        if count == 0:
            print("[INIT] Banco vazio. Populando com dados iniciais...")
            seed_db()
            print("[INIT] Seed concluído com sucesso!")
        else:
            print(f"[INIT] Banco já contém {count} registros. Skip seed.")
    except Exception as e:
        print(f"[INIT] Erro ao verificar banco: {e}")
    finally:
        session.close()
