from typing import List, Tuple
from tools import InputProcessor
from dataclasses import dataclass


@dataclass
class Signal:
    values: List[str]

@dataclass
class OutputDigits:
    values: List[str]


class SignalPatternInputProcessor(InputProcessor[Tuple[Signal, OutputDigits]]):
    def process_line(self, line: str) -> Tuple[Signal, OutputDigits]:
        line = line.strip('\n')
        raw_signal = line.split('|')[0]
        raw_digits = line.split('|')[1]
        return (Signal(values=raw_signal.split()), OutputDigits(values=raw_digits.split()))

messages = SignalPatternInputProcessor('08.txt').process_input()

easy_numbers = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}
c=0
for signal, digits in messages:
    for digit in digits.values:
        if len(digit) in easy_numbers:
            c+=1

print(c)