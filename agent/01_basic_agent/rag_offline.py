"""Offline document ingestion and vector-store setup for the basic RAG example."""

from datetime import UTC, datetime
from pathlib import Path

from dotenv import load_dotenv

from chroma import COLLECTION_NAME, Chunk, get_chroma_client, make_new_collection

DOCS_DIR = "docs"

load_dotenv()


def load_doc_chunks(path: Path) -> list[Chunk]:
    text = path.read_text(encoding="utf-8")
    parts = text.split("\n\n")
    title = parts[0]
    timestamp = datetime.now(tz=UTC).strftime("%Y-%m-%d %H:%M:%S UTC")

    result = []
    for index, paragraph in enumerate(parts[1:]):
        result.append(
            Chunk(
                id=f"{path.stem}-chunk-{index}",
                text=f"{title}\n{paragraph}",
                metadata={"source": str(path), "timestamp": timestamp},
            )
        )
    return result


def load_chunks(paths: list[Path]) -> list[Chunk]:
    chunks = []
    for path in paths:
        chunks.extend(load_doc_chunks(path))
    return chunks


def populate_collection(chunks: list[Chunk]) -> None:
    collection.add(
        ids=[chunk.id for chunk in chunks],
        documents=[chunk.text for chunk in chunks],
        metadatas=[chunk.metadata for chunk in chunks],
    )


def offline_stage(paths: list[Path]) -> None:
    populate_collection(load_chunks(paths))


if __name__ == "__main__":
    chroma_client = get_chroma_client()
    collection = make_new_collection(chroma_client, COLLECTION_NAME)
    offline_stage(list(Path(DOCS_DIR).glob("*.md")))
