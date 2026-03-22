# Stack is a linear data structure that follows the LIFO (Last In First Out) principle.
# Stack can be implemented using array or linked list.
# Stack is used in various applications such as function calls, expression evaluation, etc.

# Operations in Stack:
# 1. Push: Adds an element to the top of the stack.
# 2. Pop: Removes the element from the top of the stack.
# 3. Peek: Returns the element at the top of the stack.
# 4. isEmpty: Checks if the stack is empty.
# 5. isFull: Checks if the stack is full.

# Implementation of Stack using Array
class Stack:
    def __init__(self):
        self.items = []
    
    def  is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Cannot pop, stack is empty"
        x = self.items.pop()
        return x
    
    def top(self):
        if len(self.items) == 0:
            return "Cannot top, stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)
    
    def display(self):
        print(self.items)
    
stack = Stack()
stack.display()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print(stack.pop())
print(stack.top())
print(stack.size())
print(stack.is_empty())