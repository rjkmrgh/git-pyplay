#Greedy Algorithm - Dijkstra Single Source Shortest path.
#Time - O[E.log(V)]
#Total vertices and E times decrease and extract operations
#Space - O[E.V]

def ShortestPath(graph, d, p, m):
    
    while  m:
        v = min(m, key = m.get)
        d[v] = m[v]        
        m.pop(v, None)
        
        for u in graph[v]:
            if u in m:
                if m[u] > d[v] + graph[v][u]:
                    m[u] = d[v] + graph[v][u]
                    p[u] = v        
    return d, p

def initialize(graph, source):
    
    d = {}
    p = {}
    m = {}

    for u in graph:
        m[u] = float('Inf')

    m[source] = 0 
    p[source] = None

    return d, p, m


def Dijkstra(graph, source):

    d, p, m = initialize(graph, source)
    
    print(m)

    d, p = ShortestPath(graph, d, p, m)
        
    return d, p

def test():

        graph = {
                'a' : {'b': 2, 'd': 5},
                'b' : {'c': 4},
                'd' : {'e': 1, 'f': 2},
                'f' : {'c': 3},
                'c' : {},
                'e' : {}
            }

        d, p = Dijkstra(graph, 'a')

        print(p)


if __name__ == '__main__':
    test()
    
    
