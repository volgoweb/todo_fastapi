from fastapi import FastAPI

from membership.api.router import router


app = FastAPI()
app.include_router(router)
