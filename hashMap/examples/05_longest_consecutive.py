"""
=============================================================
 Example 5: Longest Consecutive Sequence (LC 128)
=============================================================

Find the longest consecutive sequence in unsorted array.
BF: O(n log n) with sorting
Set: O(n) — only start from sequence beginnings!

Time:  O(n)
Space: O(n)
"""


def longest_consecutive_sort(nums):
    """Sort approach: O(n log n)."""
    if not nums:
        return 0
    nums = sorted(set(nums))
    best = curr = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            curr += 1
            best = max(best, curr)
        else:
            curr = 1
    return best


def longest_consecutive_set(nums):
    """
    Hash Set: O(n).
    Key: only start counting from BEGINNING of sequence.
    How? Check if (n-1) is NOT in set → n is a start!
    """
    num_set = set(nums)
    best = 0

    for n in num_set:
        # Only start from beginning of sequence
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)

    return best


def longest_consecutive_trace(nums):
    """Set approach with trace."""
    num_set = set(nums)
    best = 0

    print(f"  nums={nums}")
    print(f"  set={sorted(num_set)}")
    print()

    for n in sorted(num_set):
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)
            seq = list(range(n, n + length))
            is_best = " 🏆" if length == best and length > 1 else ""
            print(f"    Start {n}: sequence={seq} "
                  f"len={length}{is_best}")
        else:
            print(f"    Skip  {n}: {n-1} exists, not a start")

    return best


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Longest Consecutive — Trace")
    print("=" * 60)
    result = longest_consecutive_trace([100, 4, 200, 1, 3, 2])
    assert result == 4
    print(f"\n  Longest = {result} ✅")
    print()

    print("=" * 60)
    print("TEST 2: More Cases")
    print("=" * 60)
    cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1, 2, 0, 1], 3),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),
    ]
    for nums, expected in cases:
        sort_r = longest_consecutive_sort(nums)
        set_r = longest_consecutive_set(nums)
        match = sort_r == set_r == expected
        status = "✅" if match else "❌"
        print(f"  {nums[:6]}{'...' if len(nums) > 6 else ''} "
              f"→ sort={sort_r} set={set_r} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Sort O(n log n) vs Set O(n)")
    print("=" * 60)
    import time
    import random

    for n in [1000, 10000, 50000, 100000]:
        nums = random.sample(range(n * 2), n)

        start = time.perf_counter()
        r1 = longest_consecutive_sort(nums)
        t1 = time.perf_counter() - start

        start = time.perf_counter()
        r2 = longest_consecutive_set(nums)
        t2 = time.perf_counter() - start

        assert r1 == r2
        print(f"  n={n:>6}: sort={t1*1000:>7.2f}ms | "
              f"set={t2*1000:>6.2f}ms")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Skip non-starts: if n-1 in set → skip")
    print("   2. Each element visited at most twice → O(n)")
    print("   3. set() removes duplicates + O(1) lookup")
