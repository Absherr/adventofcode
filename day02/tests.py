import unittest
from solution import calculate_first_checksum, calculate_second_checksum


class TestDay2(unittest.TestCase):
    def test_first_task(self):
        self.assertEqual(calculate_first_checksum("task1_input.txt"), 18)

    def test_second_task(self):
        self.assertEqual(calculate_second_checksum("task2_input.txt"), 9)


if __name__ == '__main__':
    unittest.main()
