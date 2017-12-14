def convert_to_ascii_table(data):
    result = []
    for char in data:
        result.append(ord(char))
    return result

def append_lengths_suffix(data):
    return data + [17, 31, 73, 47, 23]

def perform_tying_rount(data, list_to_be_tied, current_position, skip_size, list_length=256):
    for length in data:
        old_list = list(list_to_be_tied)
        for i in range(length):
            l = (current_position + i) % list_length
            r = (current_position + length - i - 1) % list_length
            list_to_be_tied[l] = old_list[r]

        current_position = (current_position + length + skip_size) % list_length
        skip_size += 1

    return list_to_be_tied, current_position, skip_size

def solve_first_task(data, list_length=256):
    list_to_be_tied = list(range(list_length))
    current_position = 0
    skip_size = 0

    return perform_tying_rount(data, list_to_be_tied, 0, 0, list_length)

def xor(l):
    result = 0
    for item in l:
        result ^= item
    return result

def calculate_sparse_hash(list_to_be_tied, data, list_length=256):
    current_position = 0
    skip_size = 0

    # prepare sparse hash
    for i in range(64):
        list_to_be_tied, current_position, skip_size = perform_tying_rount(data, list_to_be_tied, current_position, skip_size, list_length)
    
    return list_to_be_tied

def calculate_hash(data, list_length=256):
    data = append_lengths_suffix(convert_to_ascii_table(data))

    sparse_hash = calculate_sparse_hash(list(range(list_length)), data, list_length)

    dense_hash = [xor(sparse_hash[i*16:(i+1)*16]) for i in range(list_length//16)]

    result_hash = "".join(["{:02x}".format(num) for num in dense_hash])

    return result_hash

class Board:
    def __init__(self):
        self.board = []

    def add_row(self, row):
        self.board.append(row)

    def find_any_one(self):
        for row_index, row in enumerate(self.board):
            if "1" in  row:
                return (row_index, row.index("1"))
        return None

    def process_region(self, row_index, pos):
        if 0 <= row_index < 128 and 0 <= pos < 128:
            if self.board[row_index][pos] == "1":
                self.board[row_index][pos] = "X"
                for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
                    try:
                        self.process_region(row_index+dx, pos+dy)
                    except IndexError as e:
                        pass

    def count_regions(self):
        region = 0

        position = self.find_any_one()
        while position is not None:
            row_index, pos = position
            self.process_region(row_index, pos)
            position = self.find_any_one()
            region += 1

        return region

if __name__ == "__main__":
    # data = "flqrgnkx"
    data = "xlqgujun"

    board = Board()

    no_of_squares = 0

    for i in range(128):
        knot_hash = calculate_hash("%s-%d" % (data, i))

        row = "".join("{0:04b}".format(int(single_hex, 16)) for single_hex in knot_hash)
        
        no_of_squares += row.count("1")

        board.add_row(list(row))

    print(no_of_squares)

    print(board.count_regions())
