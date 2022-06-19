from structure.treenode import *


def _levelOrder(root):
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


def levelOrder(root):
    res = []
    levelTravel(res, root, 0)
    return res


def levelTravel(total, root, level):
    if root:
        if len(total) == level:
            total.append([])
        total[level].append(root.val)
        levelTravel(total, root.left, level + 1)
        levelTravel(total, root.right, level + 1)


if __name__ == "__main__":
    node = listToTree([1, 2, 2, 4, 3, 4, 3])
    print
    levelOrder(node)
