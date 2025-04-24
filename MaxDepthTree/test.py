import unittest
from solution import *

class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.maxDepth(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.maxDepth(root), 1)

    def test_two_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.maxDepth(root), 2)

    def test_balanced_tree(self):
        root = TreeNode(1,
                        TreeNode(2, TreeNode(4), TreeNode(5)),
                        TreeNode(3))
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.maxDepth(root), 3)

if __name__ == "__main__":
    unittest.main()