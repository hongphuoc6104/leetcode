"""
=============================================================
 Example 4: Prefix Sum + Hash Map (LC 560)
=============================================================

The POWER COMBO for subarray problems.
(Bộ đôi SỨC MẠNH cho bài toán subarray.)

"How many subarrays have sum = k?"
BF: O(n²) — try all subarrays
Prefix+Hash: O(n) — genius trick!

Time:  O(n)
Space: O(n)
"""


def subarray_sum_brute(nums, k):
    """BF: O(n²) — check all subarrays."""
    count = 0
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1
    return count


def subarray_sum_hash(nums, k):
    """
    Prefix Sum + Hash Map: O(n).

    Key insight:
      sum(nums[i..j]) = prefix[j] - prefix[i-1]
      If prefix[j] - k exists in map → found a subarray!
    """
    count = 0
    prefix = 0
    seen = {0: 1}  # prefix 0 occurs once (empty prefix)

    for num in nums:
        prefix += num
        # How many times have we seen (prefix - k)?
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1

    return count


def subarray_sum_trace(nums, k):
    """Prefix + Hash with trace."""
    count = 0
    prefix = 0
    seen = {0: 1}

    print(f"  nums={nums}, k={k}")
    print(f"  {'i':>3} | {'num':>4} | {'prefix':>6} | "
          f"{'need':>5} | {'found':>5} | {'count':>5}")
    print(f"  {'-'*3}-+-{'-'*4}-+-{'-'*6}-+-"
          f"{'-'*5}-+-{'-'*5}-+-{'-'*5}")

    for i, num in enumerate(nums):
        prefix += num
        need = prefix - k
        found = seen.get(need, 0)
        count += found

        print(f"  {i:>3} | {num:>4} | {prefix:>6} | "
              f"{need:>5} | {found:>5} | {count:>5}"
              f"{'  🎯' if found > 0 else ''}")

        seen[prefix] = seen.get(prefix, 0) + 1

    return count


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Subarray Sum = K — Trace")
    print("=" * 60)
    result = subarray_sum_trace([1, 2, 3, -1, 1, 2], 3)
    assert result == 4  # [1,2], [3], [3,-1,1], [1,2]
    print(f"\n  Subarrays with sum=3: {result} ✅")
    print()

    print("=" * 60)
    print("TEST 2: More Cases")
    print("=" * 60)
    cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
        ([0, 0, 0], 0, 6),
    ]
    for nums, k, expected in cases:
        bf = subarray_sum_brute(nums, k)
        hm = subarray_sum_hash(nums, k)
        match = bf == hm == expected
        status = "✅" if match else "❌"
        print(f"  {nums}, k={k} → BF={bf} Hash={hm} {status}")
    print()

    print("=" * 60)
    print("TEST 3: BF O(n²) vs Hash O(n)")
    print("=" * 60)
    import time
    import random

    for n in [500, 2000, 5000, 10000]:
        nums = [random.randint(-10, 10) for _ in range(n)]
        k = 5

        start = time.perf_counter()
        bf = subarray_sum_brute(nums, k)
        t_bf = time.perf_counter() - start

        start = time.perf_counter()
        hm = subarray_sum_hash(nums, k)
        t_hm = time.perf_counter() - start

        assert bf == hm
        speedup = t_bf / t_hm if t_hm > 0 else float('inf')
        print(f"  n={n:>5}: BF={t_bf*1000:>8.2f}ms | "
              f"Hash={t_hm*1000:>6.3f}ms | {speedup:.0f}x")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. prefix[j] - prefix[i-1] = sum(i..j)")
    print("   2. Look up (prefix - k) in hash map → O(1)")
    print("   3. Initialize seen = {0: 1} for empty prefix!")
