from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
            
        temp = head
        values = []

        # Odd indices
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break

        # Even indices
        temp = head.next
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
        
        temp = head
        index = 0
        while temp and index < len(values):
            temp.val = values[index]
            index += 1
            temp = temp.next

        return head
    
# T(n) = O(n)
# S(n) = O(n)


def build_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_list(head: Optional[ListNode]) -> None:
    parts = []

    while head:
        parts.append(str(head.val))
        head = head.next

    print(" -> ".join(parts) if parts else "Empty List")


if __name__ == "__main__":
    sol = Solution()

    head1 = build_list([1, 2, 3, 4, 5])
    print("Original :", end=" ")
    print_list(head1)
    head1 = sol.oddEvenList(head1)
    print("Odd-Even :", end=" ")
    print_list(head1)

    print()

    head2 = build_list([2, 1, 3, 5, 6, 4, 7])
    print("Original :", end=" ")
    print_list(head2)
    head2 = sol.oddEvenList(head2)
    print("Odd-Even :", end=" ")
    print_list(head2)

    print()

    head3 = build_list([10])
    print("Original :", end=" ")
    print_list(head3)
    head3 = sol.oddEvenList(head3)
    print("Odd-Even :", end=" ")
    print_list(head3)

    print()

    head4 = build_list([])
    print("Original :", end=" ")
    print_list(head4)
    head4 = sol.oddEvenList(head4)
    print("Odd-Even :", end=" ")
    print_list(head4)
