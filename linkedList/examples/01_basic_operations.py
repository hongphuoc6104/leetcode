"""
=============================================================
 Example 1: Basic Linked List Operations
=============================================================

Demonstrates:
  - Building a linked list from array
  - Traversal, search, insert, delete
  - Dummy Head pattern

Time:  O(n) for most operations
Space: O(1) extra
"""


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def build_list(values):
    """Build linked list from array."""
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    """Convert linked list to array."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def print_list(head, label=""):
    """Print linked list with arrows."""
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next
    chain = " → ".join(parts) + " → None"
    if label:
        print(f"  {label}: {chain}")
    else:
        print(f"  {chain}")


def insert_at_head(head, val):
    """Insert at beginning: O(1)."""
    new_node = ListNode(val, head)
    return new_node


def insert_at_tail(head, val):
    """Insert at end: O(n)."""
    new_node = ListNode(val)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head


def delete_value(head, val):
    """Delete first occurrence using Dummy Head: O(n)."""
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
            break
        curr = curr.next
    return dummy.next


def remove_all(head, val):
    """Remove ALL occurrences using Dummy Head."""
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next


def search(head, val):
    """Search for value: O(n)."""
    idx = 0
    while head:
        if head.val == val:
            return idx
        head = head.next
        idx += 1
    return -1


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Build & Traverse")
    print("=" * 60)
    head = build_list([1, 2, 3, 4, 5])
    print_list(head, "Original")
    assert to_list(head) == [1, 2, 3, 4, 5]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Insert Operations")
    print("=" * 60)
    head = build_list([2, 3, 4])
    print_list(head, "Before")
    head = insert_at_head(head, 1)
    print_list(head, "Insert 1 at head")
    head = insert_at_tail(head, 5)
    print_list(head, "Insert 5 at tail")
    assert to_list(head) == [1, 2, 3, 4, 5]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 3: Delete Operations")
    print("=" * 60)
    head = build_list([1, 2, 3, 4, 5])
    head = delete_value(head, 3)
    print_list(head, "Delete 3")
    assert to_list(head) == [1, 2, 4, 5]

    head = delete_value(head, 1)
    print_list(head, "Delete head (1)")
    assert to_list(head) == [2, 4, 5]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 4: Remove All Occurrences")
    print("=" * 60)
    head = build_list([1, 2, 6, 3, 6, 6, 4])
    print_list(head, "Before")
    head = remove_all(head, 6)
    print_list(head, "Remove all 6s")
    assert to_list(head) == [1, 2, 3, 4]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 5: Search")
    print("=" * 60)
    head = build_list([10, 20, 30, 40])
    cases = [(20, 1), (40, 3), (50, -1)]
    for val, expected in cases:
        result = search(head, val)
        status = "✅" if result == expected else "❌"
        print(f"  search({val}) = {result} {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it:")
    print("   1. Why does delete_value use Dummy Head?")
    print("   2. What happens if we delete from an empty list?")
    print("   3. How to make insert_at_tail O(1)?")
