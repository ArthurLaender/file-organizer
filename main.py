# main.py
from pathlib import Path
from organizer.scanner import scan_folder
from organizer.sorter import decide_folder
from organizer.mover import move_file


def main():
    base_path = Path(".")

    files = scan_folder(base_path)

    for file in files:
        folder_name = decide_folder(file)
        destination_folder = base_path / folder_name

        new_path = move_file(file, destination_folder)
        print(f"Moved {file.name} -> {new_path}")


if __name__ == "__main__":
    main()
