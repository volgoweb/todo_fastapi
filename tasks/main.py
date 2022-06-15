from fastapi import FastAPI

from tasks.containers.core import Container
from tasks.api.router import router

app = FastAPI()
app.include_router(router)
container = Container()
container.wire(packages=["tasks"])
def bla(x: int):
    print("x")

bla(2)
# ..
