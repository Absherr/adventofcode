def convert_to_ascii_table(data):
    result = []
    for char in data:
        result.append(ord(char))
    return result

def append_lengths_suffix(lengths):
    return lengths + [17, 31, 73, 47, 23]

def perform_tying_rount(lenghts, list_to_be_tied, current_position, skip_size, list_length=256):
    for length in lenghts:
        old_list = list(list_to_be_tied)
        for i in range(length):
            l = (current_position + i) % list_length
            r = (current_position + length - i - 1) % list_length
            list_to_be_tied[l] = old_list[r]

        current_position = (current_position + length + skip_size) % list_length
        skip_size += 1

    return list_to_be_tied, current_position, skip_size

def solve_first_task(lengths, list_length=256):
    list_to_be_tied = list(range(list_length))
    current_position = 0
    skip_size = 0

    return perform_tying_rount(lengths, list_to_be_tied, 0, 0, list_length)

def xor(l):
    result = 0
    for item in l:
        result ^= item
    return result

def calculate_sparse_hash(list_to_be_tied, lengths, list_length=256):
    current_position = 0
    skip_size = 0

    # prepare sparse hash
    for i in range(64):
        list_to_be_tied, current_position, skip_size = perform_tying_rount(lengths, list_to_be_tied, current_position, skip_size, list_length)
    
    return list_to_be_tied

def solve_second_task(lengths, list_length=256):
    lengths = append_lengths_suffix(convert_to_ascii_table(lengths))

    sparse_hash = calculate_sparse_hash(list(range(list_length)), lengths, list_length)

    dense_hash = [xor(sparse_hash[i*16:(i+1)*16]) for i in range(list_length//16)]

    result_hash = "".join(["{:02x}".format(num) for num in dense_hash])

    return result_hash


if __name__ == "__main__":
    l = solve_first_task([106, 16, 254, 226, 55, 2, 1, 166, 177, 247, 93, 0, 255, 228, 60, 36])
    print(l)

    l = solve_second_task("106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36")
    print(l)
