from dataclasses import dataclass
from typing import Annotated, get_args, get_origin, get_type_hints

from utils import cyan_print, sep_print  # pyright: ignore[reportMissingTypeStubs]

p = cyan_print
s = sep_print


def simple_annotated(
    annotated: Annotated[object, "I have annotation"]
    ) -> Annotated[object, "I have annotation"]:
    return annotated

s()

type_hints = get_type_hints(simple_annotated, include_extras=True)
type_args = get_args(type_hints["annotated"])
type_return = get_args(type_hints["return"])
type_origin = get_origin(type_hints["annotated"])

p(f"{type_hints=!r}")
p(f"{type_args=!r}")
p(f"{type_return=!r}")
p(f"{type_origin=!r}")

s()

@dataclass
class Person:
    name: Annotated[str, "O nome completo da pessoa"]
    age: Annotated[int | None, "A idade"] = None


def print_annotated[T: object](obj: T) -> T:
    obj_class = obj.__class__
    obj_name = getattr(obj, "__name__", "")

    if not obj_name:
        obj_name = obj_class.__name__

    hints = get_type_hints(obj, include_extras=True)

    if not hints:
        return obj

    p("🧐 Verificando a tipagem de:", obj_name)
    p(f"🎲 Objeto Real: {obj!r}")

    for key, value in hints.items():
        val = getattr(obj, key, "NO VALUE")

        type_, *metadata = get_args(value)

        p(
            f"🔑 Key={key!r} 📋 Type={type_!r} 📝 Meta={metadata!r} Value={val!r}",
        )

    p()
    s()

    return obj


if __name__ == "__main__":
    print_annotated(simple_annotated)

    person = Person("Gabriel", 20)
    print_annotated(person)

    print_annotated(Person)
