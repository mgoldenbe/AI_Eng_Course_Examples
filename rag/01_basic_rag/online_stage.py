from dotenv import load_dotenv
from openai import OpenAI

from chroma import COLLECTION_NAME, Chunk, get_chroma_client, get_collection

LLM_MODEL = "gpt-5.6-luna"
N_SEARCH_RESULTS = 3

load_dotenv()

def dump_chunks(chunks: list[Chunk]) -> None:
    for chunk in chunks:
        actual_chunk = chunk.text.partition("\n")[2]
        print(f"Chunk: {actual_chunk[:60]}...    Distance: {chunk.distance:.3f}")

def retrieve_chunks(query: str) -> list[Chunk]:
    res = collection.query(
        query_texts=[query],
        n_results=N_SEARCH_RESULTS,
    )
    ids, texts, metadatas, distances = \
        res["ids"][0], res["documents"][0], res["metadatas"][0], res["distances"][0]

    retrieved_chunks = []
    for index in range(len(ids)):
        chunk = Chunk(
            id=ids[index],
            text=texts[index],
            metadata=metadatas[index],
            distance=distances[index]
        )
        retrieved_chunks.append(chunk)

    dump_chunks(retrieved_chunks)
    return retrieved_chunks


def compute_augmented_context(
        query: str,
        retrieved_chunks: list[Chunk]) -> list:
    retrieved_context = "\n\n---\n\n".join(
            chunk.text for chunk in retrieved_chunks
    )
    return [
        {
            "role": "developer",
            "content": (
                "Answer the user's question using the retrieved information "
                "below. If the retrieved information does not contain the "
                "answer, say that you don't know.\n\n"
                f"Retrieved information:\n{retrieved_context}"
            ),
        },
        {
            "role": "user",
            "content": query,
        },
    ]

def generate_answer(augmented_context: list) -> str:
    response = llm_client.chat.completions.create(
        model=LLM_MODEL,
        messages=augmented_context
    )
    return response.choices[0].message.content

def online_stage(query: str) -> str:
    retrieved_chunks = retrieve_chunks(query)
    augmented_context = compute_augmented_context(query, retrieved_chunks)
    return generate_answer(augmented_context)

def process_queries(queries: list[str]) -> list[str]:
    for query in queries:
        print(f"Question: {query}")
        answer = online_stage(query)
        print(f"Answer: {answer}\n")


if __name__ == "__main__":
    llm_client = OpenAI()
    chroma_client = get_chroma_client()
    collection = get_collection(chroma_client, name=COLLECTION_NAME)
    questions = [
        "Where can I work without people talking?",
        "Where do people dance on this campus?",
    ]
    process_queries(questions)
