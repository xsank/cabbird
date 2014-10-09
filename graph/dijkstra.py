from collections import defaultdict

G={
    'a':{'b':7,'c':5,'d':2},
    'b':{'a':7,'d':4,'e':8},
    'c':{'a':5,'d':1,'f':6},
    'd':{'c':1,'e':3,'a':2,'b':4},
    'e':{'d':3,'f':4,'b':8},
    'f':{'c':6,'e':4},
}

def dijkstra(g,start,end):
    if start==end:
        return 0
    if not (start in g and end in g):
        raise Exception('invalid node %s or %s' % (start,end))
    labels={}
    path=defaultdict(list)
    for vertex in g:
        labels[vertex]=0 if vertex==start else float("inf")
    drops=labels.copy()
    while drops:
        min_v=min(drops,key=drops.get)
        path[min_v].append(min_v)
        for i in g[min_v]:
            if labels[i]>(labels[min_v]+g[min_v][i]):
                drops[i]=labels[i]=labels[min_v]+g[min_v][i]
                path[i]=[]
                path[i].extend(path[min_v])
        del drops[min_v]
    print "shortest path from a to f:%s" % path[end]
    print "value:%d" % labels[end]

if __name__=="__main__":
    dijkstra(G,'a','f')
