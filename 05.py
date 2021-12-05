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
    UP=0
    DOWN=1
    RIGHT=2
    LEFT=3


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
                return Direction.DOWN
            else:
                return Direction.UP
        elif self.start.y == self.end.y:
            # horizontal
            if self.start.x < self.end.x:
                return Direction.RIGHT
            else:
                return Direction.LEFT
        else:
            raise Exception

    def calulate_path(self) -> List[Coordinate]:
        result:List[Coordinate] = []
        if self.direction == Direction.DOWN:
            for i in range(self.start.y , self.end.y +1):
                result.append(Coordinate(x=self.start.x, y=i))
        elif self.direction == Direction.UP:
            for i in range(self.end.y , self.start.y +1):
                result.append(Coordinate(x=self.start.x, y=i))
        elif self.direction == Direction.RIGHT:
             for i in range(self.start.x , self.end.x +1):
                  result.append(Coordinate(x=i, y=self.start.y))
        elif self.direction == Direction.LEFT:
            for i in range(self.end.x, self.start.x +1):
                result.append(Coordinate(x=i, y=self.start.y))
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
    clouds = CloudInputProcessor('05.txt').process_input()
    spreads = []
    for cloud in clouds:
        try:
            spreads += cloud.spread
        except Exception:
            pass
    print(len([v for k,v in Counter(spreads).items() if v > 1 ]))  # 6687