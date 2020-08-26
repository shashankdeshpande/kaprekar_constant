def get_steps(num):
    num = int(num)
    steps = []
    prev_num = 0
    if num not in range(1,10000):
        error_msg = "Number not in range [1-9999]"
        raise Exception(error_msg)

    while num != prev_num:
        prev_num = num
        str_num = str(num).zfill(4)
        asc = int("".join(sorted(str_num)))
        desc = int("".join(sorted(str_num, reverse=True)))
        num = desc - asc
        if num != prev_num:
            steps.append(f"{desc} - {asc} = {num}")
    return steps

def step_count(num):
    steps = get_steps(num)
    return len(steps)
