class Node:
    def __init__(self, item=None, next=None):
        self.item = item 
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self,data):
        n = Node(data)
        if self.start is not None:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start 
        while temp != None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        n = Node(data)
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n

    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end="-->")
            temp = temp.next
    
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        temp = self.start
        if self.start == None:
            pass
        elif self.start.next == None:
            self.start =  None
        else:
            temp = self.start 
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else: 
            temp = self.start 
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next





# Driver code
mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.delete_item(20)
mylist.delete_first()
mylist.delete_last()
mylist.display()
