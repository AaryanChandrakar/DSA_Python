# Implementing queue using 2 stack

class QueueUsing2Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        if not self.stack1:
            return "Queue is empty."
        return self.stack1.pop()
    
    def peek(self):
        if not self.stack1:
            print("Queue is empty.")
            return -1
        return self.stack1[0]
    
    def is_empty(self):
        return len(self.stack1) == 0
    
    def size(self):
        return len(self.stack1)

    def display(self):
        return list(self.stack1)

# Testing
queue = QueueUsing2Stack()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
print(queue.display())
print(queue.pop())
print(queue.peek())
print(queue.is_empty())
print(queue.size())
            

