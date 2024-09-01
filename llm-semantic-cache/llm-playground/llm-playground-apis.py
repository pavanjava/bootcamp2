from litellm import completion
from litellm.types.utils import ModelResponse
from litellm.utils import CustomStreamWrapper
from dotenv import load_dotenv, find_dotenv
from typing import Optional, Any
from fastapi import FastAPI
from pydantic import BaseModel
from utils.app_utils import time_it
import uvicorn
import os


# class defined for the llm packs which operate on multiple LLM responses
class LLMPack:
    def __init__(self, openai_model: str = 'gpt-3.5-turbo', open_source_model: str = 'ollama/llama3.1'):
        _ = load_dotenv(find_dotenv())
        self.openai_model = openai_model
        self.open_source_model = open_source_model

    @time_it
    # messages = [{"content": "Hello, how are you?", "role": "user"}]
    def invoke_llm(self, messages) -> (ModelResponse, CustomStreamWrapper):
        # openai call
        openai_response = completion(model=self.openai_model, messages=messages, api_key=os.environ["OPENAI_API_KEY"])

        # open source call (ollama)
        open_source_response = completion(model=self.open_source_model, messages=messages)

        return openai_response, open_source_response


# class used for fastapi payload
class UserMessages(BaseModel):
    openai_model: Optional[str] = None
    open_source_model: Optional[str] = None
    content: str


app = FastAPI()
llm_pack = LLMPack()


@app.post('/v1/chat/completions')
def chat_completions(user_messages: UserMessages) -> Any:
    if user_messages.openai_model is not None:
        llm_pack.openai_model = user_messages.openai_model
    if user_messages.open_source_model is not None:
        llm_pack.open_source_model = user_messages.open_source_model

    if user_messages.content is not None or user_messages.content != '':
        messages = [{"content": user_messages.content, "role": "user"}]
        response1, response2 = llm_pack.invoke_llm(messages=messages)
        return {'response1': response1, 'response2': response2}
    else:
        return {'response': 'payload cannot be empty'}


if __name__ == '__main__':
    uvicorn.run(host='0.0.0.0', port=8002, reload=False, access_log=True, app=app)
