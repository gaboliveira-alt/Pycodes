from typing import NotRequired, ReadOnly, Required, TypedDict

from utils import cyan_print, sep_print


class MyDict(TypedDict, total=True):
    id: int
    name: str
    email: Required[str]
    gender: NotRequired[str]
    birth: Required[ReadOnly[str | None]]


if __name__ == "__main__":
    sep_print()

    my_dict: MyDict = {
        "id": 1,
        "name": "Otávio Miranda",
        "email": "email@email.com",
        "gender": "masculino",
        "birth": None,
    }


    cyan_print(my_dict["id"])
    cyan_print(my_dict["birth"])
    cyan_print(my_dict["gender"])

    sep_print()


    my_dict_2 = MyDict(id=123, name="Gabriel", email="email@email.com", birth=None)

    cyan_print(my_dict_2["id"])

    sep_print()
