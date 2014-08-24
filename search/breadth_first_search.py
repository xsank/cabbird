
def broad_search(node=None):

    def visit(node):
        print node.value

    queue=[node]
    while queue:
        tmp=queue.pop(0)
        if tmp is not None:
            visit(tmp)
        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.right)

