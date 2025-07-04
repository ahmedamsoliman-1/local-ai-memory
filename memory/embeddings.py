from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once globally
_model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text):
    """
    Generate a sentence embedding for the given text.
    """
    # You can truncate text here if needed
    if not text.strip():
        return np.zeros((384,), dtype=np.float32)

    embedding = _model.encode(text, normalize_embeddings=True)
    return embedding
