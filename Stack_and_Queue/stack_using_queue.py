# Implementing stack using queue

from collections import deque
class StackUingQueue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        if len(self.queue) == 0:
            return "Stack is empty."
        return self.queue.popleft()

    def peek(self):
        if len(self.queue) == 0:
            return "Stack is empty."
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len((self.queue))
    
    def display(self):
        return list(self.queue)


# Testing
stack = StackUingQueue()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.display())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.size())