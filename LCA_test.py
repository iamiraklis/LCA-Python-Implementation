import unittest
import LCA
from LCA import Node


class TestLCA(unittest.TestCase):

    def test_lca(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(19)
        root.left.left = Node(1)
        root.left.right = Node(6)
        root.right.left = Node(17)
        root.right.right = Node(21)
        self.assertEqual(LCA.findLCA(root, 1, 6), 5)
        self.assertEqual(LCA.findLCA(root, 17, 21), 19)
        self.assertEqual(LCA.findLCA(root, 1, 21), 10)
        self.assertEqual(LCA.findLCA(root, 4, 19), -1)


    def test_null(self):
        root = None
        self.assertEqual(LCA.findLCA(root, 1, 6), -1)
