from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import BinaryTree

class test_binarytree(TestCase):
    def setUp(self):
        self.binarytree = BinaryTree()
        rt = self.binarytree.addroot(1)
        el1 = self.binarytree.addleft(2, rt)
        el2 = self.binarytree.addright(3, rt)
        self.binarytree.addleft(4, el1)
        self.binarytree.addright(5,el1)
    def test_inorder(self):
        self.assertListEqual([node for node in self.binarytree.inorder()],[4,2,5,1,3])
    def test_preorder(self):
        self.assertListEqual([node for node in self.binarytree.preorder()],[1,2,4,5,3])
    def test_postorder(self):
        self.assertListEqual([node for node in self.binarytree.postorder()],[4,5,2,3,1])
    def test_breadthfirsttraversal(self):
        self.assertListEqual([node for node in self.binarytree.breadthfirst()],[1,2,3,4,5])

if __name__ == "__main__":
    main()
    


