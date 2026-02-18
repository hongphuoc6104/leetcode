"""
=============================================================
 Example 1: Fixed Size Window (Cửa sổ kích thước cố định)
=============================================================

Demonstrates Fixed Window:
  - Max sum of k consecutive elements
  - BF vs Sliding Window comparison

Time:  O(n) — single pass
Space: O(1) — just a running sum
"""


def max_sum_brute(arr, k):
    """BF: O(n×k) — recompute sum for each window."""
    n = len(arr)
    max_sum = float('-inf')
    ops = 0

    for i in range(n - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            window_sum += arr[j]
            ops += 1
        max_sum = max(max_sum, window_sum)

    return max_sum, ops


def max_sum_sliding(arr, k):
    """Sliding Window: O(n) — add right, remove left."""
    window_sum = sum(arr[:k])
    max_sum = window_sum
    ops = k  # Initial sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
        ops += 2  # One add, one subtract

    return max_sum, ops


def max_sum_sliding_trace(arr, k):
    """Sliding Window with step-by-step trace."""
    window_sum = sum(arr[:k])
    max_sum = window_sum

    print(f"  Array: {arr}, k={k}")
    print(f"  Initial window: {arr[:k]}, sum={window_sum}")
    print()

    for i in range(k, len(arr)):
        removed = arr[i - k]
        added = arr[i]
        window_sum += added - removed
        max_sum = max(max_sum, window_sum)

        window = arr[i - k + 1:i + 1]
        print(f"  Slide: remove {removed}, add {added} "
              f"→ window={window} sum={window_sum} "
              f"{'🏆 new max!' if window_sum == max_sum else ''}")

    return max_sum


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Fixed Window — Step Trace")
    print("=" * 60)
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    result = max_sum_sliding_trace(arr, 3)
    assert result == 13
    print(f"\n  Max sum of 3 consecutive = {result} ✅")
    print()

    print("=" * 60)
    print("TEST 2: BF O(n×k) vs SW O(n)")
    print("=" * 60)
    import time
    import random

    for n, k in [(100, 10), (1000, 50), (10000, 100), (50000, 500)]:
        arr = [random.randint(-100, 100) for _ in range(n)]

        start = time.perf_counter()
        bf_result, bf_ops = max_sum_brute(arr, k)
        bf_time = time.perf_counter() - start

        start = time.perf_counter()
        sw_result, sw_ops = max_sum_sliding(arr, k)
        sw_time = time.perf_counter() - start

        assert bf_result == sw_result
        speedup = bf_time / sw_time if sw_time > 0 else float('inf')
        print(f"  n={n:>5}, k={k:>3}: "
              f"BF={bf_time*1000:>8.2f}ms ({bf_ops:>8} ops) | "
              f"SW={sw_time*1000:>6.3f}ms ({sw_ops:>6} ops) | "
              f"{speedup:>.1f}x")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it:")
    print("   1. What if k = 1? What if k = n?")
    print("   2. How would you find the MIN sum instead?")
    print("   3. Can you track the window's START INDEX too?")
