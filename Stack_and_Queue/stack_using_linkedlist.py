# Implementing stack using doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return -1
        popped = self.top.data
        self.top = self.top.next
        return popped   

    def peek(self):
        if self.top is None:
            return -1
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        count = 0
        temp = self.top
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end="<==>")
            temp = temp.next

# Testing
stack = MyStack()
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
print(stack.display())