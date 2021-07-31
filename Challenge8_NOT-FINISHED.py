# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1
# ________________________________________
#
#


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node:{}, Left:{}, Right:{}".format(self.val, self.left, self.right)


tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))


def count_unival_tree(tree: Node) -> int:
    pass
