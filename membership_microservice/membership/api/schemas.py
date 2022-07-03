from pydantic import BaseModel


class MsgResponse(BaseModel):
    msg: str


class MyMembershipResponse(BaseModel):
    is_premium: bool
    plan: str
