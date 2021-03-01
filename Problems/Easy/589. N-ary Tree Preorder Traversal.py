"""

589. N-ary Tree Preorder Traversal
Simple preorder calculation through recursion

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        if root == None:
            return []
        result = []
        def get_preorder(current, result):
            result.append(current.val)
            for child in current.children:
                get_preorder(child, result)
        get_preorder(root, result)
        print(result)
        return result
                
        