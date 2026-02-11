
from collections.abc import Sequence
from typing import Iterator


class MyList(Sequence):
    def __init__(self) -> None:
        self._data = {}
        self._index = 0
        self._next_index = 0
        
    def append(self, *values) -> None:
        for value in values:
            self._data[self._index] = value
            self._index += 1
    
    def __len__(self) -> int:
        return self._index
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        
        value = self._data[self._next_index]
        self._next_index += 1
        return value
        