"""
=============================================================
 Example 2: Monotonic Stack — Next Greater & Daily Temps
=============================================================

The MOST IMPORTANT Stack pattern for interviews.
(Pattern Stack QUAN TRỌNG NHẤT.)

Demonstrates:
  - Next Greater Element
  - Daily Temperatures (LC 739)
  - BF O(n²) vs Monotonic Stack O(n)

Time:  O(n) — each element pushed/popped at most once
Space: O(n)
"""


def next_greater_brute(nums):
    """BF: O(n²) — scan right for each element."""
    n = len(nums)
    result = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
    return result


def next_greater_mono(nums):
    """Monotonic Stack: O(n)."""
    n = len(nums)
    result = [-1] * n
    stack = []  # indices, values are decreasing

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)

    return result


def next_greater_trace(nums):
    """Monotonic Stack with trace."""
    n = len(nums)
    result = [-1] * n
    stack = []

    print(f"  Array: {nums}")
    print()

    for i in range(n):
        pops = []
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
            pops.append(f"{nums[idx]}→{nums[i]}")

        stack.append(i)
        stack_vals = [nums[j] for j in stack]
        pop_info = f" pop: {pops}" if pops else ""
        print(f"    i={i} val={nums[i]:>2}: "
              f"stack={stack_vals}{pop_info}")

    print(f"\n  Result: {result}")
    return result


def daily_temperatures(temps):
    """
    Daily Temperatures (LC 739).
    Find how many days until a warmer temperature.
    Same as "next greater index difference".
    """
    n = len(temps)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and temps[stack[-1]] < temps[i]:
            idx = stack.pop()
            result[idx] = i - idx  # Days difference
        stack.append(i)

    return result


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Next Greater — Trace")
    print("=" * 60)
    result = next_greater_trace([2, 1, 4, 3, 5])
    assert result == [4, 4, 5, 5, -1]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: BF vs Monotonic Stack")
    print("=" * 60)
    cases = [
        [2, 1, 4, 3, 5],
        [4, 3, 2, 1],
        [1, 2, 3, 4],
        [1, 3, 2, 4],
    ]
    for nums in cases:
        bf = next_greater_brute(nums)
        ms = next_greater_mono(nums)
        status = "✅" if bf == ms else "❌"
        print(f"  {nums} → {ms} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Daily Temperatures")
    print("=" * 60)
    cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73],
         [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ]
    for temps, expected in cases:
        result = daily_temperatures(temps)
        status = "✅" if result == expected else "❌"
        print(f"  {temps}")
        print(f"    → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 4: Performance BF O(n²) vs MS O(n)")
    print("=" * 60)
    import time
    import random

    for n in [1000, 5000, 10000]:
        nums = [random.randint(1, 1000) for _ in range(n)]

        start = time.perf_counter()
        bf = next_greater_brute(nums)
        t_bf = time.perf_counter() - start

        start = time.perf_counter()
        ms = next_greater_mono(nums)
        t_ms = time.perf_counter() - start

        assert bf == ms
        speedup = t_bf / t_ms if t_ms > 0 else float('inf')
        print(f"  n={n:>5}: BF={t_bf*1000:>7.2f}ms | "
              f"MS={t_ms*1000:>6.3f}ms | {speedup:.1f}x")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Monotonic Stack: each element O(1) amortized")
    print("   2. Stack stores INDICES, not values")
    print("   3. Daily Temps = Next Greater (index difference)")
