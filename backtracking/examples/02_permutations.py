"""
=============================================================
 Example 2: Permutations (LC 46) & Permutations II (LC 47)
=============================================================

Generate all orderings. With duplicates: sort + used array.
Time:  O(n!) — n × (n-1) × ... × 1
Space: O(n) recursion depth
"""


def permutations(nums):
    """All permutations of distinct nums (LC 46)."""
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    backtrack([], nums)
    return result


def permutations_with_dup(nums):
    """Permutations with duplicates (LC 47)."""
    nums.sort()
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue  # Skip duplicate!
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Permutations")
    print("=" * 60)
    result = permutations([1, 2, 3])
    assert len(result) == 6  # 3! = 6
    print(f"  [1,2,3] → {len(result)} permutations ✅")
    for p in result:
        print(f"    {p}")
    print()

    print("=" * 60)
    print("TEST 2: Permutations with Duplicates")
    print("=" * 60)
    result = permutations_with_dup([1, 1, 2])
    assert len(result) == 3  # Not 6!
    print(f"  [1,1,2] → {len(result)} permutations ✅")
    for p in result:
        print(f"    {p}")
    print()

    print("✅ All tests passed!")
