class Empty(Exception):
    """ Custom exception class for Empty Stack """
    pass

class ArrayStack:
    """
    LIFO (Last In First Out) implementation using python List
    """
    def __init__(self):
        """ Create and empty Stack """
        self._data = [] #non-public empty list
    
    def __len__(self):
        """ Return number of elements in Stack """
        return len(self._data)

    def is_empty(self):
        """ Return True if Stack is empty """
        return len(self._data) == 0

    def push(self, e):
        """ Add element to Stack """
        self._data.append(e) #New element added at the end
    
    def top(self):
        """ Return but do not remove top element from Stack """
        if not self.is_empty():
            return self._data[-1]
        else:
            raise Empty('Stack is empty') #Raise an excepton if Stack is empty
    
    def pop(self):
        """ Return and remove last element from Stack """
        if not self.is_empty():
            return self._data.pop()
        else:
            raise Empty('Stack is empty') #Raise an excepton if Stack is empty

if __name__ == "__main__":
    try:
        a = ArrayStack()
        a.push(1)
        a.push('a')
        a.push(1.2)
        a.push('Test')

        print('Top element is {}'.format(a.top())) #check the top element

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
