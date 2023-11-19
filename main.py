import os

from utils import parse_xml


def copy_folder_structure(source_dir: str, destination_dir: str) -> None:
    """Создает исходную структуру папок в новой папке."""
    for root, _, files in os.walk(source_dir):
        relative_path = os.path.relpath(root, source_dir)
        new_dir = os.path.join(destination_dir, relative_path)
        os.makedirs(new_dir, exist_ok=True)
        for file in files:
            filename, extension = os.path.splitext(file)
            if extension.lower() == '.xml':
                source_file = os.path.join(root, file)
                destination_file = os.path.join(new_dir, f'{filename}.txt')
                parse_xml(source_file, destination_file)


if __name__ == '__main__':
    source_dir = 'data'
    destination_dir = 'output'
    copy_folder_structure(source_dir, destination_dir)
