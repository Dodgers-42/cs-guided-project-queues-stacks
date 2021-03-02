class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LlStack:
    def __init__(self):
        self.top = None


    def push(self, item):
        # Create a new node
        new_node = LinkedListNode(item)
        # Set the new node to the current top
        new_node.next = self.top
        # make the new node, the new top
        self.top = new_node


    def pop(self):
        if self.top is None:
            return None
        #save the current top in a variable to return it
        old_top = self.top# move the top to the next node
        self.top + old_top.next

        return old_top.data




class Stack:
    def __init__(self):
        self.items = []


    def push(self, value):
        # add item to end of our items array
        items.append(value)

    def pop(self):
        if not self.items:
            return None
        # remove the top item
        top_item = self.items.pop()
        return top_item

    def peek(self):
        if not self.items:
            return None
        # return the last item of the stack (don't remove it though)
        return self.item[-1]











my_stack = Stack()

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')

print(f'The top of my stack is {my_stack.top.data}')

print(f'We just popped {my_stack.top.pop()}')

print(f'The top of my stack is {my_stack.top.data}')