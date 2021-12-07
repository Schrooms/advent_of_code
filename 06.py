from typing import List
from tools import CommaInputProcessor, InputProcessor
from collections import deque


inital_state = CommaInputProcessor('06.txt').process_input()[0]

# ammount of fish per day old:
#               0  1  2  3  4  5  6  7  8
fishes = deque([0, 0, 0, 0, 0, 0, 0, 0, 0]) # rotatable list thingy
for fish in inital_state:
    fishes[fish] += 1

for day in range(256):
    fishes.rotate(-1) #  all parents have one child
    fishes[6] += fishes[8] # all childs had one parent

print(sum(fishes))