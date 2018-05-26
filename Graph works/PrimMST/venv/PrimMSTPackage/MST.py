


class Graph:

    def __init__(self, v):
        self.Size = v
        self.Graph = [[0 for c in range(v)] for rw in range(v)]
        
    def addNode(self, u, v, data):
        self.Graph[u][v] = data
        
    def finMin(self, key, mSet):
        
        mIndex = -1
        minVal = 10
        
        for rw in range(self.Size):
            if key[rw] < minVal and mSet[rw] == False:
                mIndex = rw
                minVal = key[rw]
        return mIndex

    def PrimMST(self):
        pass
