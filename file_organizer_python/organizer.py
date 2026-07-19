from pathlib import Path
import shutil

from file_types import FILE_TYPES


def organize(folder_path):

    folder = Path(folder_path)

    for item in folder.iterdir():

        if not item.is_file():
            continue

        extension = item.suffix.lower()

        if extension not in FILE_TYPES:
            continue

        category = FILE_TYPES[extension]

        destination = folder / category

        destination.mkdir(exist_ok=True)

        shutil.move(item, destination / item.name)