from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class BodyResponse(BaseModel):
    conv_code: str
    department_id: str
    subject: str
    source: str
    tags: List[str]

@app.get("/")
async def root():
    return "Working"

@app.post("/echo")
async def echo(body: BodyResponse):
    return body