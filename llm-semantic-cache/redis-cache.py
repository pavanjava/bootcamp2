import litellm
from litellm import completion
from litellm.caching import Cache

# litellm.enable_cache()
# litellm.cache = Cache(type="redis", host="localhost", port="6379")  # password=<password>

context = (
    "Redis, short for Remote Dictionary Server, is an open-source, in-memory data structure store that is widely used as a database, cache, and message broker. It was initially released in 2009 and quickly gained popularity due to its versatility, performance, and simplicity. Unlike traditional relational databases, Redis is designed to store data in a variety of data structures such as strings, hashes, lists, sets, and sorted sets, among others. This makes Redis particularly well-suited for use cases that require real-time processing and data retrieval, such as caching, session management, real-time analytics, and pub/sub messaging."
    "One of the key features of Redis is its ability to persist data to disk while maintaining the high-speed characteristics of an in-memory store. This is achieved through a combination of snapshotting and append-only file (AOF) persistence mechanisms, allowing users to balance the trade-off between performance and durability. Additionally, Redis supports replication, enabling data to be copied across multiple servers, which not only enhances data availability but also allows for horizontal scaling in distributed environments. With built-in support for clustering, Redis can handle large datasets that exceed the memory capacity of a single node, further boosting its scalability."
    "Redis is also known for its simplicity and ease of use. It provides a straightforward command-line interface, and its API is accessible from numerous programming languages, making it easy to integrate into a wide range of applications. Its rich set of commands and data structures, combined with high performance and scalability, have made Redis a popular choice among developers for building high-performance, distributed systems. Moreover, the active community around Redis continuously contributes to its ecosystem, extending its functionality through various modules and tools, ensuring that Redis remains a relevant and powerful tool in modern software development.")
# Make completion calls
response1 = completion(
    model="ollama/llama3.1",
    messages=[{"role": "user", "content": f"summarize the given context:{context}"}],
    # cache={"no-cache": False, "no-store": False}
)
response2 = completion(
    model="ollama/llama3.1",
    messages=[{"role": "user", "content": f"summarize the given context:{context}"}],
    # cache={"no-cache": False, "no-store": False}
)

print(response1)
print(response2)
# assert response1.id == response2.id  # response 1 is cached

