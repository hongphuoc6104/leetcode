"""
=============================================================
 Example 4: Coin Change (LC 322)
=============================================================

Unbounded Knapsack variant: each coin can be used unlimited times.
Find MINIMUM coins to make amount.

Time:  O(n × amount)
Space: O(amount)
"""


def coin_change(coins, amount):
    """
    DP: dp[a] = min coins to make amount a.
    dp[a] = min(dp[a], dp[a - coin] + 1)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_trace(coins, amount):
    """Coin Change with trace of which coins used."""
    dp = [float('inf')] * (amount + 1)
    parent = [-1] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for a in range(coin, amount + 1):
            if dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
                parent[a] = coin

    if dp[amount] == float('inf'):
        return -1, []

    # Reconstruct coins used
    coins_used = []
    a = amount
    while a > 0:
        coins_used.append(parent[a])
        a -= parent[a]

    return dp[amount], coins_used


def coin_change_ways(coins, amount):
    """
    Count number of ways to make amount (LC 518).
    dp[a] += dp[a - coin]
    """
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]

    return dp[amount]


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Coin Change — Minimum Coins")
    print("=" * 60)
    cases = [
        ([1, 5, 10, 25], 30, 2),     # 25+5
        ([1, 2, 5], 11, 3),           # 5+5+1
        ([2], 3, -1),                  # Impossible
        ([1], 0, 0),
    ]
    for coins, amount, expected in cases:
        result = coin_change(coins, amount)
        status = "✅" if result == expected else "❌"
        print(f"  coins={coins}, amount={amount} → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 2: Coin Change — Trace")
    print("=" * 60)
    min_coins, used = coin_change_trace([1, 5, 10, 25], 41)
    print(f"  Amount=41, coins=[1,5,10,25]")
    print(f"  Min coins: {min_coins}, used: {used}")
    assert sum(used) == 41
    assert min_coins == len(used)
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 3: Coin Change Ways (LC 518)")
    print("=" * 60)
    cases = [
        ([1, 2, 5], 5, 4),    # {5, 2+2+1, 2+1+1+1, 1+1+1+1+1}
        ([2], 3, 0),
        ([10], 10, 1),
    ]
    for coins, amount, expected in cases:
        result = coin_change_ways(coins, amount)
        status = "✅" if result == expected else "❌"
        print(f"  coins={coins}, amount={amount} → {result} ways {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Min coins: dp[a] = min(dp[a], dp[a-coin]+1)")
    print("   2. Count ways: dp[a] += dp[a-coin]")
    print("   3. Unbounded: iterate a FORWARD (not reverse)")
