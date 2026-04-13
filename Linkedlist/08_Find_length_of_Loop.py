from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def lengthOfLoop(self, head):
        #code here
        temp = head
        mydict = dict()
        travel = 0
        while temp:
            if temp in mydict:
                return travel - mydict[temp]
            else:
                mydict[temp] = travel
                travel += 1
                temp = temp.next
        return 0

# T(n) = O(n)
# S(n) = O(n)

# ── Helper utilities ──────────────────────────────────────
def build_list_with_cycle(values: list, cycle_pos: int = -1) -> Optional[ListNode]:
    """
    Create a linked list from a Python list.
    If cycle_pos >= 0, the tail's next pointer connects back
    to the node at that index (0-based), creating a cycle.
    """
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if 0 <= cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0]


def print_list(head: Optional[ListNode], limit: int = 15) -> None:
    """Print the linked list (with a safety limit to avoid infinite loops)."""
    parts, seen = [], set()
    while head and len(parts) < limit:
        if head in seen:
            parts.append(f"... cycle back to {head.val}")
            break
        seen.add(head)
        parts.append(str(head.val))
        head = head.next
    print(" -> ".join(parts) if parts else "Empty List")


# ── Run & Test ────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Loop of length 3  (nodes: 2 → 0 → -4 → back to 2)
    head1 = build_list_with_cycle([3, 2, 0, -4], cycle_pos=1)
    print("List        :", end=" "); print_list(head1)
    print("Loop Length :", sol.lengthOfLoop(head1))

    print()

    # Test 2: Loop of length 2  (nodes: 1 → 2 → back to 1)
    head2 = build_list_with_cycle([1, 2], cycle_pos=0)
    print("List        :", end=" "); print_list(head2)
    print("Loop Length :", sol.lengthOfLoop(head2))

    print()

    # Test 3: No loop
    head3 = build_list_with_cycle([1, 2, 3, 4, 5])
    print("List        :", end=" "); print_list(head3)
    print("Loop Length :", sol.lengthOfLoop(head3))

    print()

    # Test 4: Empty list
    head4 = build_list_with_cycle([])
    print("List        :", end=" "); print_list(head4)
    print("Loop Length :", sol.lengthOfLoop(head4))