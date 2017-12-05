def load_instructions(filename):
    instructions = []
    with open(filename, "r") as f:
        for line in f.readlines():
            instructions.append(int(line))
    return instructions

def change_number_for_task1(number):
    return number + 1

def change_number_for_task2(number):
    if number >= 3:
        return number - 1
    else:
        return number + 1

def solve(instructions, method_for_changing_number):
    current_pos = 0

    steps = 0
    
    while current_pos < len(instructions):
        steps += 1

        jump = instructions[current_pos]
        instructions[current_pos] = method_for_changing_number(jump)

        current_pos += jump

    return steps


if __name__ == "__main__":
    print(solve(load_instructions("day05_input.txt"), change_number_for_task1))
    print(solve(load_instructions("day05_input.txt"), change_number_for_task2))
