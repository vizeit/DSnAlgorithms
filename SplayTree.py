import BinaryTree
import random

class SplayTree(BinaryTree.BinaryTree):
    """ Splay tree with binary tree """
    
    def _splay(self, p):
        """ non-public function to splay tree node p """
        while p!= self._root:
            parent = p._parent
            grand = parent._parent if parent else None
            if grand == None:
                self._rotate(p) #Zig case
            elif((grand._left == parent and parent._left == p) or (grand._right == parent and parent._right == p)):
                #zig-zig case
                self._rotate(parent)
                self._rotate(p)
            else:
                #zig-zag case
                self._rotate(p)
                self._rotate(p)

    def _rotate(self, p):
        """ non-public function to rotate at node p to move p up """
        newp = p
        oldp = p._parent
        if oldp._left == newp:
            newtree = newp._right
            oldp._left = newtree
            newp._right = oldp
        else:
            newtree = newp._left
            oldp._right = newtree
            newp._left = oldp
        if newtree: newtree._parent = oldp
        if oldp._parent:
            newp._parent = oldp._parent
            if oldp._parent._left == oldp: 
                oldp._parent._left = newp
            else:
                oldp._parent._right = newp
        else:
            self._root = newp
            newp._parent = None
        oldp._parent = newp
                

    def insert(self, e):
        """ insert element into BST """
        if self._root == None:
            self.addroot(e)
        else:
            self._subinsert(self._root, e)

    def _subinsert(self, p, e):
        """ non-public subroutine to recursively insert element """
        if e <= p._element:
            self.addleft(e, p) if p._left == None else self._subinsert(p._left, e) 
        else:
            self.addright(e, p) if p._right == None else self._subinsert(p._right, e)

    def search(self, e):
        """ search element in AVL, return True if found """
        if self._root:
            return self._subsearch(self._root, e)
    
    def _subsearch(self, p, e):
        """ non-public subroutine to recursively search element """
        if e == p._element:
            self._splay(p)
            return True
        elif e < p._element:
            return False if p._left == None else self._subsearch(p._left, e)
        else:
            return False if p._right == None else self._subsearch(p._right, e)


if __name__ == "__main__":
    bt = SplayTree()

    rn = 100

    for i in range(rn):
        bt.insert(random.randrange(rn))

    for e in bt.inorder():
        print(e, end = ' ')
    print('\n')

    value = input('Enter element to search in Tree: ')

    if bt.search(int(value)):
        print('{} is found in Tree'.format(value))
    else:
        print('{} is not found in Tree'.format(value))
    
    print('Tree After splay')
    for e in bt.inorder():
        print(e, end = ' ')
    print('\n')