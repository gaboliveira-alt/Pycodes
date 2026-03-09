from typing import Final

name: str = "Gabriel Oliveira Pinto"
x: int = 123
y: float = 23.33
c: complex = 2 + 4j
is_valid: bool = True
data: bytes = b"biubububu"

EXAMPLE_CONST = "valor ai"

EXAMPLE_CONST = 'm'


numbers_list: list[int] = [1, 2, 3, 4, 5]
two_values_tuple: tuple[str, int] = ("qualquer", 123)
multiple_values_tuple: tuple[str, ...] = ("a", "b")
example_set: set[int] = {1, 2, 3, 4}
imutable_set: frozenset[int] = frozenset([2, 4, 6])
example_dict: dict[str, str] = {"key": "value", "key1": "value1"}
numbers: range = range(20)


example_none: None
other_thing: object = 123
example_type: type = int


TWO_CONST = Final[list[str]] = ["a", "b"]
three_const: Final[dict[str, int]] = {"key": 123}
