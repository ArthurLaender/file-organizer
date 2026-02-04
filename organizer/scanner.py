# scanner.py

from pathlib import Path


def scan_folder(folder_path):
    #Receives a folder path and returns a list of files inside it.

    path = Path(folder_path)

    #Verifies if path exists and it's a directory
    if not path.exists():
        raise FileNotFoundError(f"The path '{folder_path}' does not exist")
    if not path.is_dir():
        raise NotADirectoryError(f"'{folder_path}' is not a directory")

    files = []

    #lists files (not folders) inside current folder and
    for item in path.iterdir():
        if item.is_file():
            files.append(item)

    return files
        

    pass
