"""

101. Symmetric Tree

Notes:
Initially I thought the inorder traversal would be the solution to this problem. However, while it works for perfect binary trees, it
will not work for the 2nd case given in this problem.

I found this solution online and its a simple and effective approach.
The base case for an empty tree is obviously True (an empty tree is symmetric)

I then created a function called isMirror that recurses down the left and right subtree,
There are three conditions that are being checked here.
1. If both the left and right are equal, return True.
2. If either left and right are None and the other isn't, return False.
3. If they are both unequal, return False.

Now the recursion between two trees takes place.
The last call to isMirror checks that these two conditions return the same boolean value:
1. The left value of the left node is equal to the right value of the right node.
2. The right value of the left node is equal to the left value of the right node.



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        elif left == None and right != None or left != None and right == None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
