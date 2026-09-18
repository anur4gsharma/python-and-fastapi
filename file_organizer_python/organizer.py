from pathlib import Path
import shutil
from collections import defaultdict
from file_types import FILE_TYPES

CATEGORY_FOLDERS = set(FILE_TYPES.values()) | {"Others"}


def _get_unique_destination(destination_dir: Path, filename: str) -> Path:
    target = destination_dir / filename
    if not target.exists():
        return target

    stem = Path(filename).stem
    suffix = Path(filename).suffix
    counter = 1
    while target.exists():
        target = destination_dir / f"{stem} ({counter}){suffix}"
        counter += 1
    return target


def organize(folder: Path, recursive: bool = False, dry_run: bool = False) -> dict:
    folder = Path(folder)
    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError(f"Directory not found: {folder}")

    stats = defaultdict(int)

    items = list(folder.iterdir())
    for item in items:
        if item.name.startswith("."):
            continue

        if item.is_file():
            extension = item.suffix.lower()
            category = FILE_TYPES.get(extension, "Others")
            dest_dir = folder / category

            dest_path = _get_unique_destination(dest_dir, item.name)

            if not dry_run:
                dest_dir.mkdir(exist_ok=True)
                shutil.move(item, dest_path)

            stats[category] += 1

        elif item.is_dir() and recursive:
            if item.name not in CATEGORY_FOLDERS:
                sub_stats = organize(item, recursive=True, dry_run=dry_run)
                for cat, count in sub_stats.items():
                    stats[cat] += count

    return dict(stats)