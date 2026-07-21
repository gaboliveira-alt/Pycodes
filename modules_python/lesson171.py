import math
import os
from itertools import count


def format_size(bytes_in_size: int, base: int = 1000) -> str:
    if bytes_in_size <= 0:
        return "0B"

    sizes_abbreviation: tuple[str, ...] = "B", "KB", "MB", "GB", "TB", "PB"
    size_index_abbreviation: int = int(math.log(bytes_in_size, base))


    potential: int = base ** size_index_abbreviation
    final_size = bytes_in_size / potential


    size_abbreviation = sizes_abbreviation[size_index_abbreviation]
    return f"{final_size:.2f} {size_abbreviation}"

print(format_size(1000000000))
print(format_size(1000000))
print(format_size(10000))

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
        size_files = os.path.getsize(path_complete)
        print(" ", loop_counter, "FILE: ", file_, format_size(size_files))
