""" 
This is the binary search tree practice problem. The insert method
has already been completed. The task at hand is to finish the contains method
that searches for a value within the tree.
"""

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def __iter__(self):
        """
        Allows the tree to be interrable
        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Allows the tree to be iterrbale
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        

    def insert(self, data):
        """
        Insert data into the BST.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        This method is already completed.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data == node.data:
            return
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
    

    def __contains__(self, data):
        """ 
        Checks if data is in the BST.
        """

        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        the data we are looking for. This method is incomplete.
        """
        pass


# Tests
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)
for x in tree:
    print(x)  # 1, 3, 4, 5, 6, 7, 10
"""
print(3 in tree) # True
print(2 in tree) # False
print(7 in tree) # True
print(6 in tree) # True
print(9 in tree) # False
"""