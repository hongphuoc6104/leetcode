"""
=============================================================
 Example 2: Nested Loops — Two Sum Brute Force
=============================================================

Problem: Find two numbers in an array that add up to a target.
         (Tìm 2 số trong mảng cộng lại bằng target.)

Variant: Nested Loops — Brute Force Variant 2
Time:    O(n²) — check every pair
Space:   O(1) — no extra data structures

How it works (Cách hoạt động):
  Step 1: Pick the first element with index i (Chọn phần tử thứ nhất i)
  Step 2: Pick the second element with index j > i (Chọn phần tử thứ hai j > i)
  Step 3: Check if arr[i] + arr[j] == target (Kiểm tra tổng = target?)
  Step 4: If yes → return [i, j]. If no → try next pair. (Đúng → trả về. Sai → thử cặp tiếp)
"""


def two_sum_brute(nums, target):
    """
    Find two indices whose values add up to target.
    (Tìm 2 index mà giá trị cộng lại bằng target.)

    Visualize: we check the upper triangle of the pair matrix.
    (Hình dung: ta kiểm tra tam giác trên của ma trận cặp.)

    Time: O(n²) | Space: O(1)
    """
    n = len(nums)
    pair_count = 0  # Count total pairs checked (Đếm tổng cặp đã kiểm tra)

    for i in range(n):
        for j in range(i + 1, n):
            pair_count += 1
            current_sum = nums[i] + nums[j]
            print(f"  Pair #{pair_count}: nums[{i}]={nums[i]} + nums[{j}]={nums[j]} = {current_sum}", end="")

            if current_sum == target:
                print(f" ✅ MATCH! Return [{i}, {j}]")
                print(f"  (Total pairs checked: {pair_count})")
                return [i, j]
            else:
                print(" ✗")

    print(f"  ❌ No pair found after checking {pair_count} pairs")
    return []


def three_sum_brute(nums, target):
    """
    Find three indices whose values add up to target.
    (Tìm 3 index mà giá trị cộng lại bằng target.)

    Time: O(n³) | Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    return [i, j, k]
    return []


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Two Sum — nums=[2, 7, 11, 15], target=9")
    print("=" * 60)
    result = two_sum_brute([2, 7, 11, 15], 9)
    assert result == [0, 1], f"Expected [0, 1], got {result}"
    print()

    print("=" * 60)
    print("TEST 2: Two Sum — nums=[3, 2, 4], target=6")
    print("=" * 60)
    result = two_sum_brute([3, 2, 4], 6)
    assert result == [1, 2], f"Expected [1, 2], got {result}"
    print()

    print("=" * 60)
    print("TEST 3: Three Sum — nums=[1, 2, 3, 4, 5], target=9")
    print("=" * 60)
    result = three_sum_brute([1, 2, 3, 4, 5], 9)
    print(f"  Result: {result}")
    assert result == [0, 2, 4], f"Expected [0, 2, 4], got {result}"
    print(f"  ✅ nums[{result[0]}] + nums[{result[1]}] + nums[{result[2]}] = "
          f"{1} + {3} + {5} = 9")
    print()

    # Show pair count analysis (Phân tích số cặp)
    print("=" * 60)
    print("ANALYSIS: How many pairs for different n?")
    print("(Phân tích: Bao nhiêu cặp cho các giá trị n khác nhau?)")
    print("=" * 60)
    for n in [5, 10, 100, 1000]:
        pairs = n * (n - 1) // 2
        print(f"  n = {n:>5} → pairs = {pairs:>10,} → {'✅ Fast' if pairs <= 10**8 else '❌ TLE'}")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. This is O(n²). Can you solve Two Sum in O(n)?")
    print("      (Đây là O(n²). Bạn giải Two Sum trong O(n) được không?)")
    print("      Hint: What data structure gives O(1) lookup?")
    print("      (Gợi ý: Cấu trúc dữ liệu nào cho tra cứu O(1)?)")
    print("   2. Why do we start j at i+1, not at 0?")
    print("      (Tại sao j bắt đầu từ i+1, không phải 0?)")
