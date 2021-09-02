from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import ArrayStack, EmptyStack

class test_arraystack(TestCase):
    def test_push(self):
        stack = ArrayStack()
        stack.push(1)
        stack.push('a')
        stack.push(1.2)
        stack.push('Test')
        self.assertEqual(stack.top(),'Test')
    def test_pop(self):
        stack = ArrayStack()
        stack.push(1)
        stack.push('a')
        stack.push(1.2)
        self.assertEqual(stack.pop(),1.2)
    def test_empty(self):
        stack = ArrayStack()
        self.assertTrue(stack.is_empty())
    def test_emptyException(self):
        stack = ArrayStack()
        with self.assertRaises(EmptyStack) as context:
            stack.pop()
            self.assertTrue('Stack is empty', context.exception)
    
if __name__ == "__main__":
    main()
    


