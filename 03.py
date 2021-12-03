from typing import List
from tools import InputProcessor

class GammaProcessor(InputProcessor[List[int]]):
    def process_line(self, line:str) -> List[int]:
        _line = line.strip('\n')
        return [int(x) for x in _line]


def get_gamma(bit_list: List[List[int]]) -> str:
    bits_result: List[int] = []
    for i in range(len(bit_list[0])):
        zeros = 0
        ones = 0
        for bits in bit_list:
            if bits[i] == 0:
                zeros += 1
            else:
                ones += 1
        if ones > zeros:
            bits_result.append(1)
        else:
            bits_result.append(0)
    return ''.join([str(bit) for bit in bits_result])





if __name__ == '__main__':
    prosessor = GammaProcessor('03.txt')
    bit_list = prosessor.process_input()
    gamma = get_gamma(bit_list)
    epsilon = int(gamma, 2) ^ int('1'*len(gamma),2)
    print(int(gamma, 2) * epsilon)