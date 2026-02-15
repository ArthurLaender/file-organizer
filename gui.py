import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from collections import defaultdict

from organizer.scanner import scan_folder
from organizer.sorter import decide_folder
from organizer.mover import move_file


class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")

        # Selected folder path
        self.selected_path = tk.StringVar()

        # Dry-run option
        self.dry_run = tk.BooleanVar()

        # --- UI Layout ---

        # Folder selection
        tk.Label(root, text="Folder:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(root, textvariable=self.selected_path, width=50).grid(row=0, column=1, padx=5)
        tk.Button(root, text="Browse", command=self.browse_folder).grid(row=0, column=2, padx=5)

        # Dry-run checkbox
        tk.Checkbutton(root, text="Dry Run (no changes)", variable=self.dry_run).grid(
            row=1, column=1, sticky="w", padx=5
        )

        # Run button
        tk.Button(root, text="Organize", command=self.run_organizer).grid(
            row=2, column=1, pady=10
        )

        # Output box
        self.output_box = tk.Text(root, height=15, width=70)
        self.output_box.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.selected_path.set(folder_selected)

    def run_organizer(self):
        folder = self.selected_path.get()

        if not folder:
            messagebox.showerror("Error", "Please select a folder.")
            return

        base_path = Path(folder)
        files = scan_folder(base_path)

        total_files = 0
        moved_files = 0
        skipped_files = 0
        category_count = defaultdict(int)

        self.output_box.delete("1.0", tk.END)

        for file in files:
            total_files += 1
            folder_name = decide_folder(file)

            if folder_name is None:
                skipped_files += 1
                continue

            category_count[folder_name] += 1
            destination_folder = base_path / folder_name

            if self.dry_run.get():
                self.output_box.insert(tk.END, f"[DRY RUN] {file.name} -> {destination_folder}\n")
            else:
                move_file(file, destination_folder)
                moved_files += 1
                self.output_box.insert(tk.END, f"Moved {file.name}\n")

        # Summary
        self.output_box.insert(tk.END, "\nSummary\n")
        self.output_box.insert(tk.END, "-" * 30 + "\n")
        self.output_box.insert(tk.END, f"Files processed: {total_files}\n")
        self.output_box.insert(tk.END, f"Files moved: {moved_files}\n")
        self.output_box.insert(tk.END, f"Files skipped: {skipped_files}\n\n")

        self.output_box.insert(tk.END, "By category:\n")
        for category, count in category_count.items():
            self.output_box.insert(tk.END, f"  {category}: {count}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()