# 📖 Chapter 2: Binary Search Patterns (Các Pattern Tìm Kiếm Nhị Phân)

## Pattern 1: Exact Search — O(log n)

### 🔍 Signal
- "Find target in sorted array" (Tìm target trong mảng sorted)
- Return index or -1

### 💻 Code
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 📌 LeetCode: Binary Search (LC 704), Guess Number (LC 374)

---

## Pattern 2: Lower/Upper Bound — O(log n)

### 🔍 Signal
- "First position of target" / "Last position" (Vị trí đầu/cuối)
- "Insert position" (Vị trí chèn)
- "First element ≥ target"

### 💻 Code — Find First and Last

```python
def find_first(nums, target):
    """First index where nums[i] >= target."""
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def find_last(nums, target):
    """Last index where nums[i] <= target."""
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left - 1
```

### 📌 LeetCode: Search Insert (LC 35), Find First and Last (LC 34), First Bad Version (LC 278)

---

## Pattern 3: Rotated Sorted Array — O(log n)

### 🔍 Signal
- "Rotated sorted array" (Mảng sorted bị xoay)
- Array was sorted, then rotated at some pivot

### 💡 Key Insight
One half is ALWAYS sorted. Determine which half, then decide (Một nửa LUÔN được sắp xếp. Xác định nửa nào, rồi quyết định).

```
[4, 5, 6, 7, 0, 1, 2]    target = 0
         ↑ pivot
 [4,5,6,7] → sorted     [0,1,2] → sorted
```

### 💻 Code
```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        
        # Left half is sorted (Nửa trái sorted)
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1    # Target in left half
            else:
                left = mid + 1     # Target in right half
        # Right half is sorted (Nửa phải sorted)
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

### 📌 LeetCode: Search Rotated (LC 33), Find Min Rotated (LC 153)

---

## Pattern 4: Binary Search on Answer — O(n × log(range))

### 🔍 Signal
- "Minimum capacity/speed to finish in time" (Công suất/tốc độ tối thiểu)
- "Maximum minimum distance" (Khoảng cách tối thiểu lớn nhất)
- Answer is a NUMBER in a range → binary search on it!

### 💡 Key Insight
```
Instead of searching IN the array,
search for the ANSWER in [min_possible, max_possible].

For each candidate answer, check: "Is this feasible?"
If yes → try smaller (minimize) or larger (maximize)
If no → try the other direction
```

### 💻 Code — Koko Eating Bananas
```python
import math

def min_eating_speed(piles, h):
    """
    Find minimum speed k to eat all bananas in h hours.
    BS range: [1, max(piles)]
    Feasible: can finish in <= h hours at speed mid?
    """
    def can_finish(speed):
        hours = sum(math.ceil(p / speed) for p in piles)
        return hours <= h
    
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if can_finish(mid):
            hi = mid             # Can finish → try slower
        else:
            lo = mid + 1         # Can't finish → need faster
    return lo
```

### 📌 LeetCode: Koko Bananas (LC 875), Ship Packages (LC 1011), Split Array (LC 410)

---

## Pattern 5: Peak / Valley Finding — O(log n)

### 🔍 Signal
- "Find peak element" (Tìm đỉnh)
- "Find local maximum/minimum"
- Array is NOT sorted, but has a peak property

### 💡 Key Insight
Compare `mid` with `mid+1`. If going up → peak is on right. If going down → peak is on left (So sánh `mid` với `mid+1`. Đi lên → đỉnh bên phải. Đi xuống → đỉnh bên trái).

### 💻 Code
```python
def find_peak(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1    # Going up → peak on right
        else:
            right = mid       # Going down → peak on left/here
    return left
```

### 📌 LeetCode: Find Peak (LC 162), Single Element Sorted (LC 540)

---

## 📊 Quick Reference Table

| Pattern | Template | Signal | Search Space |
|---------|----------|--------|-------------|
| Exact Search | `<=` | "find target" | Array indices |
| Lower/Upper Bound | `<` | "first/last position" | Array indices |
| Rotated Array | `<=` | "rotated sorted" | Array indices |
| Search on Answer | `<` | "min/max to achieve" | Answer range |
| Peak Finding | `<` | "find peak" | Array indices |

---

## ❓ Self-Check Questions

1. **"Find minimum in rotated sorted array"** — is this Pattern 3 or Pattern 5? (Pattern nào?)

2. **In Search on Answer, how do you determine lo and hi?** Give example for "minimum speed" (Xác định lo, hi thế nào?)

3. **Why does Peak Finding work on unsorted arrays?** What's the monotonic property? (Tại sao hoạt động trên mảng chưa sorted?)

4. **Trace Pattern 2 (lower_bound) for `arr=[1,3,5,7,7,9]`, target=7`** — show left, right, mid each step.

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)
**Next →** [Chapter 3: Complexity](./03_complexity.md)
