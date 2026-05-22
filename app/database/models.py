# Cria a tabela GPU (Nome, FPS_1080p, FPS_1440p, FPS_4k)

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class GpuBenchmark(Base):
    __tablename__ = "gpu_benchmarks"

    # 1. Identificador Único (Obrigatório para toda tabela)
    id = Column(Integer, primary_key=True, autoincrement=True)

    # 2. Informações Básicas da Placa (Textos)
    name = Column(String(100), nullable=False)  # nullable=False significa que o nome é obrigatório
    brand = Column(String(50), nullable=False) # Para separar Nvidia de AMD/Intel

    # 3. Os Dados de Desempenho do Tom's Hardware (Números Inteiros)
    fps_1080p = Column(Integer, nullable=False)
    fps_1440p = Column(Integer, nullable=False)
    fps_4k = Column(Integer, nullable=False)

