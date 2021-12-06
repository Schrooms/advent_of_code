from typing import List
from tools import InputProcessor
from collections import deque

class StateInputProcessor(InputProcessor[List[int]]):
    def process_line(self, line: str) -> List[int]:
        return [int(n) for n in line.split(',')]


inital_state = StateInputProcessor('06.txt').process_input()[0]

# ammount of fish per day old:
#               0  1  2  3  4  5  6  7  8
fishes = deque([0, 0, 0, 0, 0, 0, 0, 0, 0]) # rotatable list thingy
for fish in inital_state:
    fishes[fish] += 1

for day in range(256):
    fishes.rotate(-1) #  all parents have one child
    fishes[6] += fishes[8] # all childs had one parent

print(sum(fishes))