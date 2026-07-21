import os
from itertools import count

path_notebook: str = os.path.join(
    "\\Users", "kylor", "OneDrive", "Documentos", "Artigos_China"
    )

counter = count()

for root, dirs, files in os.walk(path_notebook):
    loop_counter = next(counter)
    print(loop_counter, "Pasta Atual: ", root)

    for dir_ in dirs:
        print(" ", loop_counter, "Dir: ", dir_)

    for file_ in files:
        path_complete = os.path.join(root, file_)
        print(" ", loop_counter, "FILE: ", file_)
