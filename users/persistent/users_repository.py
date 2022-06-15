from typing import Optional, Dict


class UsersRepository:
    __fake_db_table: Dict[int, Dict[str, str]] = {
        0: {
            "first_name": "John",
            "last_name": "Carlson",
            "email": "jcarlson@test.test",
        }
    }

    def get_by_id(self, id_: int) -> Optional[Dict]:
        return self.__fake_db_table.get(id_)

"""
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
"""
