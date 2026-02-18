# 📖 Chapter 2: Array & String Patterns (Các Pattern Mảng & Chuỗi)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Recognize 6 core patterns that appear in 90%+ of Array/String problems (Nhận diện 6 pattern xuất hiện trong 90%+ bài)
- Know the "signal" to identify each pattern (Biết tín hiệu nhận biết từng pattern)
- Write skeleton code for each pattern (Viết code khung cho từng pattern)

---

## Pattern 1: Traversal & Accumulation (Duyệt & Tích lũy) — O(n)

### What it does (Cách hoạt động)

Scan through the array **once**, maintaining a running value (sum, max, min, count) (Duyệt mảng **một lần**, duy trì giá trị chạy: tổng, max, min, đếm).

### 🔍 Signal (Tín hiệu nhận biết)

- "Find the maximum / minimum / sum / count of..." (Tìm max / min / tổng / đếm...)
- "Track something as you iterate" (Theo dõi gì đó khi duyệt)
- Single pass through data (Một lần duyệt)

### 💻 Code

```python
def find_max(arr):
    """Find maximum element in one pass. (Tìm max trong 1 lần duyệt.)"""
    max_val = arr[0]           # Initialize with first element (Khởi tạo bằng phần tử đầu)
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]   # Update running max (Cập nhật max chạy)
    return max_val

def count_if(arr, condition):
    """Count elements satisfying a condition. (Đếm phần tử thỏa điều kiện.)"""
    count = 0
    for val in arr:
        if condition(val):
            count += 1
    return count
```

### 📌 LeetCode Examples

- **Best Time to Buy/Sell Stock** (LC 121): Track `min_price` while scanning, update `max_profit`
- **Single Number** (LC 136): XOR accumulation — `result ^= num`

---

## Pattern 2: Prefix Sum (Tổng tiền tố) — O(n) build, O(1) query

### What it does (Cách hoạt động)

Pre-compute cumulative sums so you can answer "sum from index i to j" in O(1) (Tính trước tổng tích lũy để trả lời "tổng từ i đến j" trong O(1)).

```
Array:       [2, 4, 1, 3, 5]
Prefix Sum:  [0, 2, 6, 7, 10, 15]
                  ↑  ↑          ↑
            prefix[0]=0   prefix[5]=sum of all

Sum from index 1 to 3 = prefix[4] - prefix[1] = 10 - 2 = 8
Check: arr[1]+arr[2]+arr[3] = 4+1+3 = 8 ✅
```

### 🔍 Signal (Tín hiệu nhận biết)

- "Sum of subarray" or "sum between indices" (Tổng subarray hoặc tổng giữa 2 index)
- "How many queries about subarray sums?" (Bao nhiêu truy vấn về tổng subarray?)
- "Difference between prefix sums" (Hiệu tổng tiền tố)

### 💻 Code

```python
def build_prefix_sum(arr):
    """Build prefix sum array. (Xây mảng tổng tiền tố.)"""
    n = len(arr)
    prefix = [0] * (n + 1)            # prefix[0] = 0 (base case)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

def range_sum(prefix, i, j):
    """Sum of arr[i..j] in O(1). (Tổng arr[i..j] trong O(1).)"""
    return prefix[j + 1] - prefix[i]  # Inclusive both ends
```

### ⚡ Why is this powerful? (Tại sao mạnh?)

Without prefix sum, answering Q queries about subarray sums costs **O(Q × n)** (Không có prefix sum, Q truy vấn tốn O(Q × n)).
With prefix sum: **O(n)** to build + **O(1)** per query = **O(n + Q)** total! (Có prefix sum: O(n) xây + O(1) mỗi truy vấn!)

### 📌 LeetCode Examples

- **Subarray Sum Equals K** (LC 560): Prefix sum + Hash Map
- **Product Except Self** (LC 238): Prefix AND suffix products

---

## Pattern 3: In-Place Modification (Thay đổi tại chỗ) — O(n) time, O(1) space

