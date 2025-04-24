# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.preorder(p) == self.preorder(q)

    def preorder(self, node):
        if not node:
            return [None]
        return [node.val] + self.preorder(node.left) + self.preorder(node.right)
