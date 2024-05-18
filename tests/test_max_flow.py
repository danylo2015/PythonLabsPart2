import unittest
from src.max_flow import max_flow


class TestFlowersMaxFlow(unittest.TestCase):
    def test_farms_stores_graph(self):
        result = max_flow("../resources/roads.csv")
        self.assertEqual(result, 16)

    def test_empty_input(self):
        result = max_flow("../resources/empty_roads.csv")
        self.assertEqual(result, None)
