from typing import List
from tools import InputProcessor, get_increases

class IntLineProcessor(InputProcessor[int]):
    def process_line(self, line:str) -> int:
        return int(line)


def get_numbers_to_sum(numbers: List[int]) -> List[List[int]]:
    result:List[List[int]] = []
    for idx, _ in enumerate(numbers):
        if len(numbers[idx:idx+3]) < 3:
            break
        result.append(numbers[idx:idx+3])
    return result

if __name__ == '__main__':
    number_to_sum = get_numbers_to_sum(IntLineProcessor('01.txt').process_input())
    print(get_increases([sum(numbers) for numbers in number_to_sum]))
