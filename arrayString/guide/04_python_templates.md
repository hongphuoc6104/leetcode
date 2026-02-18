# 📖 Chapter 4: Python Templates (Templates Python sẵn dùng)

## 🎯 How to Use (Cách sử dụng)

1. **Identify the pattern** from Chapter 2 (Nhận diện pattern từ Chương 2)
2. **Copy the template** below (Copy template)
3. **Fill in `# TODO`** markers (Điền chỗ trống)
4. **Test** with example inputs (Kiểm tra)

---

## ✅ Pre-Coding Checklist (Kiểm tra trước khi code)

```
□ 1. What TYPE of problem is this?
     (Loại bài gì?)
     → Traversal? Prefix sum? In-place? Frequency? Matrix? Interval?

□ 2. What DATA STRUCTURE fits?
     (Cấu trúc dữ liệu nào phù hợp?)
     → Array? Hash Map? Set? Counter?

□ 3. What is the constraint on n?
     (Ràng buộc n là bao nhiêu?)
     → Determines max allowed complexity

□ 4. Is in-place modification required?
     (Cần sửa tại chỗ không?)
     → If yes → write pointer or swap pattern
```

---

## Template 1: Single-Pass Accumulation — O(n)

```python
def single_pass(arr):
    """Track a running value in one pass. (Theo dõi giá trị chạy trong 1 lần duyệt.)"""
    result = initial_value              # TODO: 0, float('inf'), float('-inf'), etc.
    
    for val in arr:
        result = update(result, val)    # TODO: max, min, sum, xor, etc.
    
    return result

# --- Specific: Track min while computing max profit --- #
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
```

---

## Template 2: Prefix Sum — O(n) build + O(1) query

```python
def prefix_sum_template(arr):
    """Build prefix sum and answer range queries. (Xây prefix sum, truy vấn khoảng.)"""
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    # Query: sum of arr[i..j] inclusive
    def range_sum(i, j):
        return prefix[j + 1] - prefix[i]
    
    return range_sum                     # TODO: Use range_sum in your logic
```

---

## Template 3: Write Pointer (In-Place) — O(n) time, O(1) space

```python
def write_pointer(arr):
    """
    Process array in-place using a write pointer.
    (Xử lý mảng tại chỗ bằng con trỏ ghi.)
    """
    write = 0                            # Position to write next valid element
    
    for read in range(len(arr)):
        if should_keep(arr[read]):       # TODO: Your condition
            arr[write] = arr[read]
            write += 1
    
    return write                         # New length of valid portion
```

---

## Template 4: Frequency Counting — O(n)

```python
from collections import Counter

def frequency_template(arr):
    """Count and use frequencies. (Đếm và sử dụng tần suất.)"""
    freq = Counter(arr)                  # {element: count}
    
    # Common operations (Thao tác thường dùng):
    # freq.most_common(k)              → top k elements
    # freq[x]                          → count of x
    # sum(freq.values())               → total count
    # max(freq, key=freq.get)          → most frequent element
    
    return process(freq)                 # TODO: Your logic
```

---

## Template 5: Two-Pointer In-Place Swap — O(n)

```python
def two_pointer_swap(arr):
    """
    Process array from both ends using two pointers.
    (Xử lý mảng từ 2 đầu bằng 2 con trỏ.)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        if condition(arr[left], arr[right]):  # TODO: Your condition
            arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr
```

---

## Template 6: Matrix Traversal — O(m × n)

```python
def matrix_template(matrix):
    """Traverse and process a 2D matrix. (Duyệt và xử lý ma trận 2D.)"""
    if not matrix:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    
    # Row-by-row traversal (Duyệt theo hàng)
    for r in range(rows):
        for c in range(cols):
            process(matrix[r][c])        # TODO: Your logic
    
    # Neighbors (4 directions) (4 hướng lân cận)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbor = matrix[nr][nc]
```

---

## Template 7: Interval Merge — O(n log n)

```python
def merge_intervals(intervals):
    """Merge overlapping intervals. (Gộp khoảng chồng nhau.)"""
    intervals.sort(key=lambda x: x[0])  # Sort by start
    merged = [intervals[0]]
    
    for curr in intervals[1:]:
        if curr[0] <= merged[-1][1]:     # Overlap? (Chồng nhau?)
            merged[-1][1] = max(merged[-1][1], curr[1])
        else:
            merged.append(curr)
    
    return merged
```

---

## 🔧 Utility: String Building — Always O(n)

```python
def build_string(n):
    """Safe string building pattern. (Mẫu xây chuỗi an toàn.)"""
    parts = []                           # Collect parts in list
    for i in range(n):
        parts.append(compute(i))         # O(1) each
    return ''.join(parts)                # O(n) once, NOT O(n²)
```

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **"Remove all zeroes from array in-place"** — which template? (Template nào?)

2. **When would you use Template 2 (Prefix Sum) vs Template 1 (Single Pass)?** Give an example of each (Cho ví dụ mỗi loại).

3. **In Template 3, why does `write` start at 0, not 1?** (Tại sao `write` bắt đầu từ 0?)

4. **What is the key difference between Template 5 (Swap) and Template 3 (Write Pointer)?** (Khác biệt chính là gì?)

---

**← Previous:** [Chapter 3: Complexity](./03_complexity.md)
**Next →** [Run the Examples!](../examples/) 🚀
