from pathlib import Path
import shutil


FILE_CATEGORIES = {
    "Images": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".svg", ".webp", ".ico"
    },

    "Videos": {
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm"
    },

    "Audio": {
        ".mp3", ".wav", ".aac", ".flac",
        ".ogg", ".m4a"
    },

    "Documents": {
        ".pdf", ".doc", ".docx", ".txt",
        ".rtf", ".odt"
    },

    "Spreadsheets": {
        ".xls", ".xlsx", ".csv", ".ods"
    },

    "Presentations": {
        ".ppt", ".pptx", ".odp"
    },

    "Archives": {
        ".zip", ".rar", ".7z", ".tar",
        ".gz", ".bz2"
    },

    "Code": {
        ".py", ".java", ".c", ".cpp", ".h",
        ".js", ".html", ".css", ".sql",
        ".json", ".xml"
    },

    "Executables": {
        ".exe", ".msi", ".apk", ".deb"
    }
}


def get_category(file_path):
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    """
    Prevents overwriting an existing file.
    Example:
        report.pdf
        report_1.pdf
        report_2.pdf
    """

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        new_path = destination.parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def organize_folder(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.exists():
        print("❌ Folder does not exist.")
        return

    if not folder.is_dir():
        print("❌ The provided path is not a folder.")
        return

    organized_count = 0

    for file in folder.iterdir():

        # Ignore folders
        if not file.is_file():
            continue

        # Ignore this Python script
        if file.name == Path(__file__).name:
            continue

        category = get_category(file)

        category_folder = folder / category
        category_folder.mkdir(exist_ok=True)

        destination = category_folder / file.name
        destination = get_unique_path(destination)

        try:
            shutil.move(str(file), str(destination))

            print(
                f"✓ {file.name} → "
                f"{category}/{destination.name}"
            )

            organized_count += 1

        except PermissionError:
            print(f"⚠ Permission denied: {file.name}")

        except OSError as error:
            print(f"⚠ Could not move {file.name}: {error}")

    print()
    print(f"✅ Organized {organized_count} file(s).")


def main():
    print("=" * 45)
    print("        PYTHON FILE ORGANIZER")
    print("=" * 45)

    folder_path = input(
        "\nEnter the folder path to organize: "
    ).strip()

    if not folder_path:
        print("❌ No folder path provided.")
        return

    organize_folder(folder_path)


if __name__ == "__main__":
    main()
