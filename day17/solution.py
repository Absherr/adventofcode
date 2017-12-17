class Buffer:
    def __init__(self):
        self.buffer = [0, ]
        self.current_position = 0

    def move(self, step):
        self.current_position = (self.current_position + step) % len(self.buffer)

    def insert(self, value):
        self.current_position += 1
        self.buffer.insert(self.current_position, value)


def solve_first_task():
    b = Buffer()

    for i in range(1, 2018):
        b.move(303)
        b.insert(i)
    return b.buffer[b.current_position+1]

def solve_second_task():
    current_position = 0
    current_lenght = 1

    step = 303

    inserted_after_zero = None

    for i in range(1, 50000001):
        current_position = (current_position + step) % current_lenght
        current_position += 1
        if current_position == 1:
            inserted_after_zero = i

        current_lenght += 1

    return inserted_after_zero

if __name__ == "__main__":
    print(solve_first_task())
    print(solve_second_task())
