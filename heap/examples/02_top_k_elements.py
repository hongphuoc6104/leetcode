"""
=============================================================
 Example 2: Top K Elements (LC 215, LC 347)
=============================================================

Find Kth largest or K most frequent using a heap.
Time:  O(n log k) — much better than O(n log n) sort when k << n
Space: O(k)
"""
import heapq
from collections import Counter


def kth_largest(nums, k):
    """Kth largest element (LC 215). Min-heap of size k."""
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap[0]  # Top of min-heap = kth largest


def top_k_frequent(nums, k):
    """K most frequent elements (LC 347)."""
    counts = Counter(nums)
    return heapq.nlargest(k, counts.keys(), key=counts.get)


def k_closest_points(points, k):
    """K Closest Points to Origin (LC 973). Max-heap of size k."""
    heap = []
    for x, y in points:
        dist = x * x + y * y
        if len(heap) < k:
            heapq.heappush(heap, (-dist, x, y))
        elif -dist > heap[0][0]:
            heapq.heapreplace(heap, (-dist, x, y))
    return [[x, y] for _, x, y in heap]


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Kth Largest Element")
    print("=" * 60)
    cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
    ]
    for nums, k, expected in cases:
        result = kth_largest(nums, k)
        status = "✅" if result == expected else "❌"
        print(f"  k={k}: {result} {status}")
    print()

    print("=" * 60)
    print("TEST 2: Top K Frequent")
    print("=" * 60)
    result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert set(result) == {1, 2}
    print(f"  [1,1,1,2,2,3] → top 2: {result} ✅")

    result = top_k_frequent([1], 1)
    assert result == [1]
    print(f"  [1] → top 1: {result} ✅")
    print()

    print("=" * 60)
    print("TEST 3: K Closest Points")
    print("=" * 60)
    result = k_closest_points([[1, 3], [-2, 2]], 1)
    assert result == [[-2, 2]]
    print(f"  k=1: {result} ✅")

    result = k_closest_points([[3, 3], [5, -1], [-2, 4]], 2)
    dists = sorted([x*x + y*y for x, y in result])
    print(f"  k=2: {result}, dists: {dists} ✅")
    print()

    print("=" * 60)
    print("TEST 4: Performance — Heap vs Sort")
    print("=" * 60)
    import time
    import random
    n = 100000
    k = 10
    data = [random.randint(0, 10**6) for _ in range(n)]

    start = time.perf_counter()
    r1 = sorted(data, reverse=True)[k - 1]
    t_sort = time.perf_counter() - start

    start = time.perf_counter()
    r2 = kth_largest(data[:], k)
    t_heap = time.perf_counter() - start

    assert r1 == r2
    print(f"  n={n}, k={k}")
    print(f"  Sort: {t_sort*1000:.2f}ms | Heap: {t_heap*1000:.2f}ms")
    print()

    print("✅ All tests passed!")
