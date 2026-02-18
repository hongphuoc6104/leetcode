"""
=============================================================
 Example 1: Basic Binary Search (Tìm kiếm nhị phân cơ bản)
=============================================================

Demonstrates:
  - Linear Search O(n) vs Binary Search O(log n)
  - Step-by-step trace of BS

Time:  O(log n)
Space: O(1)
"""


def linear_search(arr, target):
    """O(n) — check every element."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr, target):
    """O(log n) — halve search space each step."""
    left, right = 0, len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, steps


def binary_search_trace(arr, target):
    """BS with step-by-step trace."""
    left, right = 0, len(arr) - 1
    step = 0

    print(f"  Array: {arr}")
    print(f"  Target: {target}")
    print()

    while left <= right:
        step += 1
        mid = left + (right - left) // 2
        cmp = ("==" if arr[mid] == target else
               "<" if arr[mid] < target else ">")
        action = ("FOUND!" if arr[mid] == target else
                  "go RIGHT" if arr[mid] < target else
                  "go LEFT")

        print(f"  Step {step}: left={left} mid={mid} right={right} "
              f"→ arr[{mid}]={arr[mid]} {cmp} {target} → {action}")

        if arr[mid] == target:
            return mid, step
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"  Step {step}: left={left} > right={right} → NOT FOUND")
    return -1, step


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    import math

    print("=" * 60)
    print("TEST 1: Basic BS — Step Trace")
    print("=" * 60)
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    idx, steps = binary_search_trace(arr, 13)
    assert idx == 6
    print(f"\n  Found at index {idx} in {steps} steps ✅")
    print(f"  Linear would need up to {len(arr)} steps")
    print()

    print("=" * 60)
    print("TEST 2: Target Not Found")
    print("=" * 60)
    idx, steps = binary_search_trace(arr, 8)
    assert idx == -1
    print(f"\n  Not found, used {steps} steps ✅")
    print()

    print("=" * 60)
    print("TEST 3: Linear O(n) vs BS O(log n)")
    print("=" * 60)
    import time

    for n in [1000, 10000, 100000, 1000000]:
        arr = list(range(n))
        target = n - 1  # Worst case for linear

        start = time.perf_counter()
        for _ in range(100):
            linear_search(arr, target)
        t_lin = (time.perf_counter() - start) / 100

        start = time.perf_counter()
        for _ in range(100):
            binary_search(arr, target)
        t_bs = (time.perf_counter() - start) / 100

        _, bs_steps = binary_search(arr, target)
        speedup = t_lin / t_bs if t_bs > 0 else float('inf')
        print(f"  n={n:>7}: Linear={t_lin*1000:>8.3f}ms | "
              f"BS={t_bs*1000:>6.4f}ms ({bs_steps} steps) | "
              f"{speedup:>.0f}x")

    print(f"\n  log₂(10⁶) = {math.log2(1000000):.1f} steps max")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it:")
    print("   1. What if the array is NOT sorted?")
    print("   2. Why use mid = left + (right-left)//2?")
    print("   3. What if there are duplicate targets?")
