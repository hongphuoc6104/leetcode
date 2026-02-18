# 📖 Topic 0: Brute Force Search (Vét Cạn)

## Theory (Lý thuyết cơ bản)

**Brute Force** is the algorithmic strategy of trying **every possible solution** and checking which one satisfies the problem's conditions (Vét cạn là chiến lược thử **mọi lời giải** và kiểm tra cái nào thỏa). It's the foundation of algorithmic thinking — every optimization starts from understanding the BF approach.

> 📚 For detailed study materials, see [`brute_force/guide/`](../../brute_force/guide/)

### 5 Variants (5 Biến thể)

| Variant | Time | When to Use |
|---------|------|-------------|
| Linear Search | O(n) | Find element in unsorted data |
| Nested Loops | O(n²)/O(n³) | Check all pairs/triples |
| Permutations | O(n!) | Try all orderings (n ≤ 12) |
| Subsets | O(2ⁿ) | Try all combinations (n ≤ 25) |
| Subarrays | O(n²) | Try all contiguous sections |

### Core Template (Template cốt lõi)

```python
# Linear Search — O(n)
def brute_force_linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Pair Search (Nested Loops) — O(n²)
def brute_force_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Subset Search (Bitmask) — O(2ⁿ)
def brute_force_subsets(nums, target):
    n = len(nums)
    for mask in range(1 << n):
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        if sum(subset) == target:
            return subset
    return []

# Permutation Search — O(n!)
from itertools import permutations
def brute_force_permutations(nums):
    best = None
    for perm in permutations(nums):
        score = evaluate(perm)
        if best is None or score > best:
            best = score
    return best
```

---

## 30 LeetCode Problems (30 bài LeetCode)

> Brute Force is often the first approach. Many of these problems have optimized solutions — try BF first, then optimize (BF thường là cách tiếp cận đầu tiên. Nhiều bài có lời giải tối ưu — thử BF trước, rồi tối ưu).

### 🟢 Easy (10 bài)

| # | Problem | Link | BF Variant | BF Time | Optimize With |
|---|---------|------|-----------|---------|--------------|
| 1 | Two Sum | [LC 1](https://leetcode.com/problems/two-sum/) | Nested Loops | O(n²) | Hash Map O(n) |
| 2 | Contains Duplicate | [LC 217](https://leetcode.com/problems/contains-duplicate/) | Nested Loops | O(n²) | Hash Set O(n) |
| 3 | Best Time Buy/Sell Stock | [LC 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Nested Loops | O(n²) | Track min O(n) |
| 4 | Valid Anagram | [LC 242](https://leetcode.com/problems/valid-anagram/) | Linear Scan | O(n) | Counter/Sort |
| 5 | Missing Number | [LC 268](https://leetcode.com/problems/missing-number/) | Linear Scan | O(n) | Math/XOR O(n) |
| 6 | Single Number | [LC 136](https://leetcode.com/problems/single-number/) | Nested Loops | O(n²) | XOR O(n) |
| 7 | Majority Element | [LC 169](https://leetcode.com/problems/majority-element/) | Nested Loops | O(n²) | Boyer-Moore O(n) |
| 8 | Pascal's Triangle | [LC 118](https://leetcode.com/problems/pascals-triangle/) | Linear Scan | O(n²) | Direct build |
| 9 | Plus One | [LC 66](https://leetcode.com/problems/plus-one/) | Linear Scan | O(n) | Reverse iterate |
| 10 | Move Zeroes | [LC 283](https://leetcode.com/problems/move-zeroes/) | Linear Scan | O(n) | Two Pointers O(n) |

### 🟡 Medium (10 bài)

| # | Problem | Link | BF Variant | BF Time | Optimize With |
|---|---------|------|-----------|---------|--------------|
| 1 | 3Sum | [LC 15](https://leetcode.com/problems/3sum/) | Nested 3 Loops | O(n³) | Sort + Two Pointers O(n²) |
| 2 | Subarray Sum Equals K | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | Subarrays | O(n²) | Prefix Sum + Hash O(n) |
| 3 | Longest Substring No Repeat | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Subarrays | O(n³) | Sliding Window O(n) |
| 4 | Container With Most Water | [LC 11](https://leetcode.com/problems/container-with-most-water/) | Nested Loops | O(n²) | Two Pointers O(n) |
| 5 | 4Sum | [LC 18](https://leetcode.com/problems/4sum/) | Nested 4 Loops | O(n⁴) | Sort + Two Pointers O(n³) |
| 6 | Combination Sum | [LC 39](https://leetcode.com/problems/combination-sum/) | Subsets | O(2ⁿ) | Backtracking + pruning |
| 7 | Permutations | [LC 46](https://leetcode.com/problems/permutations/) | Permutations | O(n!) | Backtracking |
| 8 | Subsets | [LC 78](https://leetcode.com/problems/subsets/) | Subsets | O(2ⁿ) | Bitmask/Backtrack |
| 9 | Max Product Subarray | [LC 152](https://leetcode.com/problems/maximum-product-subarray/) | Subarrays | O(n²) | DP O(n) |
| 10 | Generate Parentheses | [LC 22](https://leetcode.com/problems/generate-parentheses/) | Permutations | O(2²ⁿ) | Backtracking + validation |

### 🔴 Hard (10 bài)

| # | Problem | Link | BF Variant | BF Time | Optimize With |
|---|---------|------|-----------|---------|--------------|
| 1 | Median Two Sorted Arrays | [LC 4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Merge + Scan | O(n+m) | Binary Search O(log min(n,m)) |
| 2 | N-Queens | [LC 51](https://leetcode.com/problems/n-queens/) | Permutations | O(n!) | Backtracking + pruning |
| 3 | Sudoku Solver | [LC 37](https://leetcode.com/problems/sudoku-solver/) | Subsets | O(9⁸¹) | Backtracking + constraints |
| 4 | Min Window Substring | [LC 76](https://leetcode.com/problems/minimum-window-substring/) | Subarrays | O(n²·m) | Sliding Window O(n) |
| 5 | Trapping Rain Water | [LC 42](https://leetcode.com/problems/trapping-rain-water/) | Nested Loops | O(n²) | Two Pointers O(n) |
| 6 | Word Break II | [LC 140](https://leetcode.com/problems/word-break-ii/) | Permutations | O(2ⁿ) | DP + Backtrack |
| 7 | Palindrome Partitioning | [LC 131](https://leetcode.com/problems/palindrome-partitioning/) | Subsets | O(n·2ⁿ) | Backtracking + DP |
| 8 | Split Array Largest Sum | [LC 410](https://leetcode.com/problems/split-array-largest-sum/) | Subsets | O(2ⁿ) | Binary Search on Answer |
| 9 | Unique Paths III | [LC 980](https://leetcode.com/problems/unique-paths-iii/) | Permutations | O(4^(m·n)) | Backtracking on grid |
| 10 | Sliding Window Maximum | [LC 239](https://leetcode.com/problems/sliding-window-maximum/) | Subarrays | O(n·k) | Monotonic Deque O(n) |

---

## Tips

- **Always start with BF** (Luôn bắt đầu bằng BF) — understand the problem fully before optimizing
- **Check constraints first** (Kiểm tra ràng buộc trước): n ≤ 20? BF is likely intended. n ≥ 10⁵? Optimize
- **Use BF to verify** (Dùng BF để xác minh) — run BF on small inputs to check your optimized solution
- **BF → Optimization mapping**: Nested Loops → Hash Map/Two Pointers, Subarrays → Sliding Window, Subsets → DP
