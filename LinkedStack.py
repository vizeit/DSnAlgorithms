class Empty(Exception):
    """ Custom exception class for Empty Stack """
    pass

class LinkedStack:
    """
    LIFO (Last In First Out) implementation using python Linked List
    """

    class _node:
        """ non-public class for Node of Linked List """
        __slots__ = '_element', '_next' #streamline memory

        def __init__(self, e, next):
            self._element = e
            self._next = next

    def __init__(self):
        """ Create and empty Stack """
        self._head = None
        self._size = 0
    
    def __len__(self):
        """ Return number of elements in Stack """
        return self._size

    def is_empty(self):
        """ Return True if Stack is empty """
        return self._size == 0

    def push(self, e):
        """ Add element to Stack """
        self._head = self._node(e, self._head)
        self._size += 1
    
    def top(self):
        """ Return but do not remove top element from Stack """
        if not self.is_empty():
            return self._head._element
        else:
            raise Empty('Stack is empty') #Raise an excepton if Stack is empty
    
    def pop(self):
        """ Return and remove last element from Stack """
        if not self.is_empty():
            e = self._head._element
            self._head = self._head._next
            self._size -= 1
            return e
        else:
            raise Empty('Stack is empty') #Raise an excepton if Stack is empty

if __name__ == "__main__":
    try:
        a = LinkedStack()
        a.push(1)
        a.push('a')
        a.push(1.2)
        a.push('Test')
        print('Lenght of Stack is {}'.format(len(a)))
        print('Last element added is {}'.format(a.top()))
        print('Pop element {}'.format(a.pop()))
        print('Lenght of Stack is {}'.format(len(a)))
        print('Pop element {}'.format(a.pop()))
        print('Lenght of Stack is {}'.format(len(a)))
        print('Pop element {}'.format(a.pop()))
        print('Lenght of Stack is {}'.format(len(a)))
        print('Pop element {}'.format(a.pop()))
        print('Lenght of Stack is {}'.format(len(a)))
        #try pop when Stack is empty
        print('Pop element {}'.format(a.pop()))
        print('Lenght of Stack is {}'.format(len(a)))
    except Empty as e:
        print(e)
