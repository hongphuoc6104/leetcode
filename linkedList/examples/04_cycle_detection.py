"""
=============================================================
 Example 4: Cycle Detection (Phát hiện vòng lặp)
=============================================================

Demonstrates Floyd's Cycle Detection:
  - has_cycle: detect if cycle exists
  - find_cycle_start: find where cycle begins
  - find_cycle_length: find cycle length

Time:  O(n)
Space: O(1) — no hash set needed!
"""


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def build_list_with_cycle(values, cycle_pos=-1):
    """Build list; if cycle_pos >= 0, tail → node[cycle_pos]."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0]


def has_cycle(head):
    """Floyd's: slow ×1, fast ×2. If they meet → cycle!"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def find_cycle_start(head):
    """
    Floyd's Phase 2: After detection, reset one to head.
    Move both 1 step. They meet at cycle start!
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Phase 2
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


def find_cycle_length(head):
    """After pointers meet, advance one until it circles back."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length = 1
            runner = slow.next
            while runner != slow:
                runner = runner.next
                length += 1
            return length
    return 0


def has_cycle_trace(head):
    """Cycle detection with trace."""
    slow = fast = head
    step = 0

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        step += 1
        s_val = slow.val if slow else "None"
        f_val = fast.val if fast else "None"
        met = " 🔄 MEET!" if slow == fast else ""
        print(f"    Step {step}: slow={s_val}, fast={f_val}{met}")

        if slow == fast:
            return True

    print("    ❌ No cycle (fast reached end)")
    return False


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Cycle Detection — WITH Cycle")
    print("=" * 60)
    # 1 → 2 → 3 → 4 → 5 → back to 3
    head = build_list_with_cycle([1, 2, 3, 4, 5], cycle_pos=2)
    print("  List: 1→2→3→4→5→(back to 3)")
    result = has_cycle_trace(head)
    assert result is True
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Cycle Detection — NO Cycle")
    print("=" * 60)
    head = build_list_with_cycle([1, 2, 3, 4, 5])
    print("  List: 1→2→3→4→5→None")
    result = has_cycle_trace(head)
    assert result is False
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 3: Find Cycle Start")
    print("=" * 60)
    cases = [
        ([1, 2, 3, 4, 5], 2, 3),
        ([1, 2, 3, 4, 5], 0, 1),
        ([1, 2], 0, 1),
    ]
    for vals, pos, expected_val in cases:
        head = build_list_with_cycle(vals, pos)
        start = find_cycle_start(head)
        assert start.val == expected_val
        print(f"  {vals}, cycle at pos {pos} "
              f"→ start={start.val} ✅")
    print()

    print("=" * 60)
    print("TEST 4: Cycle Length")
    print("=" * 60)
    cases = [
        ([1, 2, 3, 4, 5], 2, 3),   # cycle: 3→4→5→3 = length 3
        ([1, 2, 3], 0, 3),          # cycle: 1→2→3→1 = length 3
        ([1, 2, 3, 4, 5], -1, 0),   # no cycle
    ]
    for vals, pos, expected in cases:
        head = build_list_with_cycle(vals, pos)
        length = find_cycle_length(head)
        status = "✅" if length == expected else "❌"
        label = f"cycle at {pos}" if pos >= 0 else "no cycle"
        print(f"  {vals}, {label} → length={length} {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Floyd's uses O(1) space — no hash set!")
    print("   2. Phase 1: detect. Phase 2: find start.")
    print("   3. Why Phase 2 works: mathematical proof with distances")
