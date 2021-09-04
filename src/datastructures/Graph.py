from .LinkedQueue import LinkedQueue
from .PriorityQueue import PriorityQueue
from .Partition import Partition
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
        q = LinkedQueue()
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
        pq = PriorityQueue()
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
    def mst_primjarnik(self):
        d = {}
        tree = []
        pq = PriorityQueue()
        pqloc = {}
        for v in self.vertices():
            if len(d) == 0:
                d[v] = 0
            else:
                d[v] = float('inf')
            pqloc[v] = pq.add(d[v], (v, None))
        while not pq.is_empty():
            key, val = pq.remove_min()
            u, e = val
            del pqloc[u]
            if e is not None:
                tree.append(e)
            for link in self.incident_edges(u):
                v = link.opposite(u)
                if v in pqloc:
                    w = link.element()
                    if w < d[v]:
                        d[v] = w
                        pq.update(pqloc[v], d[v], (v, link))
        return tree
    def mst_kruskal(self):
        tree = []
        pq = PriorityQueue()
        forest = Partition()
        position = {}
        for v in self.vertices():
            position[v] = forest.make_group(v)
        for e in self.edges():
            pq.add(e.element(), e)
        size = self.vertex_count()
        while len(tree) != size - 1 and not pq.is_empty():
            weight, edge = pq.remove_min()
            u, v = edge.endpoints()
            a = forest.find(position[u])
            b = forest.find(position[v])
            if a != b:
                tree.append(edge)
                forest.union(a, b)
        return tree