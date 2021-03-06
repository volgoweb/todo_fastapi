from fastapi import APIRouter
from tasks.api.schemas import MsgResponse

router = APIRouter()


@router.get("/healthcheck", response_model=MsgResponse)
async def healthcheck():
    return MsgResponse(msg="pong")
