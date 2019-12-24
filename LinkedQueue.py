class Empty(Exception):
    """ Custom exception class for Empty Stack """
    pass

class LinkedQueue:
    """ FIFO (Fist In First Out) implementation using Python Linked list """

    class _node:
        """ non-public class for Node of Linked List  """
        __slots__ = '_element', '_next'

        def __init__(self, e, next):
            self._element = e
            self._next = next
    
    def __init__(self):
        """ Create empty queue """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ return number of elements in queue """
        return self._size

    def is_empty(self):
        """ return True if queue is empty """
        return self._size == 0

    def put(self, e):
        """ Add element to queue """
        newnode = self._node(e, None)
        if self._size == 0:
            self._head = newnode
        else:
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1

    def first(self):
        """ return but do not remove first element of queue """
        if not self.is_empty():
            return self._head._element
        else:
            raise Empty('Queue is empty') #Raise an excepton if Queue is empty

    def get(self):
        """ remove first element from queue """
        if not self.is_empty():
            e = self._head._element
            self._head = self._head._next
            self._size -= 1
            if self.is_empty():
                self._tail = None
            return e
        else:
            raise Empty('Queue is empty') #Raise an excepton if Queue is empty

if __name__ == "__main__":
    try:
        q = LinkedQueue()

        print('Size of Queue {}'.format(len(q)))

        q.put(1)
        q.put('a')
        q.put(2.1)
        q.put('Test')
        print('Size of Queue {}'.format(len(q)))

        print('First element is {}'.format(q.first())) #check the first element

        print('Get element from queue {}'.format(q.get()))
        print('Size of Queue {}'.format(len(q)))
        print('Get element from queue {}'.format(q.get()))
        print('Size of Queue {}'.format(len(q)))
        print('Get element from queue {}'.format(q.get()))
        print('Size of Queue {}'.format(len(q)))
        print('Get element from queue {}'.format(q.get()))
        print('Size of Queue {}'.format(len(q)))
        #try get when queue is empty
        print('Get element from queue {}'.format(q.get()))
        print('Size of Queue {}'.format(len(q)))
    except Empty as e:
        print(e)



