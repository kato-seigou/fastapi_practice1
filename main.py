from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
    x: int
    y: int

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello Deta!"}

@app.post("/")
async def calc(data: Data):
    z = data.x * data.y
    return {"result": z}