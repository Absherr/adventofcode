import unittest
from solution import convert_to_ascii_table, append_lengths_suffix, solve_second_task, xor, solve_first_task


class TestDay10(unittest.TestCase):
    def test_first_task(self):
        pass

    def test_second_task(self):
        self.assertEqual(solve_second_task(''), 'a2582a3a0e66e6e86e3812dcb672a272')
        self.assertEqual(solve_second_task('AoC 2017'), '33efeb34ea91902bb2f59c9920caa6cd')
        self.assertEqual(solve_second_task('1,2,3'), '3efbe78a8d82f29979031a4aa0b16a9d')
        self.assertEqual(solve_second_task('1,2,4'), '63960835bcdc130f0b66d7ff4f6a5a8e')

    def test_converting_to_ascii_table(self):
        self.assertEqual(convert_to_ascii_table("1,2,3"), [49,44,50,44,51])
        self.assertEqual(convert_to_ascii_table(""), [])

    def test_appending_suffix(self):
        self.assertEqual(append_lengths_suffix([49,44,50,44,51]), [49,44,50,44,51,17,31,73,47,23])
        self.assertEqual(append_lengths_suffix([]), [17,31,73,47,23])

    def test_xor(self):
        self.assertEqual(xor([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]), 64)


    def test_xor(self):
        self.assertEqual(solve_first_task([3, 4, 1, 5], list_length=5), ([3, 4, 2, 1, 0], 4, 4))


if __name__ == '__main__':
    unittest.main()
