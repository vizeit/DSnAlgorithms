from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import SplayTree

class test_avltree(TestCase):
    def setUp(self):
        self.splaytree = SplayTree()
        self.splaytree.insert(5)
        self.splaytree.insert(4)
        self.splaytree.insert(3)
        self.splaytree.insert(2)
        self.splaytree.insert(1)
        
    def test_search(self):
        self.assertTrue(self.splaytree.search(3))
    

if __name__ == "__main__":
    main()
    


