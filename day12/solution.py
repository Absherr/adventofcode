from collections import deque

def load_pipes(filename):
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip().replace(",", "").replace("<->", "").split()
            yield (line[0], line[1:])

def load_graph(filename):
    graph = {}
    for pipe_start, pipe_destinations in load_pipes(filename):
        graph[pipe_start] = pipe_destinations
    return graph

def extract_group(starting_program, graph):
    programs_in_group = []

    programs_to_be_visited = deque()
    programs_to_be_visited.append(starting_program)

    while len(programs_to_be_visited):
        program_to_check = programs_to_be_visited.pop()

        for piping in graph[program_to_check]:
            if piping not in programs_in_group:
                programs_in_group.append(piping)
                programs_to_be_visited.append(piping)

    return programs_in_group

def solve_first_task(graph):
    return len(extract_group("0", graph))

def solve_second_task(graph):
    nodes = deque(graph.keys())
    groups_counter = 0

    while len(nodes):
        n = nodes.pop()
        
        group = extract_group(n, graph)
        for item_in_group in group:
            try:
                nodes.remove(item_in_group)
            except ValueError, e:
                pass
        groups_counter += 1

    return groups_counter


if __name__ == "__main__":
    graph = load_graph("day12_input.txt")

    print(solve_first_task(graph))
    print(solve_second_task(graph))
