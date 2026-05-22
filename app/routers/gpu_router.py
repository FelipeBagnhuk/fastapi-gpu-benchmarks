from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import re
from app.database.connection import get_db
from app.database.models import GpuBenchmark

router = APIRouter(prefix="/gpus", tags=["GPUs"])

@router.get("/")
def get_all_gpus(db: Session = Depends(get_db)):
    """
    Retorna todas as GPUs cadastradas.
    """
    gpus = db.query(GpuBenchmark).all()
    return gpus


def normalize_text(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def matches_gpu_name(query: str, gpu_name: str) -> bool:
    normalized_query = normalize_text(query)
    normalized_name = normalize_text(gpu_name)

    if not normalized_query:
        return False

    for token in normalized_query.split(" "):
        if not re.search(rf"\b{re.escape(token)}\b", normalized_name):
            return False

    return True


def choose_best_gpu(candidates: list[GpuBenchmark], query: str) -> GpuBenchmark:
    normalized_query = normalize_text(query)
    query_tokens = normalized_query.split(" ")

    def score(gpu: GpuBenchmark) -> tuple[int, int, int]:
        name_tokens = normalize_text(gpu.name).split(" ")
        matched_count = sum(1 for token in query_tokens if token in name_tokens)
        extra_tokens = len(name_tokens) - len(query_tokens)
        return (matched_count, -extra_tokens, -len(name_tokens))

    return max(candidates, key=score)


def find_best_gpu_by_query(q: str, db: Session) -> GpuBenchmark:
    term = f"%{q}%"
    candidates = db.query(GpuBenchmark).filter(GpuBenchmark.name.ilike(term)).all()
    results = [gpu for gpu in candidates if matches_gpu_name(q, gpu.name)]

    if not results:
        raise HTTPException(
            status_code=404,
            detail="Não temos essa GPU em nosso banco de dados"
        )

    return choose_best_gpu(results, q)


@router.get("/search")
def search_gpus(q: str = Query(..., min_length=1, description="Nome ou parte do nome da GPU"),
                db: Session = Depends(get_db)):
    """
    Busca GPUs pelo nome com correspondência inteligente e case-insensitive.
    Retorna apenas um resultado, escolhendo o nome mais preciso.
    """
    return find_best_gpu_by_query(q, db)


@router.get("/cost")
def calculate_gpu_cost(
    q: str = Query(..., min_length=1, description="Nome ou parte do nome da GPU"),
    price: float = Query(..., gt=0, description="Preço atual da GPU"),
    db: Session = Depends(get_db)
):
    """
    Calcula o custo por frame da GPU pesquisada em todas as resoluções.
    """
    gpu = find_best_gpu_by_query(q, db)

    return {
        "gpu": gpu.name,
        "brand": gpu.brand,
        "price": price,
        "cost_per_frame": {
            "1080p_medium": round(price / gpu.fps_1080p_medium, 4),
            "1080p_ultra": round(price / gpu.fps_1080p_ultra, 4),
            "1440p": round(price / gpu.fps_1440p, 4),
            "4k": round(price / gpu.fps_4k, 4),
        }
    }


@router.get("/brand")
def get_gpus_by_brand(
    brand: str = Query(
        ..., 
        description="Escolha a marca da GPU",
        enum=["Nvidia", "AMD", "Intel"]
    ),
    db: Session = Depends(get_db)
):
    """
    Retorna todas as GPUs da marca escolhida.
    """
    results = db.query(GpuBenchmark).filter(GpuBenchmark.brand.ilike(brand)).all()

    if not results:
        raise HTTPException(
            status_code=404,
            detail="Não temos GPUs dessa marca em nosso banco de dados"
        )

    return results


@router.get("/{gpu_id}")
def get_gpu_by_id(gpu_id: int, db: Session = Depends(get_db)):
    gpu = db.query(GpuBenchmark).filter(GpuBenchmark.id == gpu_id).first()
    return gpu