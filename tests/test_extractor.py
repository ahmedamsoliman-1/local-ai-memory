from memory.extractor import extract_text

if __name__ == "__main__":
    path = input("Enter the file path to extract text: ").strip()
    text = extract_text(path)
    print("\n--- Extracted Text ---\n")
    print(text[:10])
