from memory.search import search_files

if __name__ == "__main__":
    query = input("Enter search query: ").strip()
    results = search_files(query)

    print("\nTop matches:")
    for i, r in enumerate(results, 1):
        print(f"{i}. {r['filename']} ({r['score']:.2f})")
        print(f"   Path: {r['path']}")
        print(f"   Snippet: {r['snippet']}\n")
