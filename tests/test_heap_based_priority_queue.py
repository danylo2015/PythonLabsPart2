from src.heap_based_priority_queue import *
import unittest


class TestPriorityQueue(unittest.TestCase):

    def test_example_1(self):
        pq = PriorityQueue()

        pq.insert('1', 3)
        pq.insert('2', 1)
        pq.insert('3', 8)
        pq.insert('4', 8)
        pq.insert('5', 4)
        pq.insert('6', 8)
        self.assertEqual(pq.view(), None)

    def test_example_2(self):
        pq = PriorityQueue()

        pq.insert('1', 4)
        pq.insert('2', 4)
        pq.insert('3', 4)
        pq.insert('4', 4)
        pq.insert('5', 4)
        pq.insert('6', 4)

        self.assertEqual(pq.view(), None)

    def test_example_3(self):
        pq = PriorityQueue()

        with self.assertRaises(Exception) as context:
            pq.remove_max_priority()

        self.assertEqual(str(context.exception), "Queue is empty")