import unittest
from solution import solve_first_task, solve_second_task


class TestDay9(unittest.TestCase):
    def test_first_task(self):
        self.assertEqual(solve_first_task("{}"), 1)
        self.assertEqual(solve_first_task("{{{}}}"), 6)
        self.assertEqual(solve_first_task("{{},{}}"), 5)
        self.assertEqual(solve_first_task("{{{},{},{{}}}}"), 16)
        self.assertEqual(solve_first_task("{<a>,<a>,<a>,<a>}"), 1)
        self.assertEqual(solve_first_task("{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)
        self.assertEqual(solve_first_task("{{<!!>},{<!!>},{<!!>},{<!!>}}"), 9)
        self.assertEqual(solve_first_task("{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)

    def test_second_task(self):
        self.assertEqual(solve_second_task('<>'), 0)
        self.assertEqual(solve_second_task('<random characters>'), 17)
        self.assertEqual(solve_second_task('<<<<>'), 3)
        self.assertEqual(solve_second_task('<{!>}>'), 2)
        self.assertEqual(solve_second_task('<!!>'), 0)
        self.assertEqual(solve_second_task('<!!!>>'), 0)
        self.assertEqual(solve_second_task('<{o"i!a,<{i<a>'), 10)


if __name__ == '__main__':
    unittest.main()
