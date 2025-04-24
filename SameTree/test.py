import unittest
from solution import *

class TestSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_both_empty(self):
        self.assertTrue(self.solution.isSameTree(None, None))

    def test_one_empty(self):
        t1 = TreeNode(1)
        self.assertFalse(self.solution.isSameTree(t1, None))
        self.assertFalse(self.solution.isSameTree(None, t1))

    def test_identical_trees(self):
        t1 = TreeNode(1, TreeNode(2), TreeNode(3))
        t2 = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(self.solution.isSameTree(t1, t2))

    def test_different_structure(self):
        t1 = TreeNode(1, TreeNode(2), None)
        t2 = TreeNode(1, None, TreeNode(2))
        self.assertFalse(self.solution.isSameTree(t1, t2))

    def test_different_values(self):
        t1 = TreeNode(1, TreeNode(2), TreeNode(3))
        t2 = TreeNode(1, TreeNode(3), TreeNode(2))
        self.assertFalse(self.solution.isSameTree(t1, t2))

if __name__ == "__main__":
    unittest.main()