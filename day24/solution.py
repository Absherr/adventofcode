from collections import namedtuple

Component = namedtuple("Component", ['left', 'right'])

def load_component(filename):
	components = []

	with open(filename, "r") as f:
		for line in f.readlines():
			line = map(int, line.strip().split("/"))
			components.append(Component(*line))
	return components

def filter_matching_parts(end, components):
	matching_parts = list(filter(lambda c: end in [c.left, c.right], components))
	return matching_parts

def find_bridges(filename):
	components = load_component(filename)

	starting_parts = filter_matching_parts(0, components)

	bridges = []
	
	for starting_part in starting_parts:
		c = list(components)
		c.remove(starting_part)
		if starting_part.left == 0:
			end = starting_part.right
		else:
			end = starting_part.left

		bridges.extend(_find_bridges(end, [starting_part,], c))

	return bridges

def _find_bridges(end, already_used_parts, parts_left):
	matching_parts = filter_matching_parts(end, parts_left)
	
	if matching_parts:
		results = []
		for matching_part in matching_parts:
			if matching_part.left == end:
				new_end = matching_part.right
			else:
				new_end = matching_part.left
			c = list(parts_left)
			c.remove(matching_part)
			
			results.extend(_find_bridges(new_end, already_used_parts+[matching_part,], c))
		
		return results
	else:
		return [already_used_parts, ]

def calculate_strenght(bridge):
	bridge_strenght = 0
	for part in bridge:
		bridge_strenght += part.left + part.right
	return bridge_strenght

def find_strength_of_the_strongest_bridge(bridges):
	max_str = -1
	for bridge in bridges:
		bridge_strenght = calculate_strenght(bridge)
		if bridge_strenght > max_str:
			max_str = bridge_strenght
	return max_str

def find_the_longest_bridge(bridges):
	max_len = len(max(bridges, key=len))
	the_longest_bridges = list(filter(lambda b: len(b)==max_len, bridges))

	return the_longest_bridges


if __name__ == '__main__':
	bridges = find_bridges("day24_input.txt")
	# bridges = find_bridges("day24_test.txt")

	print("#1: %d" % find_strength_of_the_strongest_bridge(bridges))
	print("#2: %d" % find_strength_of_the_strongest_bridge(find_the_longest_bridge(bridges)))
