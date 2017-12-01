def solve_captcha(seq, step):
    result = 0

    for index, char in enumerate(seq):
        if char == seq[(index + step) % len(seq)]:
            result += int(char)

    return result


def solve_first_task(seq):
    return solve_captcha(seq, 1)


def solve_second_task(seq):
    return solve_captcha(seq, len(seq) // 2)


if __name__ == "__main__":
    seq = input("Paste sequence: ")
    print(solve_first_task(seq))
    print(solve_second_task(seq))
