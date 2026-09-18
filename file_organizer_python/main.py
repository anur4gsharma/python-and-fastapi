import argparse
from pathlib import Path
from organizer import organize


def parse_args():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by file type."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default="Downloads",
        help="Path to the directory to organize (default: Downloads)",
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Organize subdirectories recursively",
    )
    parser.add_argument(
        "-d", "--dry-run",
        action="store_true",
        help="Preview file movements without moving files",
    )
    return parser.parse_args()


def print_summary(stats: dict, dry_run: bool):
    if not stats:
        print("No files found to organize.")
        return

    action_label = "[DRY-RUN] Files to organize" if dry_run else "Files organized"
    total = sum(stats.values())
    print(f"\n{action_label} ({total} total):")
    for category, count in sorted(stats.items()):
        print(f"  • {category}: {count}")


def main():
    args = parse_args()
    target_folder = Path(args.folder)

    if not target_folder.exists() or not target_folder.is_dir():
        print(f"Error: Directory '{target_folder}' does not exist.")
        return

    print(f"Processing directory: {target_folder.resolve()}")
    stats = organize(target_folder, recursive=args.recursive, dry_run=args.dry_run)
    print_summary(stats, dry_run=args.dry_run)


if __name__ == "__main__":
    main()