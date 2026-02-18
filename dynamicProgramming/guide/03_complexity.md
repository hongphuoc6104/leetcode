# 📖 Chapter 3: Complexity Analysis

## 1. DP Time = States × Transition Cost

The time complexity of DP is determined by: **number of states** × **cost to compute each state**.
(Thời gian DP = Số trạng thái × Chi phí tính mỗi trạng thái.)

| Pattern | States | Transition | Total Time |
|---------|--------|-----------|-----------|
| 1D Linear (stairs, robber) | O(n) | O(1) | **O(n)** |
| Knapsack (0/1) | O(n × W) | O(1) | **O(n × W)** |
| LCS / Edit Distance | O(m × n) | O(1) | **O(m × n)** |
| LIS (naive) | O(n) | O(n) | **O(n²)** |
| LIS (binary search) | O(n) | O(log n) | **O(n log n)** |
| Grid DP | O(R × C) | O(1) | **O(R × C)** |
| Interval DP | O(n²) | O(n) | **O(n³)** |

> ⚠️ **Knapsack is pseudo-polynomial:** O(n × W) depends on the VALUE of W, not its bit-length. If W = 10⁹, this is too slow!

---

## 2. Space Complexity & Optimization

### Standard space
| Pattern | Space |
|---------|-------|
| 1D DP | O(n) |
| 2D DP (LCS, Knapsack) | O(m × n) or O(n × W) |

### Space optimization techniques

#### Rolling Array: O(n) → O(1) for 1D
```python
# Before: dp = [0] * (n+1), using dp[i-1], dp[i-2]
# After: only keep last 2 values
a, b = 1, 2
for i in range(3, n + 1):
    a, b = b, a + b
# Space: O(n) → O(1)
```

#### 2D → 1D for Knapsack
```python
# Before: dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt]+val)
# Key insight: row i only depends on row i-1

# After: single 1D array, iterate REVERSE
dp = [0] * (W + 1)
for i in range(n):
    for w in range(W, weights[i] - 1, -1):  # REVERSE!
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
# Space: O(n × W) → O(W)
```

#### 2D → two rows for LCS
```python
# Only need current row and previous row
prev = [0] * (n + 1)
curr = [0] * (n + 1)
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i-1] == s2[j-1]:
            curr[j] = prev[j-1] + 1
        else:
            curr[j] = max(prev[j], curr[j-1])
    prev, curr = curr, [0] * (n + 1)
# Space: O(m × n) → O(n)
```

---

## 3. Common Mistakes (Lỗi thường gặp)

### Wrong iteration order for 0/1 Knapsack ⚠️
```python
# ❌ WRONG — forward iteration uses item multiple times!
for w in range(weights[i], W + 1):  # Forward
    dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
# This solves UNBOUNDED knapsack, not 0/1!

# ✅ CORRECT for 0/1 — reverse iteration
for w in range(W, weights[i] - 1, -1):  # Reverse
    dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
```

### Off-by-one in DP table ⚠️
```python
# ❌ dp = [[0]*n for _ in range(m)]  — too small!
# ✅ dp = [[0]*(n+1) for _ in range(m+1)]  — need extra row/col for base case
```

### Forgetting edge cases ⚠️
```python
# Edge cases for common DP problems:
# - Empty input: return 0
# - Single element: return element itself
# - n=1 or n=2: handle separately before loop
```

### Wrong definition of dp state ⚠️
The hardest part of DP is defining what `dp[i]` means. If your solution gives wrong answers, re-examine your state definition FIRST.

```python
# LC 300: LIS
# ❌ dp[i] = length of LIS in nums[:i+1]  — ambiguous!
# ✅ dp[i] = length of LIS ENDING AT index i — precise!
```

---

## 4. Constraint Guide (Hướng dẫn từ constraints)

| Constraint | Approach | Expected Time |
|-----------|----------|--------------|
| n ≤ 20 | Bitmask DP or backtracking | O(2^n × n) |
| n ≤ 100 | O(n³) interval DP OK | O(n²) ~ O(n³) |
| n ≤ 1000 | O(n²) LIS, LCS OK | O(n²) |
| n ≤ 10⁴ | Need O(n log n) for LIS | O(n log n) |
| n ≤ 10⁵ | 1D DP O(n) or O(n log n) | O(n) |
| W ≤ 10⁵ | Knapsack O(n×W) OK | O(n × W) |

---

## ❓ Self-Check Questions

1. **Why is Knapsack O(n×W) called "pseudo-polynomial"?** (Tại sao gọi là "giả đa thức"?)
2. **Can you always optimize 2D DP to 1D?** When can't you? (Khi nào không thể tối ưu?)
3. **LIS O(n²) vs O(n log n): which should you use for n=10⁵?** (Chọn cái nào?)
4. **How do you decide the iteration order (forward vs reverse)?** (Chọn thứ tự duyệt?)

---

**← Previous:** [Chapter 2: Patterns](./02_patterns.md)  
**Next →** [Chapter 4: Templates](./04_python_templates.md)
