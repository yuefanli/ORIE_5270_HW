import unittest
from Tree.Tree import Tree
from Tree.Tree import Node


class TestTree(unittest.TestCase):
    def test_tree_one_node(self):
        node_a = Node(10)
        tree = Tree(node_a)
        answer = [['10']]
        assert tree.tree_print() == answer

    def test_tree_full(self):
        node_4_1 = Node(8)
        node_4_2 = Node(9)
        node_4_3 = Node(10)
        node_4_4 = Node(11)
        node_4_5 = Node(12)
        node_4_6 = Node(13)
        node_4_7 = Node(14)
        node_4_8 = Node(15)
        node_3_1 = Node(4, node_4_1, node_4_2)
        node_3_2 = Node(5, node_4_3, node_4_4)
        node_3_3 = Node(6, node_4_5, node_4_6)
        node_3_4 = Node(7, node_4_7, node_4_8)
        node_2_1 = Node(2, node_3_1, node_3_2)
        node_2_2 = Node(3, node_3_3, node_3_4)
        node_1_1 = Node(1, node_2_1, node_2_2)
        tree = Tree(node_1_1)
        answer = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                  ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '3', '|', '|', '|'],
                  ['|', '4', '|', '|', '|', '5', '|', '|', '|', '6', '|', '|', '|', '7', '|'],
                  ['8', '|', '9', '|', '10', '|', '11', '|', '12', '|', '13', '|', '14', '|', '15']]
        assert tree.tree_print() == answer

    def test_tree_single(self):
        node_4_1 = Node(4)
        node_3_1 = Node(3, node_4_1, None)
        node_2_1 = Node(2, node_3_1, None)
        node_1_1 = Node(1, node_2_1, None)
        tree = Tree(node_1_1)
        answer = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                  ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                  ['|', '3', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                  ['4', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        assert tree.tree_print() == answer

    def test_tree_exotic(self):
        node_4_6 = Node(8)
        node_3_2 = Node(7)
        node_3_3 = Node(5, None, node_4_6)
        node_2_1 = Node(4, None, node_3_2)
        node_2_2 = Node(3, node_3_3, None)
        node_1_1 = Node(1, node_2_1, node_2_2)
        tree = Tree(node_1_1)
        answer = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                  ['|', '|', '|', '4', '|', '|', '|', '|', '|', '|', '|', '3', '|', '|', '|'],
                  ['|', '|', '|', '|', '|', '7', '|', '|', '|', '5', '|', '|', '|', '|', '|'],
                  ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '8', '|', '|', '|', '|']]
        assert tree.tree_print() == answer
