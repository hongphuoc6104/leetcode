# 📖 Chủ đề 4: Binary Search

## Lý thuyết cơ bản

**Binary Search** chia đôi không gian tìm kiếm mỗi bước, giảm từ O(n) xuống **O(log n)**. Yêu cầu dữ liệu **đã sắp xếp** hoặc có tính **monotonic**.

### Template cơ bản
```python
# Tìm chính xác
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Tìm lower bound (phần tử đầu tiên >= target)
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Binary Search on Answer
def binary_search_answer(lo, hi):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

---

## Danh sách 30 bài LeetCode

> ⚡ Đã hoàn thành 7/30 bài. Chi tiết tại [README.md](../../README.md).

### 🟢 Easy (7/10 ✅)
| # | Bài | Trạng thái | Gợi ý |
|---|-----|------------|-------|
| 1 | 704. Binary Search | ✅ | Template cơ bản |
| 2 | 035. Search Insert Position | ✅ | Lower bound |
| 3 | 069. Sqrt(x) | ✅ | BS on answer |
| 4 | 278. First Bad Version | ✅ | Lower bound |
| 5 | 367. Valid Perfect Square | ✅ | BS on answer |
| 6 | 374. Guess Number | ✅ | Template cơ bản |
| 7 | 744. Find Smallest Letter | ✅ | Upper bound |
| 8 | 1351. Count Negative Numbers | ⬜ | BS mỗi row hoặc staircase |
| 9 | 1608. Special Array | ⬜ | BS on answer |
| 10 | 2089. Find Target Indices | ⬜ | BS tìm bounds |

### 🟡 Medium (0/10)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Search in Rotated Array | [LC 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Xác định nửa sorted |
| 2 | Find First and Last | [LC 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | 2 lần BS |
| 3 | Search a 2D Matrix | [LC 74](https://leetcode.com/problems/search-a-2d-matrix/) | Treat as 1D |
| 4 | Find Min Rotated | [LC 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | BS trên rotated |
| 5 | Find Peak Element | [LC 162](https://leetcode.com/problems/find-peak-element/) | BS on slope |
| 6 | Single Element Sorted | [LC 540](https://leetcode.com/problems/single-element-in-a-sorted-array/) | BS trên index parity |
| 7 | K Closest Elements | [LC 658](https://leetcode.com/problems/find-k-closest-elements/) | BS on left bound |
| 8 | Koko Eating Bananas | [LC 875](https://leetcode.com/problems/koko-eating-bananas/) | BS on answer |
| 9 | Time Based Key-Value | [LC 981](https://leetcode.com/problems/time-based-key-value-store/) | BS on timestamp |
| 10 | Ship Packages D Days | [LC 1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | BS on answer |

### 🔴 Hard (0/10)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Median Two Sorted Arrays | [LC 4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | BS on partition |
| 2 | Find Min Rotated II | [LC 154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | Handle duplicates |
| 3 | Split Array Largest Sum | [LC 410](https://leetcode.com/problems/split-array-largest-sum/) | BS on answer |
| 4 | Kth Smallest Mult Table | [LC 668](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/) | BS + count |
| 5 | Kth Smallest Pair Dist | [LC 719](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) | BS + two pointers |
| 6 | Swim in Rising Water | [LC 778](https://leetcode.com/problems/swim-in-rising-water/) | BS + BFS/DFS |
| 7 | Nth Magical Number | [LC 878](https://leetcode.com/problems/nth-magical-number/) | BS + LCM |
| 8 | Divide Chocolate | [LC 1231](https://leetcode.com/problems/divide-chocolate/) | BS on answer |
| 9 | Max Value Equation | [LC 1499](https://leetcode.com/problems/max-value-of-equation/) | Deque/heap |
| 10 | Min Deviation Array | [LC 1675](https://leetcode.com/problems/minimize-deviation-in-array/) | Heap + greedy |

---

## Tips
- **"Binary Search on Answer"** là pattern quan trọng nhất: đoán answer, check feasibility
- Luôn cẩn thận với **boundary conditions** (`left <= right` vs `left < right`)
- Dùng `mid = left + (right - left) // 2` thay `(left + right) // 2` để tránh overflow
