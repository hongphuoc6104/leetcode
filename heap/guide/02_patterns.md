# 📖 Chapter 2: Heap Patterns

## Pattern 1: Top K Elements

### 🔍 Signal: "kth largest", "k most frequent", "top k"

### 💡 Key Insight
Use a **min-heap of size K**. Keep only K largest elements. Heap top = Kth largest.

```python
import heapq
def top_k_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return sorted(heap, reverse=True)
```
📌 LC 215, LC 347, LC 692, LC 973

---

## Pattern 2: Merge K Sorted Lists/Arrays

### 🔍 Signal: "merge k sorted", "smallest range"

### 💡 Key Insight
Push first element from each list. Pop min, push next element from that list.

```python
def merge_k_sorted(lists):
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
```
📌 LC 23, LC 378, LC 632

---

## Pattern 3: Two Heaps — Median

### 🔍 Signal: "median of stream", "balance two groups"

### 💡 Key Insight
Use **max-heap** for lower half, **min-heap** for upper half. Median is at the tops.

```python
class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (negate values)
        self.hi = []  # min-heap
    
    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
    
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```
📌 LC 295, LC 480

---

## Pattern 4: Greedy + Heap — Scheduling

### 🔍 Signal: "task scheduler", "meeting rooms", "minimum cost"

```python
# Reorganize String (LC 767)
from collections import Counter
def reorganize(s):
    counts = Counter(s)
    heap = [(-cnt, ch) for ch, cnt in counts.items()]
    heapq.heapify(heap)
    result = []
    prev = (0, '')
    while heap:
        cnt, ch = heapq.heappop(heap)
        result.append(ch)
        if prev[0] < 0:
            heapq.heappush(heap, prev)
        prev = (cnt + 1, ch)
    return ''.join(result) if len(result) == len(s) else ""
```
📌 LC 621, LC 767, LC 253

---

## Pattern 5: Custom Comparator — Tuple Heap

### 🔍 Signal: "sort by multiple criteria", "closest points"

```python
# K Closest Points (LC 973)
def k_closest(points, k):
    heap = []
    for x, y in points:
        dist = x*x + y*y
        if len(heap) < k:
            heapq.heappush(heap, (-dist, x, y))
        elif -dist > heap[0][0]:
            heapq.heapreplace(heap, (-dist, x, y))
    return [[x, y] for _, x, y in heap]
```

---

## 📊 Pattern Decision Table

| Signal | Pattern | Heap Type |
|--------|---------|-----------|
| "K largest/smallest" | Top K | min-heap of size K |
| "K sorted streams" | Merge K | min-heap of K elements |
| "Running median" | Two Heaps | max-heap + min-heap |
| "Schedule optimally" | Greedy + Heap | varies |
| "Multi-criteria sort" | Custom | tuple heap |

---

**← Previous:** [Chapter 1](./01_introduction.md) | **Next →** [Chapter 3](./03_complexity.md)
