"""
Implementation of a Binary Tree

Todo:
- Add "delete" function
- Add all traversals
- Fix inorder traversal print statement

"""

class Node():
    def __init__(self, value=0, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

class BinaryTree():
    def __init__(self):
        print("Binary Tree Initialized")
        self.root = None

    def add(self, valToAdd):
        current = self.root
        def addNode(current, valToAdd):
            if current == None:
                return Node(valToAdd)
            else:
                if valToAdd < current.value:
                    current.left = addNode(current.left, valToAdd)
                elif valToAdd > current.value:
                    current.right = addNode(current.right, valToAdd)
                else:
                    raise NotImplementedError("This tree does not account for repetitive values")
            return current
        self.root = addNode(current, valToAdd)

    def inorderTraversal(self):
        result = []
        current = self.root
        def getInorderTraversal(current, result):
            if current == None:
                result.append("none")
            else:
                getInorderTraversal(current.left, result)
                result.append(current.value)
                getInorderTraversal(current.right, result)
            return result
        return getInorderTraversal(current, result)
        

if __name__ == "__main__":
    myTree = BinaryTree()
    myTree.add(3)
    myTree.add(1)
    myTree.add(2)
    myTree.add(4)
    myTree.add(5)
    # myTree.add(5)
    print(myTree.inorderTraversal())
