"""
=============================================================
 Example 2: Reverse Linked List (Đảo ngược Linked List)
=============================================================

Demonstrates:
  - Iterative reverse (3 pointers)
  - Recursive reverse
  - Reverse between positions m and n

Time:  O(n)
Space: O(1) iterative, O(n) recursive
"""


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def reverse_iterative(head):
    """Reverse using 3 pointers: prev, curr, nxt."""
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def reverse_trace(head):
    """Reverse with step-by-step trace."""
    prev, curr = None, head
    step = 0

    while curr:
        step += 1
        nxt = curr.next
        curr.next = prev

        prev_val = prev.val if prev else "None"
        nxt_val = nxt.val if nxt else "None"
        print(f"    Step {step}: curr={curr.val} "
              f"→ curr.next = {prev_val} "
              f"| prev={curr.val}, curr={nxt_val}")

        prev = curr
        curr = nxt

    return prev


def reverse_recursive(head):
    """Reverse using recursion."""
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def reverse_between(head, m, n):
    """Reverse nodes from position m to n (1-indexed)."""
    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(m - 1):
        prev = prev.next

    curr = prev.next
    for _ in range(n - m):
        nxt = curr.next
        curr.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt

    return dummy.next


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Iterative Reverse — Trace")
    print("=" * 60)
    head = build_list([1, 2, 3, 4, 5])
    print(f"  Before: {to_list(head)}")
    result = reverse_trace(head)
    print(f"  After:  {to_list(result)}")
    assert to_list(result) == [5, 4, 3, 2, 1]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Recursive Reverse")
    print("=" * 60)
    head = build_list([1, 2, 3, 4, 5])
    result = reverse_recursive(head)
    print(f"  Result: {to_list(result)}")
    assert to_list(result) == [5, 4, 3, 2, 1]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 3: Reverse Between Positions")
    print("=" * 60)
    cases = [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
        ([1, 2, 3], 1, 3, [3, 2, 1]),
    ]
    for vals, m, n, expected in cases:
        head = build_list(vals)
        result = reverse_between(head, m, n)
        r = to_list(result)
        status = "✅" if r == expected else "❌"
        print(f"  {vals} reverse [{m},{n}] → {r} {status}")
    print()

    print("=" * 60)
    print("TEST 4: Edge Cases")
    print("=" * 60)
    # Empty list
    assert reverse_iterative(None) is None
    print("  Empty list → None ✅")

    # Single node
    head = build_list([1])
    result = reverse_iterative(head)
    assert to_list(result) == [1]
    print("  Single node → [1] ✅")

    # Two nodes
    head = build_list([1, 2])
    result = reverse_iterative(head)
    assert to_list(result) == [2, 1]
    print("  Two nodes → [2, 1] ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. 3 pointers: prev, curr, nxt — MEMORIZE this!")
    print("   2. Save nxt BEFORE changing curr.next")
    print("   3. Reverse returns prev (new head)")