### What it does (Cách hoạt động)

Modify the array **without using extra space** — usually by swapping or overwriting elements (Sửa mảng **không dùng bộ nhớ thêm** — thường bằng hoán đổi hoặc ghi đè).

### 🔍 Signal (Tín hiệu nhận biết)

- "Modify **in-place**" or "Do not allocate extra space" (Sửa **tại chỗ**, không dùng bộ nhớ thêm)
- "Return the new length" (Trả về độ dài mới)
- "Rearrange elements" (Sắp xếp lại phần tử)

### 💻 Code — Remove Duplicates Pattern

```python
def remove_duplicates(nums):
    """
    Remove duplicates from sorted array IN-PLACE.
    (Xóa trùng lặp từ mảng đã sort TẠI CHỖ.)
    
    Key idea: 'write pointer' tracks where to write next unique element.
    (Ý chính: 'con trỏ ghi' đánh dấu vị trí ghi phần tử unique tiếp.)
    
    Example:
    [1, 1, 2, 2, 3] → write=1
     r     ↑ new unique → write to position 1, write=2
           r     ↑ new unique → write to position 2
    Result: [1, 2, 3, _, _], return 3
    """
    if not nums:
        return 0
    write = 1                          # Position to write next unique
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:  # New unique element found
            nums[write] = nums[read]
            write += 1
    return write
```

### 💻 Code — Swap Pattern

```python
def reverse_array(arr):
    """Reverse array in-place using two pointers. (Đảo mảng tại chỗ bằng 2 con trỏ.)"""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap
        left += 1
        right -= 1
```

### 📌 LeetCode Examples

- **Remove Duplicates** (LC 26): Write pointer
- **Move Zeroes** (LC 283): Swap non-zero to front
- **Remove Element** (LC 27): Write pointer, skip target

---

## Pattern 4: Frequency Counting (Đếm tần suất) — O(n)

### What it does (Cách hoạt động)

Count how many times each element appears using a Hash Map or array (Đếm mỗi phần tử xuất hiện bao nhiêu lần bằng Hash Map hoặc mảng).

### 🔍 Signal (Tín hiệu nhận biết)

- "Anagram", "frequency", "count occurrences" (Đảo chữ, tần suất, đếm số lần)
- "Most frequent", "majority", "duplicate" (Thường xuyên nhất, đa số, trùng lặp)
- "Group by property" (Nhóm theo thuộc tính)

### 💻 Code

```python
from collections import Counter

def is_anagram(s, t):
    """Check if t is an anagram of s. (Kiểm tra t có phải đảo chữ của s?)"""
    return Counter(s) == Counter(t)

def top_k_frequent(nums, k):
    """Find k most frequent elements. (Tìm k phần tử xuất hiện nhiều nhất.)"""
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]

# Manual counting with dict (Đếm thủ công bằng dict)
def count_frequency(arr):
    freq = {}
    for val in arr:
        freq[val] = freq.get(val, 0) + 1
    return freq
```

### 📌 LeetCode Examples

- **Valid Anagram** (LC 242): Compare character counts
- **Contains Duplicate** (LC 217): Any frequency > 1?
- **Majority Element** (LC 169): Element with freq > n/2
- **Group Anagrams** (LC 49): Group by sorted key or count key

---

## Pattern 5: Matrix / 2D Array (Ma trận / Mảng 2 chiều)

### What it does (Cách hoạt động)

Process 2D grids using row/column iteration, boundaries, or transformation (Xử lý lưới 2D bằng duyệt hàng/cột, biên, hoặc biến đổi).

### 🔍 Signal (Tín hiệu nhận biết)

- "Matrix", "grid", "2D array" (Ma trận, lưới)
- "Spiral", "rotate", "transpose" (Xoắn ốc, xoay, chuyển vị)
- "Row/column operations" (Thao tác hàng/cột)

### 💻 Code — Spiral Traversal

