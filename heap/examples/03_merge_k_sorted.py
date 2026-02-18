"""
=============================================================
 Example 3: Merge K Sorted Lists (LC 23)
=============================================================

Use min-heap of size K to always pick the smallest element.
Time:  O(N log K) where N = total elements, K = number of lists
Space: O(K)
"""
import heapq


def merge_k_sorted_arrays(lists):
    """Merge K sorted arrays using heap."""
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_linked(lists):
    """Merge K sorted linked lists (LC 23)."""
    heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))

    dummy = curr = ListNode(0)
    while heap:
        val, idx, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def from_list(arr):
    dummy = curr = ListNode(0)
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Merge K Sorted Arrays")
    print("=" * 60)
    lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    result = merge_k_sorted_arrays(lists)
    assert result == list(range(1, 10))
    print(f"  {lists} → {result} ✅")

    lists2 = [[1, 3, 5], [2, 4, 6], [0]]
    result = merge_k_sorted_arrays(lists2)
    assert result == [0, 1, 2, 3, 4, 5, 6]
    print(f"  {lists2} → {result} ✅")
    print()

    print("=" * 60)
    print("TEST 2: Merge K Linked Lists")
    print("=" * 60)
    linked = [from_list([1, 4, 5]),
              from_list([1, 3, 4]),
              from_list([2, 6])]
    merged = merge_k_linked(linked)
    result = to_list(merged)
    assert result == [1, 1, 2, 3, 4, 4, 5, 6]
    print(f"  Merged: {result} ✅")
    print()

    print("=" * 60)
    print("TEST 3: Edge Cases")
    print("=" * 60)
    assert merge_k_sorted_arrays([]) == []
    print("  Empty → [] ✅")
    assert merge_k_sorted_arrays([[], [1], []]) == [1]
    print("  [[], [1], []] → [1] ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Heap always has K elements (one per list)")
    print("   2. Tuple: (value, list_index, element_index)")
    print("   3. O(N log K) — much better than O(N log N) merge all")
