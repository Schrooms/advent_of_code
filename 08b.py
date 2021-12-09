from typing import Dict, List, Tuple
from tools import InputProcessor
from dataclasses import dataclass


@dataclass
class Signal:
    values: List[str]

    def __iter__(self):
        return iter(self.values)

@dataclass
class OutputDigits:
    values: List[str]

    def __iter__(self):
        return iter(self.values)


class SignalPatternInputProcessor(InputProcessor[Tuple[Signal, OutputDigits]]):
    def process_line(self, line: str) -> Tuple[Signal, OutputDigits]:
        line = line.strip('\n')
        raw_signal = line.split('|')[0]
        raw_digits = line.split('|')[1]
        return (Signal(values=raw_signal.split()), OutputDigits(values=raw_digits.split()))


# normal_decoder = {
#     'abcefg': 0,
#     'cf': 1,
#     'acdeg': 2,
#     'acdfg': 3,
#     'bdcf': 4,
#     'abdfg': 5,
#     'abdefg': 6,
#     'acf': 7,
#     'abcdefg': 8,
#     'abcdfg': 9
# }

uniqe_number_sizes = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


def sure_numbers(signals: Signal) -> Dict[int, str]:
    result: Dict[int, str] = {}
    for signal in signals:
        for k,v in uniqe_number_sizes.items():
            if k == len(signal):
                result[v] = signal
    return result


def get_numbers(signals: Signal) -> Dict[int, str]:
    sure = sure_numbers(signals)
    L = sure[4].translate({ord(x):None for x in sure[1]})

    for sig in  [sig for sig in signals if len(sig) == 5]:
        if len(sig.translate({ord(x):None for x in L})) == 3:
            sure[5] = sig
        elif len(sig.translate({ord(x):None for x in sure[1]})) == 3:
            sure[3] = sig
        else:
            sure[2] = sig
    for sig in [sig for sig in signals if len(sig) == 6]:
        if len(sig.translate({ord(x):None for x in sure[4]})) == 2:
            sure[9] = sig
        elif len(sig.translate({ord(x):None for x in L})) == 4:
            sure[6] = sig
        else:
            sure[0] = sig
    return sure


def match_all(signal: str, digit: str) -> bool:
    return sorted(signal) == sorted(digit)


def decode_digits(decoded:Dict[int, str], digits: OutputDigits) -> int:
    match: str =''
    for digit in digits:
        match += str([x for x, v in decoded.items() if match_all(v, digit)][0])
    return int(match)

messages = SignalPatternInputProcessor('08b.txt').process_input()
result: List[int] =[]
for signals, digits in messages:
    decoded = get_numbers(signals)
    result.append(decode_digits(decoded, digits))

print(sum(result))