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
    def edges(self):
        return self._edges
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