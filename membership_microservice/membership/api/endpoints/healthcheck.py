from fastapi import APIRouter
from membership.api.schemas import MsgResponse

router = APIRouter()


@router.get("/healthcheck", response_model=MsgResponse)
async def healthcheck():
    return MsgResponse(msg="pong")
