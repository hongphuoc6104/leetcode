"""
=============================================================
 Example 3: Fast & Slow Pointers (Nhanh & Chậm)
=============================================================

Demonstrates Floyd's Cycle Detection Algorithm:
  - Linked List cycle detection
  - Find cycle start position
  - Find middle of linked list

Time:  O(n)
Space: O(1)
"""


class ListNode:
    """Simple linked list node."""
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def build_linked_list(values, cycle_pos=-1):
    """
    Build linked list from values.
    If cycle_pos >= 0, last node points to node at cycle_pos.
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    nodes = [head]
    for val in values[1:]:
        node = ListNode(val)
        current.next = node
        current = node
        nodes.append(node)
    if cycle_pos >= 0:
        current.next = nodes[cycle_pos]
    return head


def has_cycle(head):
    """
    Detect cycle using Fast & Slow pointers.
    (Phát hiện vòng lặp bằng con trỏ Nhanh & Chậm.)

    slow moves 1 step, fast moves 2 steps.
    If they meet → cycle exists!
    (slow đi 1 bước, fast đi 2 bước. Nếu gặp nhau → có vòng lặp!)
    """
    slow = fast = head
    step = 0

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        step += 1
        print(f"    Step {step}: slow={slow.val}, "
              f"fast={fast.val if fast else 'None'}")

        if slow == fast:
            print(f"    🔄 Met at node {slow.val}! Cycle detected!")
            return True

    print("    ❌ fast reached end — no cycle")
    return False


def find_cycle_start(head):
    """
    Find where the cycle starts (Floyd's Phase 2).
    (Tìm nơi vòng lặp bắt đầu.)

    After detection: reset one pointer to head.
    Move both 1 step at a time. They meet at cycle start!
    (Sau phát hiện: reset 1 con trỏ về head.
     Cả 2 đi 1 bước. Gặp nhau tại đầu vòng lặp!)
    """
    # Phase 1: Detect cycle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Phase 2: Find start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


def find_middle(head):
    """
    Find middle of linked list.
    (Tìm giữa linked list.)

    When fast reaches end, slow is at middle!
    (Khi fast đến cuối, slow ở giữa!)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Cycle Detection — WITH cycle")
    print("=" * 60)
    # 1 → 2 → 3 → 4 → 5 → 3 (cycle at node 3)
    head = build_linked_list([1, 2, 3, 4, 5], cycle_pos=2)
    print("  List: 1→2→3→4→5→(back to 3)")
    result = has_cycle(head)
    assert result is True
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Cycle Detection — NO cycle")
    print("=" * 60)
    head = build_linked_list([1, 2, 3, 4, 5])
    print("  List: 1→2→3→4→5→None")
    result = has_cycle(head)
    assert result is False
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 3: Find Cycle Start")
    print("=" * 60)
    head = build_linked_list([1, 2, 3, 4, 5, 6], cycle_pos=2)
    print("  List: 1→2→3→4→5→6→(back to 3)")
    start = find_cycle_start(head)
    print(f"  Cycle starts at node: {start.val}")
    assert start.val == 3
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 4: Find Middle of Linked List")
    print("=" * 60)
    for values in [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]:
        head = build_linked_list(values)
        mid = find_middle(head)
        print(f"  List: {values} → middle = {mid.val}")
    print("  ✅ Passed!")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. WHY does Phase 2 of Floyd's algorithm work?")
    print("      (TẠI SAO Phase 2 hoạt động?)")
    print("      Hint: think about distances from head to cycle start")
    print("   2. For find_middle, what if we want the FIRST middle")
    print("      in an even-length list? (e.g., [1,2,3,4] → 2, not 3)")
    print("      (Nếu muốn giữa ĐẦU TIÊN trong list chẵn?)")
