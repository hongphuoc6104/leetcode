# 📖 Chapter 2: DP Patterns

Five patterns that cover ~80% of DP problems in interviews (5 pattern bao phủ ~80% bài DP phỏng vấn).

---

## Pattern 1: 1D DP — Linear Sequence

### 🔍 Signal (Dấu hiệu)
- "climbing stairs", "min cost", "house robber"
- Problem depends on **previous 1-2 states**

### 💡 Key Insight
`dp[i]` depends only on `dp[i-1]` and/or `dp[i-2]` → can optimize to O(1) space!

### 💻 Code — Climbing Stairs (LC 70)
```python
def climb(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

### 💻 Code — House Robber (LC 198)
```python
def rob(nums):
    if not nums: return 0
    if len(nums) <= 2: return max(nums)
    a, b = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        a, b = b, max(b, a + nums[i])  # Rob or skip
    return b
```

### 📌 LC 70, LC 198, LC 213, LC 746, LC 91

---

## Pattern 2: Knapsack — Choose or Skip Items

### 🔍 Signal
- "partition into subsets", "target sum", "can you make amount?"
- **Choose/skip** decision for each item

### 💡 Key Insight
For each item: `dp[w] = max(skip, take)`.
- **0/1 Knapsack:** Each item used at most once → iterate w in **REVERSE**
- **Unbounded:** Each item unlimited → iterate w **FORWARD**

### 💻 Code — 0/1 Knapsack (Space-Optimized)
```python
def knapsack_01(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):  # REVERSE!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]
```

### 💻 Code — Subset Sum / Partition (LC 416)
```python
def can_partition(nums):
    total = sum(nums)
    if total % 2: return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for t in range(target, num - 1, -1):
            dp[t] = dp[t] or dp[t - num]
    return dp[target]
```

> ⚠️ **Why reverse?** Forward iteration would let the same item be used multiple times (Unbounded Knapsack). Reverse ensures each item used at most once.

### 📌 LC 416, LC 494, LC 322, LC 518, LC 474

---

## Pattern 3: String DP (LCS / Edit Distance) — Two Sequences

### 🔍 Signal
- "longest common subsequence", "edit distance", "interleaving"
- **Two strings/sequences** compared character by character

### 💡 Key Insight
`dp[i][j]` = answer for `s1[:i]` and `s2[:j]`. Compare last characters:
- **Match:** diagonal `dp[i-1][j-1] + 1`
- **No match:** best of skip from either sequence

### 💻 Code — LCS (LC 1143)
```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1   # Match!
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

### 💻 Code — Edit Distance (LC 72)
```python
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i   # Delete all
    for j in range(n+1): dp[0][j] = j   # Insert all
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],       # Delete
                                   dp[i][j-1],       # Insert
                                   dp[i-1][j-1])     # Replace
    return dp[m][n]
```

### 📌 LC 1143, LC 72, LC 583, LC 97, LC 115

---

## Pattern 4: LIS — Longest Increasing Subsequence

### 🔍 Signal
- "longest increasing", "longest chain", "number of LIS"
- Need to find optimal subsequence (not contiguous)

### 💡 Key Insight
`dp[i]` = length of LIS ending at index i. For each j < i where `nums[j] < nums[i]`, update `dp[i] = max(dp[i], dp[j]+1)`.

### 💻 Code — O(n²)
```python
def lis(nums):
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

### 💻 Code — O(n log n) with Binary Search
```python
import bisect
def lis_fast(nums):
    tails = []  # tails[i] = smallest tail of LIS of length i+1
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

> 💡 The O(n log n) version uses patience sorting — `tails` is NOT the actual LIS, just tracks the best possible endings.

### 📌 LC 300, LC 354, LC 673, LC 334

---

## Pattern 5: Grid DP / 2D Path

### 🔍 Signal
- "unique paths", "minimum path sum", "triangle"
- Grid traversal with constraints (usually right/down only)

### 💡 Key Insight
`dp[r][c]` = answer to reach cell (r, c). Transition from top or left.

### 💻 Code — Unique Paths (LC 62)
```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[m-1][n-1]
```

### 💻 Code — Minimum Path Sum (LC 64)
```python
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    for r in range(m):
        for c in range(n):
            if r == 0 and c == 0: continue
            elif r == 0: grid[r][c] += grid[r][c-1]
            elif c == 0: grid[r][c] += grid[r-1][c]
            else: grid[r][c] += min(grid[r-1][c], grid[r][c-1])
    return grid[m-1][n-1]
```

### 📌 LC 62, LC 63, LC 64, LC 120, LC 221

---

## 📊 Pattern Decision Table

| Signal | Pattern | State | Time |
|--------|---------|-------|------|
| "step/stair/rob" | 1D Linear | dp[i] | O(n) |
| "subset/partition/target" | Knapsack | dp[i][w] | O(n×W) |
| "two strings/sequences" | String DP | dp[i][j] | O(m×n) |
| "longest increasing" | LIS | dp[i] | O(n²) or O(n log n) |
| "grid path/sum" | Grid DP | dp[r][c] | O(R×C) |

---

## ❓ Self-Check Questions

1. **Climbing stairs with 1,2,3 steps — what's the recurrence?** (Bước 1,2,3 — công thức?)
2. **0/1 Knapsack iterates w in reverse. What problem does forward solve?** (w thuận giải bài gì?)
3. **LCS of "ABCDE" and "ACE"?** Trace through the DP table.
4. **Can you optimize 2D grid DP to 1D?** How? (Tối ưu không gian?)

---

**← Previous:** [Chapter 1: Introduction](./01_introduction.md)  
**Next →** [Chapter 3: Complexity](./03_complexity.md)
