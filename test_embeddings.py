from memory.embeddings import generate_embedding

if __name__ == "__main__":
    text = input("Enter some text to embed: ").strip()
    embedding = generate_embedding(text)
    print("\nEmbedding shape:", embedding.shape)
    print("First 5 values:", embedding[:5])
