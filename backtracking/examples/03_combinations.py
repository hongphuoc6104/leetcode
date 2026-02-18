"""
=============================================================
 Example 3: Combinations & Combination Sum (LC 77, 39, 40)
=============================================================

Choose K from N, or find all combos summing to target.
"""


def combine(n, k):
    """All combinations C(n,k) (LC 77)."""
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        # Pruning: need k-len(path) more, can't go beyond n
        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    backtrack(1, [])
    return result


def combination_sum(candidates, target):
    """Combination Sum (LC 39) — each number reusable."""
    candidates.sort()
    result = []
    def backtrack(start, path, remain):
        if remain == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break  # Pruning!
            path.append(candidates[i])
            backtrack(i, path, remain - candidates[i])  # i, not i+1
            path.pop()
    backtrack(0, [], target)
    return result


def combination_sum2(candidates, target):
    """Combination Sum II (LC 40) — each number used once."""
    candidates.sort()
    result = []
    def backtrack(start, path, remain):
        if remain == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break
            if i > start and candidates[i] == candidates[i-1]:
                continue  # Skip duplicates!
            path.append(candidates[i])
            backtrack(i + 1, path, remain - candidates[i])
            path.pop()
    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Combinations C(4,2)")
    print("=" * 60)
    result = combine(4, 2)
    assert len(result) == 6  # C(4,2) = 6
    print(f"  C(4,2) → {len(result)} combos ✅")
    for c in result:
        print(f"    {c}")
    print()

    print("=" * 60)
    print("TEST 2: Combination Sum (reusable)")
    print("=" * 60)
    result = combination_sum([2, 3, 6, 7], 7)
    expected = [[2, 2, 3], [7]]
    assert result == expected
    print(f"  [2,3,6,7] target=7 → {result} ✅")
    print()

    print("=" * 60)
    print("TEST 3: Combination Sum II (each once)")
    print("=" * 60)
    result = combination_sum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(f"  target=8 → {len(result)} combos ✅")
    for c in result:
        print(f"    {c}")
        assert sum(c) == 8
    print()

    print("✅ All tests passed!")
