from dataclasses import dataclass
from typing import List
from tools import InputProcessor

@dataclass(frozen=True)
class Command:
    direction:str
    value: int


class Submarine:
    def __init__(self) -> None:
        self.depth = 0
        self.horizontal = 0
        self.aim = 0
    
    def down(self, value:int ) -> None:
        self.aim += value 
    
    def up(self, value: int) -> None:
        self.aim -= value
    
    def forward(self, value:int) -> None:
        self.horizontal += value
        self.depth += self.aim * value

    def execute_command(self, command: Command) -> None:
       getattr(self, command.direction)(command.value)

class CommandLineProcessor(InputProcessor[Command]):
    def process_line(self, line:str):
        return Command(direction=line.split()[0], value=int(line.split()[1]))


if __name__ == '__main__':
    commands = CommandLineProcessor('02.txt').process_input()
    sub = Submarine()
    for command in commands:
        sub.execute_command(command)
    print(sub.horizontal * sub.depth)