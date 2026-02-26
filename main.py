from fastapi import FastAPI, Form
from typing import Optional

app = FastAPI()

@app.post("/echo")
async def echo(
    conv_code: str = Form(...),
    agent_id: Optional[str] = Form(None),
    department_id: Optional[str] = Form(None),
    subject: Optional[str] = Form(None),
    source: Optional[str] = Form(None),
    tags: Optional[str] = Form(None)
):
    tags_list = [t.strip() for t in (tags or "").split(",") if t.strip()]
    data = {
        "conv_code": conv_code,
        "agent_id": agent_id,
        "department_id": department_id,
        "subject": subject,
        "source": source,
        "tags_raw": tags,
        "tags": tags_list
    }

    print(f"data: {data}")
    return data