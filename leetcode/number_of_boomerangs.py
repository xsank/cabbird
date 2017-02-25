import collections


def numberOfBoomerangs(points):
    res=0
    _map=collections.defaultdict(int)
    for i in points:
        _map.clear()
        for j in points:
            if i!=j:
                _map[(i[0]-j[0])**2+(i[1]-j[1])**2]+=1
        for k in _map:
            res+=_map[k]*(_map[k]-1)
    return res
        

if __name__=="__main__":
    print numberOfBoomerangs([[0,0],[1,0],[2,0]])
