"""
=============================================================
 Example 4: Subset Search using Bitmask (Tìm kiếm tập con)
=============================================================

Problem: Generate all subsets of a list, and find subsets
         whose sum equals a target.
         (Sinh mọi tập con, tìm tập con có tổng bằng target.)

Variant: Subset/Combination Search — Brute Force Variant 4
Time:    O(2ⁿ × n) — 2ⁿ subsets, each needs O(n) to process
Space:   O(n) — for storing current subset

How it works — Bitmask (Cách hoạt động — Mặt nạ bit):
  Each element has 2 choices: INCLUDE (1) or EXCLUDE (0).
  (Mỗi phần tử có 2 lựa chọn: LẤY (1) hoặc BỎ (0).)
  
  A number from 0 to 2ⁿ-1 represents one subset.
  (Một số từ 0 đến 2ⁿ-1 đại diện cho một tập con.)
  
  Example: nums = [a, b, c], mask = 5 = 101₂ → {a, c}
"""


def generate_all_subsets(nums, verbose=True):
    """
    Generate all 2ⁿ subsets using bitmask enumeration.
    (Sinh mọi 2ⁿ tập con bằng duyệt mặt nạ bit.)

    Time: O(2ⁿ × n) | Space: O(2ⁿ × n) for storing all subsets
    """
    n = len(nums)
    total = 1 << n  # 2ⁿ (2 mũ n)
    all_subsets = []

    if verbose:
        print(f"  n = {n}, total subsets = 2^{n} = {total}")
        print(f"  {'Mask':>6} | {'Binary':>{n+2}} | Subset")
        print(f"  {'-'*6}-+-{'-'*(n+2)}-+-{'-'*20}")

    for mask in range(total):
        subset = []
        for i in range(n):
            if mask & (1 << i):  # Bit i is set → include nums[i]
                subset.append(nums[i])

        all_subsets.append(subset)

        if verbose:
            binary = format(mask, f'0{n}b')
            print(f"  {mask:>6} | {binary:>{n+2}} | {subset}")

    return all_subsets


def subset_sum_brute(nums, target):
    """
    Find ALL subsets whose sum equals target.
    (Tìm TẤT CẢ tập con có tổng bằng target.)

    This is a classic problem where BF works for small n.
    (Đây là bài kinh điển mà BF phù hợp khi n nhỏ.)

    Time: O(2ⁿ × n) | Space: O(n)
    """
    n = len(nums)
    results = []
    subsets_checked = 0

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])

        subsets_checked += 1

        if sum(subset) == target:
            results.append(subset)

    return results, subsets_checked


def subset_sum_recursive(nums, target):
    """
    Find subsets summing to target using recursive backtracking.
    (Tìm tập con có tổng = target bằng đệ quy quay lui.)

    Time: O(2ⁿ) | Space: O(n)
    """
    results = []

    def backtrack(index, current, current_sum):
        if current_sum == target:
            results.append(current[:])
            # Don't return — there might be subsets with 0s that also work
            # (Không return — có thể có tập con chứa 0 cũng thỏa)

        if index == len(nums):
            return

        # Option 1: Include nums[index] (Lấy)
        current.append(nums[index])
        backtrack(index + 1, current, current_sum + nums[index])
        current.pop()  # Backtrack (Quay lui)

        # Option 2: Exclude nums[index] (Bỏ)
        backtrack(index + 1, current, current_sum)

    backtrack(0, [], 0)
    return results


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: All subsets of ['a', 'b', 'c']")
    print("Bitmask Table (Bảng mặt nạ bit):")
    print("=" * 60)
    subsets = generate_all_subsets(['a', 'b', 'c'])
    assert len(subsets) == 8, f"Expected 8 subsets, got {len(subsets)}"
    print(f"\n  Total subsets: {len(subsets)} ✅")
    print()

    print("=" * 60)
    print("TEST 2: Subset Sum — nums=[3, 1, 4, 2], target=5")
    print("=" * 60)
    results, checked = subset_sum_brute([3, 1, 4, 2], 5)
    print(f"  Subsets checked: {checked}")
    print(f"  Subsets summing to 5:")
    for s in results:
        print(f"    {s} → sum = {sum(s)} ✅")
    assert len(results) > 0
    print()

    print("=" * 60)
    print("TEST 3: Subset Sum Recursive — same problem")
    print("=" * 60)
    results_rec = subset_sum_recursive([3, 1, 4, 2], 5)
    print(f"  Results: {results_rec}")
    print(f"  Count: {len(results_rec)} ✅")
    print()

    # Growth analysis (Phân tích tốc độ tăng)
    print("=" * 60)
    print("ANALYSIS: Exponential growth of 2ⁿ")
    print("(Phân tích: Tốc độ tăng mũ 2 của 2ⁿ)")
    print("=" * 60)
    for n in range(1, 31):
        count = 2 ** n
        feasible = "✅" if count <= 10**7 else ("⚠️" if count <= 10**8 else "❌")
        if n <= 10 or n % 5 == 0 or n >= 25:
            print(f"  n = {n:>2} → 2ⁿ = {count:>15,} {feasible}")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. What is `1 << n` in Python? Why not use `2 ** n`?")
    print("      (1 << n là gì? Tại sao không dùng 2 ** n?)")
    print("   2. For Subset Sum with n=20, how many subsets to check?")
    print("      (Với n=20, kiểm tra bao nhiêu tập con?)")
    print("   3. How could Dynamic Programming solve this faster?")
    print("      (DP giải nhanh hơn bằng cách nào?)")
