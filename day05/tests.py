import unittest
from solution import change_number_for_task1, change_number_for_task2, solve, load_instructions


class TestDay4(unittest.TestCase):
    def test_changing_numbers_for_first_task(self):
        self.assertEquals(change_number_for_task1(0), 1)
        self.assertEquals(change_number_for_task1(1), 2)
        self.assertEquals(change_number_for_task1(-1), 0)

    def test_changing_numbers_for_second_task(self):
        self.assertEquals(change_number_for_task2(1), 2)
        self.assertEquals(change_number_for_task2(2), 3)
        self.assertEquals(change_number_for_task2(3), 2)
        self.assertEquals(change_number_for_task2(4), 3)
        self.assertEquals(change_number_for_task2(4), 3)

    def test_first_task(self):
        self.assertEquals(solve(load_instructions("day05_test.txt"), change_number_for_task1), 5)

    def test_second_task(self):
        self.assertEquals(solve(load_instructions("day05_test.txt"), change_number_for_task2), 10)


if __name__ == '__main__':
    unittest.main()
