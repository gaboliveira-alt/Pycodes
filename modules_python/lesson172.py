import os
import shutil

HOME = os.path.expanduser("~")
DOCUMENTS = os.path.join(HOME, "OneDrive", "Documentos")
ORIGINAL_FOLDER = os.path.join(DOCUMENTS, "Artigos_China")
NEW_FOLDER = os.path.join(DOCUMENTS, "Artigos_Copia")

os.makedirs(NEW_FOLDER, exist_ok=True)

for root, dirs, files in os.walk(ORIGINAL_FOLDER):
    for dir_ in dirs:
        new_directory_path = os.path.join(
            root.replace(ORIGINAL_FOLDER, NEW_FOLDER), dir_
        )
        os.makedirs(new_directory_path, exist_ok=True)

    for file in files:
        path_file = os.path.join(root, file)
        new_file_path = os.path.join(
            root.replace(ORIGINAL_FOLDER, NEW_FOLDER), file
        )
        shutil.copy(path_file, new_file_path)
