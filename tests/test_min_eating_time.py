from src.min_eating_time import *
import unittest


class TestMinEatingSpeed(unittest.TestCase):

    def test_example_1(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(min_eating_speed(piles, h), 4)

    def test_example_2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(min_eating_speed(piles, h), 30)

    def test_example_3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(min_eating_speed(piles, h), 23)

    def test_h_lower_then_piles(self):
        piles = [30, 11, 23, 4, 20]
        h = 4
        self.assertEqual(min_eating_speed(piles, h), "The hours must be equal or greater then size of piles")


if __name__ == '__main__':
    unittest.main()
