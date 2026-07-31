import os
import shutil
from pathlib import Path
from zipfile import ZipFile

HOME_PATH = Path(__file__).parent
ZIP_DIR_PATH = HOME_PATH / "lesson183_dir_zip"
COMPACT_PATH = HOME_PATH / "lesson183_compact.zip"
DESCOMPACT_PATH = HOME_PATH / "lesson183_descompact"

shutil.rmtree(ZIP_DIR_PATH, ignore_errors=True)
Path.unlink(COMPACT_PATH, missing_ok=True)
shutil.rmtree(str(COMPACT_PATH).replace(".zip", ""), ignore_errors=True)
shutil.rmtree(COMPACT_PATH, ignore_errors=True)

ZIP_DIR_PATH.mkdir(exist_ok=True)

def create_files(quantity_files: int, zip_dir: Path) -> None:
    for i in range(quantity_files):
        text_file = f"arquivo_{i}"
        with open(zip_dir / f"{text_file}.txt", "w") as file:
            file.write(text_file)

create_files(10, ZIP_DIR_PATH)

with ZipFile(COMPACT_PATH, "w") as file_zip:
    for root, dirs_, files in os.walk(ZIP_DIR_PATH):
        for file in files:
            file_zip.write(os.path.join(root, file), file)

with ZipFile(COMPACT_PATH) as file_zip:
    for file in file_zip.namelist():
        print(file)

with ZipFile(COMPACT_PATH) as file_zip:
    file_zip.extractall()
