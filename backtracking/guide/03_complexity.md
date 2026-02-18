# 📖 Chapter 3: Complexity Analysis (Phân tích Độ phức tạp)

## 1. Core Complexities (Độ phức tạp cốt lõi)

| Problem Type | Time | Space | Why (Giải thích) |
|-------------|------|-------|-------------------|
| **Subsets** | O(2ⁿ) | O(n) recursion | Each element: include or exclude (2 choices) |
| **Permutations** | O(n!) | O(n) recursion | n choices, then n-1, then n-2... |
| **Combinations C(n,k)** | O(C(n,k) · k) | O(k) | Binomial coefficient × copy |
| **N-Queens** | O(n!) | O(n) | At most n choices per row (decreasing) |
| **Word Search** | O(m·n · 4^L) | O(L) | Start at each cell, 4 dirs per step |
| **Sudoku** | O(9^(empty)) | O(81) | 9 choices per empty cell |

### Key Principle: Branching Factor × Depth

```
Time ≈ (branching factor) ^ (depth)

Subsets:      branching = 2 (include/exclude),  depth = n  → O(2ⁿ)
Permutations: branching = n on avg,             depth = n  → O(n!)  
N-Queens:     branching ≤ n (with pruning < n), depth = n  → better than O(n!)
```

---

## 2. Space Complexity (Không gian)

Backtracking space = **recursion stack depth** + **path/solution storage**.

| Problem | Stack Depth | Path Storage | Total |
|---------|------------|--------------|-------|
| Subsets | O(n) | O(n) per path | O(n) + O(2ⁿ · n) results |
| Permutations | O(n) | O(n) per path | O(n) + O(n! · n) results |
| Grid search | O(L) word length | O(L) | O(L) |
| N-Queens | O(n) rows | O(n) board | O(n) + O(solutions) |

> 💡 **Important:** The path array is O(n), but if you STORE all solutions, total space is O(number_of_solutions × solution_size).
>
> **Quan trọng:** Mảng path là O(n), nhưng nếu LƯU tất cả lời giải, tổng space = O(số_lời_giải × kích_thước).

---

## 3. Pruning — The Key to Speed! (Cắt tỉa — chìa khóa tốc độ!)

**Without pruning**, backtracking = brute force. **With pruning**, we skip entire branches.

### Example: Combination Sum (Tổng tổ hợp)

```python
# ❌ Without pruning: tries ALL subsets, checks sum at end
def combinationSum_bad(candidates, target):
    result = []
    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:   # Only stop AFTER exceeding — wastes time!
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()
    backtrack(0, [], 0)
    return result

# ✅ With pruning: skip entire branches when remaining candidates too large
def combinationSum_good(candidates, target):
    candidates.sort()   # ← Sort first for pruning!
    result = []
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # ← ALL remaining candidates are too large, SKIP ALL!
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()
    backtrack(0, [], target)
    return result
```

### Pruning Impact (Hiệu quả cắt tỉa)

| Problem | Without Pruning | With Pruning | Improvement |
|---------|----------------|--------------|-------------|
| N-Queens n=8 | 40320 states | 876 states | **46x** faster |
| Sudoku typical | 9^81 | ~10⁸ | **Massive** |
| Combination Sum | 2ⁿ subsets | Much fewer | ~10x-100x |

---

## 4. Common Mistakes (Lỗi thường gặp)

### Mistake 1: Forgetting to undo choice (Quên bỏ chọn)
```python
# ❌ WRONG: No backtrack step!
path.append(nums[i])
backtrack(path, i + 1)
# Missing: path.pop()  ← BUG: path keeps growing forever!

# ✅ RIGHT: Always undo
path.append(nums[i])
backtrack(path, i + 1)
path.pop()              # ← MUST undo after recursion
```

### Mistake 2: Saving reference instead of copy (Lưu tham chiếu thay vì bản sao)
```python
# ❌ WRONG: Appends reference — all results are the SAME empty list!
result.append(path)     # path gets modified later by pop()!

# ✅ RIGHT: Append a COPY
result.append(path[:])  # path[:] creates a new list
# OR: result.append(list(path))
```

### Mistake 3: Not handling duplicates (Không xử lý trùng)
```python
# ❌ For [1, 1, 2], subsets gives [[1,2], [1,2]] — duplicates!

# ✅ FIX: Sort + skip consecutive duplicates
candidates.sort()
for i in range(start, len(candidates)):
    if i > start and candidates[i] == candidates[i-1]:
        continue  # Skip duplicate at same level!
```

---

## ❓ Self-Check Questions

1. **Why is subsets O(2ⁿ) and permutations O(n!)?** (Tại sao subsets O(2ⁿ) nhưng permutations O(n!)?)
2. **What is the space complexity of N-Queens?** Include both stack and solution storage.
3. **How does sorting help with pruning in Combination Sum?** (Sorting giúp cắt tỉa thế nào?)
4. **What happens if you don't copy the path before appending to results?** (Không copy path thì sao?)

---

**← Previous:** [Chapter 2](./02_patterns.md) | **Next →** [Chapter 4: Templates](./04_python_templates.md)
