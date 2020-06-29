class Partition:
    """
    Union-find structure for maintaining disjoint sets.
    """
    class Position:
        __slots__ = '_container', '_element', '_size', '_parent'
        def __init__(self, container, e):
            self._container = container #reference to Partition instance
            self._element = e
            self._parent = self
            self._size = 1
        def element(self):
            return self._element 
    def make_group(self, e):
        return self.Position(self, e)
    def find(self, p):
        if p._parent != p:
            #Very import step, overwrite parent after recursion
            #helps quick find parent next time
            p._parent = self.find(p._parent) 
        return p._parent
    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)
        if a is not b:
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size

if __name__ == "__main__":
    p = Partition()
    pos = {}
    for i in range(10):
        pos[i] = p.make_group(i)
    
    for i, j in zip(range(5), range(9,4, -1)):
        p.union(pos[i], pos[j])

