from collections import defaultdict


class Solution:
    def __init__(self):
        self.dir_order = "RULD"

        self.current = 0
        self.box_size = 2

        self.direction = 0
        self.movement_counter = 0

        # first move is to right to set 1, so actual diff at beginning is (-1, 0)
        self.diff_x = -1
        self.diff_y = 0

        self.memory_map = defaultdict(int)
        self.memory_map[(0, 0)] = 1

    def move(self):
        self.current += 1

        if self.movement_counter == self.box_size:
            self.movement_counter = 1
            self.direction = (self.direction + 1) % len(self.dir_order)

            if self.dir_order[self.direction] in ["R", "L"]:
                self.box_size += 1

        self.movement_counter += 1

        self.recalculate_diff()

        if not self.current == 1:
            self.update_memory_map()

    def update_memory_map(self):
        neighbours_sum = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                neighbours_sum += self.memory_map[(self.diff_x + dx, self.diff_y + dy)]
        self.memory_map[(self.diff_x, self.diff_y)] = neighbours_sum

    def recalculate_diff(self):
        current_direction = self.dir_order[self.direction]
        if current_direction == "R":
            self.diff_x += 1
        elif current_direction == "U":
            self.diff_y += 1
        elif current_direction == "L":
            self.diff_x -= 1
        elif current_direction == "D":
            self.diff_y -= 1

    def move_until_value_in_memory_map(self, value):
        while self.memory_map[(self.diff_x, self.diff_y)] <= value:
            self.move()


if __name__ == "__main__":
    # task 1
    s = Solution()
    task_input = 361527
    for i in range(task_input):
        s.move()
    print(s.diff_x + s.diff_y)

    # task 2
    s = Solution()
    s.move_until_value_in_memory_map(task_input)
    print(s.memory_map[(s.diff_x, s.diff_y)])
