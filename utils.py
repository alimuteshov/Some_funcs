from typing import Dict


def sum_count(num: int) -> int:
    cnt = 0
    for digit in str(num):
        cnt += int(digit)
    return cnt


def count_groups_num(n_customers: int) -> Dict[int, int]:
    groups_dct = {}

    for i in range(n_customers):
        counted = sum_count(i)
        if counted in groups_dct:
            groups_dct[counted] += 1
        else:
            groups_dct[counted] = 1

    return groups_dct


def count_groups_num_mod(n_customers: int, n_first_id: int = 0) -> Dict[int, int]:
    groups_dct = {}

    for i in range(n_first_id, n_first_id + n_customers):
        counted = sum_count(i)
        if counted in groups_dct:
            groups_dct[counted] += 1
        else:
            groups_dct[counted] = 1

    return groups_dct
