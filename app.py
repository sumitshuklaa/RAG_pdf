from src.rag.data_loader import load_all_documents
from src.rag.vectorstore import FaissVectorStore

# Example usage

if __name__ == "__main__":
    #docs = load_all_documents("data")
    store= FaissVectorStore("faiss_store")
    #store.build_from_documents(docs)
    store.load()
    print(store.query("What is programming", top_k=3))
    
    
  