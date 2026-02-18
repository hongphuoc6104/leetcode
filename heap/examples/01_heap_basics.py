"""
=============================================================
 Example 1: Heap Basics — heapq API
=============================================================

Demonstrates Python's heapq: push, pop, heapify, nsmallest/nlargest.
Shows min-heap default and max-heap trick (negate values).

Time:  O(log n) push/pop, O(n) heapify
"""
import heapq


def demo_basic_heap():
    """Basic heap operations."""
    nums = [5, 3, 8, 1, 4, 2, 7, 6]
    print(f"  Original: {nums}")

    # Heapify: O(n) — transforms list in-place into min-heap
    heapq.heapify(nums)
    print(f"  After heapify: {nums}")
    print(f"  Min (peek): {nums[0]}")

    # Pop smallest: O(log n)
    smallest = heapq.heappop(nums)
    print(f"  Popped: {smallest}, heap: {nums}")

    # Push: O(log n)
    heapq.heappush(nums, 0)
    print(f"  Pushed 0, heap: {nums}, min: {nums[0]}")

    return True


def demo_max_heap():
    """Max-heap using negation trick."""
    nums = [5, 3, 8, 1, 4]
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)

    print(f"  Original: {nums}")
    results = []
    while max_heap:
        results.append(-heapq.heappop(max_heap))
    print(f"  Popped in desc order: {results}")

    assert results == sorted(nums, reverse=True)
    return True


def demo_nsmallest():
    """heapq.nsmallest and nlargest."""
    nums = [5, 3, 8, 1, 4, 2, 7, 6]

    smallest_3 = heapq.nsmallest(3, nums)
    largest_3 = heapq.nlargest(3, nums)

    print(f"  nums: {nums}")
    print(f"  3 smallest: {smallest_3}")
    print(f"  3 largest: {largest_3}")

    assert smallest_3 == [1, 2, 3]
    assert largest_3 == [8, 7, 6]
    return True


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Basic Heap Operations")
    print("=" * 60)
    assert demo_basic_heap()
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Max-Heap via Negation")
    print("=" * 60)
    assert demo_max_heap()
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 3: nsmallest / nlargest")
    print("=" * 60)
    assert demo_nsmallest()
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 4: Heap Sort")
    print("=" * 60)
    data = [9, 4, 7, 1, 3, 8, 2, 6, 5]
    heap = data[:]
    heapq.heapify(heap)
    sorted_result = [heapq.heappop(heap) for _ in range(len(heap))]
    assert sorted_result == sorted(data)
    print(f"  Heap sort: {sorted_result} ✅")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. heapq = MIN-heap. Negate for MAX.")
    print("   2. heapify is O(n), not O(n log n)!")
    print("   3. heap[0] is always the smallest")
