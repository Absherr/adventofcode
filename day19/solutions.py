def load_routing(filename):
    routing = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")

            routing.append(line)
    return routing


def solve(filename):
    letters = "ZXCVBNMASDFGHJKLQWERTYUIOP"
    walkable_characters = list(letters+"|-+")

    routing = load_routing(filename)

    # direction constans
    DOWN = 0
    UP = 1
    LEFT = 2
    RIGHT = 3

    # current position & direction
    pos_x = 0
    pos_y = 0
    direction = DOWN

    # result
    letters_visited = ""
    steps = 0

    # starting position
    for index, char in enumerate(routing[0]):
        if char == "|":
            pos_x = index
            pos_y = 0
            break

    char_under = routing[pos_y][pos_x]
    while char_under in walkable_characters:
        steps += 1

        # is there is a letter under - remember it
        if char_under in letters:
            letters_visited += char_under

        # if it is crossroad
        if char_under == "+":
            neighbours_to_check = {
                (0, -1): LEFT, 
                (0, 1): RIGHT, 
                (-1, 0): UP, 
                (1, 0): DOWN
            }
            # make sure that we wont do 180* turn
            if direction == DOWN:
                del neighbours_to_check[(-1,0)]
            elif direction == UP:
                del neighbours_to_check[(1,0)]
            elif direction == LEFT:
                del neighbours_to_check[(0,1)]
            elif direction == RIGHT:
                del neighbours_to_check[(0,-1)]

            # check neighbours for any walkable character
            for dy, dx in neighbours_to_check:
                try:
                    if routing[pos_y+dy][pos_x+dx] in walkable_characters:
                        direction = neighbours_to_check[(dy, dx)]
                        pos_x += dx
                        pos_y += dy
                        break
                except IndexError:
                    pass
        else:
            # just walking along
            if direction == DOWN:
                pos_y += 1
            elif direction == UP:
                pos_y -= 1
            elif direction == LEFT:
                pos_x -= 1
            elif direction == RIGHT:
                pos_x += 1

        char_under = routing[pos_y][pos_x]

    return (letters_visited, steps)


if __name__ == '__main__':
    print(solve("day19_test.txt"))
    print(solve("day19_input.txt"))
