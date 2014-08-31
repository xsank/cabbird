
from binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    def __init__(self,value=0):
        super(BinarySearchTree,self).__init__(value)

    def insert(self,node):
        if node.value>self.value:
            self.right=self.right and self.right.insert(node) or node
        else:
            self.left=self.left and self.left.insert(node) or node
        return self


