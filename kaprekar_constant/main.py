#!/usr/local/bin/python3

from .object import Kaprekar

def kaprekar_routine(n: int) -> object:
    """
        Input  : 4 digit Integer Number
                 1, 2, 3 digit numbers are also valid, we will pad those with leading zeros.
                 Allowed range - [1-9999]

        Output : Object containing constant, steps & step count
    """
    n = int(n)
    check_range(n)
    steps = []
    prev_n = 0
    while n != prev_n:
        prev_n = n
        n_str = pad_leading_zeros(n)
        asc = int("".join(sorted(n_str)))
        desc = int("".join(sorted(n_str, reverse=True)))
        n = desc - asc
        if n != prev_n:
            steps.append(f"{pad_leading_zeros(desc)} - {pad_leading_zeros(asc)} = {pad_leading_zeros(n)}")

    constant = n
    step_count = len(steps)
    kc_obj = Kaprekar(constant, steps, step_count)
    return kc_obj

def pad_leading_zeros(n: int) -> str:
    """
        This function will pad 1,2,3 digit numbers with leading zeros and convert to string.
    """
    n_str = str(n).zfill(4)
    return n_str

def check_range(n: int) -> None:
    """
        To check if number is in allowed range [1-9999]
    """
    if n not in range(1,10000):
        error_msg = "Number not in range [1-9999]"
        raise Exception(error_msg)
