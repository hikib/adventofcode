import functools
from typing import Tuple, List


def main():
    # TEST DATA
    # forest = """
    #     ..##.......
    #     #...#...#..
    #     .#....#..#.
    #     ..#.#...#.#
    #     .#...##..#.
    #     ..#.##.....
    #     .#.#.#....#
    #     .#........#
    #     #.##...#...
    #     #...##....#
    #     .#..#...#.#
    #     """.splitlines()[1:-1]
    # forest = [i.strip() for i in forest]
    with open("input.txt", "r") as f:
        forest = [row.strip() for row in f.readlines()]

    # PART I
    slope = (3, 1)
    trees = count_trees(forest, slope)
    print(f"{trees} on a {slope} slope.")

    # PART II
    slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)]
    trees = functools.reduce(
            lambda x, y: x * y,
            (count_trees(forest, sl) for sl in slopes))
    print(f"{trees} on all slopes.")


def count_trees(
        forest: List[str],
        slope: Tuple[int, int]) -> int:

    row = 0
    col = 0

    is_tree = lambda r, c: forest[r][c] == "#"
    tree_count = 0

    goal = len(forest)
    rep = len(forest[0])

    while row < goal:
        if is_tree(row, col % rep):
            tree_count += 1
        col += slope[0]
        row += slope[1]

    return tree_count


if __name__ == "__main__":
    main()

