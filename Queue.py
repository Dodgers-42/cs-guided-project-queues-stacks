class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        #Add item to the end of queue
        new_node = LinkedListNode(value)
        if self.rear is None:
            # The queue is empty so far
            self.rear = new_node
            self.front = new_node
        else:
            #Add node to the current rear node
            self.rear.next = new_node
            self.rear = new_node


    def dequeue(self):
        # remove and return item from front of queue
        # Store the old front node, so we can return it
        old_front = self.front
        # Move the front pointer to the next node 
        self.front = self.front.next

        if self.front is None:
            #we just deleted the last node
            self.rear = None

        return old_front


my_queue = Queue()

my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')

print(f'The front is now {my_queue.front.data}')

print(f'The front is now {my_queue.front.data}')
print(f'The front is now {my_queue.front.data}')
print(f'The front is now {my_queue.front.data}')
