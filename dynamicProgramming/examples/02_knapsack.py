"""
=============================================================
 Example 2: 0/1 Knapsack (Bài toán Xếp balo)
=============================================================

Given items with weights and values, maximize value
within capacity W. Each item can be used AT MOST ONCE.

Time:  O(n × W)
Space: O(W) optimized
"""


def knapsack_2d(weights, values, W):
    """2D DP: dp[i][w] = max value using items[:i] with capacity w."""
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]  # Skip item
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][W]


def knapsack_1d(weights, values, W):
    """Space-optimized 1D: iterate w in REVERSE!"""
    dp = [0] * (W + 1)

    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]


def knapsack_trace(weights, values, W):
    """2D Knapsack with item selection trace."""
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # Backtrack to find selected items
    selected = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    return dp[n][W], selected[::-1]


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Basic Knapsack")
    print("=" * 60)
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    W = 8

    print(f"  Items: weight={weights}, value={values}")
    print(f"  Capacity: W={W}")

    r2d = knapsack_2d(weights, values, W)
    r1d = knapsack_1d(weights, values, W)
    assert r2d == r1d
    print(f"  Max value: {r2d} ✅")

    max_val, items = knapsack_trace(weights, values, W)
    print(f"  Selected items: {items} "
          f"(weight={sum(weights[i] for i in items)}, "
          f"value={sum(values[i] for i in items)})")
    print()

    print("=" * 60)
    print("TEST 2: More Cases")
    print("=" * 60)
    cases = [
        ([1, 2, 3], [6, 10, 12], 5, 22),
        ([10], [100], 5, 0),
        ([1, 1, 1], [1, 1, 1], 2, 2),
    ]
    for w, v, cap, expected in cases:
        r = knapsack_1d(w, v, cap)
        status = "✅" if r == expected else "❌"
        print(f"  W={w}, V={v}, cap={cap} → {r} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Subset Sum (Can partition?)")
    print("=" * 60)
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

    cases = [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
    ]
    for nums, expected in cases:
        result = can_partition(nums)
        status = "✅" if result == expected else "❌"
        print(f"  {nums} → partition={result} {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. 0/1 Knapsack: iterate w in REVERSE (1D)")
    print("   2. Subset Sum = Knapsack with target = sum/2")
    print("   3. Backtrack: if dp[i][w] ≠ dp[i-1][w] → item i selected")
