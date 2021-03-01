"""

226. Invert Binary Tree

Recursively going through the tree to invert it. Its a simple but interesting problem.
All you need to do is go through the tree, at each step reverse the left and right tree and call your function again.
This ends up inverting the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        else:
            left = root.left
            right = root.right
            root.left = right
            root.right = left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root