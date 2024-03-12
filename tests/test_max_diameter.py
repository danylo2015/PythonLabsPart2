from src.max_diameter import *
import unittest


class TestDiameter(unittest.TestCase):
    def test_example(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.right.right = BinaryTree(5)
        root.left.left.left.left = BinaryTree(9)
        root.left.right.right.right = BinaryTree(6)
        self.assertEqual(diameter(root), 6)

    def test_example_1(self):
        root = BinaryTree(100)
        root.left = BinaryTree(50)
        root.right = BinaryTree(120)
        root.left.left = BinaryTree(10)
        root.right.right = BinaryTree(125)
        root.right.left = BinaryTree(105)
        root.left.right = BinaryTree(71)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(12)
        root.left.left.left.left = BinaryTree(6)
        root.left.left.left.left.left = BinaryTree(5)
        root.left.left.right.right = BinaryTree(15)
        root.left.left.right.right.right = BinaryTree(18)
        root.left.left.right.right.right.left = BinaryTree(19)
        root.left.left.right.right.right.left.left = BinaryTree(20)
        self.assertEqual(diameter(root), 9)


