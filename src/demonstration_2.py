"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        # Your code here
        self.in_stack = Stack()
        self.out_stack = Stack()
        
    def enqueue(self, item):
        # Your code here
        #Add item to input stack
        self.in_stack.push(item)

    def dequeue(self):
        # Your code here
        # Remove the appropriate item
        if len(self.out_stack.data) == 0:
            # If the output stack is empty
            # Reverse all the items from input stack to output stack
            while len(self.in_stack.data) > 0:
                # Pop from in_stack
                popped_item = self.in_stack.pop()
                # Push to our_stack
                self.out_stack.push(popped_item)

        #Remove items from the output stack
        return self.out_stack.pop()
