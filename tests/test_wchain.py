import unittest
from src.wchain import *


class TestWchain(unittest.TestCase):
    def test_default_condition(self):
        write_output_file("wchain_in.txt", "wchain_out.txt")
        with open("../resources/wchain_out.txt", "r", encoding="utf-8") as wchain_out:
            result = int(wchain_out.readline())
        self.assertEqual(result, 6)

    def test_empty_wchain(self):
        write_output_file("empty_wchain_in.txt", "empty_wchain_out.txt")
        with open("../resources/empty_wchain_out.txt", "r", encoding="utf-8") as wchain_out:
            result = int(wchain_out.readline())
        self.assertEqual(result, 0)

    def test_wrong_filename(self):
        write_output_file("wrong_wchain_in.txt", "wrong_wchain_out.txt")
        with open("../resources/empty_wchain_out.txt", "r", encoding="utf-8") as wchain_out:
            result = int(wchain_out.readline())
        self.assertEqual(result, 0)
