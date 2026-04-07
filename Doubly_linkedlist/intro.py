class Node:
    def __init__(self,prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(prev=None, item=data, next=self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self,data):
        temp = self.start 
        if self.start != None:
            while temp.next != None:
                temp = temp.next
        n = Node(prev=temp, item=data, next=None)

        if temp == None:
            self.start = n
        else:
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp != None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp != None:
            n = Node(prev=temp, item=data, next=temp.next)
            if temp.next != None:
                temp.next.prev = n
            temp.next = n

    def delete_first(self):
        if self.start != None:
            self.start = self.start.next
            if self.start != None:
                self.start.prev = None

    def delete_last(self):
        if self.start == None:
            pass
        elif self.start.next == None:
            self.start = None 
        else:
            temp = self.start 
            while temp.next != None:
                temp = temp.next
            temp.prev.next = None
        
    def delete_item(self, data):
        if self.start != None:
            temp = self.start
            while temp != None:
                if temp.item == data:
                    if temp.next != None:
                        temp.next.prev = temp.prev
                    if temp.prev != None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next

    def display(self):
        temp = self.start
        while temp != None:
            print(temp.item, end="<==>")
            temp = temp.next




mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10),15)
mylist.delete_item(15)
mylist.delete_first()
mylist.delete_last()
mylist.insert_at_start(100)
mylist.insert_at_last(200)

mylist.display()
             
