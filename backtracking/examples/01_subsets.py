"""
=============================================================
 Example 1: Subsets (LC 78) & Subsets II (LC 90)
=============================================================

Generate all subsets. With duplicates: sort + skip.
Time:  O(2^n) — each element included or excluded
Space: O(n) recursion depth
"""


def subsets(nums):
    """All subsets of distinct nums (LC 78)."""
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result


def subsets_with_dup(nums):
    """All subsets with duplicates (LC 90)."""
    nums.sort()
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # Skip duplicate at same level!
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Subsets")
    print("=" * 60)
    result = subsets([1, 2, 3])
    assert len(result) == 8  # 2^3 = 8
    print(f"  [1,2,3] → {len(result)} subsets ✅")
    for s in result:
        print(f"    {s}")
    print()

    print("=" * 60)
    print("TEST 2: Subsets with Duplicates")
    print("=" * 60)
    result = subsets_with_dup([1, 2, 2])
    assert len(result) == 6  # Not 8!
    print(f"  [1,2,2] → {len(result)} subsets ✅")
    for s in result:
        print(f"    {s}")
    print()

    print("=" * 60)
    print("TEST 3: Empty & Single")
    print("=" * 60)
    assert subsets([]) == [[]]
    print("  [] → [[]] ✅")
    assert subsets([1]) == [[], [1]]
    print("  [1] → [[], [1]] ✅")
    print()

    print("✅ All tests passed!")
