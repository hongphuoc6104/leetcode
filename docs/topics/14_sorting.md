# 📖 Chủ đề 14: Sorting

## Lý thuyết cơ bản

### Các thuật toán sắp xếp

| Thuật toán | Time (avg) | Time (worst) | Space | Stable |
|------------|-----------|--------------|-------|--------|
| Bubble Sort | O(n²) | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(1) | ❌ |
| Insertion Sort | O(n²) | O(n²) | O(1) | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick Sort | O(n log n) | O(n²) | O(log n) | ❌ |
| Heap Sort | O(n log n) | O(n log n) | O(1) | ❌ |
| Counting Sort | O(n+k) | O(n+k) | O(k) | ✅ |
| Radix Sort | O(d×n) | O(d×n) | O(n) | ✅ |

### Implementations quan trọng
```python
# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort (Lomuto partition)
def quick_sort(arr, lo, hi):
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot - 1)
        quick_sort(arr, pivot + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i

# Python built-in (Timsort - hybrid merge+insertion)
arr.sort()              # In-place, O(n log n)
sorted_arr = sorted(arr) # Returns new list
arr.sort(key=lambda x: x[1])  # Custom key
```

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Merge Sorted Array | [LC 88](https://leetcode.com/problems/merge-sorted-array/) | Merge from end |
| 2 | Majority Element | [LC 169](https://leetcode.com/problems/majority-element/) | Sort or Boyer-Moore |
| 3 | Contains Duplicate | [LC 217](https://leetcode.com/problems/contains-duplicate/) | Sort and check adjacent |
| 4 | Valid Anagram | [LC 242](https://leetcode.com/problems/valid-anagram/) | Sort compare |
| 5 | Intersection Arrays | [LC 349](https://leetcode.com/problems/intersection-of-two-arrays/) | Sort + two pointers |
| 6 | Intersection II | [LC 350](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | Sort + two pointers |
| 7 | Third Maximum | [LC 414](https://leetcode.com/problems/third-maximum-number/) | Track top 3 |
| 8 | Array Partition | [LC 561](https://leetcode.com/problems/array-partition/) | Sort, sum of odds |
| 9 | Largest Perimeter | [LC 976](https://leetcode.com/problems/largest-perimeter-triangle/) | Sort desc, first valid |
| 10 | Relative Sort | [LC 1122](https://leetcode.com/problems/relative-sort-array/) | Custom sort key |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Merge Intervals | [LC 56](https://leetcode.com/problems/merge-intervals/) | Sort by start, merge |
| 2 | Sort Colors | [LC 75](https://leetcode.com/problems/sort-colors/) | Dutch National Flag |
| 3 | Sort List | [LC 148](https://leetcode.com/problems/sort-list/) | Merge sort on LL |
| 4 | Largest Number | [LC 179](https://leetcode.com/problems/largest-number/) | Custom comparator |
| 5 | Kth Largest | [LC 215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Quick select |
| 6 | H-Index | [LC 274](https://leetcode.com/problems/h-index/) | Sort desc, find h |
| 7 | Wiggle Sort II | [LC 324](https://leetcode.com/problems/wiggle-sort-ii/) | Find median, 3-way |
| 8 | Top K Frequent | [LC 347](https://leetcode.com/problems/top-k-frequent-elements/) | Bucket sort |
| 9 | Non-overlapping | [LC 435](https://leetcode.com/problems/non-overlapping-intervals/) | Sort by end |
| 10 | Sort an Array | [LC 912](https://leetcode.com/problems/sort-an-array/) | Implement merge/quick |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Median Two Arrays | [LC 4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Binary search |
| 2 | Merge k Sorted | [LC 23](https://leetcode.com/problems/merge-k-sorted-lists/) | Heap merge |
| 3 | Maximum Gap | [LC 164](https://leetcode.com/problems/maximum-gap/) | Radix/bucket sort |
| 4 | Find Median Stream | [LC 295](https://leetcode.com/problems/find-median-from-data-stream/) | Two heaps |
| 5 | Count Smaller After | [LC 315](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Merge sort + count |
| 6 | Count Range Sum | [LC 327](https://leetcode.com/problems/count-of-range-sum/) | Merge sort |
| 7 | Reverse Pairs | [LC 493](https://leetcode.com/problems/reverse-pairs/) | Merge sort + count |
| 8 | Smallest Range K Lists | [LC 632](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Sort + sliding |
| 9 | Max Profit Job Sched | [LC 1235](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) | Sort + DP + BS |
| 10 | Closest Room | [LC 1847](https://leetcode.com/problems/closest-room/) | Offline sort + SortedList |

---

## Tips
- Python `sort()` dùng **Timsort** (hybrid, O(n log n), **stable**)
- **Merge Sort** biến thể: dùng để đếm inversions, count smaller
- **Quick Select**: tìm kth element trong O(n) average
- Bài interval → **sort by start or end** là bước đầu tiên
