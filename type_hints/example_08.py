
type C[T] = tuple[T, ...]

integers: C[int] = 1, 0, 1, 0
booleans: C[bool] = True, False, True, False

# booleans = integers # Não funciona  # noqa: ERA001
integers = booleans

def wants_integer(integers: tuple[int, ...]) -> None:
    ...

wants_integer(booleans)
