from typing import Optional

from fastapi import APIRouter, Header

from users.persistent.users_repository import UsersRepository

api_router = APIRouter()


@api_router.get("/me")
async def me(x_user: Optional[str] = Header("")):
    # if not x_user:
    #     raise HTTPException(status_code=403)

    user_id: int = int(x_user or 1)
    data = UsersRepository().get_by_id(user_id)
    return data
