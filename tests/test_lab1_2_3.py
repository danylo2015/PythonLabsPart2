import unittest
from src.lab1_2_3 import *


class QuickSortTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(quick_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(quick_sort([4, 3, 2, 1]), [4, 3, 2, 1])

    def test_unsorted_list(self):
        unsorted_list = [4, 2, 6, 1, 3, 5]
        expected_sorted = [6, 5, 4, 3, 2, 1]
        self.assertEqual(quick_sort(unsorted_list), expected_sorted)

    def test_find_kth_largest_valid_k(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        expected_output = f"The {k} largest element in list is: 22, the index of the element in the original list is:2"
        self.assertEqual(find_kth_largest_el(arr.copy(), k), expected_output)


if __name__ == '__main__':
    unittest.main()
