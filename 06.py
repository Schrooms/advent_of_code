from dataclasses import dataclass
from typing import List, Optional
from tools import InputProcessor

@dataclass
class Fish:
    age: int


class StateInputProcessor(InputProcessor):
    def process_line(self, line: str) -> List[int]:
        return [int(n) for n in line.split(',')]

    def getstate(self) -> List[Fish]:
        numbers = self.process_input()[0]
        return [Fish(age) for age in numbers]




def create_baby_fish(mamma: Fish) -> Optional[Fish]:
    if mamma.age == 0:
        return Fish(age=8)
    return None

fishes = StateInputProcessor('06.txt').getstate()

for day in range(256):
    babies = []
    for fish in fishes:
        baby = create_baby_fish(mamma=fish)
        if baby:
            babies.append(baby)
            fish.age =6
            continue
        fish.age -=1
    fishes += babies
    print(day)

print(len(fishes))