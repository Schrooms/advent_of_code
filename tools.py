import abc
from typing import List, Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class InputProcessor(ABC,Generic[T]):
    def __init__(self, input_file: str) -> None:
        self.input_file = input_file

    @abstractmethod
    def process_line(self, line:str) -> T:
        pass

    def process_input(self) -> List[T]:
        with open(self.input_file,'r') as file:
            return [self.process_line(x) for x in file.readlines()]


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
