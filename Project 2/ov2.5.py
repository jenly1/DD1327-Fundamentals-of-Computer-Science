# Jennifer Ly, grudat20 uppg 2.5

import random

# A tree node that stores value  
class Node:
    def __init__(self, data): 
        """Constructs nodes"""   
        self.data = data
        self.priority = random.random()
        self.right = None
        self.left = None

    def __lt__(self, other):    
        """Less-than comparison."""
        return self.data < other.data

    def __repr__(self):
        """Returns a string, otherwise error will be thrown"""
        return str(self.data)

    # Rotates the subtree to this specific node using a right rotation
    # O(1)
    def rightRotation(self): 
        rnode = self.left 
        self.left = rnode.right
        rnode.right = self
        return rnode

    # Rotates the subtree to this specific node using a left rotation
    # O(1)
    def leftRotation(self):
        lnode = self.right
        self.right = lnode.left
        lnode.left = self
        return lnode

# A balanced randomized binary tree
class Treap:                              
    def __init__(self):
        """Constructs binary search tree"""  
        self.root = None
        self._size = 0
        self.array = []

    # Inserts a new node in the tree 
    # O(1)
    def addNode(self, data):
        if self.root == None:                      # if empty, creates the root and two None children
            self.root = Node(data)
        else:
            self._addNode(data, self.root)
        self._size += 1

    # Private due to recursive function
    # O(log(n))
    def _addNode(self, data, node):
        if data < node.data:                                   # if node is a child and childs key is lower than parents key, create a node
            if node.left == None:
                node.left = Node(data)                     
            else:
                node.left = self._addNode(data, node.left)     # if node is a parent, go further in path by making fuction calling on itself
            if node.left.priority < node.priority:             # if child has lower priority than parent, rotate
                node = node.rightRotation()
        elif data > node.data:
            if node.right == None:
                node.right = Node(data)
            else:
                node.right = self._addNode(data, node.right) 
            if node.right.priority < node.priority:
                node = node.leftRotation()
        else:                                                   
            print(data, "already exist in the tree!")           # if same element is added 
        self.root = node                                        # declares the root in the new tree to be the new root
        return node 

    # Returns the number of elements in the tree
    # O(1)
    def size(self):
        return self._size 

    # Returns an array with all elements in alphabetic order
    # O(1)
    def getList(self) :
        if self.root == None:
            return []
        else:
            self.array = self._getList(self.root)
            return self.array

    # Goes through all the nodes in the treap and saves the nodes in an array, returns that array
    # Private due to recursive function
    # O(n)
    def _getList(self, node):
        if node == None:                   # if current node is None
            return 
        else:
            self._getList(node.left)
            self._getList(node.right)
            self.array.append(node.data)   # saves the nodes keys in an array
        return sorted(self.array)          # sorted()=built in function which sorts the elements in the list


# Unit test
def main():
    t = Treap()
    c = 0
    
    # Tests the size and nodes of the empty tree
    assert t.size() == c
    assert t.getList() == []
    
    # Tests the size and nodes after adding nodes to the tree
    for i in ["D", "A", "B", "F", "E", "AA", "GGG"]:
        t.addNode(i)
        c += 1
        assert t.size() == c
    assert t.getList() == ["A", "AA", "B", "D", "E", "F", "GGG"]

    # Tests that tree follows Max-Heap property
    def _priority(node):
        if node.left != None:
            assert node.left.priority > node.priority
            _priority(node.left)
        if node.right != None:
            assert node.right.priority > node.priority
            _priority(node.right)

    _priority(t.root)                                   
     
main()
