#!/usr/bin/env python3

import copy
from dataclasses import dataclass


def main():
    data = get_data()
    sheet = InstructionSheet()
    for d in data:
        action = d.split()[0]
        count = int(d.split()[1])
        instruction = Instruction(action, count)
        sheet.add_instruction(instruction)

    game = GameConsole()
    try:
        print("Running game...")
        game.run(sheet)
    except InfiniteError:
        # PART I
        print("ERROR: Loop at accumulator: ", game.accumulator)

        # PART II
        print("Fixing instructions ...")
        sheet.fix()
        print("Rerunning game ...")
        game.reset()
        game.run(sheet)

    print("Termination at accumulator: ", game.accumulator)
    return

def get_data():
    with open("input.prod", "r") as f:
        data = [d.strip() for d in f.readlines()]
    return data


class InstructionSheet:
    def __init__(self):
        self._index = 0
        self._ran = list()
        self._instructions = list()

    def add_instruction(self, instruction):
        self._instructions.append(instruction)

    def _reset_run(self):
        self._index = 0
        self._ran.clear()

    def __iter__(self):
        return self

    def __next__(self):
        if self._index in self._ran:
            raise InfiniteError
        elif self._ran and self._ran[-1] == len(self._instructions) - 1:
            raise StopIteration

        self._ran.append(self._index)
        instruction = self._instructions[self._index]

        if instruction.action == "jmp":
            self._index += instruction.count
        else:
            self._index += 1
        return instruction

    def fix(self):
        is_jmp_np = lambda x: x.action == "jmp" or x.action == "nop"
        values = {"jmp": "nop", "nop": "jmp"}
        for i, inst in enumerate(self._instructions):
            if is_jmp_np(inst):
                tmp = copy.deepcopy(self)
                tmp._reset_run()
                tmp._instructions[i].action = values[inst.action]
                try:
                    GameConsole().run(tmp)
                except InfiniteError:
                    continue
                break
        self._instructions[i].action = tmp._instructions[i].action
        self._reset_run()


class GameConsole:
    def __init__(self):
        self.accumulator = 0

    def run(self, sheet):
        for instruction in sheet:
            if instruction.action == "acc":
                self.accumulator += instruction.count

    def reset(self):
        self.accumulator = 0


@dataclass
class Instruction:
    action: str
    count: int



class InfiniteError(Exception):
    """ Raised when game is infinite """
    pass


if __name__ == "__main__":
    main()

