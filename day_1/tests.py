import unittest
from solution import solve_first_task, solve_second_task


class TestDay1(unittest.TestCase):
    def test_first_task(self):
        self.assertEqual(solve_first_task("1122"), 3)
        self.assertEqual(solve_first_task("1111"), 4)
        self.assertEqual(solve_first_task("1234"), 0)
        self.assertEqual(solve_first_task("91212129"), 9)

    def test_second_task(self):
        self.assertEqual(solve_second_task("1212"), 6)
        self.assertEqual(solve_second_task("1221"), 0)
        self.assertEqual(solve_second_task("123425"), 4)
        self.assertEqual(solve_second_task("123123"), 12)
        self.assertEqual(solve_second_task("12131415"), 4)


if __name__ == '__main__':
    unittest.main()
