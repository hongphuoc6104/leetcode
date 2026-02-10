# 📖 Chủ đề 1: Array & String

## Lý thuyết cơ bản

**Array (Mảng)** là cấu trúc dữ liệu lưu trữ các phần tử liên tiếp trong bộ nhớ. **String** là mảng ký tự.

### Đặc điểm
- Truy cập phần tử: **O(1)** qua index
- Thêm/xóa ở cuối: **O(1)** (amortized)
- Thêm/xóa ở giữa: **O(n)** (phải dịch phần tử)
- Tìm kiếm: **O(n)** (linear), **O(log n)** (nếu sorted)

### Khai báo trong Python
```python
# Array
arr = [1, 2, 3, 4, 5]
arr.append(6)        # O(1)
arr.pop()            # O(1)
arr.insert(0, 0)     # O(n)

# String (immutable trong Python)
s = "hello"
s_list = list(s)     # Chuyển sang list để thao tác
```

---

## Các pattern thường gặp

### 1. Duyệt mảng cơ bản
```python
for i in range(len(arr)):       # Duyệt bằng index
    print(arr[i])

for val in arr:                  # Duyệt bằng giá trị
    print(val)

for i, val in enumerate(arr):    # Duyệt cả index và giá trị
    print(i, val)
```

### 2. In-place modification
```python
# Đổi chỗ 2 phần tử
arr[i], arr[j] = arr[j], arr[i]

# Đảo ngược mảng
arr.reverse()  # hoặc arr[::-1]
```

### 3. Prefix Sum
```python
# Tính tổng từ index i đến j trong O(1)
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]
# Tổng arr[i..j] = prefix[j+1] - prefix[i]
```

---

## Complexity Analysis

| Thao tác | Time | Space |
|----------|------|-------|
| Truy cập | O(1) | - |
| Tìm kiếm | O(n) | - |
| Thêm cuối | O(1) amortized | - |
| Thêm đầu/giữa | O(n) | - |
| Xóa | O(n) | - |
| Sắp xếp | O(n log n) | O(n) |

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Two Sum | [LeetCode](https://leetcode.com/problems/two-sum/) | Hash map để tìm complement |
| 2 | Remove Duplicates from Sorted Array | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Two pointers, in-place |
| 3 | Remove Element | [LeetCode](https://leetcode.com/problems/remove-element/) | Two pointers |
| 4 | Plus One | [LeetCode](https://leetcode.com/problems/plus-one/) | Xử lý carry từ cuối |
| 5 | Merge Sorted Array | [LeetCode](https://leetcode.com/problems/merge-sorted-array/) | Merge từ cuối |
| 6 | Best Time to Buy and Sell Stock | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Track min price |
| 7 | Majority Element | [LeetCode](https://leetcode.com/problems/majority-element/) | Boyer-Moore Voting |
| 8 | Contains Duplicate | [LeetCode](https://leetcode.com/problems/contains-duplicate/) | Set hoặc sort |
| 9 | Move Zeroes | [LeetCode](https://leetcode.com/problems/move-zeroes/) | Two pointers, in-place |
| 10 | Find Disappeared Numbers | [LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | Đánh dấu bằng giá trị âm |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | 3Sum | [LeetCode](https://leetcode.com/problems/3sum/) | Sort + Two pointers |
| 2 | Valid Sudoku | [LeetCode](https://leetcode.com/problems/valid-sudoku/) | Hash set cho row/col/box |
| 3 | Group Anagrams | [LeetCode](https://leetcode.com/problems/group-anagrams/) | Sort key hoặc count key |
| 4 | Spiral Matrix | [LeetCode](https://leetcode.com/problems/spiral-matrix/) | Simulation, 4 boundaries |
| 5 | Merge Intervals | [LeetCode](https://leetcode.com/problems/merge-intervals/) | Sort rồi merge |
| 6 | Set Matrix Zeroes | [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/) | Dùng row/col đầu làm marker |
| 7 | Longest Consecutive Sequence | [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/) | Hash set, tìm start |
| 8 | Product of Array Except Self | [LeetCode](https://leetcode.com/problems/product-of-array-except-self/) | Prefix & suffix product |
| 9 | Top K Frequent Elements | [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) | Bucket sort hoặc heap |
| 10 | Subarray Sum Equals K | [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/) | Prefix sum + hash map |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Median of Two Sorted Arrays | [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Binary search trên partition |
| 2 | First Missing Positive | [LeetCode](https://leetcode.com/problems/first-missing-positive/) | Cyclic sort |
| 3 | Trapping Rain Water | [LeetCode](https://leetcode.com/problems/trapping-rain-water/) | Two pointers hoặc stack |
| 4 | Text Justification | [LeetCode](https://leetcode.com/problems/text-justification/) | Greedy, phân phối space |
| 5 | Minimum Window Substring | [LeetCode](https://leetcode.com/problems/minimum-window-substring/) | Sliding window + hash |
| 6 | Largest Rectangle in Histogram | [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Monotonic stack |
| 7 | Sliding Window Maximum | [LeetCode](https://leetcode.com/problems/sliding-window-maximum/) | Deque (monotonic) |
| 8 | Find Median from Data Stream | [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/) | Two heaps |
| 9 | Sliding Window Median | [LeetCode](https://leetcode.com/problems/sliding-window-median/) | Two heaps + lazy deletion |
| 10 | Count Unique Characters | [LeetCode](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/) | Đếm contribution |

---

## Tips

- **Easy**: Tập trung vào hiểu đề và viết code sạch. Hầu hết dùng 1-2 vòng lặp.
- **Medium**: Cần kết hợp nhiều kỹ thuật (sort + two pointers, prefix sum + hash map).
- **Hard**: Thường cần optimize từ O(n²) xuống O(n) bằng CTDL phụ trợ (stack, heap, hash).
