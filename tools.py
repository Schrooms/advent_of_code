from typing import List

def get_numbers(file_name: str) -> List[int]:
    with open(file_name,'r') as file:
        return [int(x) for x in file.readlines()]


def get_increases(number: List[int]) -> int:
    increaded: int = 0
    num_iter = iter(number)
    first_num = next(num_iter)
    while True:
        try:
            next_num = next(num_iter)
            increaded += 1 if next_num > first_num else 0
            first_num = next_num
        except StopIteration:
            break
    return increaded
