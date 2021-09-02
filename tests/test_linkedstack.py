from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import LinkedStack, EmptyStack

class test_linkedstack(TestCase):
    def test_push(self):
        stack = LinkedStack()
        stack.push(1)
        stack.push('a')
        stack.push(1.2)
        stack.push('Test')
        self.assertEqual(stack.top(),'Test')
    def test_pop(self):
        stack = LinkedStack()
        stack.push(1)
        stack.push('a')
        stack.push(1.2)
        self.assertEqual(stack.pop(),1.2)
    def test_empty(self):
        stack = LinkedStack()
        self.assertTrue(stack.is_empty())
    def test_emptyException(self):
        stack = LinkedStack()
        with self.assertRaises(EmptyStack) as context:
            stack.pop()
            self.assertTrue('Stack is empty', context.exception)
    
if __name__ == "__main__":
    main()
    


