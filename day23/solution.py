from collections import defaultdict
from math import sqrt

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def load_instruction(filename):
    instructions = []
    with open(filename, "r") as f:
        for line in f.readlines():
            instructions.append(line.strip().split())

    return instructions

def solve_first_task(filename, debug_mode=False):
    instructions = load_instruction(filename)
    registers = defaultdict(int)
    
    if not debug_mode:
        registers['a'] = 1
    
    instruction_pointer = 0
    mul_counter = 0

    while instruction_pointer < len(instructions):
        instruction = instructions[instruction_pointer]
        cmd = instruction[0]

        go_to_next_instruction = True

        if cmd == "set":
            if is_int(instruction[2]):
                value = int(instruction[2])
            else:
                value = registers[instruction[2]]
            registers[instruction[1]] = value

        elif cmd == "sub":
            if is_int(instruction[2]):
                value = int(instruction[2])
            else:
                value = registers[instruction[2]]
            registers[instruction[1]] -= value

        elif cmd == "mul":
            if is_int(instruction[2]):
                value = int(instruction[2])
            else:
                value = registers[instruction[2]]
            registers[instruction[1]] *= value
            mul_counter += 1

        elif cmd == "jnz":
            value_to_check = None
            if is_int(instruction[1]):
                value_to_check = int(instruction[1])
            else:
                value_to_check = registers[instruction[1]]

            if value_to_check != 0:
                go_to_next_instruction = False

                if is_int(instruction[2]):
                    value = int(instruction[2])
                else:
                    value = registers[instruction[2]]

                instruction_pointer += value

        else:
            raise Exception("I dont know this instruction: " + " ".join(instruction))

        if go_to_next_instruction:
            instruction_pointer += 1

    return registers, mul_counter

def solve_second_task():

    b = 81
    b *= 100
    b -= -100000

    c = b
    c -= -17000

    not_primes = 0

    for b in range(108100, c + 1, 17):
        prime = True
        f = 1
        for d in range(2, int(sqrt(b))):
            if b % d == 0:
                prime = False
                break
        if not prime:
            not_primes += 1
    return not_primes

if __name__ == '__main__':
    print("Debug mode")
    registers, mul_counter = solve_first_task("day23_input.txt", debug_mode=True)
    print(registers)
    print("multiplications: %d" % mul_counter)
    
    print("Optimalized mode")
    h = solve_second_task()
    print(h)
