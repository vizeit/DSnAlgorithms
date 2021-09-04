from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import Partition

class test_avltree(TestCase):       
    def test_makegroup(self):
        partition = Partition()
        self.assertEqual(partition.make_group(2).element(), 2)
    def test_union(self):
        partition = Partition()
        p = partition.make_group(1)
        q = partition.make_group(2)
        partition.union(p, q)
        self.assertEqual(p._parent.element(), 2)
    

if __name__ == "__main__":
    main()
    


