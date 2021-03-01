"""
Implementation of a Binary Search Tree

The following functions are implemented:
insert
delete
search
traversals (inorder, preorder, postorder)

"""


class Node:
    """
    Defines a node for a part of the tree
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    """
    A Binary Tree structure to easily search for elements
    """
    def __init__(self):
        self.root = None

    def insert(self, number):
        if self.root == None:
            self.root = Node(number)
        else:
            current = self.root
            def insert_node(current,number):
                if current == None:
                    return Node(number)
                if number == current.value:
                    print("{} already exists in this tree".format(number))
                    return current
                elif number < current.value:
                    current.left = insert_node(current.left, number)
                else:
                    current.right = insert_node(current.right, number)
                return current

            insert_node(current, number)
    
    def search(self, number):
        if self.root == None:
            return "Empty Tree"
        else:
            current = self.root
            def search_node(current, number):
                if current == None:
                    print("{} not found in this tree".format(number))
                    return
                if number == current.value:
                    print("Found")
                elif number < current.value:
                    search_node(current.left, number)
                else:
                    search_node(current.right, number)
                return current
            search_node(current, number)

    def delete(self, number):
        if self.root == None:
            print("Empty Tree")
        else:
            current = self.root
            def delete_node(current, number):
                # If the number does not exist, we have reached "None"
                if current == None:
                    print("{} does not exists in this tree".format(number))
                    return
                else:
                    # We have found the number
                    if number == current.value:
                        toDelete = current
                        # Case 1: This element is a leaf
                        if toDelete.left == None and toDelete.right == None:
                            return
                            # It has a right child
                        elif toDelete.left == None and toDelete.right != None:
                            return toDelete.right
                            # It has a left child
                        elif toDelete.left != None and toDelete.right == None:
                            return toDelete.left
                            # It has two children
                        else:
                            # Get inorder successor: left most node in the right subtree
                            inorder_successor = toDelete.right
                            while inorder_successor.left != None:
                                inorder_successor = inorder_successor.left
                            toDelete.value = inorder_successor.value
                            toDelete.right = delete_node(toDelete.right, inorder_successor.value)
                            return toDelete
                    if number < current.value:
                        current.left = delete_node(current.left, number)
                    elif number >current.value:
                        current.right = delete_node(current.right, number)
                    return current
            delete_node(current, number)

    def inorderTraversal(self):
        current = self.root
        def call_inorder_traversal(current):
            if current == None:
                return
            call_inorder_traversal(current.left)
            print("{}".format(current.value))
            call_inorder_traversal(current.right)
        call_inorder_traversal(current)

    def preorderTraversal(self):
        current = self.root
        def call_inorder_traversal(current):
            if current == None:
                return
            print("{}".format(current.value))
            call_inorder_traversal(current.left)
            call_inorder_traversal(current.right)
        call_inorder_traversal(current)

    def postorderTraversal(self):
        current = self.root
        def call_inorder_traversal(current):
            if current == None:
                return
            call_inorder_traversal(current.left)
            call_inorder_traversal(current.right)            
            print("{}".format(current.value))
        call_inorder_traversal(current)
        
tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.inorderTraversal()
for i in range(15):
    tree.search(i)
tree.delete(4)
tree.delete(7)
tree.inorderTraversal()