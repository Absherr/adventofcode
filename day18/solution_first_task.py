from collections import defaultdict

def load_instructions(filename):
    instructions = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip().split()
            instructions.append(line)
    return instructions

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def solve_first_task(filename):
    registers = defaultdict(int)

    last_played = None
    instructions = load_instructions(filename)
    instruction_pointer = 0
    while instruction_pointer < len(instructions):
        instruction = instructions[instruction_pointer]

        cmd = instruction[0]

        go_to_next_instruction = True

        print("Executing %s" % " ".join(instruction))

        if cmd == "snd":

            if is_int(instruction[1]):
                last_played = int(instruction[1])
            else:
                last_played = registers[instruction[1]]

        elif cmd == "set":
            if is_int(instruction[2]):
                registers[instruction[1]] = int(instruction[2])
            else:
                registers[instruction[1]] = registers[instruction[2]]

        elif cmd == "add":
            if is_int(instruction[2]):
                registers[instruction[1]] += int(instruction[2])
            else:
                registers[instruction[1]] += registers[instruction[2]]

        elif cmd == "mul":
            if is_int(instruction[2]):
                registers[instruction[1]] *= int(instruction[2])
            else:
                registers[instruction[1]] *= registers[instruction[2]]

        elif cmd == "mod":
            if is_int(instruction[2]):
                registers[instruction[1]] %= int(instruction[2])
            else:
                registers[instruction[1]] %= registers[instruction[2]]

        elif cmd == "rcv":
            value_to_check = None
            if is_int(instruction[1]):
                value_to_check = int(instruction[1])
            else:
                value_to_check = registers[instruction[1]]
            if value_to_check != 0:                
                return last_played

        elif cmd == "jgz":
            value_to_check = None
            if is_int(instruction[1]):
                value_to_check = int(instruction[1])
            else:
                value_to_check = registers[instruction[1]]

            if value_to_check > 0:
                go_to_next_instruction = False
                instruction_pointer += int(instruction[2])

        else:
            raise Exception("I dont know this instruction: " + " ".join(instruction))

        if go_to_next_instruction:
            instruction_pointer += 1

if __name__ == "__main__":
    print(solve_first_task("day18_input.txt"))
