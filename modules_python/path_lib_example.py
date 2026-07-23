from pathlib import Path
from shutil import rmtree

path_project = Path()
print(path_project.absolute())

path_file = Path(__file__)
print(path_file)

print(path_file.parent)

folder_ideas = path_file.parent / "ideas_folder"
print(folder_ideas)

file_example = Path.home() / "OneDrive" / "Documentos" / "file.txt"
# file_example.touch()
# file_example.write_text("Fabricio é conhecido como Diego Merendona\n")
# print(file_example.read_text())
# file_example.unlink()

# with file_example.open("a+") as file_exe:
#     file_exe.write("Olá mundo\n")
#     file_exe.write("Receba\n")

# print(file_example.read_text())


path_file_2 = Path.home() / "OneDrive" / "Documentos" / "Python_test"
path_file_2.mkdir(exist_ok=True)
sub_folder = path_file_2 / "sub_folder"
sub_folder.mkdir(exist_ok=True)


other_file = sub_folder / "file_test.txt"
other_file.touch()
other_file.write_text("Olá")

one_more_file = path_file_2 / "file_test2.txt"
one_more_file.touch()
one_more_file.write_text("Hey mike")

path_file_2.rmdir()

new_files = path_file_2 / "files"
new_files.mkdir(exist_ok=True)

for i in range(1, 10):
    file_example_1 = new_files / f"file{i}.txt"


    if file_example_1.exists():
        file_example_1.unlink()
    else:
        file_example_1.touch()


    with file_example_1.open("a+") as new_file:
        new_file.write("Olá receba\n")
        new_file.write(f"files{i}.txt")


def rmtree_function(root: Path, remove_tree=True) -> None:
    for new_file in root.glob("*"):
        if new_file.is_dir():
            print("DIR: ", new_file)
            rmtree(new_file, ignore_errors=False)
            new_file.rmdir()
        else:
            print("FILE: ", new_file)
            new_file.unlink()

    if remove_tree:
        root.rmdir()

rmtree_function(path_file_2)
