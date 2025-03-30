from fastapi import FastAPI
from httpx import AsyncClient

app = FastAPI()


@app.get("/api/v1/quotes/random")
async def random_quote():
    random_quote_api_base_url = "https://api.quotable.kurokeita.dev/api/quotes/random"

    async with AsyncClient() as client:
        response = await client.get(random_quote_api_base_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch quote"}
