from structure.treenode import *


def largestValues(root):
    _map={}
    dfs(root,0,_map)
    return [_map[i] for i in range(len(_map))]


def dfs(root,level,_map):
    if root:
        if root.val>_map.get(level,-1<<31):
            _map[level]=root.val
        dfs(root.left,level+1,_map)
        dfs(root.right,level+1,_map)
    

if __name__=="__main__":
    root=listToTree([1,2,3])
    print largestValues(root)
