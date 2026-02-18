# 📖 Chapter 3: Complexity Analysis (Phân tích độ phức tạp)

## 🎯 Learning Objectives (Mục tiêu)

After this chapter (Sau chương này):
- Understand WHY Two Pointers is O(n) with a proof (Hiểu TẠI SAO Two Pointers là O(n))
- Know when sorting first is worth it (Biết khi nào sort trước là đáng)
- Avoid common mistakes (Tránh lỗi thường gặp)

---

## 1. Why is Two Pointers O(n)? (Tại sao là O(n)?)

### The Proof (Chứng minh)

```
Total work = number of pointer movements (Tổng công việc = số lần di chuyển con trỏ)

Opposite Direction:
  - left starts at 0, moves RIGHT at most n times
  - right starts at n-1, moves LEFT at most n times
  - Total moves ≤ n + n = 2n = O(n) ✅

Same Direction:
  - slow moves at most n times
  - fast moves exactly n times (one pass)
  - Total moves ≤ n + n = 2n = O(n) ✅

Fast & Slow (cycle):
  - In worst case, fast traverses 2n nodes
  - slow traverses n nodes
  - Total = 3n = O(n) ✅
```

### Key Insight (Nhận xét quan trọng)

Each pointer moves in **one direction only** (monotonic). This guarantees O(n) because each pointer visits each element **at most once** (Mỗi con trỏ di chuyển **một hướng duy nhất** (đơn điệu). Đảm bảo O(n) vì mỗi con trỏ thăm mỗi phần tử **nhiều nhất 1 lần**).

---

## 2. Complexity Table (Bảng độ phức tạp)

| Pattern | Time | Space | Notes |
|---------|------|-------|-------|
| Pair Sum (sorted) | O(n) | O(1) | Array must be sorted |
| Pair Sum (unsorted) | O(n log n) | O(1) | Sort first: O(n log n) + O(n) |
| Palindrome | O(n) | O(1) | |
| Remove/Filter | O(n) | O(1) | In-place |
| Container/Area | O(n) | O(1) | |
| Subsequence | O(n + m) | O(1) | n, m = lengths of two strings |
| 3Sum | O(n²) | O(1) | 1 loop × Two Pointers = n × n |
| 4Sum | O(n³) | O(1) | 2 loops × Two Pointers |

---

## 3. Sort First? Decision Guide (Có nên sort trước?)

```
Can you sort the input?
  │
  ├─ YES, and you need Two Pointers for sorted data
  │   └─ Total: O(n log n) + O(n) = O(n log n)
  │      Still better than BF O(n²) for large n!
  │      (Vẫn tốt hơn BF O(n²) cho n lớn!)
  │
  ├─ YES, but Hash Map gives O(n) without sorting
  │   └─ Use Hash Map instead (Time: O(n), Space: O(n))
  │      Trade-off: more space for better time
  │      (Đánh đổi: nhiều bộ nhớ hơn cho thời gian tốt hơn)
  │
  └─ NO, order matters for the answer
      └─ Can't sort! Use Same Direction or other technique
```

### When Two Pointers Beats Hash Map (Khi nào Two Pointers thắng Hash Map)

| Factor | Two Pointers | Hash Map |
|--------|-------------|----------|
| Time | O(n) or O(n log n) | O(n) |
| Space | **O(1)** ✅ | O(n) |
| When to prefer | Memory-constrained, data already sorted | Need O(n), can't sort |

---

## 4. Common Mistakes (Lỗi thường gặp)

### Mistake 1: Forgetting to Sort ⚠️

```python
# ❌ WRONG — unsorted array with opposite-direction!
def two_sum_wrong(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1      # This only works if sorted!
        else:
            right -= 1
    # Will MISS valid pairs! (Sẽ BỎ QUA cặp hợp lệ!)
```

### Mistake 2: Infinite Loop ⚠️

```python
# ❌ WRONG — pointers don't always move!
while left < right:
    if some_condition:
        # Forgot to move pointer → infinite loop!
        pass  # (Quên di chuyển con trỏ → vòng lặp vô hạn!)
```

### Mistake 3: Off-by-One in Same Direction ⚠️

```python
# ❌ WRONG — slow starts at wrong position
def remove_dupes_wrong(nums):
    slow = 1            # Should be 0! (Phải là 0!)
    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1     # Off by one! (Sai 1 đơn vị!)
```

---

## 5. Constraint Guide (Hướng dẫn ràng buộc)

| n constraint | Can use BF O(n²)? | Should use Two Pointers? |
|-------------|-------------------|--------------------------|
| n ≤ 1000 | ✅ Yes | Optional (Tùy chọn) |
| n ≤ 10⁴ | ⚠️ Borderline | Recommended (Nên dùng) |
| n ≤ 10⁵ | ❌ No, TLE | **Must use** (Phải dùng) |
| n ≤ 10⁶ | ❌ No | **Must use** with O(n) (Phải O(n)) |

---

## ❓ Self-Check Questions (Câu hỏi tự kiểm tra)

1. **Why can't we use Opposite Direction Two Pointers on an unsorted array?** Give a concrete counterexample (Cho ví dụ cụ thể).

2. **For 3Sum, the total complexity is O(n²). Break down why**: O(n log n) sort + n × O(n) two pointers = ? (Phân tích chi tiết.)

3. **A problem says n ≤ 10⁵. Your BF is O(n²). Is Two Pointers fast enough?** Calculate both operation counts (Tính cả 2 số phép toán).

4. **When would you choose Hash Map over Two Pointers, even for a sorted array?** (Khi nào chọn Hash Map dù mảng đã sorted?)

---

**← Previous:** [Chapter 2: Patterns](./02_patterns.md)
**Next →** [Chapter 4: Python Templates](./04_python_templates.md)
