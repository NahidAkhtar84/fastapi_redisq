from fastapi import APIRouter

health = APIRouter()


@health.get("/health")
def get() -> bool:
    return True
