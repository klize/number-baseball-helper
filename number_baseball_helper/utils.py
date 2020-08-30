from number_baseball_helper.case import Case


def generate_number_strings(ndigit: int = 4):
    for n in range(10 ** ndigit):
        number_str = f"{n:0{ndigit}d}"

        if len(set(number_str)) == ndigit:
            yield number_str


def check_case(number_str, guess_number_str, ndigit):
    npc_numbers_index = {n: i for i, n in enumerate(number_str)}
    guess_numbers_index = {n: i for i, n in enumerate(guess_number_str)}

    npc_numbers = set(number_str)
    guess_numbers = set(guess_number_str)

    common_numbers = npc_numbers & guess_numbers

    strike = 0
    ball = 0

    for n in common_numbers:
        if npc_numbers_index.get(n) == guess_numbers_index.get(n):
            strike += 1
        else:
            ball += 1

    return Case(strike, ball, ndigit)