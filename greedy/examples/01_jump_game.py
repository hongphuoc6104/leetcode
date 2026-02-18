"""
=============================================================
 Example 1: Jump Game (LC 55) & Jump Game II (LC 45)
=============================================================

Greedy strategy:
1. Jump I: Track 'farthest' we can reach.
2. Jump II: Track 'end' of current jump range. Increment jumps when we pass it.

Time:  O(n)
Space: O(1)
"""


def can_jump(nums):
    """Can we reach the last index? (LC 55)"""
    farthest = 0
    for i, n in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + n)
    return True


def jump_game_ii(nums):
    """Minimum jumps to reach last index (LC 45)."""
    jumps = 0
    current_end = 0
    farthest = 0
    # Don't need to jump from the last element
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break
    return jumps


if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Can Jump (LC 55)")
    print("=" * 60)
    cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ]
    for nums, expected in cases:
        result = can_jump(nums)
        status = "✅" if result == expected else "❌"
        print(f"  {nums} → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 2: Min Jumps (LC 45)")
    print("=" * 60)
    result = jump_game_ii([2, 3, 1, 1, 4])
    assert result == 2  # 0->1->4
    print(f"  [2,3,1,1,4] → {result} jumps ✅")

    result = jump_game_ii([2, 3, 0, 1, 4])
    assert result == 2
    print(f"  [2,3,0,1,4] → {result} jumps ✅")
    print()

    print("✅ All tests passed!")
