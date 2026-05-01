
# fastapi_rag.py - Ayurvedic RAG Backend
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient, models
import json

app = FastAPI(title="Ayurvedic RAG API")

# Load model once
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
qdrant = QdrantClient(":memory:")  # replace with your Qdrant URL

# Load knowledge base
with open('ayurveda_knowledge_200.json', 'r', encoding='utf-8') as f:
    KB = json.load(f)

class Query(BaseModel):
    text: str
    lang: str = "hi"
    top_k: int = 3

@app.on_event("startup")
def init_db():
    qdrant.recreate_collection(
        collection_name="ayurveda",
        vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE)
    )
    # Index all shlokas
    vectors = model.encode([f"{item['condition_hindi']} {item['hindi']}" for item in KB])
    qdrant.upsert(
        collection_name="ayurveda",
        points=models.Batch(
            ids=list(range(len(KB))),
            vectors=vectors.tolist(),
            payloads=KB
        )
    )

@app.post("/search")
def search(query: Query):
    vec = model.encode(query.text).tolist()
    results = qdrant.search(
        collection_name="ayurveda",
        query_vector=vec,
        limit=query.top_k
    )
    return {
        "query": query.text,
        "results": [r.payload for r in results],
        "disclaimer": "शैक्षिक उद्देश्य मात्र। वैद्य से परामर्श करें।"
    }

@app.get("/shloka/{id}")
def get_shloka(id: str):
    item = next((x for x in KB if x['id'] == id), None)
    if not item:
        raise HTTPException(404, "Not found")
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
