# File Organizer (Python)

A lightweight CLI tool to automatically organize messy directories (such as your `Downloads` folder) into clean, categorized subfolders by file type.

## Features

- **Automatic Categorization**: Sorts files into dedicated folders (`Images`, `Videos`, `Audio`, `Documents`, `PDF`, `Spreadsheets`, `Presentations`, `Archives`, `Code`, `Applications`, and `Others`).
- **Conflict Safe**: If a file with the same name already exists in the destination, it is renamed automatically (`file (1).ext`) without overwriting.
- **Dry-Run Mode**: Preview where files will be moved before any changes are made.
- **Recursive Sorting**: Optionally scan and organize nested subdirectories.
- **Summary Report**: Prints total counts and per-category stats after completion.

## Usage

### Basic Run
Organizes the default `Downloads` folder:
```bash
python main.py
```

### Custom Directory
Provide the path to any directory:
```bash
python main.py "C:\Users\username\Desktop\messy_folder"
```

### Preview Changes (Dry Run)
Check which files would be moved without modifying anything on disk:
```bash
python main.py "path/to/folder" --dry-run
```

### Recursive Organization
Include nested subdirectories:
```bash
python main.py "path/to/folder" --recursive
```
