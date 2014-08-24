
def deep_search(node=None):

    def visit(node):
        print node.value

    if node is not None:
        visit(node)
        if node.left:
            deep_search(node.left)
        if node.right:
            deep_search(node.right)

