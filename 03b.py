from typing import List
from tools import InputProcessor


class BinaryProcessor(InputProcessor[str]):
    def process_line(self, line:str) -> str:
        return line.strip('\n')


def get_oxigen(numbers: List[str], pos: int=0) -> str:
    if len(numbers) == 1:
        return numbers[0]
    ones = [int(num[pos]) for num in numbers if num[pos]=='1']
    zeros =[int(num[pos]) for num in numbers if num[pos]=='0']
    if len(ones) >= len(zeros):
        new_list = [x for x in numbers if x[pos] == '1']
    else:
        new_list = [x for x in numbers if x[pos] == '0']
    return get_oxigen(new_list, pos=pos+1)

def get_scub_rate(numbers: List[str], pos: int=0) -> str:
    if len(numbers) == 1:
        return numbers[0]
    ones = [int(num[pos]) for num in numbers if num[pos]=='1']
    zeros =[int(num[pos]) for num in numbers if num[pos]=='0']
    if len(zeros) <= len(ones):
        new_list = [x for x in numbers if x[pos] == '0']
    else:
        new_list = [x for x in numbers if x[pos] == '1']
    return get_scub_rate(new_list, pos=pos+1)

if __name__ == '__main__':
    numbers = BinaryProcessor('03.txt').process_input()
    oxigen = get_oxigen(numbers)
    scrub = get_scub_rate(numbers)
    print(int(oxigen,2)* int(scrub,2))
