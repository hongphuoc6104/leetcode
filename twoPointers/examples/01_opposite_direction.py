"""
=============================================================
 Example 1: Opposite Direction (Đối hướng)
=============================================================

Demonstrates Opposite Direction Two Pointers:
  - Two Sum on sorted array
  - Reverse array
  - Pair with closest sum

Time:  O(n)
Space: O(1)
"""


def two_sum_sorted(nums, target):
    """
    Find pair summing to target in SORTED array.
    (Tìm cặp có tổng = target trong mảng ĐÃ SORTED.)

    Key: if sum < target → left++ (need bigger)
         if sum > target → right-- (need smaller)
    """
    left, right = 0, len(nums) - 1
    steps = 0

    print(f"  Target = {target}")
    while left < right:
        steps += 1
        current = nums[left] + nums[right]
        status = "==" if current == target else (
            "<" if current < target else ">")
        action = ("FOUND!" if current == target else
                  "left++" if current < target else "right--")
        print(f"    Step {steps}: nums[{left}]={nums[left]} + "
              f"nums[{right}]={nums[right]} = {current} "
              f"{status} {target} → {action}")

        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return []


def reverse_in_place(arr):
    """
    Reverse array using opposite-direction pointers.
    (Đảo mảng bằng con trỏ đối hướng.)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def closest_pair_sum(nums, target):
    """
    Find pair with sum CLOSEST to target.
    (Tìm cặp có tổng GẦN NHẤT target.)
    """
    left, right = 0, len(nums) - 1
    best_diff = float('inf')
    best_pair = []

    while left < right:
        current = nums[left] + nums[right]
        diff = abs(current - target)

        if diff < best_diff:
            best_diff = diff
            best_pair = [nums[left], nums[right]]

        if current < target:
            left += 1
        elif current > target:
            right -= 1
        else:
            break  # Exact match! (Khớp chính xác!)

    return best_pair, best_diff


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Two Sum on Sorted Array")
    print("=" * 60)
    nums = [1, 3, 5, 7, 9, 11, 13]
    result = two_sum_sorted(nums, 12)
    assert result == [0, 5], f"Expected [0, 5], got {result}"
    print(f"  Result: indices {result} → "
          f"{nums[result[0]]}+{nums[result[1]]}=12 ✅")
    print()

    print("=" * 60)
    print("TEST 2: Two Sum — target not found")
    print("=" * 60)
    result = two_sum_sorted(nums, 100)
    assert result == []
    print(f"  Result: {result} (not found) ✅")
    print()

    print("=" * 60)
    print("TEST 3: Reverse Array In-Place")
    print("=" * 60)
    arr = [1, 2, 3, 4, 5]
    print(f"  Before: {arr}")
    reverse_in_place(arr)
    print(f"  After:  {arr}")
    assert arr == [5, 4, 3, 2, 1]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 4: Closest Pair Sum")
    print("=" * 60)
    nums = [1, 3, 5, 7, 9]
    pair, diff = closest_pair_sum(nums, 11)
    print(f"  nums={nums}, target=11")
    print(f"  Closest pair: {pair}, diff={diff}")
    assert sum(pair) in [10, 12]
    print("  ✅ Passed!")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. What happens if there are multiple valid pairs?")
    print("      (Nếu có nhiều cặp hợp lệ thì sao?)")
    print("   2. Can you modify two_sum_sorted to find ALL pairs?")
    print("      (Có thể sửa để tìm TẤT CẢ cặp không?)")
