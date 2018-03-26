import pdb

def initialze(graph, s):
    d = {}
    p = {}
    
    for n in graph:
        d[n] = float('Inf')
        p[s] = None
    d[s] = 0
    return d, p

def BellmanFord(graph, s):
    #initializing the Dist and Parent 
    d, p = initialze(graph, s)

    #iterating V-1 time
    for _ in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)

    ##iterating Vth time to check for negative weight cycles
    for u in graph:
            for v in graph[u]:
                assert d[v] <= d[u] + graph[u][v]
##               if d[v] <= d[u] + graph[u][v]:
##                   raise AssertionError

    return d, p

def relax(curr, nxt, graph, d, p):

    if d[nxt] > d[curr] + graph[curr][nxt]:
        d[nxt] = d[curr] + graph[curr][nxt]
        p[nxt] = curr
    

def test():
    graph = {
        'a' : {'b': -1, 'c': 4},
        'b' : {'d': 2, 'c': 4, 'e': 2},
        'd' : {'b': 1, 'e': 3, 'c': 1},
        'c' : {},
        'e' : {'d': 3}
        }

    d, p = BellmanFord(graph, 'a')

    print(p)
if __name__ == '__main__' :
    test()
