# Queue is a linear data structure that follows the FIFO (First In First Out) principle.
# Queue can be implemented using array or linked list.
# Queue is used in various applications such as function calls, expression evaluation, etc.

# Operations in Queue:
# 1. Enqueue: Adds an element to the rear of the queue.
# 2. Dequeue: Removes the element from the front of the queue.
# 3. Peek: Returns the element at the front of the queue.
# 4. isEmpty: Checks if the queue is empty.
# 5. isFull: Checks if the queue is full.

# Implementation of Queue using Array
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            return "Cannot dequeue, queue is empty"
        x = self.items.pop(0)
        return x
    
    def front(self):
        if len(self.items) == 0:
            return "Cannot front, queue is empty"
        return self.items[0]

    def size(self):
        return len(self.items)
    
    def display(self):
        print(self.items)
    
queue = Queue()
queue.display()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
print(queue.dequeue())
print(queue.front())
print(queue.size())
print(queue.is_empty())