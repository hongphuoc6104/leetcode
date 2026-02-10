# 📖 Chủ đề 10: Dynamic Programming

## Lý thuyết cơ bản

**DP** giải bài toán bằng cách chia thành bài toán con, lưu kết quả để tránh tính lại.

### Hai cách tiếp cận
```python
# 1. Top-down (Memoization)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# 2. Bottom-up (Tabulation)
def fib(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Tối ưu space (chỉ dùng 2 biến)
def fib(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### Các dạng DP phổ biến
1. **1D DP**: Climbing stairs, House robber
2. **2D DP**: Unique paths, Edit distance
3. **Knapsack**: Coin change, Partition subset
4. **LIS/LCS**: Subsequence problems
5. **Interval DP**: Burst balloons

---

## Danh sách 30 bài LeetCode

### 🟢 Easy (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Climbing Stairs | [LC 70](https://leetcode.com/problems/climbing-stairs/) | Fibonacci |
| 2 | Pascal's Triangle | [LC 118](https://leetcode.com/problems/pascals-triangle/) | dp[i][j] = dp[i-1][j-1] + dp[i-1][j] |
| 3 | Best Time Buy/Sell | [LC 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Track min, max profit |
| 4 | Counting Bits | [LC 338](https://leetcode.com/problems/counting-bits/) | dp[i] = dp[i>>1] + (i&1) |
| 5 | Is Subsequence | [LC 392](https://leetcode.com/problems/is-subsequence/) | Two pointers hoặc DP |
| 6 | Fibonacci Number | [LC 509](https://leetcode.com/problems/fibonacci-number/) | Cơ bản nhất |
| 7 | Min Cost Stairs | [LC 746](https://leetcode.com/problems/min-cost-climbing-stairs/) | dp[i] = min(dp[i-1], dp[i-2]) + cost[i] |
| 8 | N-th Tribonacci | [LC 1137](https://leetcode.com/problems/n-th-tribonacci-number/) | 3 số trước |
| 9 | Max Generated Array | [LC 1646](https://leetcode.com/problems/get-maximum-in-generated-array/) | Follow formula |
| 10 | Longest Unequal Subseq | [LC 2900](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/) | Greedy pick |

### 🟡 Medium (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Longest Palindrome Sub | [LC 5](https://leetcode.com/problems/longest-palindromic-substring/) | Expand center hoặc 2D DP |
| 2 | Generate Parentheses | [LC 22](https://leetcode.com/problems/generate-parentheses/) | Backtrack + counting |
| 3 | Unique Paths | [LC 62](https://leetcode.com/problems/unique-paths/) | 2D DP, combinatorics |
| 4 | Word Break | [LC 139](https://leetcode.com/problems/word-break/) | dp[i] = can form s[:i]? |
| 5 | House Robber | [LC 198](https://leetcode.com/problems/house-robber/) | dp[i] = max(dp[i-1], dp[i-2]+nums[i]) |
| 6 | House Robber II | [LC 213](https://leetcode.com/problems/house-robber-ii/) | Circular: 2 lần House Robber |
| 7 | LIS | [LC 300](https://leetcode.com/problems/longest-increasing-subsequence/) | O(n²) DP hoặc O(n log n) BS |
| 8 | Coin Change | [LC 322](https://leetcode.com/problems/coin-change/) | Unbounded knapsack |
| 9 | Partition Equal Subset | [LC 416](https://leetcode.com/problems/partition-equal-subset-sum/) | 0/1 knapsack |
| 10 | LCS | [LC 1143](https://leetcode.com/problems/longest-common-subsequence/) | Classic 2D DP |

### 🔴 Hard (10 bài)
| # | Bài | Link | Gợi ý |
|---|-----|------|-------|
| 1 | Regex Matching | [LC 10](https://leetcode.com/problems/regular-expression-matching/) | 2D DP |
| 2 | Longest Valid Parens | [LC 32](https://leetcode.com/problems/longest-valid-parentheses/) | Stack hoặc DP |
| 3 | Wildcard Matching | [LC 44](https://leetcode.com/problems/wildcard-matching/) | 2D DP |
| 4 | Edit Distance | [LC 72](https://leetcode.com/problems/edit-distance/) | Classic 2D DP |
| 5 | Interleaving String | [LC 97](https://leetcode.com/problems/interleaving-string/) | 2D DP |
| 6 | Distinct Subsequences | [LC 115](https://leetcode.com/problems/distinct-subsequences/) | 2D DP counting |
| 7 | Buy/Sell Stock III | [LC 123](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | State machine DP |
| 8 | Burst Balloons | [LC 312](https://leetcode.com/problems/burst-balloons/) | Interval DP |
| 9 | Count Vowels Perm | [LC 1220](https://leetcode.com/problems/count-vowels-permutation/) | State transition DP |
| 10 | Min Removals Mountain | [LC 1671](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) | LIS from both sides |

---

## Tips
- Bước 1: Xác định **state** (biến nào mô tả bài toán con)
- Bước 2: Viết **transition** (công thức chuyển đổi)
- Bước 3: Xác định **base case**
- Bước 4: Xác định **order of computation**
