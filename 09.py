from typing import List
from typing_extensions import Literal
from tools import InputProcessor

class IntProcessor(InputProcessor[List[int]]):
    def process_line(self, line: str) -> List[int]:
        return [int(x) for x in line.strip('\n')]

map = IntProcessor('09.txt').process_input()

def get_low_points(height_map:List[List[int]]) -> List[int]:
    result =[]
    for row_index, row in enumerate(height_map):
        for column_index, value in enumerate(row):
            up = height_map[row_index-1][column_index] if row_index > 0 else 9
            right= height_map[row_index][column_index +1] if column_index +1 < len(row) else 9
            left= height_map[row_index][column_index -1] if column_index > 0 else 9
            down = height_map[row_index+1][column_index] if row_index+1 < len(height_map) else 9
            if value < min([up,down,left,right] ):
                result.append(value)
    return result
print(sum([x+1 for x in get_low_points(map)]))  #512