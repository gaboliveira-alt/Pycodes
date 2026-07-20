import os

path_notebook: str = os.path.join(
    "\\Users", "kylor", "OneDrive", "Documentos", "Passaporte"
    )

for folder in os.listdir(path_notebook):
    path_complete: str = os.path.join(path_notebook, folder)
    print(path_complete)

    if not os.path.isdir(path_complete):
        continue

    for files in os.listdir(path_complete):
        print(files)
