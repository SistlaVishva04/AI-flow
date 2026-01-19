from services.vector_service import collection, model

def run_rag(config, query):
    file_id = config.get("fileId")

    if not file_id:
        return None

    print("Querying RAG with fileId:", file_id)
    print("Total chunks in DB:", collection.count())

    query_embedding = model.encode([query]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=config.get("topK", 3),
        where={"fileId": file_id}
    )

    print("Raw query results:", results)

    if not results.get("documents") or len(results["documents"][0]) == 0:
        return None

    contexts = []
    for doc in results["documents"][0]:
        contexts.append({
            "text": doc,
            "source": config.get("fileName")
        })

    print("RAG results:", contexts)

    return contexts
