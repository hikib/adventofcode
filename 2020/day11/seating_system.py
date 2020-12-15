#!/usr/bin/env python3

import pathlib


def main():
    layout = Data("input.prod").as_string()

    changed = True
    while changed:
        layout, changed = change_layout(layout)

    print(sum(i.count("#") for i in layout))

def change_layout(layout):
    changed = False
    switch = {"L": "#", "#": "L"}
    new_layout = []

    for r_idx in range(len(layout)):
        new_row = []
        for s_idx in range(len(layout[0])):
            seat = layout[r_idx][s_idx]
            if seat == ".":
                new_row.append(".")
                continue

            adjacents = get_adjacents(r_idx, s_idx, layout)

            # Part I - 4
            # Part II - 5
            if (seat == "#" and adjacents.count("#") >= 5) or \
               (seat != "#" and adjacents.count("#") == 0):
                changed = True
                new_row.append(switch[seat])
            else:
                new_row.append(seat)

        new_layout.append("".join(new_row))
    return new_layout, changed


def get_adjacents(r_idx, s_idx, layout):
    # row and seat must stay within layout
    valid_row = lambda r, i: 0 < r+i+1 < len(layout) + 1
    valid_seat = lambda s, j: 0 < s+j+1 < len(layout[0]) + 1

    seat_range = range(-1, 2) # only immidiate seats (9x9 grid)

    adjacent = []
    for i in seat_range:
        if valid_row(r_idx, i):
            for j in seat_range:
                if valid_seat(s_idx, j):
                    if i == 0 and j == 0:
                        continue # ignore itself
                    seat = layout[r_idx+i][s_idx+j]

                    # Part II - search further
                    count = 1
                    while seat == "." \
                            and valid_row(r_idx, i*count) \
                            and valid_seat(s_idx, j*count):
                        seat = layout[r_idx+(i*count)][s_idx+(j*count)]
                        layout
                        count += 1

                    adjacent += seat
    return adjacent


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

