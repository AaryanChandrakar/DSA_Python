from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


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
    n1 = 2
    print("Original :", end=" ")
    print_list(head1)
    print(f"n        : {n1}")
    head1 = sol.removeNthFromEnd(head1, n1)
    print("Updated  :", end=" ")
    print_list(head1)

    print()

    head2 = build_list([1, 2, 3, 4, 5])
    n2 = 5
    print("Original :", end=" ")
    print_list(head2)
    print(f"n        : {n2}")
    head2 = sol.removeNthFromEnd(head2, n2)
    print("Updated  :", end=" ")
    print_list(head2)

    print()

    head3 = build_list([10, 20])
    n3 = 1
    print("Original :", end=" ")
    print_list(head3)
    print(f"n        : {n3}")
    head3 = sol.removeNthFromEnd(head3, n3)
    print("Updated  :", end=" ")
    print_list(head3)

    print()

    head4 = build_list([99])
    n4 = 1
    print("Original :", end=" ")
    print_list(head4)
    print(f"n        : {n4}")
    head4 = sol.removeNthFromEnd(head4, n4)
    print("Updated  :", end=" ")
    print_list(head4)
