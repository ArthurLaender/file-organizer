#mover.py

from pathlib import Path
#library for file operations
import shutil

def ensure_folder_exists(folder_path: Path):
    folder_path.mkdir(parents=True, exist_ok=True)

def get_safe_destination(destination: Path) -> Path:
    if not destination.exists():
        return destination

    #guarantees no overwrite occurs by adding a counter suffix to the file name
    counter = 1
    while True:
        new_destination = destination.with_stem(
            f"{destination.stem}_{counter}"
        )
        if not new_destination.exists():
            return new_destination
        counter += 1

def move_file(file_path: Path, destination_folder: Path) -> Path:
    ensure_folder_exists(destination_folder)

    destination = destination_folder / file_path.name
    safe_destination = get_safe_destination(destination)

    shutil.move(str(file_path), str(safe_destination))
    return safe_destination
