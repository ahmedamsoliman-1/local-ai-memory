import numpy as np
from memory.database import get_all_embeddings, get_content_by_id
from memory.embeddings import generate_embedding

def cosine_similarity(vec1, vec2):
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0.0
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def search_files(query, top_k=5):
    query_embedding = generate_embedding(query)
    files = get_all_embeddings()

    scored = []
    for file_id, path, filename, embedding in files:
        score = cosine_similarity(query_embedding, embedding)
        scored.append((score, file_id, path, filename))

    # Sort descending by similarity score
    scored.sort(key=lambda x: x[0], reverse=True)

    # Return top K results
    results = []
    for score, file_id, path, filename in scored[:top_k]:
        content = get_content_by_id(file_id)
        snippet = content[:300].replace('\n', ' ') if content else ''
        results.append({
            "score": score,
            "path": path,
            "filename": filename,
            "snippet": snippet,
        })

    return results
