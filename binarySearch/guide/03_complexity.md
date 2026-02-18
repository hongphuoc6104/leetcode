# 📖 Chapter 3: Complexity Analysis (Phân tích độ phức tạp)

## 1. Why is Binary Search O(log n)? (Tại sao O(log n)?)

### The Proof

```
After step 1: n/2 elements remain
After step 2: n/4 elements remain
After step 3: n/8 elements remain
...
After step k: n/2^k elements remain

Stop when 1 element remains:
  n/2^k = 1 → k = log₂(n)

Therefore: O(log n) ✅
```

### Concrete Numbers

| n | Linear O(n) | Binary O(log n) | Speedup |
|---|-------------|----------------|---------|
| 100 | 100 | 7 | 14x |
| 10,000 | 10,000 | 14 | 714x |
| 1,000,000 | 1,000,000 | 20 | 50,000x |
| 10⁹ | 10⁹ | 30 | 33,333,333x |

---

## 2. Complexity Table

| Pattern | Time | Space | Notes |
|---------|------|-------|-------|
| Exact Search | O(log n) | O(1) | |
| Lower/Upper Bound | O(log n) | O(1) | |
| Rotated Array | O(log n) | O(1) | |
| Search on Answer | O(n × log R) | O(1) | R = answer range |
| Peak Finding | O(log n) | O(1) | |
| 2D Matrix Search | O(log(m×n)) | O(1) | Treat as 1D |

### Why "Search on Answer" is O(n × log R)

```
R = range of possible answers (e.g., max(piles) for Koko)
log R = number of binary search steps
Each step: check feasibility → usually O(n)
Total: O(n × log R)
```

---

## 3. Common Bugs (Lỗi thường gặp)

### Bug 1: Infinite Loop ⚠️

```python
# ❌ WRONG — infinite loop when left + 1 == right
while left < right:
    mid = (left + right) // 2
    if condition:
        left = mid        # left never advances if mid == left!

# ✅ FIX — use mid + 1 for left
while left < right:
    mid = (left + right) // 2
    if condition:
        left = mid + 1    # Always advances!
```

### Bug 2: Wrong Boundary Init ⚠️

```python
# ❌ WRONG — misses last element
left, right = 0, len(arr) - 1   # For lower_bound, should be len(arr)!

# ✅ CORRECT
left, right = 0, len(arr)       # right = len(arr) for half-open interval
```

### Bug 3: Off-by-One in Answer ⚠️

```python
# ❌ WRONG — lo might be too small
lo, hi = 0, max(piles)    # lo should be 1 (speed can't be 0!)

# ✅ CORRECT
lo, hi = 1, max(piles)
```

---

## 4. Constraint Guide

| n constraint | Linear O(n) | Binary O(log n) | BS on Answer |
|-------------|-------------|----------------|-------------|
| n ≤ 10⁵ | ✅ ~0.1s | ✅ instant | ✅ |
| n ≤ 10⁶ | ⚠️ ~1s | ✅ instant | ✅ |
| n ≤ 10⁹ | ❌ TLE | ✅ ~30 steps | ✅ |
| n ≤ 10¹⁸ | ❌ | ✅ ~60 steps | ✅ |

---

## ❓ Self-Check Questions

1. **How many comparisons to search in 10 billion elements?** (Bao nhiêu phép so sánh cho 10 tỷ phần tử?)

2. **"Koko eats bananas" has piles up to 10⁹. What's the total complexity?** Break down: O(n × log(max_pile)).

3. **This code has a subtle bug. Find it:**
   ```python
   def search(arr, target):
       lo, hi = 0, len(arr)
       while lo < hi:
           mid = lo + (hi - lo) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               lo = mid + 1
           else:
               hi = mid
       return -1  # Bug: what if target is at lo?
   ```

---

**← Previous:** [Chapter 2: Patterns](./02_patterns.md)
**Next →** [Chapter 4: Python Templates](./04_python_templates.md)
