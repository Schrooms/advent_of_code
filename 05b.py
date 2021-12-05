import collections
from typing import List
from tools import InputProcessor
from dataclasses import dataclass
from enum import Enum
from collections import Counter


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

class Direction(Enum):
    NORTH=0
    NORTH_EAST=1
    EAST=2
    SOUTH_EAST=3
    SOUTH=4
    SOUTH_WEST=5
    WEST=6
    NORTH_WEST=7


@dataclass(frozen=True)
class Cloud:
    start: Coordinate
    end: Coordinate

    @property
    def spread(self) -> List[Coordinate]:
        return self.calulate_path()

    @property
    def direction(self) -> Direction:
        if self.start.x == self.end.x:
            #vertical
            if self.start.y < self.end.y:
                return Direction.SOUTH
            else:
                return Direction.NORTH
        elif self.start.y == self.end.y:
            # horizontal
            if self.start.x < self.end.x:
                return Direction.EAST
            else:
                return Direction.WEST
        elif self.start.x < self.end.x:
            if self.start.y < self.end.y:
                return Direction.SOUTH_EAST
            else:
                return Direction.NORTH_EAST # 5.5, 8.2
        elif self.start.x > self.end.x:
            if self.start.y > self.end.y:
                return Direction.NORTH_WEST #8.8 -> 0.1
            else:
                return Direction.SOUTH_WEST # 8,0 -> 0,8

        raise Exception

    def calulate_path(self) -> List[Coordinate]:
        result:List[Coordinate] = []
        if self.direction == Direction.SOUTH:
            for i in range(self.start.y , self.end.y +1):
                result.append(Coordinate(x=self.start.x, y=i))
        elif self.direction == Direction.NORTH:
            for i in range(self.end.y , self.start.y +1):
                result.append(Coordinate(x=self.start.x, y=i))
        elif self.direction == Direction.EAST:
             for i in range(self.start.x , self.end.x +1):
                  result.append(Coordinate(x=i, y=self.start.y))
        elif self.direction == Direction.WEST:
            for i in range(self.end.x, self.start.x +1):
                result.append(Coordinate(x=i, y=self.start.y))
        elif self.direction == Direction.NORTH_WEST:
            result.append(self.start)
            coord = self.start
            while coord.x != self.end.x and coord.y != self.end.y:
                coord = Coordinate(coord.x -1, coord.y-1)
                result.append(coord)
        elif self.direction == Direction.NORTH_EAST:
            result.append(self.start)
            coord = self.start
            while coord.x != self.end.x and coord.y != self.end.y:
                coord = Coordinate(coord.x +1, coord.y-1)
                result.append(coord)
        elif self.direction == Direction.SOUTH_WEST:
            result.append(self.start)
            coord = self.start
            while coord.x != self.end.x and coord.y != self.end.y:
                coord = Coordinate(coord.x -1, coord.y+1)
                result.append(coord)
        elif self.direction == Direction.SOUTH_EAST:
            result.append(self.start)
            coord = self.start
            while coord.x != self.end.x and coord.y != self.end.y:
                coord = Coordinate(coord.x +1, coord.y +1)
                result.append(coord)
        return result


class CloudInputProcessor(InputProcessor[Cloud]):
    def process_line(self, line: str) -> Cloud:
        start = self.get_coord(line.split('->')[0])
        end = self.get_coord(line.split('->')[1])
        return Cloud(start, end)

    def get_coord(self, part: str) -> Coordinate:
        return Coordinate(
            x=int(part.split(',')[0]),
            y=int(part.split(',')[1]))


if __name__ == '__main__':
    clouds = CloudInputProcessor('05b.txt').process_input()
    spreads = []
    for cloud in clouds:
        try:
            spreads += cloud.spread
        except Exception:
            pass
    print(len([v for k,v in Counter(spreads).items() if v > 1 ]))  # 19851