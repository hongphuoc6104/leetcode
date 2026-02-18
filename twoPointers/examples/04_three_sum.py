"""
=============================================================
 Example 4: Three Sum (Ba tổng)
=============================================================

Problem: Find all unique triplets that sum to zero.
         (Tìm tất cả bộ ba duy nhất có tổng bằng 0.)

Key idea: Fix one number, use Two Pointers for the remaining two.
          Sort first to enable Two Pointers + skip duplicates.
          (Cố định 1 số, dùng Two Pointers cho 2 số còn lại.)

Time:  O(n²) — n × Two Pointers
Space: O(1) — excluding output
"""


def three_sum_brute(nums):
    """
    Brute Force: try all triplets.
    (Vét cạn: thử tất cả bộ ba.)
    Time: O(n³)
    """
    n = len(nums)
    result = set()
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                count += 1
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)

    return [list(t) for t in result], count


def three_sum_two_pointers(nums):
    """
    Optimized: Sort + Fix one + Two Pointers.
    (Tối ưu: Sort + Cố định 1 + Two Pointers.)
    Time: O(n²)
    """
    nums.sort()
    result = []
    comparisons = 0

    for i in range(len(nums) - 2):
        # Skip duplicate first element (Bỏ qua phần tử đầu trùng)
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Can't sum to 0 if smallest > 0 (Không thể = 0 nếu nhỏ nhất > 0)
        if nums[i] > 0:
            break

        left = i + 1
        right = len(nums) - 1
        target = -nums[i]

        while left < right:
            comparisons += 1
            two_sum = nums[left] + nums[right]

            if two_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates (Bỏ qua trùng lặp)
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1

    return result, comparisons


def three_sum_trace(nums):
    """3Sum with step-by-step trace. (3Sum với trace từng bước.)"""
    nums.sort()
    print(f"  Sorted: {nums}")
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            print(f"\n  i={i}: nums[i]={nums[i]} SKIP (duplicate)")
            continue

        if nums[i] > 0:
            print(f"\n  i={i}: nums[i]={nums[i]} > 0, BREAK")
            break

        left = i + 1
        right = len(nums) - 1
        target = -nums[i]
        print(f"\n  i={i}: fix nums[i]={nums[i]}, "
              f"need two that sum to {target}")

        while left < right:
            s = nums[left] + nums[right]
            print(f"    L={left}({nums[left]}) "
                  f"R={right}({nums[right]}) "
                  f"sum={s}", end="")
            if s == target:
                print(f" ✅ Found! [{nums[i]},{nums[left]},{nums[right]}]")
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < target:
                print(" → L++")
                left += 1
            else:
                print(" → R--")
                right -= 1

    return result


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: 3Sum Step-by-Step Trace")
    print("=" * 60)
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum_trace(nums)
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"\n  Result: {result} ✅")
    print()

    # Compare BF vs Two Pointers
    print("=" * 60)
    print("TEST 2: BF O(n³) vs Two Pointers O(n²)")
    print("=" * 60)
    nums = [-1, 0, 1, 2, -1, -4, 3, -2, 5, -3]
    bf_result, bf_ops = three_sum_brute(nums[:])
    tp_result, tp_ops = three_sum_two_pointers(nums[:])
    print(f"  n = {len(nums)}")
    print(f"  BF:  {len(bf_result)} triplets, "
          f"{bf_ops} comparisons")
    print(f"  TP:  {len(tp_result)} triplets, "
          f"{tp_ops} comparisons")
    print(f"  Speedup: {bf_ops/tp_ops:.1f}x")

    # Verify same results (Kiểm tra cùng kết quả)
    bf_set = {tuple(sorted(t)) for t in bf_result}
    tp_set = {tuple(sorted(t)) for t in tp_result}
    assert bf_set == tp_set
    print("  ✅ Both produce same results!")
    print()

    # Performance comparison
    print("=" * 60)
    print("TEST 3: Performance at Scale")
    print("=" * 60)
    import time
    import random

    for n in [20, 50, 100]:
        nums = [random.randint(-n, n) for _ in range(n)]

        start = time.perf_counter()
        _, bf_ops = three_sum_brute(nums[:])
        bf_time = time.perf_counter() - start

        start = time.perf_counter()
        _, tp_ops = three_sum_two_pointers(nums[:])
        tp_time = time.perf_counter() - start

        speedup = bf_time / tp_time if tp_time > 0 else float('inf')
        print(f"  n={n:>4}: BF={bf_time*1000:>8.2f}ms "
              f"({bf_ops:>7} ops) | "
              f"TP={tp_time*1000:>8.2f}ms "
              f"({tp_ops:>5} ops) | "
              f"{speedup:>.1f}x")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways (Bài học chính):")
    print("   1. Sort first → enables Two Pointers")
    print("      (Sort trước → cho phép dùng Two Pointers)")
    print("   2. Fix one + Two Pointers = O(n²) instead of O(n³)")
    print("   3. Always handle duplicates to avoid duplicate triplets")
    print("      (Luôn xử lý trùng lặp để tránh bộ ba trùng)")
