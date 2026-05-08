from typing import NewType

from utils import cyan_print, sep_print

UserId = NewType("UserId", int)
PostId = NewType("PostId", int)


def get_user(user_id: UserId) -> int:
    return user_id


def get_post(post_id: PostId) -> int:
    return post_id


if __name__ == "__main__":
    sep_print()

    user_id = UserId(42)
    post_id = PostId(2)

    user1 = get_user(user_id)
    post1 = get_post(post_id)

    # user2 = get_user(post_id)  # ❌ Type Checker Rejeita
    # post2 = get_post(user_id)  # ❌

    cyan_print(f"{user1=}", type(user1))
    cyan_print(f"{post1=}", type(post1))

    result_is_int = user_id * post_id
    cyan_print(f"{result_is_int=}", type(result_is_int))

    sep_print()
