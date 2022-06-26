from fastapi import APIRouter
from tasks.api.schemas import SuccessMsg

router = APIRouter()


@router.get("/healthcheck", response_model=SuccessMsg)
async def healthcheck():
    return SuccessMsg()
