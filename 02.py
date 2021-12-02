from dataclasses import dataclass
from typing import List

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


def get_commands(file_name: str) -> List[Command]:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return [Command(direction=x.split()[0], value=int(x.split()[1])) for x in lines]


if __name__ == '__main__':
    commands = get_commands('02.txt')
    sub = Submarine()
    for command in commands:
        sub.execute_command(command)
    print(sub.horizontal * sub.depth)