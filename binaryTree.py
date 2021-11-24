import numpy as np
import time

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.p = None
        self.key = key
 
class BinaryTree():
    def __init__(self):
        self.Node = None
    
    def search(self, root, key):
        if root == None:
            return "Not found"
        elif key == root.key:
            return root.key
        if key <  root.key:
            return (self.search(root.left, key))
        elif key > root.key:
            return (self.search(root.right, key)) 

    def insert(self, element:Node):
        y:Node = None
        x = self.Node
        if(x == None):
            self.Node = element

        while x is not None:
            y = x
            if element.key < x.key:
                x = x.left
            else:
                x = x.right

        element.p = y
        if y == None:
            self.Node = element
        elif element.key < y.key:
                y.left = element
        else:
                y.right = element

    

root = BinaryTree()
root.insert(Node(9))
root.insert(Node(32))
root.insert(Node(44))
root.insert(Node(6))
root.insert(Node(34))
root.insert(Node(53))
root.insert(Node(442))
root.insert(Node(62))
root.insert(Node(66))
root.insert(Node(71))

start = time.time()
print(root.search(root.Node, 9))
end = time.time()
totalTime = end - start 
print(f"{totalTime} seconds")

