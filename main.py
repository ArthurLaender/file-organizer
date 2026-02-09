# main.py
import argparse
from pathlib import Path

from organizer.scanner import scan_folder
from organizer.sorter import decide_folder
from organizer.mover import move_file


def parse_arguments():
    """
    Defines and parses command-line arguments for the organizer.
    TO-DO: Test all.
    This function creates a CLI interface so users can
    control how the program behaves without changing code.
    """
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by type"
    )

    # --path allows the user to specify which folder should be organized. Default is the current directory.
    parser.add_argument(
        "--path",
        type=Path,
        default=Path("."),
        help="Folder to organize (default: current directory)",
    )

    # --dry-run the files will NOT be moved, it will only show what would happen
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without moving files",
    )

    return parser.parse_args()


def main():
    # Parse CLI arguments
    args = parse_arguments()
    # Base folder to organize
    base_path = args.path

    # Scan the folder and get a list of files
    files = scan_folder(base_path)

    # Process each file individually
    for file in files:
        # Decide which category folder the file belongs to
        folder_name = decide_folder(file)
        # Build the destination folder path
        destination_folder = base_path / folder_name

        # If dry-run is enabled, do NOT move files
        if args.dry_run:
            print(f"[DRY RUN] {file.name} -> {destination_folder}")
        else:
            new_path = move_file(file, destination_folder)
            print(f"Moved {file.name} -> {new_path}")



if __name__ == "__main__":
    main()
