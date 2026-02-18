# 📖 Chapter 3: Complexity Analysis (Phân tích độ phức tạp)

## 1. Why is Sliding Window O(n)? (Tại sao là O(n)?)

### The Amortized Proof (Chứng minh phân bổ)

```
Fixed Window:
  - right pointer moves n times: O(n)
  - Each move: 1 addition + 1 subtraction = O(1) work
  - Total: O(n) ✅

Variable Window:
  - right pointer moves n times total
  - left pointer ALSO moves at most n times total
  - Key: left never moves backward! (left không bao giờ lùi!)
  - Each element is added at most ONCE, removed at most ONCE
  - Total pointer movements ≤ 2n = O(n) ✅
```

### Visual Proof (Chứng minh trực quan)

```
Each element visited by right:  exactly once  = n times
Each element visited by left:   at most once  ≤ n times
                                              ─────────
                                Total work    ≤ 2n = O(n)
```

---

## 2. Complexity Table

| Pattern | Time | Space | Notes |
|---------|------|-------|-------|
| Fixed Sum | O(n) | O(1) | Just maintain running sum |
| Fixed Frequency | O(n) | O(k) | k = pattern length |
| Longest Variable | O(n) | O(min(n,k)) | k = distinct elements |
| Shortest Variable | O(n) | O(1) or O(k) | Depends on state |
| Counting (at-most-K) | O(n) | O(k) | Called twice for exactly-K |

---

## 3. Sliding Window vs Brute Force

| Problem | BF Time | SW Time | Speedup at n=10⁵ |
|---------|---------|---------|-------------------|
| Max sum of k=100 | O(n×k) = O(10⁷) | O(n) = O(10⁵) | 100x |
| Longest no repeat | O(n²×n) = O(n³) | O(n) | 10¹⁰x |
| Min window substring | O(n²×m) | O(n) | ~10⁵x |
| Find all anagrams | O(n×m) | O(n) | ~10x |

---

## 4. Common Mistakes (Lỗi thường gặp)

### Mistake 1: Forgetting to clean up frequency map ⚠️

```python
# ❌ WRONG
freq[s[left]] -= 1
left += 1
# freq still has s[left] with count 0 → wrong distinct count!

# ✅ CORRECT
freq[s[left]] -= 1
if freq[s[left]] == 0:
    del freq[s[left]]    # Remove zero entries!
left += 1
```

### Mistake 2: Wrong shrink timing ⚠️

```python
# ❌ WRONG for "longest" problems
while valid(window):     # Should shrink when INVALID!
    shrink()

# ✅ CORRECT for "longest"
while invalid(window):   # Shrink ONLY when invalid
    shrink()
max_len = max(max_len, right - left + 1)
```

### Mistake 3: Off-by-one in Fixed Window ⚠️

```python
# ❌ WRONG — missed first window
for i in range(k, len(arr)):  # Starts at k, misses initial window!
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)

# ✅ CORRECT
window_sum = sum(arr[:k])
max_sum = window_sum              # Initialize with first window!
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)
```

---

## 5. Constraint Guide

| Constraint | Approach |
|-----------|----------|
| n ≤ 10⁴ | BF O(n²) is OK, but SW is cleaner |
| n ≤ 10⁵ | **Must use Sliding Window** |
| n ≤ 10⁶ | Must be O(n), SW is perfect |

---

## ❓ Self-Check Questions

1. **Why does `left` moving at most n times guarantee O(n)?** Explain the amortized argument (Giải thích phân bổ).

2. **What is the space complexity of "Longest Substring Without Repeating"?** Hint: how many distinct characters can exist? (Bao nhiêu ký tự khác nhau tối đa?)

3. **This code has a bug. Find it:**
   ```python
   def max_sum(arr, k):
       window = sum(arr[:k])
       for i in range(1, len(arr) - k + 1):
           window += arr[i+k-1] - arr[i-1]
       return window
   ```

---

**← Previous:** [Chapter 2: Patterns](./02_patterns.md)
**Next →** [Chapter 4: Python Templates](./04_python_templates.md)
