# 📖 Chapter 3: Complexity Analysis (Phân tích Độ phức tạp)

## 1. Core Complexities (Độ phức tạp cốt lõi)

Greedy algorithms are generally **the fastest** approach for problems they apply to.

| Pattern | Time | Space | Why (Giải thích) |
|---------|------|-------|-------------------|
| Intervals (Sort by end) | **O(n log n)** | O(1) | Sort dominates (Sort chiếm chủ yếu) |
| Jump Game (Max reach) | **O(n)** | O(1) | Single pass (Duyệt 1 lần) |
| Boats (Sort + 2 ptrs) | **O(n log n)** | O(1) | Sort + linear scan |
| Stock Trading II | **O(n)** | O(1) | Single pass, accumulate diffs |
| Partition Labels | **O(n)** | O(1)* | Two passes (* = 26 chars max) |
| Gas Station | **O(n)** | O(1) | Single pass |
| Huffman Coding | **O(n log n)** | O(n) | Heap operations |
| Activity Selection | **O(n log n)** | O(1) | Sort + linear |

### Key Insight: O(n log n) Dominance

For most Greedy problems, **sorting is the bottleneck** (Sort là nút thắt). The greedy scan itself is O(n).

```
Total time = Sort O(n log n) + Scan O(n) = O(n log n)
```

---

## 2. Space Complexity (Độ phức tạp không gian)

Greedy is typically **space-efficient** because it doesn't need memoization tables:

| Approach | Space | Why |
|----------|-------|-----|
| **Greedy** | O(1) | No extra tables needed |
| **DP** | O(n) or O(n²) | dp[] array or table |
| **Backtracking** | O(n) stack + O(2ⁿ) results | Recursion depth + all solutions |

> 💡 **Python sort:** `list.sort()` uses Timsort which uses O(n) auxiliary space. If space is critical, consider in-place alternatives.

---

## 3. When Greedy Beats DP (Khi nào Greedy thắng DP)

| Problem | DP Time | Greedy Time | Speedup |
|---------|---------|-------------|---------|
| Non-overlapping Intervals | O(n²) | O(n log n) | **~100x** for n=10⁵ |
| Jump Game | O(n²) | O(n) | **~10⁵x** for n=10⁵ |
| Gas Station | O(n²) | O(n) | **~10⁵x** |
| Activity Selection | O(n²) | O(n log n) | **~100x** |

### Constraint Guide (Hướng dẫn theo ràng buộc)

| Constraint (Ràng buộc) | Maximum Feasible Complexity | Greedy possible? |
|------------------------|----------------------------|-------------------|
| n ≤ 10³ | O(n²) ✅ | Yes, but DP also works |
| n ≤ 10⁵ | O(n log n) ⚠️ | **YES — Greedy required** (DP too slow) |
| n ≤ 10⁶ | O(n) ⚠️ | **YES — Greedy or linear scan only** |
| n ≤ 10⁷ | O(n) | Need O(n) Greedy |

> 🤔 **Think:** If `n = 10⁵` and the problem involves intervals, why is DP's O(n²) = 10¹⁰ operations TOO SLOW? (Hint: ~10⁸ operations per second)

---

## 4. Common Mistakes (Lỗi thường gặp)

### Mistake 1: Assuming Greedy always works
```python
# ❌ Coin Change with coins = [1, 3, 4], target = 6
# Greedy picks 4 → 1 → 1 = 3 coins
# DP finds 3 → 3 = 2 coins ← OPTIMAL!
# ✅ Solution: Use DP for Coin Change with arbitrary coins
```

### Mistake 2: Wrong sort key for intervals
```python
# ❌ Sort by start time for "non-overlapping"
intervals.sort(key=lambda x: x[0])   # WRONG for LC 435!
# ✅ Sort by END time
intervals.sort(key=lambda x: x[1])
```

### Mistake 3: Not sorting first
```python
# ❌ Trying greedy on unsorted array for boat problem
# Without sorting, can't pair heaviest + lightest effectively
# ✅ Always sort first for pairing problems
people.sort()
```

### Mistake 4: Greedy when order matters
```python
# ❌ Using Greedy for "minimum edit distance"
# Each local choice affects future choices — need DP!
```

---

## ❓ Self-Check Questions

1. **What is the bottleneck** in most Greedy algorithms? (Nút thắt là gì?)
2. **If n = 10⁶, can you use O(n²) DP?** No — how fast must you be? (Cần nhanh bao nhiêu?)
3. **Give an example** of a problem where Greedy is WRONG. (Cho ví dụ bài Greedy sai)

---

**← Previous:** [Chapter 2](./02_patterns.md) | **Next →** [Chapter 4: Templates](./04_python_templates.md)
