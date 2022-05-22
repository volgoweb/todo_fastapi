from typing import Optional, Dict, NoReturn
from dataclasses import dataclass
from os import environ
import json

import redis
from fastapi import FastAPI, Header, HTTPException


@dataclass
class RedisConfig:
    host: str
    db: int
    port: int


redis_config = RedisConfig(
    host=environ["REDIS_HOST"],
    db=int(environ["REDIS_DB"]),
    port=int(environ["REDIS_PORT"]),
)

app = FastAPI()
app.redis = redis.Redis(
    host=redis_config.host,
    port=redis_config.port,
    db=redis_config.db,
)

fake_db_table = {
    0: {
        "first_name": "John",
        "last_name": "Carlson",
        "email": "jcarlson@test.test",
    }
}


@app.get("/")
async def root():
    return {"message": "I'm Users API"}


class GetMeData:
    def __init__(self, redis_client):
        self._redis_client = redis_client

    def run(self, user_id: int) -> Dict:
        cached = self._get_from_cache(user_id)
        if cached:
            return cached

        data = self._get_from_db(user_id)
        if data:
            self._cache(user_id, data=data)
        return data

    def _get_from_cache(self, user_id: int) -> Optional[Dict]:
        key = self._generate_cache_key(user_id)
        cached = self._redis_client.get(key)
        if not cached:
            return None
        as_dict = json.loads(cached)
        return as_dict

    def _get_from_db(self, user_id: int) -> Optional[Dict]:
        return fake_db_table.get(user_id, None)

    def _cache(self, user_id: int, data: dict) -> NoReturn:
        key = self._generate_cache_key(user_id)
        as_json = json.dumps(data)
        return self._redis_client.set(key, as_json)

    @staticmethod
    def _generate_cache_key(user_id: int) -> str:
        return f"user-{user_id}:me"


@app.get("/me")
async def me(x_user: Optional[str] = Header("")):
    if not x_user:
        raise HTTPException(status_code=403)

    user_id = int(x_user)
    data = GetMeData(redis_client=app.redis).run(user_id)
    return data
