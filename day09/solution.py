from re import sub, findall

def remove_exclamation_marks_and_ignored_chars(stream):
    return sub("!.", "", stream)

def remove_garbage(stream):
    return sub("<.*?>", "", stream)

def remove_commas(stream):
    return sub(",", "", stream)

def load_stream(filename):
    stream = ""
    with open(filename, "r+") as f:
        stream = f.read().strip()
    return stream

def solve_first_task(stream):
    stream = remove_commas(remove_garbage(remove_exclamation_marks_and_ignored_chars(stream)))
    
    result = 0
    level = 0

    for char in stream:
        if char == "{":
            level += 1
        elif char == "}":
            result += level
            level -= 1
        else:
            raise Exception("idk what it is! " + char)
    return result

def solve_second_task(stream):
    result = 0
    stream = remove_exclamation_marks_and_ignored_chars(stream)
    garbage_items = findall("<.*?>", stream)
    for garbage in garbage_items:
        garbage_content = garbage[1:-1]
        result += len(garbage_content)
    return result


if __name__ == "__main__":
    stream = load_stream("day09_input.txt")
    scores = solve_first_task(stream)
    print(scores)

    garbage_content = solve_second_task(stream)
    print(garbage_content)
