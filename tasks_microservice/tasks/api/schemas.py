from pydantic import BaseModel


class SuccessMsg(BaseModel):
    msg: str = 'ok'
