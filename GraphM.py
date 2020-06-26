from collections import defaultdict
class GraphM:
    """
    Graph with Matrix representation
    """
    class vertex:
        __slots__ = '_element'
        def __init__(self, e):
            self._element = e
        def element(self):
            return self._element
        def __hash__(self):
            return hash(id(self))
    def __init__(self):
        self._edges = defaultdict(dict)
        self._vertices = set()
    def vertices(self):
        return self._vertices
    def insert_vertex(self, e=None):
        v = self.vertex(e)
        self._vertices.add(v)
        return v
    def insert_edge(self, u, v, e):
        #u - source, v- destination
        self._edges[u][v] = e
    def vertex_count(self):
        return len(self._vertices)
    def floydwarshall(self):
        #initialize n x n matrix to calculate shortest path
        dp = defaultdict(dict)
        #empty array for reconstructing path
        nx = defaultdict(dict)
        for i in self.vertices():
            for j in self.vertices():
                if i in self._edges and j in self._edges[i]:
                    dp[i][j] = self._edges[i][j]
                else:
                    dp[i][j] = float('inf')
        
        #Execute for all pairs shorted path
        for k in self.vertices():
            for i in self.vertices():
                for j in self.vertices():
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]
        
        #check for negative cycle
        for k in self.vertices():
            for i in self.vertices():
                for j in self.vertices():
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = -float('inf')
        
        return dp
    
if __name__ == "__main__":
    g = GraphM()
    v0 = g.insert_vertex('a')
    v1 = g.insert_vertex('b')
    v2 = g.insert_vertex('c')
    v3 = g.insert_vertex('d')
    v4 = g.insert_vertex('e')
    v5 = g.insert_vertex('f')
    v6 = g.insert_vertex('g')
    g.insert_edge(v0,v1,4)
    g.insert_edge(v0,v6,2)
    g.insert_edge(v1,v1,-1)
    g.insert_edge(v1,v2,3)
    g.insert_edge(v6,v4,2)
    g.insert_edge(v2,v4,1)
    g.insert_edge(v2,v3,3)
    g.insert_edge(v3,v5,-2)
    g.insert_edge(v4,v5,2)

    d = g.floydwarshall()
    for i in g.vertices():
        for j in g.vertices():
            if d[i][j] != float('inf'):
                print(i.element(), j.element(), d[i][j])