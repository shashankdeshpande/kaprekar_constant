def kaprekar_routine(n):
    """
        Input  : 4 digit Integer Number
                 1, 2, 3 digit numbers are also valid, we will pad those with leading zeros.
                 Allowed range - [1-9999]

        Output : Kaprekar routine steps to reach constant 0/6174.
    """
    n = int(n)
    check_range(n)
    routine = []
    prev_n = 0
    while n != prev_n:
        prev_n = n
        n_str = pad_leading_zeros(n)
        asc = int("".join(sorted(n_str)))
        desc = int("".join(sorted(n_str, reverse=True)))
        n = desc - asc
        if n != prev_n:
            routine.append(f"{desc} - {asc} = {n}")
    return len(routine), routine

def pad_leading_zeros(n):
    """
        This function will pad 1,2,3 digit numbers with leading zeros and convert to string.
    """
    n_str = str(n).zfill(4)
    return n_str

def check_range(n):
    """
        To check if number is in allowed range [1-9999]
    """
    if n not in range(1,10000):
        error_msg = "Number not in range [1-9999]"
        raise Exception(error_msg)

def get_steps(n):
    """
        Input  : 4 digit number
        Output : Kaprekar routine steps to reach constant 0/6174.
    """
    _, steps = kaprekar_routine(n)
    return steps

def step_count(n):
    """
        Input  : 4 digit number
        Output : No. of iterations to reach constant 0/6174.
    """
    count, _ = kaprekar_routine(n)
    return count
