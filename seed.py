from app.database.models import GpuBenchmark
from app.database.connection import SessionLocal

gpus_for_registration = [
    GpuBenchmark(name="GeForce RTX 5090", brand="Nvidia", fps_1080p_medium=198, fps_1080p_ultra=158, fps_1440p=143, fps_4k=106),
    GpuBenchmark(name="GeForce RTX 4090", brand="Nvidia", fps_1080p_medium=196, fps_1080p_ultra=150, fps_1440p=127, fps_4k=85),
    GpuBenchmark(name="GeForce RTX 5080", brand="Nvidia", fps_1080p_medium=179, fps_1080p_ultra=134, fps_1440p=112, fps_4k=71),
    GpuBenchmark(name="GeForce RTX 4080 Super", brand="Nvidia", fps_1080p_medium=177, fps_1080p_ultra=131, fps_1440p=106, fps_4k=65),
    GpuBenchmark(name="GeForce RTX 4080", brand="Nvidia", fps_1080p_medium=175, fps_1080p_ultra=129, fps_1440p=104, fps_4k=63),
    GpuBenchmark(name="Radeon RX 7900 XTX", brand="AMD", fps_1080p_medium=174, fps_1080p_ultra=125, fps_1440p=103, fps_4k=64),
    GpuBenchmark(name="GeForce RTX 5070 Ti", brand="Nvidia", fps_1080p_medium=169, fps_1080p_ultra=124, fps_1440p=101, fps_4k=62),
    GpuBenchmark(name="Radeon RX 9070 XT", brand="AMD", fps_1080p_medium=169, fps_1080p_ultra=120, fps_1440p=98, fps_4k=61),
    GpuBenchmark(name="Radeon RX 7900 XT", brand="AMD", fps_1080p_medium=163, fps_1080p_ultra=116, fps_1440p=92, fps_4k=55),
    GpuBenchmark(name="GeForce RTX 4070 Ti Super", brand="Nvidia", fps_1080p_medium=161, fps_1080p_ultra=117, fps_1440p=92, fps_4k=55),
    GpuBenchmark(name="Radeon RX 9070", brand="AMD", fps_1080p_medium=159, fps_1080p_ultra=110, fps_1440p=87, fps_4k=53),
    GpuBenchmark(name="GeForce RTX 4070 Ti", brand="Nvidia", fps_1080p_medium=155, fps_1080p_ultra=111, fps_1440p=86, fps_4k=50),
    GpuBenchmark(name="GeForce RTX 5070", brand="Nvidia", fps_1080p_medium=149, fps_1080p_ultra=107, fps_1440p=81, fps_4k=48),
    GpuBenchmark(name="GeForce RTX 4070 Super", brand="Nvidia", fps_1080p_medium=148, fps_1080p_ultra=106, fps_1440p=80, fps_4k=46),
    GpuBenchmark(name="Radeon RX 7900 GRE", brand="AMD", fps_1080p_medium=141, fps_1080p_ultra=99, fps_1440p=78, fps_4k=46),
    GpuBenchmark(name="Radeon RX 7800 XT", brand="AMD", fps_1080p_medium=133, fps_1080p_ultra=90, fps_1440p=69, fps_4k=41),
    GpuBenchmark(name="GeForce RTX 4070", brand="Nvidia", fps_1080p_medium=131, fps_1080p_ultra=92, fps_1440p=68, fps_4k=39),
    GpuBenchmark(name="GeForce RTX 5060 Ti 16GB", brand="Nvidia", fps_1080p_medium=120, fps_1080p_ultra=84, fps_1440p=62, fps_4k=36),
    GpuBenchmark(name="Radeon RX 9060 XT 16GB", brand="AMD", fps_1080p_medium=118, fps_1080p_ultra=80, fps_1440p=59, fps_4k=34),
    GpuBenchmark(name="Radeon RX 7700 XT", brand="AMD", fps_1080p_medium=115, fps_1080p_ultra=79, fps_1440p=61, fps_4k=35),
    GpuBenchmark(name="GeForce RTX 5060 Ti 8GB", brand="Nvidia", fps_1080p_medium=118, fps_1080p_ultra=80, fps_1440p=56, fps_4k=22),
    GpuBenchmark(name="GeForce RTX 4060 Ti 16GB", brand="Nvidia", fps_1080p_medium=103, fps_1080p_ultra=73, fps_1440p=53, fps_4k=29),
    GpuBenchmark(name="GeForce RTX 4060 Ti 8GB", brand="Nvidia", fps_1080p_medium=104, fps_1080p_ultra=72, fps_1440p=49, fps_4k=22),
    GpuBenchmark(name="GeForce RTX 5060", brand="Nvidia", fps_1080p_medium=103, fps_1080p_ultra=70, fps_1440p=46, fps_4k=20),
    GpuBenchmark(name="Intel Arc B580", brand="Intel", fps_1080p_medium=80, fps_1080p_ultra=55, fps_1440p=43, fps_4k=26),
    GpuBenchmark(name="Radeon RX 7600 XT", brand="AMD", fps_1080p_medium=85, fps_1080p_ultra=57, fps_1440p=42, fps_4k=23),
    GpuBenchmark(name="GeForce RTX 4060", brand="Nvidia", fps_1080p_medium=84, fps_1080p_ultra=58, fps_1440p=39, fps_4k=17),
    GpuBenchmark(name="Intel Arc A770 16GB", brand="Intel", fps_1080p_medium=63, fps_1080p_ultra=47, fps_1440p=37, fps_4k=22),
    GpuBenchmark(name="GeForce RTX 3060 12GB", brand="Nvidia", fps_1080p_medium=70, fps_1080p_ultra=48, fps_1440p=35, fps_4k=20),
    GpuBenchmark(name="Intel Arc B570", brand="Intel", fps_1080p_medium=72, fps_1080p_ultra=48, fps_1440p=35, fps_4k=16),
    GpuBenchmark(name="Intel Arc A750", brand="Intel", fps_1080p_medium=57, fps_1080p_ultra=41, fps_1440p=31, fps_4k=17),
    GpuBenchmark(name="Radeon RX 7600", brand="AMD", fps_1080p_medium=79, fps_1080p_ultra=42, fps_1440p=28, fps_4k=13),
    GpuBenchmark(name="Intel Arc A580", brand="Intel", fps_1080p_medium=55, fps_1080p_ultra=38, fps_1440p=28, fps_4k=16),
    GpuBenchmark(name="Radeon RX 6600", brand="AMD", fps_1080p_medium=64, fps_1080p_ultra=37, fps_1440p=24, fps_4k=12),
]

def seed_db():
    db = SessionLocal()
    try:
        if db.query(GpuBenchmark).count() == 0:
            db.add_all(gpus_for_registration)
            db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    seed_db()