from depth_first_search import deep_search
from breadth_first_search import broad_search

from binary_search import binary_search


class Node(object):
    def __init__(self,value=0):
        self.value=value
        self.left=None
        self.right=None


def create_complete_binary_tree(num=10):
    nodes=[Node(i) for i in range(num)]
    for index,node in enumerate(nodes[:len(nodes)/2]):
        node.left=nodes[index*2+1]
        if index*2+2<len(nodes):
            node.right=nodes[index*2+2]
    return nodes[0]

if __name__=="__main__":
    tree=create_complete_binary_tree()
    deep_search(tree)
    broad_search(tree)

    print binary_search(range(10),5)

