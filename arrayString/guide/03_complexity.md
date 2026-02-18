# 📖 Chapter 3: Complexity Analysis (Phân tích độ phức tạp)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Know the exact Big-O of every array/string operation in Python (Biết Big-O chính xác mọi thao tác mảng/chuỗi)
- Avoid common performance traps (Tránh bẫy hiệu năng thường gặp)
- Estimate if your solution will pass LeetCode constraints (Ước tính lời giải có pass constraints không)

---

## 1. Operations Master Table (Bảng tổng hợp thao tác)

### Array (List) Operations

| Operation | Code | Time | Why |
|-----------|------|------|-----|
| Access | `arr[i]` | **O(1)** | Direct address calculation (Tính địa chỉ trực tiếp) |
| Assign | `arr[i] = x` | **O(1)** | Direct write (Ghi trực tiếp) |
| Append | `arr.append(x)` | **O(1)** amortized | May need resize occasionally (Đôi khi cần mở rộng) |
| Pop end | `arr.pop()` | **O(1)** | Remove last, no shift needed (Xóa cuối, không cần dịch) |
| Pop specific | `arr.pop(i)` | **O(n)** | Must shift elements after i (Phải dịch phần tử sau i) |
| Insert | `arr.insert(i, x)` | **O(n)** | Must shift elements right (Phải dịch phần tử sang phải) |
| Delete | `del arr[i]` | **O(n)** | Must shift elements left (Phải dịch phần tử sang trái) |
| Search | `x in arr` | **O(n)** | Linear scan (Duyệt tuyến tính) |
| Index | `arr.index(x)` | **O(n)** | Linear scan to first match (Duyệt đến phần tử đầu khớp) |
| Length | `len(arr)` | **O(1)** | Stored as attribute (Lưu sẵn) |
| Sort | `arr.sort()` | **O(n log n)** | Timsort algorithm |
| Reverse | `arr.reverse()` | **O(n)** | Swap from ends (Hoán đổi từ 2 đầu) |
| Slice | `arr[i:j]` | **O(j-i)** | Copy slice elements (Sao chép phần tử trong slice) |
| Copy | `arr.copy()` / `arr[:]` | **O(n)** | Copy all elements (Sao chép toàn bộ) |
| Extend | `arr.extend(other)` | **O(k)** | k = len(other) |
| `min()`/`max()` | `min(arr)` | **O(n)** | Must scan all (Phải duyệt hết) |
| `sum()` | `sum(arr)` | **O(n)** | Must add all (Phải cộng hết) |
| Count | `arr.count(x)` | **O(n)** | Scan all (Duyệt hết) |

### String Operations

| Operation | Code | Time | Why |
|-----------|------|------|-----|
| Access | `s[i]` | **O(1)** | Direct (Trực tiếp) |
| Length | `len(s)` | **O(1)** | Stored (Lưu sẵn) |
| Slice | `s[i:j]` | **O(j-i)** | Creates new string (Tạo chuỗi mới) |
| Concatenate | `s + t` | **O(len(s) + len(t))** | Creates new string (Tạo chuỗi mới) |
| `s += t` in loop | N/A | **O(n²) total!** ⚠️ | Creates new string each time |
| `''.join(list)` | `''.join(parts)` | **O(total length)** | Single allocation (Một lần cấp phát) |
| Find | `s.find(t)` | **O(n × m)** | n=len(s), m=len(t) |
| Replace | `s.replace(a, b)` | **O(n)** | Creates new string |
| Split | `s.split(sep)` | **O(n)** | Scan + create list |
| Lower/Upper | `s.lower()` | **O(n)** | Creates new string |
| `in` check | `t in s` | **O(n × m)** | Substring search |

---

## 2. Common Performance Traps (Bẫy hiệu năng thường gặp)

### Trap 1: String Concatenation in Loop — O(n²)! ⚠️

```python
# ❌ BAD — O(n²)
result = ""
for i in range(n):
    result += str(i)  # Each += creates a BRAND NEW string!
    # Iteration 0: copies 1 char
    # Iteration 1: copies 2 chars
    # Iteration n: copies n chars
    # Total: 1+2+3+...+n = n(n+1)/2 = O(n²)

# ✅ GOOD — O(n)
parts = []
for i in range(n):
    parts.append(str(i))  # O(1) each
result = ''.join(parts)    # O(n) once
```

