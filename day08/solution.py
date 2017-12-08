from collections import defaultdict

def solve(filename):
    registers = defaultdict(int)

    # for second task
    the_biggest_value = 0

    with open(filename, "r") as f:
        for line in f.readlines():
            register_name, operation, value, _, condition_register, condition_operation, condition_value = line.strip().split()

            query = "%d %s %s" % (registers[condition_register], condition_operation, condition_value)

            if eval(query):
                if operation == "inc":
                    registers[register_name] += int(value)
                elif operation == "dec":
                    registers[register_name] -= int(value)
                else:
                    raise ValueException("unknown operation: " + operation)
                
                if registers[register_name] > the_biggest_value:
                    the_biggest_value = registers[register_name]

    return max(registers.values()), the_biggest_value

if __name__ == "__main__":
    print(solve("day08_test.txt"))
    print(solve("day08_input.txt"))