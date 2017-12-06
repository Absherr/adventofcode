def load_banks(filename):
    banks = []
    with open(filename, "r") as f:
        s = f.read().strip()
        banks = list(map(int, s.split()))
    return banks

def solve(filename):
    banks = load_banks(filename)

    banks_count = len(banks)

    steps = 0
    duplicate_found = False

    banks_history = []
    banks_history.append(list(banks))

    while not duplicate_found:
        max_bank_value = max(banks)
        max_bank_index = banks.index(max_bank_value)
        banks[max_bank_index] = 0

        for i in range(1, max_bank_value + 1):
            banks[(max_bank_index + i) % banks_count] += 1
        steps += 1

        if banks in banks_history:
            duplicate_found = True

        banks_history.append(list(banks))

    loop_begining = banks_history.index(banks)

    return steps, (steps - loop_begining)


if __name__ == "__main__":
    print(solve("day06_test.txt"))
    print(solve("day06_input.txt"))
