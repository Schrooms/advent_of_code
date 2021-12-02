from tools import InputProcessor, get_increases

class IntLineProcessor(InputProcessor[int]):
    def process_line(self, line:str) -> int:
        return int(line)

if __name__ == '__main__':
    processor = IntLineProcessor('01.txt')
    print(get_increases(processor.process_input()))
    