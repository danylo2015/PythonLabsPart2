from src.piority_queue_heap import *
import unittest


class TestPriorityQueue(unittest.TestCase):

    def test_example_1(self):
        pq = PriorityQueue()

        pq.insert('Task 1', 3)
        pq.insert('Task 2', 1)
        pq.insert('Task 3', 8)
        pq.insert('Task 4', 8)
        pq.insert('Task 5', 4)
        pq.insert('Task 6', 8)
        self.assertEqual(pq.view(), ['Task 3', 'Task 4', 'Task 6', 'Task 2', 'Task 5', 'Task 1'])

    def test_example_2(self):
        pq = PriorityQueue()

        pq.insert('Task 1', 3)
        pq.insert('Task 2', 1)
        pq.insert('Task 3', 8)
        pq.insert('Task 4', 8)
        pq.insert('Task 5', 4)
        pq.insert('Task 6', 8)

        pq.remove_max_priority()
        pq.remove_max_priority()
        self.assertEqual(pq.view(), ['Task 6', 'Task 5', 'Task 1', 'Task 2'])
