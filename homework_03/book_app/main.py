from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_homepage():
    return {"message": "Homepage"}


@app.get("/ping")
async def get_ping():
    return {"message": "pong"}

