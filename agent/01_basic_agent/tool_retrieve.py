"""The retrieval tool exposed to the agent."""

from typing import Any

from chroma import COLLECTION_NAME, Chunk, get_chroma_client, get_collection

N_SEARCH_RESULTS = 1
seen_ids: set[str] = set()

# This JSON schema is passed directly to the OpenAI API by agent.py.
RETRIEVAL_TOOL = {
    "type": "function",
    "function": {
        "name": "retrieve",
        "description": (
            "Search the knowledge base."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "A concise well-formed sentence stating what information is missing to answer the user's query.",
                }
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
}

TOOLS = [RETRIEVAL_TOOL]


def dump_chunks(chunks: list[Chunk]) -> None:
    """Print a compact view of the chunks returned by retrieval."""
    for chunk in chunks:
        actual_chunk = chunk.text.partition("\n")[2]
        print(f"  Chunk: {actual_chunk[:60]}...    Distance: {chunk.distance:.3f}")


def _collection() -> Any:
    """Open the collection populated by rag_offline.py."""
    return get_collection(get_chroma_client(), name=COLLECTION_NAME)


def reset_seen_ids() -> None:
    """Forget chunks returned for the previous agent conversation."""
    seen_ids.clear()


def retrieve(query: str) -> dict[str, Any]:
    """Return the most relevant knowledge-base chunks for *query*."""
    print(f"  Query: {query!r}")
    query_args: dict[str, Any] = {
        "query_texts": [query],
        "n_results": N_SEARCH_RESULTS,
    }
    if seen_ids:
        query_args["where"] = {"#id": {"$nin": list(seen_ids)}}

    res = _collection().query(**query_args)
    ids, docs, metadatas, distances = \
        res["ids"][0], res["documents"][0], res["metadatas"][0], res["distances"][0]

    chunks = []
    for i in range(len(ids)):
        chunk = Chunk(
            id=ids[i],
            text=docs[i],
            metadata=metadatas[i] or {},
            distance=distances[i],
        )
        chunks.append(chunk)
        seen_ids.add(ids[i])

    dump_chunks(chunks)

    return {
        "results": [
            {
                "id": chunk.id,
                "content": chunk.text,
                "metadata": chunk.metadata,
                "distance": chunk.distance,
            }
            for chunk in chunks
        ]
    }
