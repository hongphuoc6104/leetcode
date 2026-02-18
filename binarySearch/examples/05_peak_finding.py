"""
=============================================================
 Example 5: Peak Finding (Tìm đỉnh)
=============================================================

Demonstrates:
  - Find Peak Element (LC 162)
  - Sqrt(x) using BS (LC 69)

Peak Finding works on UNSORTED arrays!
The key: compare mid vs mid+1 to determine direction.

Time:  O(log n)
Space: O(1)
"""


def find_peak_linear(nums):
    """BF: O(n) — scan for peak."""
    for i in range(len(nums)):
        left_ok = (i == 0 or nums[i] > nums[i - 1])
        right_ok = (i == len(nums) - 1 or nums[i] > nums[i + 1])
        if left_ok and right_ok:
            return i
    return 0


def find_peak_bs(nums):
    """
    BS: O(log n).
    If nums[mid] < nums[mid+1] → ascending → peak on RIGHT
    If nums[mid] > nums[mid+1] → descending → peak on LEFT/HERE
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1     # Peak on right
        else:
            right = mid        # Peak on left or at mid

    return left


def find_peak_trace(nums):
    """Peak finding with trace."""
    left, right = 0, len(nums) - 1
    step = 0

    print(f"  Array: {nums}")

    while left < right:
        step += 1
        mid = left + (right - left) // 2
        direction = "↗ ascending" if nums[mid] < nums[mid + 1] else "↘ descending"
        action = "L=mid+1" if nums[mid] < nums[mid + 1] else "R=mid"

        print(f"    Step {step}: L={left} M={mid} R={right} "
              f"→ arr[{mid}]={nums[mid]} vs arr[{mid + 1}]={nums[mid + 1]} "
              f"{direction} → {action}")

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    print(f"    Peak at index {left}, value={nums[left]}")
    return left


def sqrt_bs(x):
    """
    Sqrt(x) using BS on Answer (LC 69).
    Find largest n where n² <= x.
    """
    if x < 2:
        return x

    lo, hi = 1, x // 2

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq == x:
            return mid
        elif sq < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return hi  # hi is largest where hi² <= x


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Find Peak — Trace")
    print("=" * 60)
    nums = [1, 3, 5, 7, 6, 4, 2]
    result = find_peak_trace(nums)
    assert nums[result] == 7
    print(f"  ✅ Peak at index {result}, value {nums[result]}")
    print()

    nums = [1, 2, 1, 3, 5, 6, 4]
    result = find_peak_trace(nums)
    # Any peak is valid
    assert result in [1, 5]
    print(f"  ✅ Peak at index {result}, value {nums[result]}")
    print()

    print("=" * 60)
    print("TEST 2: Find Peak — More Cases")
    print("=" * 60)
    cases = [
        [1, 2, 3, 1],
        [1],
        [1, 2],
        [2, 1],
        [1, 3, 20, 4, 1, 0],
    ]
    for nums in cases:
        peak_lin = find_peak_linear(nums)
        peak_bs = find_peak_bs(nums)
        # Both should find A peak (not necessarily same one)
        is_peak_lin = True
        is_peak_bs = True
        if peak_lin > 0:
            is_peak_lin &= nums[peak_lin] > nums[peak_lin - 1]
        if peak_lin < len(nums) - 1:
            is_peak_lin &= nums[peak_lin] > nums[peak_lin + 1]
        if peak_bs > 0:
            is_peak_bs &= nums[peak_bs] > nums[peak_bs - 1]
        if peak_bs < len(nums) - 1:
            is_peak_bs &= nums[peak_bs] > nums[peak_bs + 1]

        status = "✅" if is_peak_lin and is_peak_bs else "❌"
        print(f"  {nums} → linear:{peak_lin} "
              f"bs:{peak_bs} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Sqrt(x) using BS")
    print("=" * 60)
    cases = [
        (0, 0), (1, 1), (4, 2), (8, 2),
        (16, 4), (25, 5), (26, 5), (100, 10),
    ]
    for x, expected in cases:
        result = sqrt_bs(x)
        status = "✅" if result == expected else "❌"
        print(f"  sqrt({x:>3}) = {result} {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Peak Finding works on UNSORTED arrays!")
    print("   2. Just compare mid vs mid+1 → O(log n)")
    print("   3. Sqrt(x) = BS on Answer: find largest n² ≤ x")
