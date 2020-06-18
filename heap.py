class Empty(Exception):
    """ Custom exception class for Empty Stack """
    pass

class heap:
    """ heap data structure """
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, d):
        self._data.append(d)
        self._upheap()
    
    def pop(self):
        if self.is_empty():
            raise Empty('Heap is empty')
        self._data[-1], self._data[0] = self._data[0], self._data[-1]
        d = self._data.pop()
        self._downheap()
        return d

    def _downheap(self, i=0):
        while i < len(self._data) // 2:
            l = 2*i+1
            r = 2*i+2
            m = min(self._data[i], self._data[l], self._data[r]) if r < len(self._data) else min(self._data[i], self._data[l])
            if m == self._data[i]:
                break
            elif m == self._data[l]:
                self._data[i], self._data[l] = self._data[l], self._data[i]
                i = l
            else:
                self._data[i], self._data[r] = self._data[r], self._data[i]
                i = r
    
    def _upheap(self):
        i = len(self._data) - 1
        while i:
            p = (i-1)//2
            if self._data[i] > self._data[p]:
                break
            else:
                self._data[i], self._data[p] = self._data[p], self._data[i]
                i = p
    
    def heapify(self, l):
        for i in l:
            self.push(i)


if __name__ == "__main__":
    try:

        import random
        rn = 1000
        h = heap()
        for i in range(rn):
            h.push(random.randrange(rn))
        for i in range(len(h)):
            print(h.pop(), end=' ')
    except Empty as e:
        print(e)