# 📖 Chủ đề 11: Heap / Priority Queue

## Lý thuyết cơ bản

**Heap** là cây nhị phân đặc biệt: **Min-Heap** (gốc nhỏ nhất), **Max-Heap** (gốc lớn nhất).

### Python Implementation
```python
import heapq

# Min-Heap (mặc định Python)
heap = []
heapq.heappush(heap, val)     # O(log n)
min_val = heapq.heappop(heap) # O(log n)
peek = heap[0]                 # O(1)

# Max-Heap (dùng giá trị âm)
heapq.heappush(heap, -val)
max_val = -heapq.heappop(heap)

# Heap từ list
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)             # O(n)

# Top K elements
heapq.nlargest(k, arr)        # O(n log k)
heapq.nsmallest(k, arr)
```

### Pattern: Two Heaps (Find Median)
```python
class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negate)
        self.large = []  # min-heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Kth Largest Stream | [LC 703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Min-heap size k |
| 2 | Last Stone Weight | [LC 1046](https://leetcode.com/problems/last-stone-weight/) | Max-heap |
| 3 | K Weakest Rows | [LC 1337](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) | Heap + counting |
| 4 | Max Product Two | [LC 1464](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) | Top 2 |
| 5 | Subsequence Length K | [LC 2099](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/) | Heap top k |
| 6 | Take Gifts | [LC 2558](https://leetcode.com/problems/take-gifts-from-the-richest-pile/) | Max-heap simulation |
| 7 | Min Ops Threshold | [LC 3065](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/) | Sort/heap |
| 8 | Relative Ranks | [LC 506](https://leetcode.com/problems/relative-ranks/) | Sort by score |
| 9 | Distance Two Arrays | [LC 1385](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/) | BS hoặc sort |
| 10 | Make Array Zero | [LC 2357](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/) | Set size = ops |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Kth Largest Element | [LC 215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Quick select / heap |
| 2 | Ugly Number II | [LC 264](https://leetcode.com/problems/ugly-number-ii/) | Min-heap |
| 3 | Top K Frequent | [LC 347](https://leetcode.com/problems/top-k-frequent-elements/) | Counter + heap |
| 4 | Design Twitter | [LC 355](https://leetcode.com/problems/design-twitter/) | Merge k feeds (heap) |
| 5 | K Pairs Smallest Sum | [LC 373](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | Min-heap BFS |
| 6 | Kth Smallest Sorted Matrix | [LC 378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Heap hoặc BS |
| 7 | Task Scheduler | [LC 621](https://leetcode.com/problems/task-scheduler/) | Max-heap + cooldown |
| 8 | Reorganize String | [LC 767](https://leetcode.com/problems/reorganize-string/) | Max-heap greedy |
| 9 | K Closest Points | [LC 973](https://leetcode.com/problems/k-closest-points-to-origin/) | Max-heap size k |
| 10 | Furthest Building | [LC 1642](https://leetcode.com/problems/furthest-building-you-can-reach/) | Min-heap greedy |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Merge k Sorted Lists | [LC 23](https://leetcode.com/problems/merge-k-sorted-lists/) | Min-heap k pointers |
| 2 | Sliding Window Max | [LC 239](https://leetcode.com/problems/sliding-window-maximum/) | Deque (or heap lazy) |
| 3 | Find Median Stream | [LC 295](https://leetcode.com/problems/find-median-from-data-stream/) | Two heaps |
| 4 | Trap Water II | [LC 407](https://leetcode.com/problems/trapping-rain-water-ii/) | BFS + min-heap |
| 5 | Sliding Window Median | [LC 480](https://leetcode.com/problems/sliding-window-median/) | Two heaps + lazy |
| 6 | IPO | [LC 502](https://leetcode.com/problems/ipo/) | Two heaps greedy |
| 7 | Smallest Range K Lists | [LC 632](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Min-heap + track max |
| 8 | Swim Rising Water | [LC 778](https://leetcode.com/problems/swim-in-rising-water/) | Dijkstra-like |
| 9 | Min Cost Hire K | [LC 857](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) | Sort + max-heap |
| 10 | Min Time Build | [LC 1199](https://leetcode.com/problems/minimum-time-to-build-blocks/) | Huffman-like heap |

---

## Tips
- **Top K** → dùng Heap size K (min-heap cho top K lớn nhất)
- **Merge K sorted** → Min-heap
- Python chỉ có **min-heap**, dùng giá trị âm cho max-heap
