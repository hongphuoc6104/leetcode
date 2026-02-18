"""
=============================================================
 Example 5: Remove Nth Node from End (LC 19)
=============================================================

Demonstrates Two Pointer Gap technique:
  - Advance fast by n, then move both until end
  - Combined with Dummy Head for clean code

Also: Palindrome check combining Reverse + Fast/Slow

Time:  O(n) — single pass
Space: O(1)
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


def remove_nth_from_end(head, n):
    """
    Remove nth node from the end using gap technique.

    Strategy:
      1. Advance fast by n+1 steps (gap)
      2. Move both until fast = None
      3. slow.next is the node to remove
    """
    dummy = ListNode(0, head)
    fast = slow = dummy

    # Create gap of n+1
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove the target node
    slow.next = slow.next.next
    return dummy.next


def remove_nth_trace(head, n):
    """Remove nth from end with trace."""
    dummy = ListNode(0, head)
    vals = to_list(head)
    fast = slow = dummy

    print(f"  List: {vals}, remove {n}th from end")

    for i in range(n + 1):
        fast = fast.next
    f_val = fast.val if fast else "None"
    print(f"  After gap: slow=dummy, fast={f_val}")

    while fast:
        slow = slow.next
        fast = fast.next
    print(f"  After walk: slow={slow.val}, "
          f"remove slow.next={slow.next.val}")

    slow.next = slow.next.next
    return dummy.next


def is_palindrome(head):
    """
    Check if linked list is palindrome.
    Combines: Fast/Slow (find middle) + Reverse (second half).
    """
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Compare first half with reversed second half
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Remove Nth from End — Trace")
    print("=" * 60)
    head = build_list([1, 2, 3, 4, 5])
    result = remove_nth_trace(head, 2)
    r = to_list(result)
    print(f"  Result: {r}")
    assert r == [1, 2, 3, 5]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Remove Nth — More Cases")
    print("=" * 60)
    cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ]
    for vals, n, expected in cases:
        head = build_list(vals)
        result = remove_nth_from_end(head, n)
        r = to_list(result)
        status = "✅" if r == expected else "❌"
        print(f"  {vals}, n={n} → {r} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Palindrome Check")
    print("=" * 60)
    cases = [
        ([1, 2, 2, 1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3], False),
        ([1], True),
        ([1, 2], False),
    ]
    for vals, expected in cases:
        head = build_list(vals)
        result = is_palindrome(head)
        status = "✅" if result == expected else "❌"
        print(f"  {vals} → {result} {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Gap technique: one pass, O(1) space")
    print("   2. Dummy Head handles removing the first node")
    print("   3. Palindrome = Fast/Slow + Reverse = 2 patterns combined!")
