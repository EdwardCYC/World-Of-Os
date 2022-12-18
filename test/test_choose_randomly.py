import unittest

from main import choose_randomly


class TestChooseRandomly(unittest.TestCase):
    def test_should_return_one(self):
        self.assertEqual(choose_randomly(0), 1)
        self.assertEqual(choose_randomly(0.59), 1)
        self.assertEqual(choose_randomly(0.60), 1)

    def test_should_return_two(self):
        self.assertEqual(choose_randomly(0.61), 2)
        self.assertEqual(choose_randomly(0.80), 2)

    def test_should_return_three(self):
        self.assertEqual(choose_randomly(0.81), 3)
        self.assertEqual(choose_randomly(1), 3)


if __name__ == '__main__':
    unittest.main()
