from collections import defaultdict
from threading import Thread
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


class Program(Thread):
    def __init__(self, program_number, instructions):
        # Thread.__init__(self)
        super(Program, self).__init__()

        self.program_number = program_number
        self.registers = defaultdict(int)
        self.registers['p'] = program_number
        self.instructions = instructions
        self.queue = []
        
        self.other_program = None
        self.waiting = False
        self.values_sent = 0

    def set_other_program(self, program_ref):
        self.other_program = program_ref

    def run(self):
        instruction_pointer = 0
        deadlock_detected = False
        while instruction_pointer < len(self.instructions) or deadlock_detected:
            instruction = self.instructions[instruction_pointer]

            cmd = instruction[0]

            go_to_next_instruction = True

            # logging.debug("Program %d: %s [%d]" % (self.program_number, " ".join(instruction), instruction_pointer))

            if cmd == "snd":
                if is_int(instruction[1]):
                    valut_to_be_sent = int(instruction[1])
                else:
                    valut_to_be_sent = self.registers[instruction[1]]
                self.values_sent += 1
                self.other_program.queue.append(valut_to_be_sent)

            elif cmd == "set":
                if is_int(instruction[2]):
                    value = int(instruction[2])
                else:
                    value = self.registers[instruction[2]]
                self.registers[instruction[1]] = value

            elif cmd == "add":
                if is_int(instruction[2]):
                    value = int(instruction[2])
                else:
                    value = self.registers[instruction[2]]
                self.registers[instruction[1]] += value

            elif cmd == "mul":
                if is_int(instruction[2]):
                    value = int(instruction[2])
                else:
                    value= self.registers[instruction[2]]
                self.registers[instruction[1]] *= value
            elif cmd == "mod":
                if is_int(instruction[2]):
                    value = int(instruction[2])
                else:
                    value = self.registers[instruction[2]]
                self.registers[instruction[1]] %= value

            elif cmd == "rcv":
                while len(self.queue) == 0:
                    self.waiting = True
                    if self.other_program.waiting:
                        deadlock_detected = True
                        raise Exception("Deadlock in %d, after sending %d values!" % (self.program_number, self.values_sent))

                    sleep(100)

                self.waiting = False
                # print("Pop  %d, after sending %d values!" % (self.program_number, self.values_sent))
                
                value = self.queue.pop(0)
                self.registers[instruction[1]] = value

            elif cmd == "jgz":
                value_to_check = None
                if is_int(instruction[1]):
                    value_to_check = int(instruction[1])
                else:
                    value_to_check = self.registers[instruction[1]]

                if value_to_check > 0:
                    go_to_next_instruction = False
                    if is_int(instruction[2]):
                        value = int(instruction[2])
                    else:
                        value += self.registers[instruction[2]]
                    instruction_pointer += value

            else:
                raise Exception("I dont know this instruction: " + " ".join(instruction))

            if go_to_next_instruction:
                instruction_pointer += 1


def load_instructions(filename):
    instructions = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip().split()
            instructions.append(line)
    return instructions


if __name__ == "__main__":
    instructions = load_instructions("day18_input.txt")

    program_zero = Program(0, list(instructions))
    program_one = Program(1, list(instructions))
    
    program_zero.set_other_program(program_one)
    program_one.set_other_program(program_zero)

    program_zero.start()
    program_one.start()
