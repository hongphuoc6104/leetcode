# 📖 Chapter 4: Python Templates

Copy-paste these templates and adapt. Each one solves a category of problems.
(Copy-paste template này và chỉnh sửa cho phù hợp.)

---

## Template 1: 1D DP — Space Optimized

```python
def climb_stairs(n):
    """Climbing Stairs (LC 70) — O(n) time, O(1) space."""
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

---

## Template 2: House Robber — Skip or Take

```python
def rob(nums):
    """House Robber (LC 198) — can't take adjacent."""
    if not nums: return 0
    if len(nums) <= 2: return max(nums)
    a, b = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        a, b = b, max(b, a + nums[i])
    return b
```

---

## Template 3: 0/1 Knapsack — 1D Space

```python
def knapsack_01(weights, values, W):
    """Each item used at most once. Iterate w in REVERSE!"""
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]
```

---

## Template 4: Coin Change — Unbounded (Forward)

```python
def coin_change(coins, amount):
    """Min coins to make amount (LC 322). Forward = unbounded."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for a in range(coin, amount + 1):  # FORWARD!
            dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

---

## Template 5: Coin Change Ways — Count combinations

```python
def change(coins, amount):
    """Number of ways to make amount (LC 518)."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]
    return dp[amount]
```

---

## Template 6: LCS — Two Strings

```python
def lcs(s1, s2):
    """Longest Common Subsequence (LC 1143). O(m×n)."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

---

## Template 7: Edit Distance

```python
def min_distance(s1, s2):
    """Edit Distance (LC 72). O(m×n)."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],       # Delete
                                   dp[i][j-1],       # Insert
                                   dp[i-1][j-1])     # Replace
    return dp[m][n]
```

---

## Template 8: LIS — O(n²)

```python
def lis(nums):
    """Longest Increasing Subsequence (LC 300). O(n²)."""
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

---

## Template 9: LIS — O(n log n) with bisect

```python
import bisect
def lis_fast(nums):
    """O(n log n) using patience sorting."""
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

---

## Template 10: Unique Paths — Grid DP

```python
def unique_paths(m, n):
    """Unique Paths in grid (LC 62). O(m×n)."""
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[m-1][n-1]
```

---

## 📋 Pre-Coding Checklist (Kiểm tra trước khi code)

1. ✅ **Define dp[i]:** What exactly does it represent?
2. ✅ **Recurrence:** dp[i] = f(dp[i-1], ...) — can you write it?  
3. ✅ **Base case:** dp[0] = ? dp[1] = ?
4. ✅ **Iteration order:** Forward or reverse? Row-first or col-first?
5. ✅ **Answer location:** dp[n]? max(dp)? dp[m][n]?
6. ✅ **Space optimization:** Can I use O(1) or O(n) instead of O(n²)?
7. ✅ **Edge cases:** Empty input? n=1? n=2?

---

## 🔄 DP Optimization Cheatsheet

| From | To | Technique |
|------|----|-----------|
| O(n) space | O(1) | Keep only last 2 values |
| O(n × W) space | O(W) | 1D array + reverse iteration |
| O(m × n) space | O(n) | Two-row rolling |
| O(n²) time LIS | O(n log n) | Binary search on tails |

---

**← Previous:** [Chapter 3: Complexity](./03_complexity.md)  
**Next →** [Examples](../examples/) 🚀
