class Empty(Exception):
    """ Custom exception class for Empty Stack """
    pass

class PriorityQueue:
    class Locator:
        __slots__ = '_key', '_value', '_index'
        def __init__(self, k, v, j):
            self._key = k
            self._value = v
            self._index = j
        def __lt__(self, other):
            return self._key < other._key
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def _parent(self, j):
        return (j-1)//2
    def _left(self, j):
        return 2*j + 1
    def _right(self, j):
        return 2*j + 2
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
        self._data[i]._index = i
        self._data[j]._index = j
    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)
    def add(self, k, v):
        token = self.Locator(k, v, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data)-1)
        return token
    def update(self, loc, k, v):
        j = loc._index
        if not (j >= 0 and j < len(self._data) and self._data[j] is loc):
            raise ValueError('Invalid Locator')
        loc._key = k
        loc._value = v
        self._bubble(j)
    def remove(self, loc):
        j = loc._index
        if not (j > 0 and j < len(self._data) and self._data[j] is loc):
            raise ValueError('Invalid Locator')
        if j == len(self._data) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self._data)-1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)
    def _upheap(self, j):
        p = self._parent(j)
        if j > 0 and self._data[j] < self._data[p]:
            self._swap(j, p)
            self._upheap(p)
    def _downheap(self, j):
        if self._has_left(j):
            l = self._left(j)
            small = l
            if self._has_right(j):
                r =  self._right(j)
                if self._data[r] < self._data[l]:
                    small = r
            if self._data[small] < self._data[j]:
                self._swap(j, small)
                self._downheap(small)
    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)
    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        self._swap(0, len(self._data)-1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

if __name__ == "__main__":
    try:
        import random
        rn = 100
        pq = PriorityQueue()
        d = {}
        for i in range(rn):
            t = random.randrange(rn)
            loc = pq.add(t, t*10)
            d[t] = loc
        m = max(d.keys())
        pq.update(d[m], -1, -1)
        for i in range(len(pq)):
            print(pq.remove_min(), end=' ')
    except Empty as e:
        print(e)