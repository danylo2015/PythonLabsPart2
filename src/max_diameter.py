class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1


def diameter(tree: BinaryTree) -> int:
    if tree is None:
        return 0

    left_height = height(tree.left)
    right_height = height(tree.right)

    left_diameter = diameter(tree.left)
    right_diameter = diameter(tree.right)

    return max(left_height + right_height, max(left_diameter, right_diameter))
