
def multiple_args[A, B, C](a: A, b: B, c: C) -> A | B | C: ...

ma = multiple_args(1, "dois", [3])
reveal_type(ma)

def add_number[T: float](a: T, b: T) -> T: ...

number = add_number(1, True)

def only_one_type_please[T: (str, bytes)](a: T, b: T) -> T: ...

anb = only_one_type_please("Abc", b"Abc")
ans = only_one_type_please("Abc", "Abc")

def default[T = str | int](a: T | None = None, b: T | None = None) -> T: ...

anb = default()
