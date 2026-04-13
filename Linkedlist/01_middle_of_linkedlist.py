from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            head = head.next
            current = current.next.next
        return head


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

    # Test 1: Odd-length list  →  middle = 3
    head1 = build_list([1, 2, 3, 4, 5])
    print("List     :", end=" "); print_list(head1)
    mid1 = sol.middleNode(head1)
    print("Middle   :", end=" "); print_list(mid1)

    print()

    # Test 2: Even-length list  →  second middle = 4
    head2 = build_list([1, 2, 3, 4, 5, 6])
    print("List     :", end=" "); print_list(head2)
    mid2 = sol.middleNode(head2)
    print("Middle   :", end=" "); print_list(mid2)

    print()

    # Test 3: Single node
    head3 = build_list([42])
    print("List     :", end=" "); print_list(head3)
    mid3 = sol.middleNode(head3)
    print("Middle   :", end=" "); print_list(mid3)
