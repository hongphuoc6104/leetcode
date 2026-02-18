"""
=============================================================
 Example 5: Trapping Rain Water (Hứng nước mưa)
=============================================================

Problem: Given heights, how much water is trapped after rain?
         (Cho chiều cao, bao nhiêu nước bị giữ sau mưa?)

Three approaches compared:
  1. Brute Force: O(n²) — for each bar, find max left & right
  2. Prefix Max:  O(n), O(n) space — precompute left_max, right_max
  3. Two Pointers: O(n), O(1) space — the optimal solution!

The key insight for Two Pointers:
  Water at position i = min(max_left, max_right) - height[i]
  We always process the side with SMALLER max height.
  (Luôn xử lý bên có chiều cao max NHỎ HƠN.)
"""


def trap_brute(height):
    """
    Brute Force: O(n²) time, O(1) space.
    For each bar, find tallest bar on left and right.
    """
    n = len(height)
    water = 0
    for i in range(1, n - 1):
        max_left = max(height[:i + 1])
        max_right = max(height[i:])
        water += min(max_left, max_right) - height[i]
    return water


def trap_prefix(height):
    """
    Prefix Max: O(n) time, O(n) space.
    Precompute left_max and right_max arrays.
    """
    n = len(height)
    if n < 3:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


def trap_two_pointers(height):
    """
    Two Pointers: O(n) time, O(1) space — OPTIMAL!
    (Hai Con Trỏ: O(n) thời gian, O(1) bộ nhớ — TỐI ƯU!)
    """
    if len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


def trap_two_pointers_trace(height):
    """Two Pointers with step trace."""
    if len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0

    print(f"  Height: {height}")
    print(f"  {'Step':>4} | {'L':>2} {'R':>2} | "
          f"{'h[L]':>4} {'h[R]':>4} | "
          f"{'Lmax':>4} {'Rmax':>4} | "
          f"{'side':>5} | {'trapped':>7} | "
          f"{'total':>5}")
    print(f"  {'-'*4}-+-{'-'*5}-+-{'-'*9}-+-"
          f"{'-'*9}-+-{'-'*5}-+-{'-'*7}-+-{'-'*5}")

    step = 0
    while left < right:
        step += 1
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            add = left_max - height[left]
            water += add
            side = "LEFT"
        else:
            right -= 1
            right_max = max(right_max, height[right])
            add = right_max - height[right]
            water += add
            side = "RIGHT"

        print(f"  {step:>4} | {left:>2} {right:>2} | "
              f"{height[left]:>4} {height[right]:>4} | "
              f"{left_max:>4} {right_max:>4} | "
              f"{side:>5} | {add:>7} | {water:>5}")

    return water


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("TEST 1: Classic Example with Trace")
    print("=" * 70)
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = trap_two_pointers_trace(height)
    assert result == 6
    print(f"\n  Total water: {result} ✅")
    print()

    # Verify all 3 methods agree
    print("=" * 70)
    print("TEST 2: All 3 Methods Agree")
    print("=" * 70)
    cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [1, 0, 1],
        [3, 0, 0, 2, 0, 4],
        [],
    ]
    for h in cases:
        bf = trap_brute(h)
        pf = trap_prefix(h)
        tp = trap_two_pointers(h)
        status = "✅" if bf == pf == tp else "❌"
        print(f"  {str(h):>40} → BF={bf} "
              f"Prefix={pf} TP={tp} {status}")
    print()

    # Performance comparison
    print("=" * 70)
    print("TEST 3: Performance Comparison")
    print("=" * 70)
    import time
    import random

    for n in [100, 1000, 5000]:
        h = [random.randint(0, 100) for _ in range(n)]

        start = time.perf_counter()
        r1 = trap_brute(h)
        t_bf = time.perf_counter() - start

        start = time.perf_counter()
        r2 = trap_prefix(h)
        t_pf = time.perf_counter() - start

        start = time.perf_counter()
        r3 = trap_two_pointers(h)
        t_tp = time.perf_counter() - start

        assert r1 == r2 == r3
        print(f"  n={n:>5}: BF={t_bf*1000:>8.2f}ms | "
              f"Prefix={t_pf*1000:>6.3f}ms | "
              f"TP={t_tp*1000:>6.3f}ms")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways (Bài học chính):")
    print("   1. BF O(n²) → Prefix O(n)+O(n) → TP O(n)+O(1)")
    print("      (Tối ưu dần dần cả time và space)")
    print("   2. The key: always process the SHORTER side")
    print("      (Luôn xử lý bên THẤP HƠN)")
    print("   3. Two Pointers saves O(n) space vs Prefix Max")
    print("      (Two Pointers tiết kiệm O(n) bộ nhớ)")
