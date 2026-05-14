import json
from pathlib import Path
from typing import Any, TypedDict, TypeGuard, cast

from utils import cyan_print, red_print, sep_print


class UserDict(TypedDict):
    firstname: str
    lastname: str
    age: int


def is_valid_dict(item: object) -> TypeGuard[UserDict]:
    if not isinstance(item, dict):
        return False

    item = cast("dict[Any, Any]", item)

    if not isinstance(item.get("firstname"), str):
        return False

    if not isinstance(item.get("lastname"), str):
        return False

    return isinstance(item.get("age"), int)


if __name__ == "__main__":
    sep_print()

    input_file = Path("example_37.json").resolve()
    with input_file.open("r", enconding="utf-8") as file:
        user_data = json.load(file)

    for user in user_data:
        if is_valid_dict(user):
            cyan_print("VALID USER")
            cyan_print(f"{user['firstname']}, {user['lastname']}, {user['age']}")
        else:
            red_print("INVALID USER")
            red_print(user)
