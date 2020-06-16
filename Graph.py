import LinkedQueue

class Graph:
    class vertex:
        __slots__ = '_element'
        def __init__(self, e):
            self._element = e
        def element(self):
            return self._element
        def __hash__(self):
            return hash(id(self))
    
    class edge:
        __slots__ = '_origin', '_destination', '_element'
        def __init__(self, u, v, e):
            self._origin = u
            self._destination = v
            self._element = e #auxiliary element, can be weight
        def endpoints(self):
            return (self._origin, self._destination)
        def opposite(self, v):
            return self._destination if v == self._origin else self._origin
        def element(self):
            return self._element
        def __hash__(self):
            return hash((self._origin, self._destination))
        
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
    def isdirected(self):
        return self._outgoing is not self._incoming
    def vertex_count(self):
        return len(self._outgoing)
    def vertices(self):
        return self._outgoing.keys()
    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.isdirected() else total // 2
    def edges(self):
        rs = set()
        for d in self._outgoing.values():
            rs.update(d.values())
        return rs
    def get_edge(self, u, v):
        return self._outgoing[u].get(v)
    def degree(self, v, outgoing=True):
        #for directed graph, indegree can be calculated with outgoing=False
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    def incident_edges(self, v, outgoing=True):
        #for directed graph, incoming edges can be returned with outgoing=False
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    def insert_vertex(self, e=None):
        v = self.vertex(e)
        self._outgoing[v] = {}
        if self.isdirected():
            self._incoming[v] = {}
        return v
    def insert_edge(self, u, v, e=None):
        edge = self.edge(u, v, e)
        self._outgoing[u][v] = edge
        self._incoming[v][u] = edge
    def dfs(self, u, discovered):#Depth First Search
        """
        u - starting vertex initialized in discovered dictionary 
        """
        for e in self.incident_edges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                self.dfs(v,discovered)
    def bfs(self, u, discovered):#Breadth first search
        """
        u - starting vertex initialized int discovered dictionary
        """
        q = LinkedQueue.LinkedQueue()
        q.put(u)
        while not q.is_empty():
            s = q.get()
            for e in self.incident_edges(s):
                v = e.opposite(s)
                if v not in discovered:
                    discovered[v] = e
                    q.put(v)

if __name__ == "__main__":
    g = Graph()
    v0=g.insert_vertex(0)
    v1=g.insert_vertex(1)
    v2=g.insert_vertex(2)
    v3=g.insert_vertex(3)
    v4=g.insert_vertex(4)
    g.insert_edge(v0,v1)
    g.insert_edge(v0,v4)
    g.insert_edge(v4,v1)
    g.insert_edge(v4,v3)
    g.insert_edge(v1,v3)
    g.insert_edge(v1,v2)
    g.insert_edge(v3,v2)
    print([v.element() for v in g.vertices()])
    print([(e.endpoints()[0].element(),e.endpoints()[1].element()) for e in g.edges()])
    ddfs = {v0:None}
    g.dfs(v0, ddfs)
    print([(i.element(), (j.endpoints()[0].element(),j.endpoints()[1].element()) if j else None) for i,j in ddfs.items()])

    dbfs = {v0:None}
    g.bfs(v0, dbfs)
    print([(i.element(), (j.endpoints()[0].element(),j.endpoints()[1].element()) if j else None) for i,j in dbfs.items()])