```python
def spiral_order(matrix):
    """
    Traverse matrix in spiral order.
    (Duyệt ma trận theo hình xoắn ốc.)
    
    Use 4 boundaries: top, bottom, left, right.
    (Dùng 4 biên: trên, dưới, trái, phải.)
    """
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Go right → (Đi phải)
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Go down ↓ (Đi xuống)
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Go left ← (Đi trái)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Go up ↑ (Đi lên)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result
```

### 📌 LeetCode Examples

- **Spiral Matrix** (LC 54): 4-boundary traversal
- **Rotate Image** (LC 48): Transpose + reverse each row
- **Set Matrix Zeroes** (LC 73): Use first row/col as markers
- **Valid Sudoku** (LC 36): Hash set per row/col/box

---

## Pattern 6: Interval / Merge Operations (Thao tác khoảng / Gộp)

### What it does (Cách hoạt động)

Sort intervals by start time, then process overlapping intervals (Sắp xếp khoảng theo thời gian bắt đầu, xử lý khoảng chồng nhau).

### 🔍 Signal (Tín hiệu nhận biết)

- "Intervals", "meetings", "ranges" (Khoảng, cuộc họp, phạm vi)
- "Overlap", "merge", "insert" (Chồng nhau, gộp, chèn)

### 💻 Code

```python
def merge_intervals(intervals):
    """
    Merge overlapping intervals.
    (Gộp các khoảng chồng nhau.)
    
    Key: Sort by start, then check if current overlaps with previous.
    (Sắp xếp theo start, kiểm tra overlap với khoảng trước.)
    """
    intervals.sort(key=lambda x: x[0])  # Sort by start (Sắp theo start)
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:        # Overlap! (Chồng nhau!)
            last[1] = max(last[1], current[1])  # Extend end (Mở rộng end)
        else:
            merged.append(current)       # No overlap (Không chồng)
    
    return merged
```

### 📌 LeetCode Examples

- **Merge Intervals** (LC 56): Sort + merge
- **Insert Interval** (LC 57): Find overlap position

---

## 📊 Quick Reference Table (Bảng tra cứu nhanh)

| Pattern | Time | Signal Keywords | Common Tools |
|---------|------|----------------|-------------|
| Traversal & Accumulation | O(n) | "max", "min", "sum", "count" | Single pass, running variable |
| Prefix Sum | O(n) build + O(1) query | "subarray sum", "range query" | prefix[] array |
| In-Place Modification | O(n) time, O(1) space | "in-place", "no extra space" | Write pointer, swap |
| Frequency Counting | O(n) | "anagram", "frequency", "duplicate" | Counter, dict, set |
| Matrix / 2D | O(m×n) | "matrix", "grid", "spiral" | Boundary tracking, transpose |
| Intervals | O(n log n) | "intervals", "overlap", "merge" | Sort + merge |

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **"Find if any two elements in an array sum to target"** — which pattern fits FIRST (before optimizing)? (Pattern nào phù hợp ĐẦU TIÊN?)

2. **Explain why Prefix Sum turns O(n) per query into O(1) per query** (Giải thích tại sao Prefix Sum biến O(n) mỗi truy vấn thành O(1)).

3. **"Remove all occurrences of value val from array in-place"** — draw the write pointer process for `arr=[3,2,2,3], val=3` (Vẽ quá trình con trỏ ghi).

4. **What data structure would you use to check if two strings are anagrams?** Why? (Dùng cấu trúc dữ liệu nào để kiểm tra đảo chữ? Tại sao?)

5. **Match each problem to a pattern** (Ghép bài với pattern):

   | Problem | Pattern? |
   |---------|----------|
   | Find max profit from stock prices | ? |
   | Check if matrix row has all zeros | ? |
   | Count subarray sums equal to K | ? |
   | Group strings that are anagrams | ? |

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)
**Next →** [Chapter 3: Complexity](./03_complexity.md)
