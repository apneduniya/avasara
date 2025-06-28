import openai
import faiss
import numpy as np

from app.config.settings import config


class VectorStore:
    """A vector store implementation using FAISS for efficient similarity search.
    
    This class provides functionality to:
    - Generate embeddings using OpenAI's embedding models
    - Build and maintain a FAISS index for fast similarity search
    - Search for similar documents based on query text
    
    Attributes:
        index (faiss.IndexFlatL2): The FAISS index for similarity search
        documents (List[str]): List of documents stored in the vector store
    """
    
    def __init__(self):
        """Initialize an empty vector store."""
        self.index = None
        self.documents = []

    def embed(self, text: str) -> np.ndarray:
        """Generate embeddings for the input text using OpenAI's embedding model.
        
        Args:
            text (str): The input text to generate embeddings for
            
        Returns:
            np.ndarray: The embedding vector as a numpy array
            
        Example:
            >>> vector_store = VectorStore()
            >>> embedding = vector_store.embed("Hello world")
            >>> embedding.shape
            (1536,)
        """
        response = openai.embeddings.create(
            model=config.DEFAULT_EMBEDDING_MODEL,
            input=text
        )
        return np.array(response['data'][0]['embedding'], dtype=np.float32)

    def build_index(self, chunks: list[str]) -> None:
        """Build a FAISS index from the given text chunks.
        It helps to find the most similar documents to the query text.
        
        Args:
            chunks (List[str]): List of text chunks to index
            
        Example:
            >>> vector_store = VectorStore()
            >>> chunks = ["Hello", "world"]
            >>> vector_store.build_index(chunks)
        """
        self.documents = chunks
        dim = len(self.embed("test"))
        self.index = faiss.IndexFlatL2(dim)
        vectors = np.array([self.embed(chunk) for chunk in chunks])
        self.index.add(vectors)

    def search(self, query: str, top_k: int = config.DEFAULT_EMBEDDING_TOP_K) -> list[str]:
        """Search for similar documents to the query text.
        
        Args:
            query (str): The search query text
            top_k (int): Number of most similar documents to return
            
        Returns:
            List[str]: List of top_k most similar documents
            
        Example:
            >>> vector_store = VectorStore()
            >>> vector_store.build_index(["Hello", "world"])
            >>> results = vector_store.search("Hello", 1)
            >>> results
            ['Hello']
        """
        query_vec = self.embed(query).reshape(1, -1)
        _, I = self.index.search(query_vec, top_k)
        return [self.documents[i] for i in I[0]]
