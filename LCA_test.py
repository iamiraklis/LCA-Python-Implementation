import unittest
import LCA
from LCA import Node


class TestLCA(unittest.TestCase):

    def test_null(self):
        self.assertEqual(LCA.dagLCA(None, 4, 6), None)

    def test_lca(self):

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.root.data, LCA.r3.data).data, 1)

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.r2, LCA.r2), 2)

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.r3, LCA.root), 1)

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.r2, LCA.r3), 1)

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.r2, LCA.r4), 1)

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.r3, LCA.r4), 1)

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.r2, LCA.r5), 1)

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.r3, LCA.r6), 1)

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.r4, LCA.r5), 3)

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.r5, LCA.r6), 4)

        self.assertEqual(LCA.dagLCA(LCA.root, LCA.r4, LCA.r6), 4)




    # def test_lca(self):
    #     root = Node(10)
    #     root.left = Node(5)
    #     root.right = Node(19)
    #     root.left.left = Node(1)
    #     root.left.right = Node(6)
    #     root.right.left = Node(17)
    #     root.right.right = Node(21)
    #     self.assertEqual(LCA.findLCA(root, 1, 6), 5)
    #     self.assertEqual(LCA.findLCA(root, 17, 21), 19)
    #     self.assertEqual(LCA.findLCA(root, 1, 21), 10)
    #     self.assertEqual(LCA.findLCA(root, 4, 19), -1)
    #
    #
    # def test_null(self):
    #     root = None
    #     self.assertEqual(LCA.findLCA(root, 1, 6), -1)
