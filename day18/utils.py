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
