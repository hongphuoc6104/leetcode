# 📖 Chapter 4: Python Templates (Templates Python)

## Template 1: Merge Sort (Stable, O(n log n))

```python
def merge_sort(arr):
    """Stable, O(n log n). Good for Linked Lists.
    (Ổn định, O(n log n). Tốt cho Linked List.)"""
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge two sorted halves (Gộp 2 nửa đã sort)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= for stability
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
```

## Template 2: Quick Sort (Lomuto Partition)

```python
def quick_sort(arr, low, high):
    """In-place, avg O(n log n), worst O(n²).
    (Tại chỗ, trung bình O(n log n), xấu nhất O(n²))"""
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
```

## Template 3: QuickSelect (Kth Element)

```python
def quick_select(nums, k):
    """Find Kth smallest. Avg O(n). (Tìm phần tử nhỏ thứ k. Trung bình O(n).)"""
    import random
    def select(l, r, k_idx):
        if l == r: return nums[l]
        # Random pivot to avoid O(n²) worst case
        pivot_idx = random.randint(l, r)
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        
        pi = partition(nums, l, r)
        if pi == k_idx:
            return nums[pi]
        elif pi < k_idx:
            return select(pi + 1, r, k_idx)
        else:
            return select(l, pi - 1, k_idx)
    
    return select(0, len(nums) - 1, k - 1)
```

## Template 4: Counting Sort (O(n+k))

```python
def counting_sort(nums):
    """O(n+k) for bounded integers. (O(n+k) cho số nguyên có giới hạn.)"""
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

## Template 5: Dutch National Flag (3-way Partition)

```python
def sort_colors(nums):
    """Sort 0s, 1s, 2s in one pass. O(n). (Sắp xếp 0/1/2 trong 1 lần duyệt.)"""
    l, r = 0, len(nums) - 1
    i = 0
    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1; i += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1        # ← DON'T increment i!
        else:
            i += 1
```

## Template 6: Custom Comparator (cmp_to_key)

```python
from functools import cmp_to_key

def largest_number(nums):
    """LC 179: Arrange nums to form largest number.
    (Sắp xếp số để tạo số lớn nhất.)"""
    strs = list(map(str, nums))
    strs.sort(key=cmp_to_key(lambda x, y:
        -1 if x+y > y+x else (1 if x+y < y+x else 0)))
    return ''.join(strs).lstrip('0') or '0'
```

## Template 7: Insertion Sort (Nearly Sorted)

```python
def insertion_sort(arr):
    """O(n) for nearly sorted arrays. (O(n) cho mảng gần đã sắp xếp.)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

---

## 📋 Pre-Coding Checklist (Checklist trước khi code)

1. ✅ **Use built-in sort** unless specifically asked to implement one (Dùng sort() trừ khi bài yêu cầu)
2. ✅ **Stability needed?** Use `.sort()` (Timsort) or Merge Sort (Cần ổn định?)
3. ✅ **Values bounded?** Consider Counting Sort (Giá trị có giới hạn? → Counting Sort)
4. ✅ **Need kth element only?** Use QuickSelect, not full sort (Chỉ cần k? → QuickSelect)
5. ✅ **Custom order?** `key=lambda` or `cmp_to_key` (Thứ tự tùy chỉnh?)
6. ✅ **3-way partition?** Dutch National Flag for 3 values (Phân 3 loại? → Dutch Flag)

---

**← Previous:** [Chapter 3](./03_complexity.md) | **Next →** [Examples](../examples/) 🚀
