def flip_horizontally(mat):
    return tuple(row[::-1] for row in mat)

def flip_vertically(mat):
    return tuple(row for row in mat[::-1])

def transpose(mat):
    z = zip(*mat)
    return tuple("".join(row) for row in z)

def rotate_counter_clockwise(pattern):
    return transpose(flip_horizontally(pattern))

def rotate_clockwise(pattern):
    return transpose(flip_vertically(pattern))

def get_rotated_patterns(pattern):
    f = set()
    mat = tuple(pattern)
    f.add(mat)
    for i in range(3):
        mat = rotate_clockwise(mat)
        f.add(mat)
    return f

def collect_all_modifications(pattern):
    found = set()

    found.update(get_rotated_patterns(pattern))

    mat = flip_vertically(pattern)
    found.update(get_rotated_patterns(mat))

    mat = flip_horizontally(pattern)
    found.update(get_rotated_patterns(mat))

    return tuple(found)

def generate_next_art(art):
    if len(art) % 2 == 0:
        square_size = 2 
    else:
        square_size = 3

    squares_count_on_each_axis = len(art) / square_size

    next_art = ["" for _ in range(squares_count_on_each_axis + len(art))]

    for x in range(squares_count_on_each_axis):
        for y in range(squares_count_on_each_axis):
            # position of top left corner of analyzed square in old art
            left = x * square_size
            top = y * square_size

            square = tuple([item[left:left+square_size] for item in art[top:top+square_size]])

            found = False
            for mod in patterns[square_size]:
                if square in mod:
                    found = True
                    result = patterns[square_size][mod]
                    
                    # copy result of using pattern to new art
                    for r_index, r in enumerate(result):
                        next_art[top+y+r_index] += r
                    break
            if not found:
                raise Exception("Pattern not found for square: %s" % ("/".join(square)))
    return next_art

def load_patterns(filename):
    patterns = {2: {}, 3: {}}

    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            pattern, result = line.split("=>")

            pattern = tuple(pattern.strip().split("/"))
            result = tuple(result.strip().split("/"))

            all_modifications = collect_all_modifications(pattern)
            patterns[len(pattern)][all_modifications] = result

    return patterns


if __name__ == '__main__':
    art = ['.#.', '..#', '###']
    patterns = load_patterns("day21_input.txt")
    # patterns = load_patterns("day21_test.txt")
    iterations = 18

    for i in range(iterations):
        art = generate_next_art(art)
        print("Iteration: %d [size: %d/hashes: %d]" % (i+1, len(art), "".join(art).count("#")))
