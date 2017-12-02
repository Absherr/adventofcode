from itertools import permutations

def spreadsheet_lines(filename):
    with open(filename, "r") as spreadsheet:
        for line in spreadsheet.readlines():
            line = tuple(map(lambda x: int(x), line.split("\t")))
            yield line


def calculate_first_checksum(filename):
    checksum = 0
    for numbers in spreadsheet_lines(filename):
        checksum += (max(numbers) - min(numbers))

    return checksum


def calculate_second_checksum(filename):
    checksum = 0
    for numbers in spreadsheet_lines(filename):
        for x, y in permutations(numbers, 2):
            if x % y == 0:
                checksum += (x // y)

    return checksum


if __name__ == "__main__":
    print(calculate_first_checksum("day02_input.txt"))
    print(calculate_second_checksum("day02_input.txt"))
