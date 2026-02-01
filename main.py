from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

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
    print(f"received: x={data.x}, y={data.y}")
    return {"result": z}

@app.get("/")
@app.get("/countries/")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no
    }