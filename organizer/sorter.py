#sorter.py
from pathlib import Path

#Mapeia que documentos irão a quais pastas baseado em suas extensões
EXTENSION_MAP = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",

    ".mp3": "Music",
    ".wav": "Music",

    ".mp4": "Videos",
    ".mkv": "Videos",
}

def decide_folder(file_path: Path) -> str:
    """
    Receives a Path object and returns the folder name
    where the file should be organized.
    """
    extension = file_path.suffix.lower()

    return EXTENSION_MAP.get(extension, "Others")

