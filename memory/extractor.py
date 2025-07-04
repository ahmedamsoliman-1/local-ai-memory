from pathlib import Path
import fitz
import docx

def extract_text(file_path):
    """
    Detects file type and extracts text.
    """
    path = Path(file_path)
    suffix = path.suffix.lower()
    
    if suffix == ".txt":
        return extract_txt(path)
    elif suffix == ".pdf":
        return extract_pdf(path)
    elif suffix == ".docx":
        return extract_docx(path)
    else:
        print(f"⚠️ Unsupported file type: {suffix}")
        return ""

def extract_txt(path):
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        print(f"❌ Error reading TXT: {e}")
        return ""

def extract_pdf(path):
    try:
        doc = fitz.open(str(path))
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        return ""

def extract_docx(path):
    try:
        doc = docx.Document(str(path))
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"❌ Error reading DOCX: {e}")
        return ""
