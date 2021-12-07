
from typing import List
from tools import CommaInputProcessor


crab_posisions = CommaInputProcessor('07.txt').process_input()[0]


def calulate_fuel(crab_posissions: List[int], pos: int) -> int:
    feul = 0
    for c in crab_posisions:
        steps = abs(c - pos)
        for i in range(1, steps+1):
            feul += i
    return feul

possible_pos = range(min(crab_posisions), max(crab_posisions)+1)
print(min([calulate_fuel(crab_posisions, pos) for pos in possible_pos])) # 92881128