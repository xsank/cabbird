
class BinaryTree(object):
    def __init__(self,value=0):
        self.value=value
        self.left=None
        self.right=None

    def is_leaf(self):
        return self.left is None and self.right is None

