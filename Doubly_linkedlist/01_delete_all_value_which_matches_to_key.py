class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        if head.next is None and head.data == x:
            return None
        
        temp = head
        prev = None
        new_head = head
        
        while temp:
            if temp.data == x:
                if prev is not None:
                    prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = prev
                if temp == new_head:
                    new_head = new_head.next
                    
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        return new_head


def build_dll(values):
    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current
        current = new_node

    return head


def print_dll(head):
    values = []
    current = head

    while current:
        values.append(str(current.data))
        current = current.next

    print(" <-> ".join(values) if values else "Empty List")


if __name__ == "__main__":
    sol = Solution()

    head1 = build_dll([2, 2, 10, 8, 4, 2, 5, 2])
    key1 = 2
    print("Original :", end=" ")
    print_dll(head1)
    print(f"Key      : {key1}")
    head1 = sol.deleteAllOccurOfX(head1, key1)
    print("Updated  :", end=" ")
    print_dll(head1)

    print()

    head2 = build_dll([1, 2, 3, 4, 5])
    key2 = 9
    print("Original :", end=" ")
    print_dll(head2)
    print(f"Key      : {key2}")
    head2 = sol.deleteAllOccurOfX(head2, key2)
    print("Updated  :", end=" ")
    print_dll(head2)

    print()

    head3 = build_dll([7, 7, 7, 7])
    key3 = 7
    print("Original :", end=" ")
    print_dll(head3)
    print(f"Key      : {key3}")
    head3 = sol.deleteAllOccurOfX(head3, key3)
    print("Updated  :", end=" ")
    print_dll(head3)
