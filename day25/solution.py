from collections import defaultdict

def load_content(filename):
    with open(filename, "r") as f:
        content = list(map(lambda x: x.strip(), f.read().split("\n")))
    return content

def read_basic_info(content):
    initial_state = content[0].split()[-1][:-1]
    steps_to_do = int(content[1].split()[-2])

    return initial_state, steps_to_do

def get_last_word_without_punctuation(line):
    return line.split()[-1][:-1]

def load_instructions(content):
    state_line = 3
    instruction_len = 10

    instructions = {}

    while state_line + instruction_len <= len(content):
        analyzed_state = get_last_word_without_punctuation(content[state_line])
        instruction = {}

        analyzed_value = get_last_word_without_punctuation(content[state_line+1])
        new_value = get_last_word_without_punctuation(content[state_line+2])
        direction = get_last_word_without_punctuation(content[state_line+3])

        if direction == "left":
            direction = -1
        else:
            direction = 1
        
        new_state = get_last_word_without_punctuation(content[state_line+4])

        instruction[analyzed_value] = (new_value, direction, new_state)

        analyzed_value = get_last_word_without_punctuation(content[state_line+5])
        new_value = get_last_word_without_punctuation(content[state_line+6])
        direction = get_last_word_without_punctuation(content[state_line+7])
        
        if direction == "left":
            direction = -1
        else:
            direction = 1

        new_state = get_last_word_without_punctuation(content[state_line+8])

        instruction[analyzed_value] = (new_value, direction, new_state)

        instructions[analyzed_state] = instruction

        state_line += instruction_len

    return instructions

def solve(filename):
    file_content = load_content(filename)
    initial_state, steps_to_do = read_basic_info(file_content)
    
    instructions = load_instructions(file_content)

    tape = defaultdict(lambda: str("0"))

    current_pos = 0
    current_state = initial_state

    for i in range(steps_to_do):
        current_value = tape[current_pos]

        new_value, direction, new_state = instructions[current_state][current_value]

        tape[current_pos] = new_value
        current_pos += direction

        current_state = new_state

    return list(tape.values()).count("1")

if __name__ == '__main__':
    print(solve("day25_input.txt"))
