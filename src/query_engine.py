from src.embedding_engine import get_embeddings
from src.vector_store import VectorStore

class QueryEngine:
    def __init__(self):
        self.vector_store = VectorStore()

    def build_knowledge_base(self, documents):
        texts = [doc[1] for doc in documents]
        embeddings = get_embeddings(texts)
        self.vector_store.add(embeddings, texts)

    def query(self, question):
        query_embedding = get_embeddings([question])[0]
        return self.vector_store.search(query_embedding)
