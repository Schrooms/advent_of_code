from typing import List, Set, Tuple
from typing_extensions import Literal
from tools import InputProcessor
from dataclasses import dataclass


class IntProcessor(InputProcessor[List[int]]):
    def process_line(self, line: str) -> List[int]:
        return [int(x) for x in line.strip('\n')]


@dataclass(frozen=True)
class Location:
    value: int
    row: int
    column: int

map = IntProcessor('09.txt').process_input()

def get_low_points(height_map:List[List[int]]) -> List[Location]:
    result =[]
    for row_index, row in enumerate(height_map):
        for column_index, value in enumerate(row):
            up = height_map[row_index-1][column_index] if row_index > 0 else 9
            right= height_map[row_index][column_index +1] if column_index +1 < len(row) else 9
            left= height_map[row_index][column_index -1] if column_index > 0 else 9
            down = height_map[row_index+1][column_index] if row_index+1 < len(height_map) else 9
            if value < min([up,down,left,right] ):
                result.append(Location(value, row_index, column_index))
    return result

def get_connected_higher_points(loc: Location, height_map: List[List[int]]) -> List[Location]:
    up = Location(height_map[loc.row -1][loc.column], loc.row -1, loc.column) if loc.row > 0 else None
    right= Location(height_map[loc.row][loc.column +1], loc.row, loc.column +1) if loc.column +1 < len(height_map[0]) else None
    left= Location(height_map[loc.row][loc.column -1], loc.row, loc.column -1) if loc.column > 0 else None
    down = Location(height_map[loc.row+1][loc.column], loc.row+1, loc.column) if loc.row+1 < len(height_map) else None
    locations:List[Location] = [x for x in [up,down,left,right] if x != None and x.value != 9]
    return [x for x in locations if x.value > loc.value]


points = get_low_points(map) #512


def get_pool(loc: Location, height_map: List[List[int]]) -> Set[Location]:
    result = set([loc])
    for x in get_connected_higher_points(loc, height_map):
        [result.add(y) for y in get_pool(x, height_map) ]
    return result


res = []
for point in points:
    x = get_pool(point, map)
    res.append(len(x))

greatest = sorted(res)[-3:]
print(greatest[0]* greatest[1]* greatest[2])



# print(get_conneted_higher_points(points[0], map))