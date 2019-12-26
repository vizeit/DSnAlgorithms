import BinaryTree
import random

class BinarySearchTree(BinaryTree.BinaryTree):
    """ Binary Search tree with Binary Tree """
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
        """ search element in BST, return True if found """
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


if __name__ == "__main__":
    bt = BinarySearchTree()

    rn = 250

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