### Trap 2: `list.insert(0, x)` in Loop — O(n²)!

```python
# ❌ BAD — O(n²)
arr = []
for x in data:
    arr.insert(0, x)  # Shifts ALL elements right each time!
    # n iterations × n shifts = O(n²)

# ✅ GOOD — O(n)
from collections import deque
dq = deque()
for x in data:
    dq.appendleft(x)  # O(1) — deque is doubly-linked
```

### Trap 3: `x in list` in Loop — O(n²)!

```python
# ❌ BAD — O(n²)
seen = []
for x in arr:
    if x in seen:       # O(n) linear search each time!
        return True
    seen.append(x)

# ✅ GOOD — O(n)
seen = set()
for x in arr:
    if x in seen:       # O(1) hash lookup!
        return True
    seen.add(x)
```

### Trap 4: Slicing Inside Loop — Hidden O(n²)!

```python
# ❌ BAD — O(n²) or worse
for i in range(n):
    sub = arr[i:i+k]    # O(k) per slice
    total = sum(sub)     # O(k) per sum
    # Both create copies unnecessarily!

# ✅ GOOD — maintain running sum O(n)
window_sum = sum(arr[:k])
for i in range(k, n):
    window_sum += arr[i] - arr[i-k]  # Slide: add right, remove left
```

---

## 3. Constraint Reading Guide (Hướng dẫn đọc ràng buộc)

When you see these constraints on LeetCode (Khi thấy các ràng buộc này trên LeetCode):

| Constraint | Expected Complexity | Array/String Approach |
|-----------|-------------------|---------------------|
| n ≤ 10 | O(n!) or O(2ⁿ) | Try all permutations/subsets |
| n ≤ 500 | O(n³) | Triple loop OK |
| n ≤ 10⁴ | O(n²) | Nested loops OK |
| n ≤ 10⁵ | O(n log n) | Sort + single pass |
| n ≤ 10⁶ | O(n) | Single pass, hash map |
| n ≤ 10⁸ | O(n) or O(log n) | Must be very efficient |

### Quick Decision (Quyết định nhanh)

```
n ≤ 10⁴?  → Nested loop OK → try simple approach first
            (Vòng lặp lồng OK → thử cách đơn giản trước)

n ≤ 10⁵?  → Need O(n) or O(n log n) → use hash map, sort, or prefix sum
            (Cần O(n) hoặc O(n log n) → dùng hash map, sort, prefix sum)

n ≤ 10⁶?  → Must be O(n) → single pass with clever state tracking
            (Phải O(n) → một lần duyệt với tracking thông minh)
```

---

## 4. Space Complexity Awareness (Nhận thức về bộ nhớ)

| Approach | Space | When is this required? |
|---------|-------|----------------------|
| In-place modification | O(1) | "Do not allocate extra array" |
| Hash Map/Set | O(n) | Default — most problems allow this |
| Prefix Sum array | O(n) | Subarray sum queries |
| New result array | O(n) | "Return new array" |
| 2D DP table | O(m×n) | "Optimize later to O(n)" |

> **Tip**: If a problem says "in-place" or "O(1) extra space", you need Pattern 3 (In-Place Modification) from Chapter 2 (Nếu bài nói "tại chỗ" hoặc "O(1) bộ nhớ thêm", dùng Pattern 3 từ Chương 2).

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **What is the time complexity of `arr.pop(0)`?** Why is it different from `arr.pop()`? (Tại sao khác `arr.pop()`?)

2. **This code has a hidden performance trap. What is it?**
   ```python
   for i in range(len(arr)):
       if arr[i] in arr[i+1:]:
           return True
   ```
   (Code này có bẫy hiệu năng ẩn. Là gì?)

3. **A problem says `n ≤ 10⁵`. Can you use two nested loops?** Calculate the operations (Tính số phép toán).

4. **Why is `''.join(list)` faster than repeated `+=` for string building?** (Tại sao `.join()` nhanh hơn `+=` lặp lại?)

5. **What is the time complexity of:**
   ```python
   for i in range(n):
       arr_copy = arr[:]         # Line A
       arr_copy.sort()           # Line B
   ```
   (Big-O tổng cộng?)

---

**← Previous:** [Chapter 2: Patterns](./02_patterns.md)
**Next →** [Chapter 4: Python Templates](./04_python_templates.md)
