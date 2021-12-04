from __future__ import annotations
from typing import Generator, List, TextIO
from tools import InputProcessor
from dataclasses import dataclass

class WonException(Exception):
    def __init__(self, board: Board, called_number: int) -> None:
       self.board = board
       self.called_number = called_number


@dataclass
class CheckedValue:
    checked: bool
    value: int
    def __repr__(self) -> str:
        return f"<CV {self.value}>"

@dataclass
class Board:
    rows: List[List[CheckedValue]]
    def __repr__(self) -> str:
        return f"<BOARD {self.rows}>"

    def ceck_value(self, value: int) -> None:
        for row in self.rows:
            for val in row:
                if val.value == value:
                    val.checked = True
        self.has_won(value)
    
    def has_won(self, value:int) -> None:
        horizontal = self._has_won_horizontal()
        vertical = self._has_won_vertical()
        if horizontal or vertical:
            raise WonException(self, value)
    
    def _has_won_horizontal(self) -> bool:
        for row in self.rows:
            if len([x for x in row if x.checked]) == 5:
                return True
        return False
    
    def _has_won_vertical(self):
        for i in range(5):
            if len([row[i] for row in self.rows if row[i].checked]) == 5:
                return True
        return False
    
    def get_unchecked_numbers(self) -> int:
        un_checked = [x.value for row in self.rows for x in row if not x.checked]
        return(sum(un_checked))

class HeaderProcessor(InputProcessor[List[int]]):
    def process_line(self, line:str) -> List[int]:
        self.stop = True
        return [int(x) for x in line.strip('\n').split(',')]

@dataclass
class BoardProcessor():
    file_name: str

    def process_input(self) -> List[Board]:
        boards: List[Board] = []
        with open(self.file_name, 'r') as file:
            # skip first 2 line
            file.readline()
            file.readline()
           
            return [i for i in self.get_boards(file)]

    def get_boards(self, file: TextIO) -> Generator[Board, None, None]:
        rows: List[List[CheckedValue]] = []
        for line in file:
            if line == '\n':
                yield Board(rows)
                rows =[]
                continue
            rows.append([ CheckedValue(False, int(x)) for x in line.split()])
        yield Board(rows)

if __name__ == '__main__':
    numbers = HeaderProcessor('04.txt').process_input()[0]
    boards = BoardProcessor('04.txt').process_input()

    try:
        for num in numbers:
            for b in boards:
                b.ceck_value(num)
    except WonException as ex:
        print(ex.board.get_unchecked_numbers() * ex.called_number)
