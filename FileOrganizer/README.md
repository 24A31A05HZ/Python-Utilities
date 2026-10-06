# 📁 File Organizer

A Python utility that automatically organizes files into folders based on their file type.

## ✨ Features

* Organizes files by extension
* Automatically creates required folders
* Supports images, videos, audio, documents, archives, code and more
* Places unknown file types into an `Others` folder
* Prevents files from being overwritten
* Uses Python's built-in `pathlib` and `shutil` modules
* No external libraries required

## 📂 Example

Before:

```text
Downloads/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── movie.mp4
├── project.py
└── archive.zip
```

After:

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
├── Code/
│   └── project.py
└── Archives/
    └── archive.zip
```

## 🚀 How to Run

Run the following command:

```bash
python file_organizer.py
```

Enter the path of the folder you want to organize.

## 🛠️ Technologies

* Python
* pathlib
* shutil

## 📚 Concepts Practiced

* Functions
* Dictionaries
* Sets
* Loops
* Conditional statements
* Exception handling
* File handling
* Path manipulation
* Directory creation
* File movement

## ⚠️ Note

Use this utility on a folder where you understand what files are being moved. The program reorganizes files by moving them into subfolders.
