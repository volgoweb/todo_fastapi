from fastapi import FastAPI
from aiohttp import ClientSession, TCPConnector


app = FastAPI()


@app.get("/")
async def root():
    # r = requests.get("http://localhost:9090/api/me")
    # print(r)
    print("(=====)")
    async with ClientSession(
            headers={"X-User": "0"},
            connector=TCPConnector(
                verify_ssl=False,
                limit=1,  # or use_dns_cache=False
            ),
    ) as http_client:
        url = "http://users_api:9090/api/me"
        print("url::::", url)
        # url = "http://nalog.gov.ru"
        async with http_client.get(url) as response:
            print("Response: ", response)
            r = await response.json()
            print(r)

    return {"message": "I'm Tasks API"}
