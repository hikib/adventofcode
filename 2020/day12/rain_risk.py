#!/usr/bin/env python3

import pathlib


def main():
    instructions = Data("input.prod").as_string()
    print(part_one(instructions))
    print(part_two(instructions))
    return

def part_one(instructions):
    face = "E"
    directions = {face: 0 for face in "NESW"}

    for inst in instructions:
        action, units = inst[0], int(inst[1:])
        if action == "F":
            directions = one_add_movement(directions, face, units)
        elif action in "NESW":
            directions = one_add_movement(directions, action, units)
        else:
            face = one_get_face(face, action, units)

    manhattan_dist = sum(abs(i) for i in directions.values())
    return manhattan_dist

def one_add_movement(directions, action, units):
    switch = {"N": "S", "S": "N", "E": "W", "W": "E"}
    rest = units - directions[switch[action]]
    directions[switch[action]] -= units - rest
    directions[action] += rest
    return directions

def one_get_face(face, action, units):
    dirs = "NESW"
    if action == "R":
        face = dirs[(dirs.index(face) + (units // 90)) % len(dirs)]
    if action == "L":
        face = dirs[(dirs.index(face) - (units // 90)) % len(dirs)]
    return face

def part_two(instructions):
    waypoint = [1, 10, 0, 0]
    ship = [0, 0, 0, 0]

    for inst in instructions:
        action, units = inst[0], int(inst[1:])
        if action == "F":
            ship = two_move_ship(ship, waypoint, units)
        elif action in "NESW":
            waypoint = two_move_waypoint(waypoint, action, units)
        else:
            waypoint = two_rotate(waypoint, action, units)

    manhattan_dist = sum(abs(i) for i in ship)
    return manhattan_dist


def two_move_ship(ship, waypoint, units):
    for i in range(len(ship)):
        opposite_i = (i + 2) % len(ship)
        distance = waypoint[i] * units
        rest = distance - ship[opposite_i]
        ship[opposite_i] -= distance - rest
        ship[i] += rest
    return ship

def two_move_waypoint(waypoint, action, units):
    positions = {d: i for (d, i) in zip("NESW", range(5))}
    direction = [0, 0, 0, 0]
    direction[positions[action]] = units

    for i in range(len(waypoint)):
        waypoint[i] += direction[i]

    return waypoint


def two_rotate(waypoint, action, units):
    rotation = units // 90 % len(waypoint)
    if action == "L":
        waypoint = waypoint[rotation:] + waypoint[:rotation]
    else:
        waypoint = waypoint[-rotation:] + waypoint[:-rotation]
    return waypoint


class Data:
    def __init__(self, file_name):
        self.file_name = file_name

    def as_int(self):
        numbers = [int(d) for d in self._get_data()]
        return numbers

    def as_string(self):
        return self._get_data()

    def _get_data(self):
        directory = pathlib.Path(__file__).parent.absolute()
        input_file = directory.joinpath(self.file_name)
        with open(input_file, "r") as f:
            data = [d.strip() for d in f.readlines()]
        return data


if __name__ == "__main__":
    main()

