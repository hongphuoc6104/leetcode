"""
=============================================================
 Example 3: Merge Sorted Lists (Gộp danh sách sorted)
=============================================================

Demonstrates:
  - Merge two sorted lists (LC 21)
  - Merge k sorted lists (LC 23) using divide & conquer

Time:  Merge two: O(n + m)
       Merge k:   O(N log k) where N = total nodes
Space: O(1) extra for merge two
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


def merge_two(l1, l2):
    """
    Merge two sorted lists into one sorted list.
    Uses Dummy Head pattern.
    """
    dummy = curr = ListNode(0)

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2
    return dummy.next


def merge_two_trace(l1, l2):
    """Merge with step trace."""
    dummy = curr = ListNode(0)
    step = 0

    while l1 and l2:
        step += 1
        if l1.val <= l2.val:
            print(f"    Step {step}: pick {l1.val} "
                  f"(L1={l1.val} ≤ L2={l2.val})")
            curr.next = l1
            l1 = l1.next
        else:
            print(f"    Step {step}: pick {l2.val} "
                  f"(L2={l2.val} < L1={l1.val})")
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    remaining = l1 or l2
    if remaining:
        rem_vals = to_list(remaining)
        print(f"    Append remaining: {rem_vals}")
    curr.next = remaining
    return dummy.next


def merge_k_lists(lists):
    """
    Merge k sorted lists using Divide & Conquer.
    Split in half, merge left, merge right, merge results.
    Time: O(N log k)
    """
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = merge_k_lists(lists[:mid])
    right = merge_k_lists(lists[mid:])
    return merge_two(left, right)


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Merge Two — Trace")
    print("=" * 60)
    l1 = build_list([1, 3, 5, 7])
    l2 = build_list([2, 4, 6])
    print(f"  L1: {to_list(l1)}")
    print(f"  L2: {to_list(l2)}")
    result = merge_two_trace(l1, l2)
    r = to_list(result)
    print(f"  Merged: {r}")
    assert r == [1, 2, 3, 4, 5, 6, 7]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Merge Two — Edge Cases")
    print("=" * 60)
    cases = [
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [1], [1]),
        ([], [], []),
        ([1], [1], [1, 1]),
    ]
    for v1, v2, expected in cases:
        l1 = build_list(v1)
        l2 = build_list(v2)
        result = merge_two(l1, l2)
        r = to_list(result)
        status = "✅" if r == expected else "❌"
        print(f"  {v1} + {v2} → {r} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Merge K Sorted Lists")
    print("=" * 60)
    lists = [
        build_list([1, 4, 7]),
        build_list([2, 5, 8]),
        build_list([3, 6, 9]),
    ]
    print("  Lists: [1,4,7], [2,5,8], [3,6,9]")
    result = merge_k_lists(lists)
    r = to_list(result)
    print(f"  Merged: {r}")
    assert r == list(range(1, 10))
    print("  ✅ Passed!")
    print()

    # Test with empty lists
    lists = [
        build_list([1, 3]),
        None,
        build_list([2, 4]),
    ]
    result = merge_k_lists(lists)
    r = to_list(result)
    print(f"  With None: {r}")
    assert r == [1, 2, 3, 4]
    print("  ✅ Passed!")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Dummy Head makes merge clean — no special first-node logic")
    print("   2. curr.next = l1 or l2 handles remaining in one line")
    print("   3. Merge k: D&C gives O(N log k) vs naive O(N×k)")
