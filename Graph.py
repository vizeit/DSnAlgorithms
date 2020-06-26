import LinkedQueue
import PriorityQueue
class Graph:
    """
    Graph with adjacency list representation
    """
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
    def dijkstra(self, src):
        """
        shortest path from src vertex to all reachable vertices
        """
        d = {}
        rs = {}
        pq = PriorityQueue.PriorityQueue()
        pqloc = {}
        for v in self.vertices():
            if v == src:
                d[v] = 0
            else:
                d[v] = float('inf')
            pqloc[v] = pq.add(d[v], v)
        while not pq.is_empty():
            key, u = pq.remove_min()
            rs[u] = key
            for e in self.incident_edges(u):
                v = e.opposite(u)
                if v not in rs:
                    wgt = e.element()
                    if d[u] + wgt < d[v]:
                        d[v] = d[u] + wgt
                        pq.update(pqloc[v], d[v], v)
        return rs
    def bellmanford(self, src):
        """
        Find negative cycles. 
        return True if no negative cycle
        return False if negative cycle
        """
        d = {}
        for v in self.vertices():
            if v == src:
                d[v] = 0
            else:
                d[v] = float('inf')
        for _ in range(self.vertex_count()-1):
            for e in self.edges():
                org, dst = e.endpoints()
                if d[org] + e.element() < d[dst]:
                    d[dst] = d[org] + e.element()
        #relax edges one more time, if value changes there is negative cycle
        for _ in range(self.vertex_count()-1):
            for e in self.edges():
                org, dst = e.endpoints()
                if d[org] + e.element() < d[dst]:
                    return False #there is a negative cycle
        return True

if __name__ == "__main__":
    g = Graph()
    v0=g.insert_vertex(0)
    v1=g.insert_vertex(1)
    v2=g.insert_vertex(2)
    v3=g.insert_vertex(3)
    v4=g.insert_vertex(4)
    g.insert_edge(v0,v1,1)
    g.insert_edge(v0,v4,3)
    g.insert_edge(v4,v1,5)
    g.insert_edge(v4,v3,2)
    g.insert_edge(v1,v3,1)
    g.insert_edge(v1,v2,4)
    g.insert_edge(v3,v2,3)
    print([v.element() for v in g.vertices()])
    print([(e.endpoints()[0].element(),e.endpoints()[1].element()) for e in g.edges()])
    ddfs = {v0:None}
    g.dfs(v0, ddfs)
    print([(i.element(), (j.endpoints()[0].element(),j.endpoints()[1].element()) if j else None) for i,j in ddfs.items()])

    dbfs = {v0:None}
    g.bfs(v0, dbfs)
    print([(i.element(), (j.endpoints()[0].element(),j.endpoints()[1].element()) if j else None) for i,j in dbfs.items()])
    print([(i.element(), j) for i, j in g.dijkstra(v0).items()])
    print(g.bellmanford(v0))
    gn = Graph()
    vn0=gn.insert_vertex(0)
    vn1=gn.insert_vertex(1)
    vn2=gn.insert_vertex(2)
    vn3=gn.insert_vertex(3)
    
    gn.insert_edge(vn0,vn2,-2)
    gn.insert_edge(vn1,vn0,4)
    gn.insert_edge(vn1,vn2,-3)
    gn.insert_edge(vn2,vn3,2)
    gn.insert_edge(vn3,vn1,-1)
    
    print(gn.bellmanford(vn1))#negative cycle detected