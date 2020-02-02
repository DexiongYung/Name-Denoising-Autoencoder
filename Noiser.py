import math
from random import randint

from Convert import ALL_CHARS, MAX_LENGTH, LETTERS_COUNT


def noise_name(x: str):
    noise_type = randint(0, 2)

    if noise_type == 0:
        return add_chars(x)
    elif noise_type == 1:
        return switch_chars(x)
    else:
        return remove_chars(x)


def add_chars(x: str, max_add: int = 3):
    if max_add + len(x) > MAX_LENGTH:
        raise Exception(f"{max_add + len(x)} is greater than max length:{MAX_LENGTH}")

    ret = x
    num_to_add = randint(0, max_add)

    for i in range(num_to_add):
        random_char = ALL_CHARS[randint(0, LETTERS_COUNT - 1)]
        pos = randint(0, len(ret) - 1)
        ret = "".join((ret[:pos], random_char, ret[pos:]))

    return ret


def switch_chars(x: str):
    ret = x
    num_to_switch = randint(0, math.floor(len(x) / 2))

    for i in range(num_to_switch):
        random_char = ALL_CHARS[randint(0, LETTERS_COUNT - 1)]
        pos = randint(0, len(ret) - 1)
        ret = "".join((ret[:pos], random_char, ret[pos + 1:]))

    return ret


def remove_chars(x: str):
    ret = x
    num_to_remove = randint(0, math.floor(len(x) / 2))

    for i in range(num_to_remove):
        pos = randint(0, len(ret) - 1)
        ret = "".join((ret[:pos], ret[pos + 1:]))

    return ret