from typing import List

def get_numbers() -> List[int]:
    with open('01.txt','r') as file:
        return [int(x) for x in file.readlines()]

if __name__ == '__main__':
    increaded: int = 0
    num_iter = iter(get_numbers())
    first_num = next(num_iter)
    while True:
        try:
            next_num = next(num_iter)
            increaded += 1 if next_num > first_num else 0
            first_num = next_num
        except StopIteration:
            break
    print(increaded)
    