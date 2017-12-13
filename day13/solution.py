from collections import deque


class Solution:
    def __init__(self, layers, delay=0):
        self.DOWN = 1
        self.UP = -1

        self.layers = layers
        self.scanners_positions = {k: 0 for k in self.layers.keys()}
        self.scanners_direction = {k: self.DOWN for k in self.layers.keys()}

        self.state_after_delay = None

        self.our_position = -1

        self.costs = 0
        self.caught = False
        self.delay = delay

        self.last_depth = max(self.layers.keys())

    def our_move(self):
        self.our_position += 1

    def scanners_move(self):
        for depth in self.layers.keys():
            self.move_single_scanner(depth)

    def move_single_scanner(self, pos):
        self.scanners_positions[pos] = self.scanners_positions[pos] + self.scanners_direction[pos]

        if self.scanners_positions[pos] == 0:
            self.scanners_direction[pos] = self.DOWN

        elif self.scanners_positions[pos] >= self.layers[pos] - 1:
            self.scanners_direction[pos] = self.UP

    def check_collisions(self):
        if self.our_position in self.scanners_positions:
            if self.scanners_positions[self.our_position] == 0:
                self.costs += self.our_position * self.layers[self.our_position]
                self.caught = True

    def tick(self):
        self.our_move()
        self.check_collisions()
        self.scanners_move()

    def move(self):
        self.process_delay()
        while self.our_position < self.last_depth:
            self.tick()

    def disp(self):
        for d in layers.keys():
            l = ""
            for x in range(layers[d]):
                if x == self.scanners_positions[d]:
                    l += "(X)"
                else:
                    l += "X"
            print("%d: %s" % (d, l))

    def process_delay(self):
        for depth in self.layers.keys():
            cycle_len = 2 * self.layers[depth] - 2

            out_of_cycle = self.delay % cycle_len
            for i in range(out_of_cycle):
                self.move_single_scanner(depth)


def load_layers(filename):
    layers = {}
    with open(filename, "r") as f:
        for line in f.readlines():
            d, r = map(int, line.strip().split(":"))

            layers[d] = r
    return layers


if __name__ == "__main__":
    # layers = load_layers("day13_test.txt")
    layers = load_layers("day13_input.txt")

    # first task
    s = Solution(layers)
    s.move()
    print(s.costs)

    # second task, not optimalized, run with pypy
    i = 3000000
    found = False
    while not found:
        s = Solution(layers, delay=i)
        s.move()
        
        if not s.caught:
            found = True
        else:
            i += 1

    print(i)
