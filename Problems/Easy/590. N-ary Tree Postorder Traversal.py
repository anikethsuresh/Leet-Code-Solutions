"""

590. N-ary Tree Postorder Traversal
Simple postorder calculation through recursion

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root):
        if root == None:
            return []
        result = []
        def get_postorder(current, result):
            for child in current.children:
                get_postorder(child, result)
            result.append(current.val)
        get_postorder(root, result)
        print(result)
        return result