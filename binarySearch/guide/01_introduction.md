# 📖 Chapter 1: Introduction to Binary Search (Giới thiệu Tìm Kiếm Nhị Phân)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Understand WHY Binary Search is O(log n) (Hiểu TẠI SAO là O(log n))
- Know the 3 core templates and their differences (3 template cốt lõi)
- Handle boundary conditions correctly (Xử lý điều kiện biên đúng)

---

## 1. What is Binary Search? (Tìm Kiếm Nhị Phân là gì?)

Binary Search halves the search space every step. It's like the "guess a number" game (Chia đôi không gian tìm kiếm mỗi bước. Giống trò "đoán số"):

```
Guess a number from 1 to 100:
  You: 50    → "Too low!"
  You: 75    → "Too high!"
  You: 62    → "Too low!"
  You: 68    → "Correct!" 🎯

Only 4 guesses for 100 numbers! → log₂(100) ≈ 7 guesses max
```

### Requirement: Monotonic Property (Yêu cầu: Tính đơn điệu)

Binary Search works when there's a **clear boundary** — everything on one side satisfies a condition, everything on the other doesn't (Hoạt động khi có **ranh giới rõ ràng** — một bên thỏa, bên kia không).

```
Sorted array:  [1, 3, 5, 7, 9, 11, 13]
                 F  F  F  T  T  T   T    ← "≥ 7?"

The boundary is clear! BS can find it in O(log n).
(Ranh giới rõ ràng! BS tìm được trong O(log n).)
```

---

## 2. The 3 Core Templates (3 Template cốt lõi)

### Template 1: Exact Match — `while left <= right`

Find the **exact** target in a sorted array (Tìm target **chính xác**).

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:              # Note: <=
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid                # Found!
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1                         # Not found
```

**When to use**: "Find target" → return index or -1.

---

### Template 2: Lower Bound — `while left < right`

Find the **first** position where condition is true (Tìm vị trí **đầu tiên** thỏa điều kiện).

```python
def lower_bound(arr, target):
    left, right = 0, len(arr)         # Note: right = len(arr)
    while left < right:               # Note: <
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid               # Note: NOT mid - 1
    return left                       # First index where arr[i] >= target
```

**When to use**: "First element ≥ target", "leftmost position", "insert position".

---

### Template 3: Binary Search on Answer — `while lo < hi`

The answer itself is in a range. Binary search for the optimal answer (Đáp án trong 1 khoảng. BS tìm đáp án tối ưu).

```python
def search_on_answer(lo, hi):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if is_feasible(mid):          # Can we achieve 'mid'?
            hi = mid                  # Try smaller (minimize)
        else:
            lo = mid + 1
    return lo
```

**When to use**: "Minimum capacity to...", "Maximum minimum...", answer is a NUMBER you binary search.

---

## 3. Template Comparison (So sánh Template)

| Aspect | Template 1 | Template 2 | Template 3 |
|--------|-----------|-----------|-----------|
| Goal | Find exact | Find boundary | Find optimal answer |
| Loop | `left <= right` | `left < right` | `lo < hi` |
| Right init | `len-1` | `len` | `max_answer` |
| On match | `return mid` | `right = mid` | `hi = mid` |
| Returns | Index or -1 | Boundary index | Optimal value |

---

## 4. The #1 Source of Bugs (Nguồn lỗi #1)

### `left <= right` vs `left < right`

```
Template 1 (left <= right):
  - Search space: [left, right] inclusive
  - Terminates when: left > right (empty space)
  - left = mid + 1, right = mid - 1 (both sides shrink)

Template 2 (left < right):
  - Search space: [left, right) half-open
  - Terminates when: left == right (single element)
  - left = mid + 1, right = mid (right side stays)
```

### `mid = (left + right) // 2` vs `mid = left + (right - left) // 2`

Both give the same result, but the second **avoids integer overflow** in languages like C/Java (Cả 2 cho cùng kết quả, nhưng cách 2 **tránh tràn số** trong C/Java).

---

## ❓ Self-Check Questions

1. **For a sorted array of 1 billion elements, how many steps does BS need?** Calculate log₂(10⁹) (Tính log₂(10⁹)).

2. **"Find the first element ≥ 7 in [1, 3, 5, 7, 7, 9]"** — which template? Trace the steps.

3. **Why does Template 2 use `right = mid` instead of `right = mid - 1`?** What happens if you use `mid - 1`?

4. **"Find minimum speed to eat all bananas in H hours"** — which template? What is the search space?

---

**Next →** [Chapter 2: Patterns](./02_patterns.md)
