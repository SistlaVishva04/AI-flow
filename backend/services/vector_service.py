from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.Client(
    settings=Settings(
        persist_directory="chroma_db"
    )
)

collection = chroma_client.get_or_create_collection("knowledge_base")

def store_chunks(file_id, chunks):
    print("store_chunks called")
    print("Chunks received:", len(chunks))
    embeddings = model.encode(chunks).tolist()

    ids = [f"{file_id}_{i}" for i in range(len(chunks))]

    # Remove old chunks if same file is re-uploaded
    try:

        existing = collection.get(where={"fileId": file_id})
        if existing["ids"]:
            collection.delete(ids=existing["ids"])
    except:

        pass


    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=[{"fileId": file_id}] * len(chunks)
    )
    

    
