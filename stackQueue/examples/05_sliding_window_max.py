"""
=============================================================
 Example 5: Sliding Window Maximum (LC 239)
=============================================================

The HARDEST classic Stack/Queue problem.
Uses Monotonic Deque (double-ended queue).

BF: O(n×k) — scan each window
DQ: O(n)   — maintain decreasing deque

Time:  O(n)
Space: O(k)
"""
from collections import deque


def max_window_brute(nums, k):
    """BF: O(n×k) — max of each window."""
    result = []
    for i in range(len(nums) - k + 1):
        result.append(max(nums[i:i + k]))
    return result


def max_window_deque(nums, k):
    """
    Monotonic Deque: O(n).
    
    Maintain deque of INDICES with DECREASING values.
    Front of deque = index of max in current window.
    """
    dq = deque()  # Stores indices
    result = []

    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller values (they'll never be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Window is full
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


def max_window_trace(nums, k):
    """Monotonic Deque with trace."""
    dq = deque()
    result = []

    print(f"  Array: {nums}, k={k}")
    print()

    for i in range(len(nums)):
        removed_old = []
        while dq and dq[0] < i - k + 1:
            removed_old.append(dq.popleft())

        removed_small = []
        while dq and nums[dq[-1]] < nums[i]:
            removed_small.append(dq.pop())

        dq.append(i)

        dq_vals = [nums[j] for j in dq]
        info = ""
        if removed_old:
            info += f" expired:{[nums[j] for j in removed_old]}"
        if removed_small:
            info += f" <{nums[i]}:{[nums[j] for j in removed_small]}"

        if i >= k - 1:
            result.append(nums[dq[0]])
            print(f"    i={i} val={nums[i]:>2}: "
                  f"deque={dq_vals} → max={nums[dq[0]]}"
                  f"{info}")
        else:
            print(f"    i={i} val={nums[i]:>2}: "
                  f"deque={dq_vals} (building window){info}")

    return result


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Sliding Window Max — Trace")
    print("=" * 60)
    result = max_window_trace([1, 3, -1, -3, 5, 3, 6, 7], 3)
    assert result == [3, 3, 5, 5, 6, 7]
    print(f"\n  Result: {result} ✅")
    print()

    print("=" * 60)
    print("TEST 2: More Cases")
    print("=" * 60)
    cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([9, 8, 7, 6, 5], 3, [9, 8, 7]),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5]),
    ]
    for nums, k, expected in cases:
        result = max_window_deque(nums, k)
        status = "✅" if result == expected else "❌"
        print(f"  {nums}, k={k} → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 3: BF O(n×k) vs Deque O(n)")
    print("=" * 60)
    import time
    import random

    for n, k in [(1000, 50), (5000, 100), (10000, 500)]:
        nums = [random.randint(-100, 100) for _ in range(n)]

        start = time.perf_counter()
        bf = max_window_brute(nums, k)
        t_bf = time.perf_counter() - start

        start = time.perf_counter()
        dq = max_window_deque(nums, k)
        t_dq = time.perf_counter() - start

        assert bf == dq
        speedup = t_bf / t_dq if t_dq > 0 else float('inf')
        print(f"  n={n:>5}, k={k:>3}: "
              f"BF={t_bf*1000:>7.2f}ms | "
              f"DQ={t_dq*1000:>6.3f}ms | "
              f"{speedup:.1f}x")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Deque front = max in current window")
    print("   2. Remove expired (popleft) + remove smaller (pop)")
    print("   3. Each element enters/leaves deque at most once → O(n)")
