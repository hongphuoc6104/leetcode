"""
=============================================================
 Example 1: Two Sum with Hash Map (LC 1)
=============================================================

THE most famous LeetCode problem. Shows why Hash Map
turns O(n²) brute force into O(n).

Time:  O(n) — single pass
Space: O(n) — hash map stores seen values
"""


def two_sum_brute(nums, target):
    """BF: O(n²) — check all pairs."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hash(nums, target):
    """Hash Map: O(n) — lookup complement."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def two_sum_trace(nums, target):
    """Two Sum with step trace."""
    seen = {}
    print(f"  nums={nums}, target={target}")
    print()

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            print(f"    i={i} num={num}: "
                  f"need {complement} → FOUND at {seen[complement]}! 🎯")
            return [seen[complement], i]
        else:
            seen[num] = i
            print(f"    i={i} num={num}: "
                  f"need {complement} → not in map, store {{{num}:{i}}}")

    return []


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Two Sum — Trace")
    print("=" * 60)
    result = two_sum_trace([2, 7, 11, 15], 9)
    assert result == [0, 1]
    print(f"\n  Result: {result} ✅")
    print()

    result = two_sum_trace([3, 2, 4], 6)
    assert result == [1, 2]
    print(f"\n  Result: {result} ✅")
    print()

    print("=" * 60)
    print("TEST 2: BF O(n²) vs Hash O(n)")
    print("=" * 60)
    import time
    import random

    for n in [100, 1000, 5000, 10000]:
        nums = list(range(n))
        target = n - 2 + n - 1  # Last two elements

        start = time.perf_counter()
        bf = two_sum_brute(nums, target)
        t_bf = time.perf_counter() - start

        start = time.perf_counter()
        hm = two_sum_hash(nums, target)
        t_hm = time.perf_counter() - start

        assert bf == hm
        speedup = t_bf / t_hm if t_hm > 0 else float('inf')
        print(f"  n={n:>5}: BF={t_bf*1000:>8.2f}ms | "
              f"Hash={t_hm*1000:>6.3f}ms | {speedup:.0f}x")
    print()

    print("=" * 60)
    print("TEST 3: Edge Cases")
    print("=" * 60)
    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for nums, target, expected in cases:
        result = two_sum_hash(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"  nums={nums}, target={target} → {result} {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. complement = target - num → O(1) lookup")
    print("   2. Store as you go → single pass O(n)")
    print("   3. Hash Map trades space for time")
