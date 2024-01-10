from pathlib import Path
import shutil
import argparse
import os


def copy_file(file: Path, target_dir: Path):
    file = file.absolute()

    target_file = target_dir.absolute() / file.suffix.strip('.') / file.name

    if not target_file.parent.exists():
        os.makedirs(target_file.parent)

    shutil.copy(file, target_file)
    print(f'copy {file} to {target_file}')


def copy_tree(source_dir: Path, target_dir: Path) -> None:
    if source_dir.is_dir():
        for child in source_dir.iterdir():
            copy_tree(child, target_dir)
    else:
        copy_file(source_dir, target_dir)


def parse_directories() -> tuple[Path, Path]:
    parser = argparse.ArgumentParser()
    parser.add_argument('source_dir', help='Path to source directory')
    parser.add_argument('target_dir', nargs='?', help='Path to target directory', default='dist')
    args = parser.parse_args()
    return Path(args.source_dir), Path(args.target_dir)


def main():
    try:
        copy_tree(*parse_directories())
    except OSError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()