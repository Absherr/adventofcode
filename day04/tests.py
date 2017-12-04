import unittest
from solution import validation_method_for_first_task, validation_method_for_second_task


class TestDay4(unittest.TestCase):
    def test_first_task(self):
        self.assertTrue(validation_method_for_first_task("aa bb cc dd ee".split()))
        self.assertFalse(validation_method_for_first_task("aa bb cc dd aa".split()))
        self.assertTrue(validation_method_for_first_task("aa bb cc dd aaa".split()))

    def test_second_task(self):
        self.assertTrue(validation_method_for_second_task("abcde fghij".split()))
        self.assertFalse(validation_method_for_second_task("abcde xyz ecdab".split()))
        self.assertTrue(validation_method_for_second_task("a ab abc abd abf abj".split()))
        self.assertTrue(validation_method_for_second_task("iiii oiii ooii oooi oooo".split()))
        self.assertFalse(validation_method_for_second_task("oiii ioii iioi iiio".split()))


if __name__ == '__main__':
    unittest.main()
