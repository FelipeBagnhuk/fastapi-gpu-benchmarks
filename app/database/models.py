from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class GpuBenchmark(Base):
    __tablename__ = "gpu_benchmarks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    brand = Column(String(50), nullable=False)
    fps_1080p_medium = Column(Integer, nullable=False)
    fps_1080p_ultra = Column(Integer, nullable=False)
    fps_1440p = Column(Integer, nullable=False)
    fps_4k = Column(Integer, nullable=False)

