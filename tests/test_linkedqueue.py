from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import LinkedQueue, EmptyQueue

class test_linkedqueue(TestCase):
    def test_put(self):
        queue = LinkedQueue()
        queue.put(1)
        queue.put('a')
        queue.put(1.2)
        queue.put('Test')
        self.assertEqual(queue.first(),1)
    def test_get(self):
        queue = LinkedQueue()
        queue.put(1)
        queue.put('a')
        queue.put(1.2)
        self.assertEqual(queue.get(),1)
    def test_empty(self):
        queue = LinkedQueue()
        self.assertTrue(queue.is_empty())
    def test_emptyException(self):
        queue = LinkedQueue()
        with self.assertRaises(EmptyQueue) as context:
            queue.get()
            self.assertTrue('Queue is empty', context.exception)
    
if __name__ == "__main__":
    main()
    


