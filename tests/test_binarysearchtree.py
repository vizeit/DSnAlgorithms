from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import BinarySearchTree

class test_binarysearchtree(TestCase):
    def setUp(self):
        self.binarysearchtree = BinarySearchTree()
        self.binarysearchtree.insert(5)
        self.binarysearchtree.insert(4)
        self.binarysearchtree.insert(3)
        self.binarysearchtree.insert(2)
        self.binarysearchtree.insert(1)
        
    def test_search(self):
        self.assertTrue(self.binarysearchtree.search(3))
    

if __name__ == "__main__":
    main()
    


