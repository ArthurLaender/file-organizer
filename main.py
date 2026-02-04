# main.py
from organizer.scanner import scan_folder


if __name__ == "__main__":
    files = scan_folder(".")

    for file in files:
        print(file)
