import sqlite3
from pathlib import Path
import numpy as np
import datetime

DB_PATH = Path("memory.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE,
            filename TEXT,
            timestamp TEXT,
            content TEXT,
            embedding BLOB
        )
    """)
    conn.commit()
    conn.close()
    print("✅ Database initialized.")

def insert_file(path, content, embedding):
    conn = get_connection()
    cursor = conn.cursor()
    filename = Path(path).name
    timestamp = datetime.datetime.utcnow().isoformat()

    # Convert embedding numpy array to bytes
    embedding_bytes = embedding.tobytes()

    cursor.execute("""
        INSERT OR REPLACE INTO files (path, filename, timestamp, content, embedding)
        VALUES (?, ?, ?, ?, ?)
    """, (path, filename, timestamp, content, embedding_bytes))
    
    conn.commit()
    conn.close()
    print(f"💾 Saved: {filename}")

def get_all_embeddings():
    """
    Returns list of tuples: (id, path, filename, embedding np.array)
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, path, filename, embedding FROM files")
    rows = cursor.fetchall()
    conn.close()
    
    result = []
    for row in rows:
        embedding = np.frombuffer(row[3], dtype=np.float32)
        result.append( (row[0], row[1], row[2], embedding) )
    return result

def get_content_by_id(file_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM files WHERE id = ?", (file_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    return ""
