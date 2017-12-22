from collections import defaultdict


class Virus(object):
    def __init__(self, filename):
        self.cluster = defaultdict(lambda: str("."))
        self.current_direction = "up"

        self.current_position_x = 0
        self.current_position_y = 0

        self.load_initial_cluster(filename)

        self.infected_counter = 0

    def load_initial_cluster(self, filename):
        initial_cluster = []
        with open(filename, "r") as f:
            for line in f.readlines():
                initial_cluster.append(line.strip())

        height = len(initial_cluster)
        width = len(initial_cluster[0])
        
        half_x = width // 2
        half_y = height // 2

        for y in range(-half_y, half_y+1):
            for x in range(-half_x, half_x+1):
                self.cluster[(x,y)] = initial_cluster[y+half_y][x+half_x]

    def pos(self):
        return self.current_position_x, self.current_position_y

    def turn_right(self):
        if self.current_direction == "up":
            self.current_direction = "right"
        elif self.current_direction == "right":
            self.current_direction = "down"
        elif self.current_direction == "down":
            self.current_direction = "left"
        elif self.current_direction == "left":
            self.current_direction = "up"

    def turn_left(self):
        if self.current_direction == "up":
            self.current_direction = "left"
        elif self.current_direction == "left":
            self.current_direction = "down"
        elif self.current_direction == "down":
            self.current_direction = "right"
        elif self.current_direction == "right":
            self.current_direction = "up"

    def burst(self):
        if self.cluster[self.pos()] == "#":
            self.turn_right()
            self.cluster[self.pos()] = "."

        elif self.cluster[self.pos()] == ".":
            self.turn_left()

            self.cluster[self.pos()] = "#"
            self.infected_counter += 1
        
        self.move()

    def move(self):
        if self.current_direction == "up":
            self.current_position_y -= 1
        elif self.current_direction == "right":
            self.current_position_x += 1
        elif self.current_direction == "down":
            self.current_position_y += 1
        elif self.current_direction == "left":
            self.current_position_x -= 1

    def disp(self):
        print("Direction: %s, infected %d" % (self.current_direction, self.infected_counter))
        for y in range(-10, 10):
            row = ""
            for x in range(-10, 10):
                if x == self.current_position_x and y == self.current_position_y:
                    row += "[%s]" % self.cluster[(x, y)]
                else:
                    row += " %s " % self.cluster[(x, y)]
            print(row)


class VirusFromSecondTask(Virus):
    def burst(self):
        # clean
        if self.cluster[self.pos()] == ".":
            self.turn_left()
            self.cluster[self.pos()] = "W"
        # weaken
        elif self.cluster[self.pos()] == "W":
            self.cluster[self.pos()] = "#"
            self.infected_counter += 1
        # infected
        elif self.cluster[self.pos()] == "#":
            self.turn_right()
            self.cluster[self.pos()] = "F"

        # flagged
        elif self.cluster[self.pos()] == "F":
            self.turn_left()
            self.turn_left()
            self.cluster[self.pos()] = "."
        self.move()

def solve_first_task(filename):
    v = Virus(filename)

    for i in range(10000):
        v.burst()
    print("#1 Infected: %d" % v.infected_counter)

def solve_second_task(filename):
    v = VirusFromSecondTask(filename)

    for i in range(10000000):    
        v.burst()
    print("#2 Infected: %d" % v.infected_counter)


if __name__ == '__main__':
    # input_file = "day22_test.txt"
    input_file = "day22_input.txt"
    
    solve_first_task(input_file)
    solve_second_task(input_file)
