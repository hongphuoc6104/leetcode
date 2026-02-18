# 📖 Chapter 4: Python Templates (Templates Python sẵn dùng)

## ✅ Pre-Coding Checklist

```
□ 1. Is data SORTED or has MONOTONIC property?
     (Dữ liệu ĐÃ SORTED hoặc có tính ĐƠN ĐIỆU?)

□ 2. Which template? Exact / Bound / Answer / Peak?
     (Template nào?)

□ 3. What is my SEARCH SPACE? [left, right] bounds?
     (Không gian tìm kiếm là gì?)

□ 4. left <= right or left < right?
     (Dùng <= hay <?)
```

---

## Template 1: Exact Match

```python
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
```

---

## Template 2: Lower Bound (First ≥ target)

```python
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

---

## Template 3: Upper Bound (First > target)

```python
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left
```

---

## Template 4: Rotated Sorted Array

```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:       # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:                              # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

---

## Template 5: Search on Answer (Minimize)

```python
def search_answer_min(lo, hi, is_feasible):
    """Find smallest value where is_feasible returns True."""
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if is_feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

---

## Template 6: Search on Answer (Maximize)

```python
def search_answer_max(lo, hi, is_feasible):
    """Find largest value where is_feasible returns True."""
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2    # Round UP to avoid infinite loop!
        if is_feasible(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo
```

---

## Template 7: Peak / Valley Finding

```python
def find_peak(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```

---

## Template 8: Python's bisect Module

```python
import bisect

# bisect_left  = lower_bound (first index >= target)
# bisect_right = upper_bound (first index > target)

arr = [1, 3, 5, 7, 7, 9]
bisect.bisect_left(arr, 7)    # → 3 (first 7)
bisect.bisect_right(arr, 7)   # → 5 (after last 7)
bisect.insort(arr, 6)         # Insert 6 in sorted position
```

---

## ❓ Self-Check Questions

1. **Why does Template 6 use `(hi - lo + 1) // 2` for rounding up?** What happens without it?
2. **Template 2 vs Template 3**: what's the ONLY difference in the code?
3. **When would you use Python's `bisect` instead of manual BS?**

---

**← Previous:** [Chapter 3: Complexity](./03_complexity.md)
**Next →** [Run the Examples!](../examples/) 🚀
