from pathlib import Path

def get_directory(filename):
    path = Path(filename)
    while path.is_file():
        path = path.parent
    return path

