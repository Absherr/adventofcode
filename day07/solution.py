class Program(object):
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = int(weight)
        self.children_weights = []
        self.balancing_weights = 0
        self.children = []
        self.parent = None
        self.level = 0

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def set_weight(self, weight):
        self.weight = int(weight)

    def __str__(self):
        try:
            c = ",".join([c.name for c in self.children])
        except AttributeError, e:
            c = "[]"

        try:
            p = self.parent.name
        except AttributeError, e:
            p = "None"
        
        return "%s (L: %d, parent: %s, child: %s, w: %d)" % (self.name, self.level, p, c, self.weight)


class ProgramsCache(object):
    def __init__(self):
        self.cache = {}

    def get(self, name):
        return self.cache[name]

    def save(self, program):
        self.cache[program.name] = program

    def get_parentless(self):
        for program in self.cache.values():
            if program.parent is None:
                return program

    def show(self):
        for program in self.cache.values():
            print(program)

    def has(self, name):
        return name in self.cache

    def calculate_weights(self):
        self._calculate_weights(self.get_parentless(), 0)

    def _calculate_weights(self, node, level):
        balancing_weights = node.weight

        children_weights = []
        node.level = level
        for c in node.children:
            c_w = self._calculate_weights(c, level+1)
            children_weights.append(c_w)
            balancing_weights += c_w

        node.children_weights = children_weights
        node.balancing_weights = balancing_weights

        return balancing_weights

    def get_unbalanced_nodes(self):
        unbalanced_nodes = []
        for program in self.cache.values():
            if len(set(program.children_weights)) > 1:
                
                unbalanced_nodes.append(program)
        return unbalanced_nodes

    def get_lowest_unbalanced_node(self):
        return max(self.get_unbalanced_nodes(), key=lambda x: x.level)

    def get_different_children_weight(self, node):
        if len(node.children_weights) < 3:
            raise Exception("Can decide which child is different!")
        

def generate_cache(filename):
    programs = ProgramsCache()

    with open(filename, "r") as program_file:
        for line in program_file.readlines():
            split = line.strip().replace(',', '').split()
            name = split[0]
            weight = split[1][1:-1]

            if programs.has(name):
                p = programs.get(name)
                p.set_weight(weight)
            else:
                p = Program(name, weight)
                programs.save(p)

            for i in range(3, len(split)):
                c_name = split[i]
                if programs.has(c_name):
                    c = programs.get(c_name)
                else:
                    c = Program(c_name)
                    programs.save(c)

                c.set_parent(p)
                p.add_child(c)

    programs.calculate_weights()
    return programs


if __name__ == "__main__":
    cache = generate_cache("day07_input.txt")

    un = cache.get_lowest_unbalanced_node()
    print(un.name)
    print(un.balancing_weights)
    print(un.children_weights)
    for c in un.children:
        print("    " + str(c) + " " + str(c.balancing_weights))
    