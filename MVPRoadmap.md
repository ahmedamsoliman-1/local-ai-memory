# 🌿 Local AI Memory – MVP Roadmap

A privacy-focused personal assistant that records your activity on your machine and makes it searchable.

## 🏗️ 1 Goal of the MVP

A simple, working app that can:

✅ Watch a folder (e.g., `~/Documents`)  
✅ Log opened files (name, path, timestamp)  
✅ Extract text content  
✅ Store all entries in a local database  
✅ Create embeddings for semantic search  
✅ Let you run a search query in CLI and get matching files

## 💡 2 Architecture Overview

```{architecture}
+-------------------+
| File Watcher |
+---------+---------+
|
v
+-------------------+
| Text Extractor |
| (PDF, TXT, DOCX) |
+---------+---------+
|
v
+-------------------+
| Embeddings Engine |
| (SentenceTransformers) |
+---------+---------+
|
v
+-------------------+
| SQLite DB |
+---------+---------+
|
v
+-------------------+
| CLI Search Tool |
+-------------------+
```

## 🧩 3 Technology Choices

**Language:**

- Python

**Libraries:**

- File Watching: [`watchdog`](https://github.com/gorakhargosh/watchdog)
- Text Extraction:
  - TXT: built-in
  - PDF: [`PyMuPDF`](https://pymupdf.readthedocs.io/)
  - DOCX: [`python-docx`](https://python-docx.readthedocs.io/)
- Embeddings: [`sentence-transformers`](https://www.sbert.net/)
- Database: `sqlite3`
- CLI: `argparse` or `click`

## 🛠️ 4 Data Model (SQLite)

**Table:** `files`

| Column     | Type      | Description                      |
|------------|-----------|----------------------------------|
| id         | INTEGER   | Primary key                     |
| path       | TEXT      | Full file path                  |
| filename   | TEXT      | File name                       |
| timestamp  | DATETIME  | When it was processed           |
| content    | TEXT      | Extracted text (truncated)      |
| embedding  | BLOB      | Numpy vector serialized         |

## ⚙️ 5 How It Works (Flow)

1️⃣ Watcher detects new or modified file  
2️⃣ Extract text  
3️⃣ Generate embedding  
4️⃣ Store everything in SQLite  
5️⃣ On search:

- Convert query to embedding
- Compute cosine similarity
- Return top N results

## 🐍 6 Step-by-Step Build Plan

### Phase 1 – Core Capture

✅ Set up `watchdog` to monitor a folder  
✅ On file change:

- Log metadata
- Extract text

### Phase 2 – Embeddings

✅ Install `sentence-transformers`  
✅ Convert text to embeddings

### Phase 3 – Database

✅ Store metadata and embeddings in SQLite

### Phase 4 – Search CLI

✅ User enters query:

- Generate embedding
- Compare against stored embeddings
- Show top matches with similarity scores

## 🧪 7 Example Usage

**Indexing:**

```arduino
$ python memory.py watch ~/Documents
Watching folder... (Ctrl+C to stop)
```

**Searching:**

```ruby
$ python memory.py search "Kubernetes configuration"
Top Matches:
1. ~/Documents/cluster-setup.docx  (score: 0.87)
2. ~/Documents/kube-notes.txt      (score: 0.82)
```

## ✨ 8 Future Extensions

- Desktop GUI (Tauri or Electron)
- Multiple folder watching
- Support more file types (Markdown, HTML)
- Encryption at rest
- Daily/weekly summaries
- Browser extension for URL capture
- Git integration

## 🧭 9 Timeline Suggestion

| Week | Goal                              |
|------|-----------------------------------|
| 1    | Project skeleton + file watcher  |
| 2    | Text extraction & embeddings     |
| 3    | SQLite storage & retrieval       |
| 4    | CLI search & end-to-end testing  |

## 🗂️ 10 Recommended Repo Structure

```tree
local-ai-memory/
memory/
init.py
watcher.py
extractor.py
embeddings.py
database.py
search.py
cli.py
requirements.txt
README.md
```
