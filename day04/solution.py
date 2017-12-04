def passphrase_lines(filename):
    with open(filename, "r") as passphrase_file:
        for line in passphrase_file.readlines():
            line = line.strip().split()
            yield line

def solve(filename, validation_method):
    valid_passphrases = 0
    for passphrase in passphrase_lines(filename):
        if validation_method(passphrase):
            valid_passphrases += 1
    return valid_passphrases

def validation_method_for_first_task(passphrase):
    words = set()
    for ph in passphrase:
        words.add(ph)
        
    return len(words) == len(passphrase)

def validation_method_for_second_task(passphrase):
    words = set()
    for ph in passphrase:
        sorted_ph = "".join(sorted(ph))
        words.add(sorted_ph)

    return len(words) == len(passphrase)


if __name__ == "__main__":
    print(solve("day04_input.txt", validation_method_for_first_task))
    print(solve("day04_input.txt", validation_method_for_second_task))
