from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import PriorityQueue

class test_avltree(TestCase):
    def setUp(self):
        self.priorityqueue = PriorityQueue()
        self.priorityqueue.add(5,5)
        self.priorityqueue.add(4,4)
        self.priorityqueue.add(3,3)
        self.priorityqueue.add(2,2)
        self.priorityqueue.add(1,1)
        
    def test_min(self):
        self.assertEqual(self.priorityqueue.min()[1], 1)
    

if __name__ == "__main__":
    main()
    


