def _generator(starting_value, multiply, criteria=lambda x: True):
    value = starting_value
    while True:
        value = (value * multiply) % 2147483647
        if criteria(value):
            yield value

def dummy_criteria(_):
    return True

def criteria_4(value):
    return value % 4 == 0

def criteria_8(value):
    return value % 8 == 0

def generatorA(starting_value, criteria=dummy_criteria):
    return _generator(starting_value, 16807, criteria)

def generatorB(starting_value, criteria=dummy_criteria):
    return _generator(starting_value, 48271, criteria)

def solve_first_task():
    gA = generatorA(634)
    gB = generatorB(301)
    rounds = 40000000

    return fight(gA, gB, rounds)

def solve_second_task():
    gA = generatorA(634, criteria_4)
    gB = generatorB(301, criteria_8)
    rounds = 5000000

    return fight(gA, gB, rounds)

def fight(genA, genB, rounds):
    mask = 0xFFFF
    matches = 0

    for i in range(rounds):
        a_value = genA.next()  & mask
        b_value = genB.next()  & mask
        matches += (a_value == b_value)

    return matches


if __name__ == "__main__":
    print(solve_first_task())
    print(solve_second_task())
