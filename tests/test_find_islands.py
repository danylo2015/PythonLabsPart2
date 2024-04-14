import unittest
from src.find_islands import *


class TestFindIslands(unittest.TestCase):
    def test_count_islands(self):
        graph = [
            ["1", "0", "1", "0", "0", "0", "1", "1", "1", "1"],
            ["0", "0", "1", "0", "1", "0", "1", "0", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "1", "0", "0", "0"],
            ["1", "0", "0", "1", "0", "1", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1"],
            ["0", "1", "0", "1", "0", "0", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0", "1", "1", "1", "0", "0"],
            ["0", "0", "0", "1", "0", "0", "1", "1", "1", "0"],
            ["1", "0", "1", "0", "1", "0", "0", "1", "0", "0"],
            ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1"]
        ]
        self.assertEqual(count_islands(graph), 5)

    def test_no_islands(self):
        graph = [
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        ]
        self.assertEqual(count_islands(graph), 0)

    def test_empty_matrix(self):
        graph = []
        self.assertEqual(count_islands(graph), 0)

    def test_island(self):
        graph = [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ]
        self.assertEqual(count_islands(graph), 1)

    def test_non_square_matrix(self):
        graph = [
            ["1", "1", "0", "1", "1", "0"],
            ["0", "0", "0", "1", "0", "1"],
            ["1", "1", "0", "1", "0", "1"]
        ]
        self.assertEqual(count_islands(graph), 3)