# main.py
from organizer.scanner import scan_folder
from organizer.sorter import decide_folder


def main():
    files = scan_folder(".")

    for file in files:
        folder = decide_folder(file)
        print(f"{file.name} -> {folder}")


if __name__ == "__main__":
    main()
