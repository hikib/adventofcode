import pathlib


def main():
    file_name = "input.prod"
    directory = pathlib.Path(__file__).parent.absolute()
    input_file = directory.joinpath(file_name)

    rows = range(128)
    cols = range(8)
    split_pass = 7
    get_id = lambda r, c: r * 8 + c

    occupied = set()
    with open(input_file, "r") as f:
        for boarding_pass in f.readlines():
            # Get row and seat binaries
            row_ind = boarding_pass[:split_pass]
            col_ind = boarding_pass[split_pass:]

            # Recursive binary search
            row = bin_search(row_ind, rows)
            col = bin_search(col_ind, cols)

            seat_id = get_id(row, col)
            occupied.add(seat_id)

    # PART I
    max_id = max(occupied)
    print(f"Highest seat ID: {max_id}")

    # PART II
    min_id = min(occupied)
    all_seats = set(range(min_id, max_id))
    free_seat = all_seats.difference(occupied)
    print(f"Free seat: {free_seat}")


def bin_search(indicator, data):
    if indicator[0] == "F" or indicator[0] == "L":
        data = data[:len(data) // 2]
    else:
        data = data[len(data) // 2:]
    if len(indicator) > 1:
        return bin_search(indicator[1:], data)
    else:
        return data[0]


if __name__ == "__main__":
    main()

