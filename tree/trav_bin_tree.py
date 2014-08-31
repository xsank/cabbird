from binary_search_tree import BinarySearchTree



def preorder(root):
    if root:
        print root.value
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print root.value
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print root.value


if __name__=="__main__":
    nodes=[2,6,1,3,5,7]
    root=BinarySearchTree(4)
    for i in nodes:
        root.insert(BinarySearchTree(i))

    preorder(root)
    inorder(root)
    postorder(root)


