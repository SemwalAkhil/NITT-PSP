# directory find all file display name and size
from pathlib import Path


def format_size(num_bytes: int) -> str:
    """Convert bytes into a human-readable string."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if num_bytes < 1024:
            return f"{num_bytes:.2f} {unit}" if unit != "B" else f"{num_bytes} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.2f} PB"


def list_files_with_sizes(root_dir, follow_symlinks: bool = False) -> None:
    root = Path(root_dir)

    if not root.exists():
        print(f"Error: '{root}' does not exist.")
        return
    if not root.is_dir():
        print(f"Error: '{root}' is not a directory.")
        return

    total_size = 0
    file_count = 0

    # rglob("*") recursively traverses all subdirectories and files
    for entry in root.rglob("*"):
        try:
            # Skip symlinks unless explicitly requested
            if entry.is_symlink() and not follow_symlinks:
                continue

            if entry.is_file():
                size = entry.stat().st_size
                total_size += size
                file_count += 1
                print(f"{format_size(size):>10}  |  {entry}")
        except PermissionError:
            print(f"{'SKIPPED':>10}  |  {entry} (Permission denied)")
        except OSError as exc:
            print(f"{'ERROR':>10}  |  {entry} ({exc})")

    print("-" * 60)
    print(f"Total files: {file_count}")
    print(f"Total size : {format_size(total_size)} ({total_size:,} bytes)")


if __name__ == "__main__":
    target_folder = input("Enter folder path (or press Enter for current folder): ").strip()
    list_files_with_sizes(target_folder or ".")