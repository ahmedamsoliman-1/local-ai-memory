import argparse
from memory.watcher import watch_folder
from memory.extractor import extract_text
from memory.embeddings import generate_embedding
from memory.database import initialize_database, insert_file
from memory.search import search_files
import os

def process_file(path):
    if not os.path.isfile(path):
        return
    print(f"🔍 Processing: {path}")
    text = extract_text(path)
    if not text.strip():
        print("⚠️ No text extracted, skipping.")
        return
    embedding = generate_embedding(text)
    insert_file(path, text, embedding)

def main():
    parser = argparse.ArgumentParser(description="Local AI Memory CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Init DB command
    parser_init = subparsers.add_parser("init", help="Initialize the local database")

    # Watch folder command
    parser_watch = subparsers.add_parser("watch", help="Watch a folder for file changes")
    parser_watch.add_argument("folder", help="Folder path to watch")

    # Search command
    parser_search = subparsers.add_parser("search", help="Search indexed files")
    parser_search.add_argument("query", help="Search query string")
    parser_search.add_argument("--top", type=int, default=5, help="Number of top results to show")

    args = parser.parse_args()

    if args.command == "init":
        initialize_database()

    elif args.command == "watch":
        folder = args.folder
        watch_folder(folder, process_file)

    elif args.command == "search":
        results = search_files(args.query, top_k=args.top)
        if not results:
            print("No results found.")
            return
        print(f"Top {len(results)} results for: '{args.query}'\n")
        for i, r in enumerate(results, 1):
            print(f"{i}. {r['filename']} (Score: {r['score']:.2f})")
            print(f"   Path: {r['path']}")
            print(f"   Snippet: {r['snippet']}\n")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
