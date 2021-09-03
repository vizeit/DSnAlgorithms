from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import AVLTree

class test_avltree(TestCase):
    def setUp(self):
        self.avltree = AVLTree()
        self.avltree.insert(5)
        self.avltree.insert(4)
        self.avltree.insert(3)
        self.avltree.insert(2)
        self.avltree.insert(1)
        
    def test_search(self):
        self.assertTrue(self.avltree.search(3))
    

if __name__ == "__main__":
    main()
    


