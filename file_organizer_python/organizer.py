from pathlib import Path
import shutil

from file_types import FILE_TYPES


def organize(folder):

    for item in folder.iterdir():

        if item.is_file():

            extension = item.suffix.lower()

            if extension in FILE_TYPES:

                category = FILE_TYPES[extension]

                destination = folder / category

                destination.mkdir(exist_ok=True)

                shutil.move(item, destination / item.name)

        elif item.is_dir():

            organize(item)