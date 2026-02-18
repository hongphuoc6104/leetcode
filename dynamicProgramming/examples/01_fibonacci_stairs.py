"""
=============================================================
 Example 1: Fibonacci & Climbing Stairs (LC 70)
=============================================================

The FOUNDATION of DP. Shows 3 approaches:
  - Naive recursion: O(2^n) ← terrible!
  - Memoization (top-down): O(n)
  - Tabulation (bottom-up): O(n), O(1) space

Time:  O(n)
Space: O(1) optimized
"""


def climb_recursive(n):
    """Naive recursion: O(2^n) — DON'T use!"""
    if n <= 2:
        return n
    return climb_recursive(n - 1) + climb_recursive(n - 2)


def climb_memo(n, memo=None):
    """Top-down memoization: O(n) time, O(n) space."""
    if memo is None:
        memo = {}
    if n <= 2:
        return n
    if n not in memo:
        memo[n] = climb_memo(n - 1, memo) + climb_memo(n - 2, memo)
    return memo[n]


def climb_tabulation(n):
    """Bottom-up tabulation: O(n) time, O(n) space."""
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def climb_optimized(n):
    """Space-optimized: O(n) time, O(1) space."""
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Correctness — All approaches same result")
    print("=" * 60)
    for n in range(1, 11):
        r = climb_recursive(n)
        m = climb_memo(n)
        t = climb_tabulation(n)
        o = climb_optimized(n)
        assert r == m == t == o
        print(f"  n={n:>2}: {o} ways")
    print("  ✅ All match!")
    print()

    print("=" * 60)
    print("TEST 2: Performance — Recursion vs DP")
    print("=" * 60)
    import time

    # Recursion gets VERY slow at n=30+
    for n in [20, 25, 30]:
        start = time.perf_counter()
        r = climb_recursive(n)
        t_rec = time.perf_counter() - start

        start = time.perf_counter()
        d = climb_optimized(n)
        t_dp = time.perf_counter() - start

        assert r == d
        print(f"  n={n}: recursive={t_rec*1000:.2f}ms | "
              f"DP={t_dp*1000:.4f}ms")
    print()

    print("=" * 60)
    print("TEST 3: Large n (only DP can handle)")
    print("=" * 60)
    for n in [100, 1000, 10000]:
        start = time.perf_counter()
        result = climb_optimized(n)
        t = time.perf_counter() - start
        digits = len(str(result))
        print(f"  n={n:>5}: {digits} digits, {t*1000:.3f}ms")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Recursion O(2^n) → DP O(n). HUGE difference!")
    print("   2. dp[i] = dp[i-1] + dp[i-2] ← THE recurrence")
    print("   3. Only need last 2 values → O(1) space")
