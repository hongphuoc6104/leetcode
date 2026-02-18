"""
=============================================================
 Example 3: Permutation Search (Tìm kiếm hoán vị)
=============================================================

Problem: Generate all permutations of a list.
         (Sinh mọi hoán vị của một danh sách.)

Variant: Permutation Search — Brute Force Variant 3
Time:    O(n!) — factorial growth
Space:   O(n) — recursion stack depth

How it works (Cách hoạt động):
  Step 1: Start with empty path [] (Bắt đầu với đường dẫn rỗng)
  Step 2: For each unused element, add it to path (Với mỗi phần tử chưa dùng, thêm vào)
  Step 3: Recurse until path has n elements (Đệ quy cho đến khi đủ n phần tử)
  Step 4: Backtrack — remove last element, try next (Quay lui — bỏ phần tử cuối, thử tiếp)
"""


def generate_permutations(nums, verbose=True):
    """
    Generate all permutations using backtracking.
    (Sinh mọi hoán vị bằng quay lui.)

    Args:
        nums: list of elements (danh sách phần tử)
        verbose: if True, print decision tree (nếu True, in cây quyết định)

    Time: O(n!) | Space: O(n)
    """
    result = []
    used = [False] * len(nums)
    call_count = [0]  # Track recursive calls (Đếm lệnh gọi đệ quy)

    def backtrack(path, depth=0):
        call_count[0] += 1
        indent = "  " * depth  # Indentation shows tree depth (Thụt lề thể hiện độ sâu)

        if len(path) == len(nums):
            result.append(path[:])  # Save a COPY (Lưu BẢN SAO — important!)
            if verbose:
                print(f"{indent}🎯 Complete permutation: {path}")
            return

        for i in range(len(nums)):
            if used[i]:
                continue  # Skip used elements (Bỏ qua phần tử đã dùng)

            if verbose:
                print(f"{indent}Choose nums[{i}] = {nums[i]}, path = {path + [nums[i]]}")

            # Choose (Chọn)
            used[i] = True
            path.append(nums[i])

            # Explore (Khám phá)
            backtrack(path, depth + 1)

            # Un-choose / Backtrack (Bỏ chọn / Quay lui)
            path.pop()
            used[i] = False

            if verbose:
                print(f"{indent}↩ Backtrack, un-choose {nums[i]}")

    backtrack([])
    return result, call_count[0]


def find_max_sum_permutation(nums):
    """
    Find the permutation whose adjacent-pair sum is maximized.
    (Tìm hoán vị có tổng cặp kề lớn nhất.)

    Example: [1,2,3] → try [1,2,3], [1,3,2], etc.
    Adjacent sum of [a,b,c] = a+b + b+c = a + 2b + c

    This shows a practical USE CASE for permutation search.
    (Đây là USE CASE thực tế cho tìm kiếm hoán vị.)
    """
    from itertools import permutations

    best_perm = None
    best_score = float('-inf')

    for perm in permutations(nums):
        # Calculate sum of adjacent pairs (Tính tổng cặp kề)
        score = sum(perm[i] + perm[i+1] for i in range(len(perm) - 1))
        if score > best_score:
            best_score = score
            best_perm = perm

    return best_perm, best_score


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: All permutations of [1, 2, 3]")
    print("Decision Tree (Cây quyết định):")
    print("=" * 60)
    perms, calls = generate_permutations([1, 2, 3])
    print(f"\n  Total permutations: {len(perms)} (expected: 3! = 6)")
    print(f"  Total recursive calls: {calls}")
    assert len(perms) == 6
    print()

    print("=" * 60)
    print("TEST 2: Permutations of [A, B] (small case)")
    print("=" * 60)
    perms, calls = generate_permutations(['A', 'B'])
    print(f"\n  Total: {len(perms)} permutations (expected: 2! = 2)")
    assert len(perms) == 2
    print()

    print("=" * 60)
    print("TEST 3: Max adjacent sum permutation of [1, 5, 3, 2]")
    print("=" * 60)
    best_perm, best_score = find_max_sum_permutation([1, 5, 3, 2])
    print(f"  Best permutation: {best_perm}")
    print(f"  Best adjacent sum: {best_score}")
    print()

    # Growth analysis (Phân tích tốc độ tăng)
    print("=" * 60)
    print("ANALYSIS: Factorial growth (Tốc độ tăng giai thừa)")
    print("=" * 60)
    import math
    for n in range(1, 16):
        fact = math.factorial(n)
        feasible = "✅" if fact <= 10**8 else ("⚠️" if fact <= 10**9 else "❌")
        print(f"  n = {n:>2} → n! = {fact:>15,} {feasible}")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. Why do we append path[:] instead of path?")
    print("      (Tại sao dùng path[:] thay vì path?)")
    print("      Hint: What happens to path after backtracking?")
    print("   2. For n=12, how long would this take approximately?")
    print("      (Với n=12, chạy mất bao lâu?)")
    print("   3. How could you speed this up if you only need")
    print("      permutations where the sum > some threshold?")
    print("      (Nếu chỉ cần hoán vị có tổng > ngưỡng, tăng tốc thế nào?)")
