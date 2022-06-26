from dataclasses import dataclass
from os import environ

import redis
from fastapi import FastAPI
from users.api.endpoints import api_router


app = FastAPI()
app.include_router(api_router, prefix="/api")


@dataclass
class RedisConfig:
    host: str
    db: int
    port: int


try:
    redis_config = RedisConfig(
        host=environ["REDIS_HOST"],
        db=int(environ["REDIS_DB"]),
        port=int(environ["REDIS_PORT"]),
    )

    redis_client = redis.Redis(
        host=redis_config.host,
        port=redis_config.port,
        db=redis_config.db,
    )
    setattr(app, "redis_client", redis_client)
except:
    print("Redis undefined")


@app.get("/")
async def root():
    return {"message": "I'm Users API"}
# ..
