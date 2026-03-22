# Implementing queue using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def push(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return 
        
        self.rear.next = new_node
        self.rear = new_node
    
    def pop(self):
        if self.front is None:
            return -1
        popped = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return popped
    
    def peek(self):
        if self.front is None:
            return -1
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        count = 0
        temp = self.front
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.data, end="<-->")
            temp = temp.next

# Testing
queue = QueueUsingLinkedList()
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
print(queue.display())