#!/usr/bin/env python3
"""
Practicing OOP, classes, deque.
... made things more complicated.
"""

import collections
import pathlib


def main():
    data = get_data("input.prod")
    adapters = [Adapter(int(d)) for d in data]

    outlet = Outlet()
    chain = AdapterChain(outlet, adapters)

    # PART I
    loads = chain.loads
    print(loads.count(1) * loads.count(3))

    # PART II
    combinations = chain.count_combinations()
    print(combinations[-1])




class AdapterChain:
    def __init__(self, outlet, adapters):
        self.outlet = outlet
        self.device = Device(max((i for i in adapters)) + 3)
        self._adapters = collections.deque(sorted(adapters))
        self._loads = collections.deque()

    def __repr__(self):
        if self.adapters:
            return (f"{self.outlet}-"
                    f"{'-'.join([str(adapter) for adapter in self.adapters])}"
                    f"-{self.device}")
        else:
            return f"<Chain>{self.outlet}-{self.device}"

    def get_differences(jolts):
        bdapters = jolts.copy()
        bdapters.rotate(1)
        return collections.deque((a - b for a, b in zip(jolts, bdapters)))

    @property
    def loads(self):
        tmpA = self._adapters.copy()
        tmpA.appendleft(self.outlet)
        tmpA.append(self.device)

        tmpB = tmpA.copy()
        tmpB.rotate(1)

        loads = collections.deque([a.jolt - b.jolt for a, b in zip(tmpA, tmpB)][1:])
        return loads

    @property
    def adapters(self):
        return list(self._adapters)

    @property
    def jolts(self):
        jolts = [a.jolt for a in self.adapters]
        jolts.append(self.device.jolt)
        jolts.insert(0, self.outlet.jolt)
        return  jolts

    def count_combinations(self):
        counts = list(range(len(self.jolts)))
        counts[0] = 1
        for idx, jolt in enumerate(self.jolts[1:], 1):
            prev_idx = idx
            counts[idx] = 0

            while prev_idx >= 0 and jolt - self.jolts[prev_idx] <= 3:
                counts[idx] += counts[prev_idx]
                prev_idx -= 1

        return counts


class Adapter:
    """
    Base class for anything having a joltage
    """
    def __init__(self, jolt):
        self.jolt = jolt

    def __add__(self, other):
        if isinstance(other, Adapter):
            return abs(self.jolt + other.jolt)
        if isinstance(other, int):
            return abs(self.jolt + other)

    def __repr__(self):
        return f"<Adapter({self.jolt})>"

    def __eq__(self, other):
        return True if self.jolt == other.jolt else False

    def __ne__(self, other):
        return True if self.jolt != other.jolt else False

    def __gt__(self, other):
        return True if self.jolt > other.jolt else False

    def __lt__(self, other):
        return True if self.jolt < other.jolt else False

    def __le__(self, other):
        return True if self.jolt <= other.jolt else False

    def __ge__(self, other):
        return True if self.jolt >= other.jolt else False

    def can_connect(self, other):
        if self + other <= 3: return True
        else: return False


class Outlet(Adapter):
    def __init__(self):
        self.jolt = 0

    def __repr__(self):
        return f"<Outlet({self.jolt})>"


class Device(Adapter):
    def __repr__(self):
        return f"<Device({self.jolt})>"


def get_data(file_name):
    directory = pathlib.Path(__file__).parent.absolute()
    input_file = directory.joinpath(file_name)
    with open(input_file, "r") as f:
        data = [d.strip() for d in f.readlines()]
    return data


if __name__ == "__main__":
    main()

