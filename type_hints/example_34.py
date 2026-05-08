from dataclasses import dataclass
from typing import NewType

from utils import cyan_print, sep_print


@dataclass
class PostId:
    value: str


StrPostId = NewType("StrPostId", PostId)

def get_post(post_id: StrPostId) -> StrPostId:
    return post_id


if __name__ == "__main__":
    sep_print()

    post_id = PostId("abcde")
    str_post_id = StrPostId(post_id)

    this_is_a_string = "ABC"
    unexpected = StrPostId(this_is_a_string)

    cyan_print(f"{post_id=}", type(post_id))
    cyan_print(f"{str_post_id=}", type(str_post_id))
    cyan_print(f"{unexpected=}", type(unexpected))

    sep_print()
