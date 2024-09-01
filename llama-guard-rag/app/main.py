from fastapi import FastAPI
from app.payload import Payload
from core.rag_guard import RagGuard
from typing import Any

app = FastAPI()
rag_guard = RagGuard()


@app.post("/moderate")
def read_item(request_body: Payload) -> Any:
    return rag_guard.moderate_chat(request_body.user_query)
