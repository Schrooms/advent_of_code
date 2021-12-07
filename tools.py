import abc
from typing import List, Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class InputProcessor(ABC,Generic[T]):
    def __init__(self, input_file: str) -> None:
        self.input_file = input_file
        self.stop = False

    @abstractmethod
    def process_line(self, line:str) -> T:
        pass

    def process_input(self) -> List[T]:
        result: List[T] = []
        with open(self.input_file,'r') as file:
            for x in file:
                if self.stop:
                    return result
                result.append(self.process_line(x))
        return result

class CommaInputProcessor(InputProcessor[List[int]]):
    def process_line(self, line: str) -> List[int]:
        return [int(n) for n in line.split(',')]

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
