import unittest
from solution import Program, hex_distance


class TestDay11(unittest.TestCase):
    def test_moving_n(self):
        p = Program()
        p.q = 3
        p.r = 3

        p.move("n")

        self.assertEqual(p.q, 3)
        self.assertEqual(p.r, 2)
    
    def test_moving_s(self):
        p = Program()
        p.q = 3
        p.r = 3

        p.move("s")

        self.assertEqual(p.q, 3)
        self.assertEqual(p.r, 4)

    def test_moving_ne_from_even_column(self):
        p = Program()
        p.q = 4
        p.r = 3

        p.move("ne")

        self.assertEqual(p.q, 5)
        self.assertEqual(p.r, 3)

    def test_moving_ne_from_odd_column(self):
        p = Program()
        p.q = 3
        p.r = 3
        
        p.move("ne")

        self.assertEqual(p.q, 4)
        self.assertEqual(p.r, 2)

    def test_moving_nw_from_even_column(self):
        p = Program()
        p.q = 4
        p.r = 3

        p.move("nw")

        self.assertEqual(p.q, 3)
        self.assertEqual(p.r, 3)

    def test_moving_nw_from_odd_column(self):
        p = Program()
        p.q = 3
        p.r = 3

        p.move("nw")

        self.assertEqual(p.q, 2)
        self.assertEqual(p.r, 2)

    def test_moving_se_from_even_column(self):
        p = Program()
        p.q = 4
        p.r = 3

        p.move("se")

        self.assertEqual(p.q, 5)
        self.assertEqual(p.r, 4)

    def test_moving_se_from_odd_column(self):
        p = Program()
        p.q = 3
        p.r = 3
        
        p.move("se")

        self.assertEqual(p.q, 4)
        self.assertEqual(p.r, 3)

    def test_moving_sw_from_even_column(self):
        p = Program()
        p.q = 4
        p.r = 3

        p.move("sw")

        self.assertEqual(p.q, 3)
        self.assertEqual(p.r, 4)

    def test_moving_sw_from_odd_column(self):
        p = Program()
        p.q = 3
        p.r = 3
        
        p.move("sw")

        self.assertEqual(p.q, 2)
        self.assertEqual(p.r, 3)

    def test_distance_for_self(self):
        self.assertEqual(hex_distance(Program(2,2), Program(2,2)), 0)

    def test_distances_for_neighbours(self):
        target = Program(3, 3)

        self.assertEqual(hex_distance(Program(2,2), target), 1)
        self.assertEqual(hex_distance(Program(3,2), target), 1)
        self.assertEqual(hex_distance(Program(4,2), target), 1)
        self.assertEqual(hex_distance(Program(4,3), target), 1)
        self.assertEqual(hex_distance(Program(3,4), target), 1)
        self.assertEqual(hex_distance(Program(2,3), target), 1)

    def test_empty_path(self):
        program = Program()
        program.move_along("")
        self.assertEqual(program.distance_from_zero(), 0)
        self.assertEqual(program.max_dist, 0)

    def test_moving_along_path_1(self):
        program = Program()
        program.move_along("ne,ne,ne")
        self.assertEqual(program.distance_from_zero(), 3)
        self.assertEqual(program.max_dist, 3)

    def test_moving_along_path_2(self):
        program = Program()
        program.move_along("ne,ne,sw,sw")
        self.assertEqual(program.distance_from_zero(), 0)
        self.assertEqual(program.max_dist, 2)

    def test_moving_along_path_3(self):
        program = Program()
        program.move_along("ne,ne,s,s")
        self.assertEqual(program.distance_from_zero(), 2)
        self.assertEqual(program.max_dist, 2)

    def test_moving_along_path_4(self):
        program = Program()
        program.move_along("se,sw,se,sw,sw")
        self.assertEqual(program.distance_from_zero(), 3)
        self.assertEqual(program.max_dist, 3)


if __name__ == '__main__':
    unittest.main()
