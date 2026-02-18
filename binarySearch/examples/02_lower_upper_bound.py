"""
=============================================================
 Example 2: Lower & Upper Bound (Biên dưới & trên)
=============================================================

Demonstrates:
  - lower_bound: first index where arr[i] >= target
  - upper_bound: first index where arr[i] > target
  - Find first and last occurrence
  - Comparison with Python's bisect module

Time:  O(log n)
Space: O(1)
"""
import bisect


def lower_bound(arr, target):
    """First index where arr[i] >= target."""
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arr, target):
    """First index where arr[i] > target."""
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def find_first_last(arr, target):
    """Find first and last index of target."""
    first = lower_bound(arr, target)
    if first == len(arr) or arr[first] != target:
        return [-1, -1]
    last = upper_bound(arr, target) - 1
    return [first, last]


def lower_bound_trace(arr, target):
    """Lower bound with trace."""
    left, right = 0, len(arr)
    step = 0

    print(f"  Array: {arr}, target={target}")
    while left < right:
        step += 1
        mid = left + (right - left) // 2
        cmp = "<" if arr[mid] < target else ">="
        action = "left=mid+1" if arr[mid] < target else "right=mid"
        print(f"    Step {step}: L={left} M={mid} R={right} "
              f"→ arr[{mid}]={arr[mid]} {cmp} {target} → {action}")
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    print(f"    Result: index {left}")
    return left


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Lower Bound Trace")
    print("=" * 60)
    arr = [1, 3, 5, 7, 7, 7, 9, 11]
    result = lower_bound_trace(arr, 7)
    assert result == 3
    print(f"  First index >= 7: {result} ✅")
    print()

    result = lower_bound_trace(arr, 6)
    assert result == 3
    print(f"  First index >= 6: {result} (no 6, points to 7) ✅")
    print()

    print("=" * 60)
    print("TEST 2: Find First and Last")
    print("=" * 60)
    cases = [
        ([1, 3, 5, 7, 7, 7, 9], 7, [3, 5]),
        ([1, 3, 5, 7, 7, 7, 9], 3, [1, 1]),
        ([1, 3, 5, 7, 7, 7, 9], 10, [-1, -1]),
        ([1], 1, [0, 0]),
    ]
    for arr, target, expected in cases:
        result = find_first_last(arr, target)
        status = "✅" if result == expected else "❌"
        print(f"  arr={arr}, target={target} → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Verify Against Python bisect")
    print("=" * 60)
    arr = [1, 3, 5, 7, 7, 7, 9, 11, 13]
    for target in [0, 1, 5, 7, 10, 15]:
        lb = lower_bound(arr, target)
        ub = upper_bound(arr, target)
        py_lb = bisect.bisect_left(arr, target)
        py_ub = bisect.bisect_right(arr, target)
        match = (lb == py_lb and ub == py_ub)
        status = "✅" if match else "❌"
        print(f"  target={target:>2}: "
              f"lower={lb} (bisect_left={py_lb}) "
              f"upper={ub} (bisect_right={py_ub}) {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it:")
    print("   1. How to count occurrences using bounds?")
    print("      Hint: upper_bound - lower_bound")
    print("   2. Why does lower_bound use right=len(arr)?")
