import re
from pathlib import Path


def search_in_current_dir() -> list[Path]:
    directory = Path(__file__).parent
    print(directory)
    files = []
    for file in directory.iterdir():  
        if re.search(pattern=r'^student.*csv', string=file.name):
            files.append(file.name)
    if not files:
        raise FileNotFoundError(
            'Укажите путь к файлам в параметре --file.',
        )
    return files
