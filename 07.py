
from typing import List
from tools import CommaInputProcessor


crab_posisions = CommaInputProcessor('07.txt').process_input()[0]


def calulate_fuel(crab_posissions: List[int], pos: int) -> int:
    feul = 0
    for c in crab_posisions:
        feul += abs(c - pos)
    return feul

print(min([calulate_fuel(crab_posisions, pos) for pos in crab_posisions]))