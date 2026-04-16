
from collections.abc import Hashable, MutableMapping

from utils import cyan_print, sep_print


def invert_mapping[K, V: Hashable](
    mapping: MutableMapping[K, V]
    ) -> MutableMapping[V, K]:
    return {value: key for key, value in mapping.items()}

if __name__ == "__main__":
    sep_print()

    dict1 = {
        "a": 1,
        "b": 2,
        (1, 2): 3,
    }
    invert = invert_mapping(dict1)
    revert = invert_mapping(invert)

    cyan_print(dict1)
    cyan_print(invert)
    cyan_print(revert)

    sep_print()