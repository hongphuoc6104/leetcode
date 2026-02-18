# 📖 Chapter 2: Sorting Patterns (Các dạng Sorting)

## Pattern 1: Merge Sort — Divide & Conquer (Chia và Trị)

### 🔍 Signal: "sort linked list", "count inversions", "external sort"

### 💡 Key Insight

Split array in half. Recursively sort each half. **Merge** two sorted halves. Guaranteed O(n log n).

**Chia mảng đôi. Sort đệ quy mỗi nửa. Gộp (merge) 2 nửa đã sort.**

```python
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= for stability!
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### 🪲 Common Bug

```python
# ❌ WRONG: Using < instead of <= in merge (breaks stability!)
if left[i] < right[j]:   # Unstable: equal elements from right come first

# ✅ RIGHT: Use <= to keep stability
if left[i] <= right[j]:   # Stable: equal elements from left come first
```

### Counting Inversions (Đếm nghịch thế — LC 493)
Merge Sort can count inversions during merge step! If `left[i] > right[j]`, all remaining left elements form inversions with `right[j]`.

📌 LC 148 (Sort List), LC 912, LC 493 (Reverse Pairs)

---

## Pattern 2: Quick Sort — Partitioning (Phân hoạch)

### 🔍 Signal: "kth largest (QuickSelect)", "sort colors", "partition"

### 💡 Key Insight

Pick a **pivot**. Partition array into elements `< pivot`, `== pivot`, `> pivot`.

**Chọn pivot. Phân hoạch mảng thành < pivot, == pivot, > pivot.**

```python
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    """Lomuto partition: pivot = last element."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
```

### Dutch National Flag (3-way partition) — LC 75
```python
def sort_colors(nums):
    """Sort array of 0s, 1s, 2s in one pass. O(n)."""
    l, r = 0, len(nums) - 1
    i = 0
    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1; i += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1          # Don't increment i! Check swapped value
        else:
            i += 1
```

### 🪲 Common Bug

```python
# ❌ WRONG: increment i after swapping with right
elif nums[i] == 2:
    nums[i], nums[r] = nums[r], nums[i]
    r -= 1
    i += 1   # BUG! The swapped value hasn't been checked

# ✅ RIGHT: DON'T increment i when swapping with right
elif nums[i] == 2:
    nums[i], nums[r] = nums[r], nums[i]
    r -= 1   # Don't touch i — need to check new nums[i]
```

📌 LC 75 (Sort Colors), LC 215 (Kth Largest — QuickSelect), LC 912

---

## Pattern 3: Counting Sort — Small Range (Khoảng giá trị nhỏ)

### 🔍 Signal: "values in range [0, 100]", "sort digits", "h-index"

### 💡 Key Insight

If values are bounded (e.g., grades 0-100), **count frequencies** and rebuild the array. O(n+k) where k = range.

**Nếu giá trị bị giới hạn, đếm tần suất và tạo lại mảng. O(n+k).**

```python
def counting_sort(nums):
    if not nums: return
    _min, _max = min(nums), max(nums)
    count = [0] * (_max - _min + 1)
    for x in nums:
        count[x - _min] += 1
    
    idx = 0
    for val, freq in enumerate(count):
        for _ in range(freq):
            nums[idx] = val + _min
            idx += 1
```

> 🤔 **Think:** Why doesn't Counting Sort violate the O(n log n) lower bound? (Tại sao Counting Sort không vi phạm giới hạn dưới O(n log n)?) Answer: It's a **non-comparison** sort — it doesn't compare elements, it uses their values directly as indices.

📌 LC 1122 (Relative Sort Array), LC 274 (H-Index), LC 912

---

## Pattern 4: Bucket Sort — Uniform Distribution (Phân bổ đều)

### 🔍 Signal: "maximum gap", "top k frequent" (bucket by freq)

### 💡 Key Insight

Distribute elements into `n` buckets. Sort each bucket (often constant size). Combine.

```python
from collections import Counter
def top_k_frequent(nums, k):
    """LC 347: Top K Frequent Elements. O(n) via bucket sort!"""
    count = Counter(nums)
    # Bucket by frequency: buckets[freq] = [nums with this freq]
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    
    # Flatten from highest frequency
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result
```

📌 LC 164 (Maximum Gap), LC 347 (Top K Frequent)

---

## Pattern 5: Custom Sort — Lambda / Comparator (Sắp xếp tùy chỉnh)

### 🔍 Signal: "sort logs", "largest number", "custom order"

### 💡 Key Insight

Use `key=lambda` for simple keys. Use `functools.cmp_to_key` for complex comparisons.

```python
# Largest Number (LC 179)
from functools import cmp_to_key

def largest_number(nums):
    """Arrange numbers to form largest number."""
    strs = list(map(str, nums))
    strs.sort(key=cmp_to_key(lambda x, y: 
        -1 if x+y > y+x else (1 if x+y < y+x else 0)))
    return ''.join(strs).lstrip('0') or '0'
```

### Multi-key sorting (Sort nhiều tiêu chí)
```python
# Sort by length, then alphabetically
words = ["apple", "bat", "code", "a"]
words.sort(key=lambda w: (len(w), w))
# Result: ['a', 'bat', 'code', 'apple']
```

📌 LC 179 (Largest Number), LC 937 (Reorder Logs), LC 1383

---

## 📊 Decision Table (Bảng quyết định)

| Signal (Dấu hiệu) | Pattern | Time |
|---------------------|---------|------|
| General sorting | Python `sort()` (Timsort) | O(n log n) |
| Sort linked list | Merge Sort | O(n log n) |
| Count inversions | Merge Sort | O(n log n) |
| Kth largest element | QuickSelect | O(n) avg |
| Sort 0s, 1s, 2s | Dutch National Flag | O(n) |
| Values in [0, k] | Counting Sort | O(n+k) |
| Maximum gap | Bucket Sort | O(n) |
| Custom order (concatenation) | cmp_to_key | O(n log n) |

---

## ❓ Self-Check Questions

1. **Merge Sort vs Quick Sort:** When would you prefer Merge Sort over Quick Sort? (Khi nào dùng Merge Sort thay vì Quick Sort?)
2. **LC 75:** Can you solve Sort Colors without counting? (Không đếm mà phân loại 0/1/2 được không?)
3. **Why is QuickSelect O(n) on average but O(n²) worst case?** (Tại sao QuickSelect trung bình O(n) nhưng xấu nhất O(n²)?)

---

**← Previous:** [Chapter 1](./01_introduction.md) | **Next →** [Chapter 3: Complexity](./03_complexity.md)
