"""
=============================================================
 Example 3: Rotated Sorted Array (Mảng sorted bị xoay)
=============================================================

Demonstrates:
  - Search in rotated sorted array (LC 33)
  - Find minimum in rotated sorted array (LC 153)

Key insight: One half is ALWAYS sorted!
(Nhận xét: Một nửa LUÔN sorted!)

Time:  O(log n)
Space: O(1)
"""


def search_rotated(nums, target):
    """Search target in rotated sorted array."""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def search_rotated_trace(nums, target):
    """Search rotated with trace."""
    left, right = 0, len(nums) - 1
    step = 0

    print(f"  Array: {nums}, target={target}")

    while left <= right:
        step += 1
        mid = left + (right - left) // 2

        if nums[mid] == target:
            print(f"    Step {step}: L={left} M={mid} R={right} "
                  f"→ arr[{mid}]={nums[mid]} == {target} FOUND!")
            return mid

        if nums[left] <= nums[mid]:
            sorted_half = "LEFT sorted"
            if nums[left] <= target < nums[mid]:
                print(f"    Step {step}: L={left} M={mid} R={right} "
                      f"→ {sorted_half}, target in left → R=M-1")
                right = mid - 1
            else:
                print(f"    Step {step}: L={left} M={mid} R={right} "
                      f"→ {sorted_half}, target in right → L=M+1")
                left = mid + 1
        else:
            sorted_half = "RIGHT sorted"
            if nums[mid] < target <= nums[right]:
                print(f"    Step {step}: L={left} M={mid} R={right} "
                      f"→ {sorted_half}, target in right → L=M+1")
                left = mid + 1
            else:
                print(f"    Step {step}: L={left} M={mid} R={right} "
                      f"→ {sorted_half}, target in left → R=M-1")
                right = mid - 1

    print(f"    Not found!")
    return -1


def find_min_rotated(nums):
    """
    Find minimum in rotated sorted array (LC 153).
    Compare mid with right to determine which half has min.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1    # Min is in right half
        else:
            right = mid       # Min is in left half or at mid

    return nums[left]


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Search Rotated — Trace")
    print("=" * 60)
    nums = [4, 5, 6, 7, 0, 1, 2]
    result = search_rotated_trace(nums, 0)
    assert result == 4
    print(f"  Found at index {result} ✅")
    print()

    result = search_rotated_trace(nums, 3)
    assert result == -1
    print(f"  Not found ✅")
    print()

    print("=" * 60)
    print("TEST 2: Search Rotated — All Cases")
    print("=" * 60)
    cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 5, 1),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([1, 3], 3, 1),
    ]
    for nums, target, expected in cases:
        result = search_rotated(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"  {nums}, target={target} → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Find Minimum in Rotated")
    print("=" * 60)
    cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([2, 1], 1),
    ]
    for nums, expected in cases:
        result = find_min_rotated(nums)
        status = "✅" if result == expected else "❌"
        print(f"  {nums} → min={result} {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it:")
    print("   1. What if there are DUPLICATES? (LC 154)")
    print("   2. Can you find the ROTATION POINT (pivot)?")
    print("   3. Why compare nums[mid] with nums[right], not nums[left]?")
