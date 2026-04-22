import json
from collections.abc import Callable
from pathlib import Path
from typing import Protocol

from utils import cyan_print, sep_print


class SupportsRead[Out](Protocol):
    def read(self) -> Out: ...


class SupportsWrite[In](Protocol):
    def write(self, data: In) -> None: ...


class SupportsReadWrite[In, Out](SupportsRead[Out], SupportsWrite[In], Protocol): ...


class FileDataManager[Out](SupportsReadWrite[str, Out]):
    def __init__(self, path: Path, parse: Callable[[str], Out]) -> None:
        self.path = path
        self.parse = parse

    def read(self) -> Out:
        with self.path.open("r", encoding="utf-8") as file:
            data = file.read()

        return self.parse(data)

    def write(self, data: str) -> None:
        with self.path.open("w", encoding="utf-8") as file:
            file.write(data)


def manage_file[Out](file_manager: SupportsReadWrite[str, Out], data: str) -> Out:
    file_manager.write(data)
    return file_manager.read()


if __name__ == "__main__":
    sep_print()

    file_manager = FileDataManager(Path(".\\type_hints\\example_24a.txt"), int)
    data = manage_file(file_manager, "123")
    cyan_print(data, type(data))


    file_manager = FileDataManager[list[int]](
        Path(".\\type_hints\\example_24a.txt"), json.loads
        )
    data = manage_file(file_manager, "[1, 2, 3, 4]")
    cyan_print(data)


    file_manager = FileDataManager[dict[str, int]](
        Path(".\\type_hints\\example_24a.txt"),
        json.loads
        )
    data = manage_file(file_manager, "{'a': 12, 'b': 14}")
    cyan_print(data)
