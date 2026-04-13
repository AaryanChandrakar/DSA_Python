from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head 
        while temp: 
            stack.append(temp.val)
            temp = temp.next

        temp = head 
        while temp:
            temp.val = stack.pop()
            temp = temp.next
        return head

# T(n) = O(n) + O(n) = O(n)
# S(n) = O(n)

# ── Helper utilities ──────────────────────────────────────
def build_list(values: list) -> Optional[ListNode]:
    """Create a linked list from a Python list."""
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_list(head: Optional[ListNode]) -> None:
    """Print the linked list in a readable format."""
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next
    print(" -> ".join(parts) if parts else "Empty List")


# ── Run & Test ────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    # Test 1: General case
    head1 = build_list([1, 2, 3, 4, 5])
    print("Original :", end=" "); print_list(head1)
    head1 = sol.reverseList(head1)
    print("Reversed :", end=" "); print_list(head1)

    print()

    # Test 2: Single node
    head2 = build_list([42])
    print("Original :", end=" "); print_list(head2)
    head2 = sol.reverseList(head2)
    print("Reversed :", end=" "); print_list(head2)

    print()

    # Test 3: Empty list
    head3 = build_list([])
    print("Original :", end=" "); print_list(head3)
    head3 = sol.reverseList(head3)
    print("Reversed :", end=" "); print_list(head3)