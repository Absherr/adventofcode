class Particle:
    def __init__(self, name, x, y, z, v_x, v_y, v_z, a_x, a_y, a_z):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.v_x = int(v_x)
        self.v_y = int(v_y)
        self.v_z = int(v_z)
        self.a_x = int(a_x)
        self.a_y = int(a_y)
        self.a_z = int(a_z)

    def dist(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def update_velocity(self):
        self.v_x += self.a_x
        self.v_y += self.a_y
        self.v_z += self.a_z

    def update_position(self):
        self.x += self.v_x
        self.y += self.v_y
        self.z += self.v_z

    def pos(self):
        return self.x, self.y, self.z

    def __str__(self):
        return "%s p=<%d,%d,%d> v=<%d,%d,%d> a=<%d,%d,%d> [D: %d]" % (self.name, self.x, self.y, self.z, self.v_x, self.v_y, self.v_z, self.a_x, self.a_y, self.a_z, self.dist())


def tick(particles):
    for particle in particles:
        particle.update_velocity()
        particle.update_position()


def check_collisions(particles):
    points_where_collision_happened = []
    memory = {}

    for particle in particles:
        pos = particle.pos()
        if pos in memory:
            # second particle in the same spot
            points_where_collision_happened.append(pos)
            del memory[pos]
        elif pos in points_where_collision_happened:
            # next particle in the same spot
            pass
        else:
            memory[pos] = particle

    return memory.values()


def find_closest_to_zero(particles):
    min_p = particles[0]
    min_d = particles[0].dist()

    for p in particles:
        if p.dist() < min_d:
            min_d = p.dist()
            min_p = p
    
    return min_p

def solve_first_task(particles, iterations):
    for i in range(iterations):
        tick(particles)
    return find_closest_to_zero(particles)


def solve_second_task(particles, iterations):
    for i in range(iterations):
        tick(particles)
        particles = check_collisions(particles)
    return len(particles)


def load_particles(filename):
    particles = []

    with open(filename) as f:
        for line_index, line in enumerate(f.readlines()):
            line = line.replace("p=<", "").replace(">, v=<",",").replace(">, a=<", ",").replace(">", "").strip().split(",")
            p = Particle(line_index, *line)

            particles.append(p)

        print("Loaded %d particles" % len(particles))

    return particles

if __name__ == '__main__':
    long_run = 2000

    particles = load_particles("day20_input.txt")
    print(solve_first_task(particles, long_run))
    
    particles = load_particles("day20_input.txt")
    print(solve_second_task(particles, long_run))
