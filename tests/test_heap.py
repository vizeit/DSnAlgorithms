from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import Heap, EmptyHeap

class test_heap(TestCase):
    def test_push(self):
        stack = Heap()
        stack.push(4)
        stack.push(5)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(),1)
    def test_pop(self):
        stack = Heap()
        stack.push(3)
        stack.push(4)
        stack.push(1)
        self.assertEqual(stack.pop(),1)
    def test_empty(self):
        stack = Heap()
        self.assertTrue(stack.is_empty())
    def test_emptyException(self):
        stack = Heap()
        with self.assertRaises(EmptyHeap) as context:
            stack.pop()
            self.assertTrue('Heap is empty', context.exception)
    
if __name__ == "__main__":
    main()
    


