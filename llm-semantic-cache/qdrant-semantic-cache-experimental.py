import litellm
from litellm import completion
from litellm.caching import Cache
from dotenv import load_dotenv, find_dotenv
import random
import os
import asyncio

_ = load_dotenv(find_dotenv())

litellm.enable_cache()


async def test_qdrant_semantic_cache_acompletion():
    # litellm.set_verbose = True
    random_number = random.randint(
        1, 100000
    )  # add a random number to ensure it's always adding /reading from cache

    print("Testing Qdrant Semantic Caching with acompletion")

    print(f"question: write a one sentence poem about: {random_number}")
    litellm.cache = Cache(
        type="qdrant-semantic",
        _host_type="cloud",
        qdrant_api_base=os.getenv("QDRANT_API_BASE"),
        qdrant_api_key=os.getenv("QDRANT_API_KEY"),
        qdrant_collection_name="semantic-cache",
        similarity_threshold=0.95,
        qdrant_quantization_config="binary",
        # qdrant_semantic_cache_embedding_model='ollama/llama3.1'
    )

    response1 = await litellm.acompletion(
        api_base='http://localhost:11434',
        model="ollama/llama3.1",
        messages=[
            {
                "role": "user",
                "content": f"write a one sentence poem about: {random_number}",
            }
        ],
        # mock_response="hello",
        max_tokens=20
    )
    print(f"Response1: {response1}")

    response2 = await litellm.acompletion(
        api_base='http://localhost:11434',
        model="ollama/llama3.1",
        messages=[
            {
                "role": "user",
                "content": f"write a one sentence poem about: {random_number}",
            }
        ],
        max_tokens=20
    )
    print(f"Response2: {response2}")
    # assert response1.id == response2.id


if __name__ == "__main__":
    asyncio.run(test_qdrant_semantic_cache_acompletion())
