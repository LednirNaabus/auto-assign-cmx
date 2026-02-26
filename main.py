from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union, Optional

app = FastAPI()

class BodyResponse(BaseModel):
    conv_code: str
    agent_id: Optional[str] = None
    department_id: Optional[str] = None
    subject: Optional[str] = None
    source: Optional[str] = None
    tags: Union[List[str], str, None] = None

@app.get("/")
async def root():
    return "Working"

@app.post("/echo")
async def echo(body: BodyResponse):
    tags = body.tags
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    return {**body.model_dump(), "tags": tags}