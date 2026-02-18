# 📖 Chapter 4: Python Templates

## Template 1: Top K Largest

```python
import heapq
def top_k_largest(nums, k):
    """Min-heap of size K. Top = Kth largest."""
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return sorted(heap, reverse=True)
```

## Template 2: Top K Smallest

```python
def top_k_smallest(nums, k):
    """Max-heap (negate) of size K."""
    heap = [-x for x in nums[:k]]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num < -heap[0]:
            heapq.heapreplace(heap, -num)
    return sorted([-x for x in heap])
```

## Template 3: K Most Frequent

```python
from collections import Counter
def top_k_frequent(nums, k):
    counts = Counter(nums)
    return heapq.nlargest(k, counts.keys(), key=counts.get)
```

## Template 4: Merge K Sorted Lists

```python
def merge_k(lists):
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    result = []
    while heap:
        val, li, ei = heapq.heappop(heap)
        result.append(val)
        if ei + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][ei+1], li, ei+1))
    return result
```

## Template 5: Two Heaps — Median

```python
class MedianFinder:
    def __init__(self):
        self.lo = []   # max-heap (negate)
        self.hi = []   # min-heap
    
    def add(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
    
    def median(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

## Template 6: Custom Comparator via Tuple

```python
# heapq compares tuples element by element
# (priority, tie_breaker, data)
heap = []
heapq.heappush(heap, (distance, index, point))
```

---

## 📋 Pre-Coding Checklist

1. ✅ **Min or Max?** Negate for max-heap
2. ✅ **Fixed size K?** Use heapreplace
3. ✅ **Streaming data?** Heap is ideal
4. ✅ **Multiple criteria?** Use tuple (priority, tiebreaker)

---

**← Previous:** [Chapter 3](./03_complexity.md) | **Next →** [Examples](../examples/) 🚀
