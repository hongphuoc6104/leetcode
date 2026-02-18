"""
=============================================================
 Example 5: House Robber (LC 198, LC 213)
=============================================================

Classic 1D DP: can't rob adjacent houses.
dp[i] = max(rob this + dp[i-2], skip + dp[i-1])

Time:  O(n)
Space: O(1)
"""


def rob_basic(nums):
    """House Robber I: linear houses."""
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    a, b = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        a, b = b, max(b, a + nums[i])
    return b


def rob_circular(nums):
    """
    House Robber II (LC 213): houses in a circle.
    Solution: max(rob[0..n-2], rob[1..n-1]).
    """
    if len(nums) <= 2:
        return max(nums) if nums else 0

    def rob_range(start, end):
        a, b = 0, 0
        for i in range(start, end):
            a, b = b, max(b, a + nums[i])
        return b

    return max(rob_range(0, len(nums) - 1),
               rob_range(1, len(nums)))


def rob_trace(nums):
    """House Robber with decision trace."""
    if not nums:
        return 0, []
    if len(nums) == 1:
        return nums[0], [0]

    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    # Backtrack to find which houses were robbed
    robbed = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i - 1]:
            robbed.append(i)
            i -= 2
        else:
            i -= 1

    return dp[-1], robbed[::-1]


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: House Robber I")
    print("=" * 60)
    cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([1], 1),
    ]
    for nums, expected in cases:
        result = rob_basic(nums)
        status = "✅" if result == expected else "❌"
        print(f"  {nums} → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 2: House Robber — Trace")
    print("=" * 60)
    nums = [2, 7, 9, 3, 1]
    total, houses = rob_trace(nums)
    print(f"  Houses: {nums}")
    print(f"  Robbed: indices {houses} "
          f"(values {[nums[i] for i in houses]})")
    print(f"  Total: {total}")
    assert total == 12
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 3: House Robber II (Circular)")
    print("=" * 60)
    cases = [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
        ([0], 0),
    ]
    for nums, expected in cases:
        result = rob_circular(nums)
        status = "✅" if result == expected else "❌"
        print(f"  {nums} → {result} {status}")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. dp[i] = max(skip: dp[i-1], rob: dp[i-2]+nums[i])")
    print("   2. Only need last 2 values → O(1) space")
    print("   3. Circular: split into 2 ranges, take max")
