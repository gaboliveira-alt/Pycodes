from typing import Protocol

from utils import sep_print


class SupportsRead(Protocol):
    path: str

    def read(self) -> object: ...


class JsonManager:
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> dict[str, object]: ...


class CsvManager:
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> str: ...


def load_data(reader: SupportsRead) -> object:
    reader.read()


if __name__ == "__main__":
    sep_print()


    json_data = load_data(JsonManager("file.json"))
    csv_data = load_data(CsvManager("file.csv"))


    sep_print()
