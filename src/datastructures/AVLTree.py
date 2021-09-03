from . import BinaryTree

class AVLTree(BinaryTree):
    """ AVL tree with binary tree """
    class _node(BinaryTree._node):
        """ AVL node class maintains height and balance """
        __slots__ = '_height'

        def __init__(self, e, parent=None):
            """ Initialize node in AVL and super class BinaryTree """
            super().__init__(e, parent)
            self._height = 1 
        
    def _calheight(self, p):
        """ non-public function to calculate height of tree at node p"""
        p._height = 1 + max((p._left._height if p._left else 0) , (p._right._height if p._right else 0))

    
    def _getbalance(self, p):
        """ non-public function to return balanced at node p 
        -1 to +1 balanced
        > +1 left tree height is greater than right, need right rotation
            < 0 for node.left, need left rotation before right rotation at node
        < -1 right tree height is greater than left, need left rotation
            > 0 for node.right, need right rotation before left rotation at node
        """
        return ((p._left._height if p._left else 0) - (p._right._height if p._right else 0))
    
    def _rotateright(self, p):
        """ non-public function to rotate tree to right at node p """
        newp = p._left #initialize new root with left node of p
        newltree = newp._right #initialize new left subtree 
        oldp = p #store initial value of p

        if p._parent:
            if p == p._parent._left:
                p._parent._left = newp
            else:
                p._parent._right = newp
            newp._parent = p._parent #update to new parent
        else:
            newp._parent = None 
            self._root = p = newp #change p to new p
        oldp._left = newltree # add right of initial p to new left tree
        if newltree: newltree._parent = oldp #update to new parent
        newp._right = oldp #add initial p to right of new p
        oldp._parent = newp #update to new parent
        self._calheight(oldp) #recalculate height of oldp after rotate
        self._calheight(newp) #recalculate height at new node p

    def _rotateleft(self, p):
        """ non-public function to rotate tree to left at node p """
        newp = p._right #initialize new root with right node of p
        newrtree = newp._left #initialize new right subtree
        oldp = p
        if p._parent:
            if p == p._parent._left:
                p._parent._left = newp
            else:
                p._parent._right = newp
            newp._parent = p._parent #update to new parent  
        else:
            newp._parent = None 
            self._root = p = newp #change p to new p
        oldp._right = newrtree # add left of initial p to new right tree
        if newrtree: newrtree._parent = oldp #update to new parent
        newp._left = oldp #add initial p to left of new p
        oldp._parent = newp #update to new parent
        self._calheight(oldp) #recalculate height of oldp after rotate
        self._calheight(newp) #recalculate height at new node p
    
    def _rebalance(self, p):
        """ non-public function to rebalance tree at node p """
        self._calheight(p)
        if self._getbalance(p) < -1:
            if p._right and self._getbalance(p._right) > 0: #first rotate right at child
                self._rotateright(p._right)
            self._rotateleft(p)
        elif self._getbalance(p) > 1:
            if p._left and self._getbalance(p._left) < 0: #first rotate left at child
                self._rotateleft(p._left)
            self._rotateright(p)
    
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
            self._rebalance(p)
        else:
            self.addright(e, p) if p._right == None else self._subinsert(p._right, e)
            self._rebalance(p)

    def search(self, e):
        """ search element in AVL, return True if found """
        if self._root:
            return self._subsearch(self._root, e)
    
    def _subsearch(self, p, e):
        """ non-public subroutine to recursively search element """
        if e == p._element:
            return True
        elif e < p._element:
            return False if p._left == None else self._subsearch(p._left, e)
        else:
            return False if p._right == None else self._subsearch(p._right, e)