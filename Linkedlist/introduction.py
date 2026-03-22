class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1.next)
print(node1.data)
print(node1.next)
print(node1.next.data)
print(node1.next.next.data)
print(node3.next.data)

class LinkedList:
    def __init__(self):
        self.head = None
          
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if self.head is None:
            print('SLL is empty')
        else:
            current = self.head
            while current is not None:
                print(current.data, end = '->')
                current = current.next
            print('None')
    
    def insert_at(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current

    def delete_at(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            prev_node = None
            while current is not None and current.data != data:
                prev_node = current
                current = current.next
            prev_node.next = current.next

ssl = LinkedList()
ssl.append(10)
ssl.append(20)
ssl.append(30)
ssl.append(40)
ssl.append(1)
ssl.traverse()



