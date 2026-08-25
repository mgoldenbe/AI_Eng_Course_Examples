"""Configuration for the basic RAG example."""

import os
from dataclasses import dataclass

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

COLLECTION_NAME = "campus"
EMBEDDING_MODEL = "text-embedding-3-small"

@dataclass
class Chunk:
    id: str
    text: str
    metadata: dict[str, str]
    distance: float | None = None

def get_chroma_client() -> chromadb.Client:
    return (
        chromadb.CloudClient(api_key=os.getenv("CHROMA_API_KEY"))
    )


def make_new_collection(
    chroma_client: chromadb.Client,
    name: str,
) -> chromadb.api.models.Collection:
    embedding_function = OpenAIEmbeddingFunction(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name=EMBEDDING_MODEL,
    )

    try:
        chroma_client.delete_collection(name=name)
        print(f"Deleted existing collection: {name}")
    except ValueError:
        pass

    return chroma_client.get_or_create_collection(
        name=name,
        embedding_function=embedding_function,
    )


def get_collection(
    chroma_client: chromadb.Client,
    name: str,
) -> chromadb.api.models.Collection:
    return chroma_client.get_collection(name=name)
