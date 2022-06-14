from aiohttp import ClientSession, TCPConnector


async def request_something():
    async with ClientSession(
            headers={"X-User": "0"},
            connector=TCPConnector(
                verify_ssl=False,
                limit=1,  # or use_dns_cache=False
            ),
    ) as http_client:
        url = "http://users_api:9000/api/me"
        async with http_client.get(url) as response:
            print("Response: ", response)
            r = await response.json()
            print(r)

    return r
