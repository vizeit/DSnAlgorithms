from . import LinkedQueue

class BinaryTree:
    """ Binary tree with Python Linked List """
    class _node:
        """ non-public class for Node of tree """
        __slots__ = '_element', '_left', '_right','_parent'

        def __init__(self, e, parent=None):
            """ initialize node """
            self._element = e
            self._left = None
            self._right = None
            self._parent = parent

    def __init__(self):
        """ create empty tree """
        self._root = None
    
    def getroot(self):
        """ return root """
        return self._root

    def addroot(self, e):
        """ add root element """
        if self._root == None:
            newnode = self._node(e)
            self._root = newnode
            return newnode
        else:
            raise ValueError('Root already exists')

    def addleft(self, e, parent):
        """ add left node """
        if parent._left == None:
            newnode = self._node(e, parent)
            parent._left = newnode
            return newnode
        else:
            raise ValueError('Left child already exists')
    
    def addright(self, e, parent):
        """ add right node """
        if parent._right == None:
            newnode = self._node(e, parent)
            parent._right = newnode
            return newnode
        else:
            raise ValueError('Right child already exists')
    
    def inorder(self):
        """ Traverse the tree inorder; leftsubtree -> root -> rightsubtree """
        yield from self._subinorder(self._root)
    
    def _subinorder(self, root):
        """ non-public subroutine Traverse the tree recursively inorder """
        if root:
            yield from self._subinorder(root._left)
            yield root._element
            yield from self._subinorder(root._right)
    
    def preorder(self):
        """ Traverse the tree preorder; root -> leftsubtree -> rightsubtree """
        yield from self._subpreorder(self._root)

    def _subpreorder(self, root):
        """ non-public subroutine Traverse the tree recursively preorder """
        if root:
            yield root._element
            yield from self._subpreorder(root._left)
            yield from self._subpreorder(root._right)

    def postorder(self):
        """ Traverse the tree postorder; leftsubtree -> rightsubtree -> root """
        yield from self._subpostorder(self._root)
    
    def _subpostorder(self, root):
        """ non-public subroutine Traverse the tree recursively postorder """
        if root:
            yield from self._subpostorder(root._left)
            yield from self._subpostorder(root._right)
            yield root._element
    
    def breadthfirst(self):
        """ Traverse the tree breadth first """
        yield from self._subbreadthfirst(self._root)

    def _subbreadthfirst(self, root):
        """ non-public subroutine Traverse the tree breadth first """
        if root:
            q = LinkedQueue()
            q.put(root) #start from the root
            while not q.is_empty():
                n = q.get()
                yield n._element
                if n._left: q.put(n._left)
                if n._right: q.put(n._right)

if __name__ == "__main__":
    try:
        t = BinaryTree()
        rt = t.addroot(1)
        el1 = t.addleft(2, rt)
        el2 = t.addright(3, rt)
        t.addleft(4, el1)
        t.addright(5,el1)

        print('Inorder Traversal')
        for e in t.inorder():
            print(e, end='')
        print('\nPreorder Traversal')
        for e in t.preorder():
            print(e, end='')
        print('\nPostorder Traversal')
        for e in t.postorder():
            print(e, end='')
        print('\nBreadth first Traversal')
        for e in t.breadthfirst():
            print(e, end='')
        print('\n')
        #test adding root element if it already exists
        t.addroot('$')

    except ValueError as ve:
        print(ve)

