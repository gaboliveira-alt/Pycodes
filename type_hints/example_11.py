
from collections.abc import Iterator, Sequence
from typing import overload, override

from utils import cyan_print, sep_print  # pyright: ignore[reportMissingTypeStubs]

type T = str

class ReadOnlySequence(Sequence[T]):
    def __init__(self, *args: T) -> None:
        self._data: dict[int, T] = {}
        self._index = 0
        self._next_index = 0

        self._add_initial_values(*args)

    def _add_initial_values(self, *args: T) -> None:
        for arg in args:
            self._data[self._index] = arg
            self._index += 1

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    @override
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, int):
            return self._data[index]

        values = list(self._data.values())[index]
        return ReadOnlySequence(*values)

    @override
    def __len__(self) -> int:
        return self._index

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        if not self._data or self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1

        return value

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        attrs = ", ".join([f"{value!r}" for value in self._data.values()])
        return f"{cls_name}{attrs}"


if __name__ == "__main__":
    sequence_01 = ReadOnlySequence("a", "b", "c")
    sep_print()

    cyan_print(sequence_01)
    cyan_print(sequence_01[0])
    cyan_print(sequence_01[1])
    cyan_print(sequence_01[0:2])
    cyan_print(list(reversed(sequence_01)))
    cyan_print(len(sequence_01))

    print("for 1")
    for value in sequence_01:
        print(value)

    print("for 2")
    for value in sequence_01:
        print(value)
