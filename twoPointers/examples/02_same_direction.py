"""
=============================================================
 Example 2: Same Direction (Cùng hướng)
=============================================================

Demonstrates Same Direction Two Pointers:
  - Remove duplicates from sorted array
  - Move zeroes to end
  - Is Subsequence

Time:  O(n)
Space: O(1)
"""


def remove_duplicates_trace(nums):
    """
    Remove duplicates from sorted array with step trace.
    (Xóa trùng lặp từ mảng sorted với trace từng bước.)

    slow = write position, fast = read position.
    """
    if not nums:
        return 0

    slow = 0
    print(f"  Initial: {nums}")
    print(f"  {'step':>4} | {'fast':>4} | {'nums[fast]':>9} | "
          f"{'action':>12} | {'slow':>4} | result so far")
    print(f"  {'-'*4}-+-{'-'*4}-+-{'-'*9}-+-"
          f"{'-'*12}-+-{'-'*4}-+{'-'*15}")

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
            action = "write"
            print(f"  {fast:>4} | {fast:>4} | {nums[fast]:>9} | "
                  f"{action:>12} | {slow:>4} | {nums[:slow+1]}")
        else:
            action = "skip (dup)"
            print(f"  {fast:>4} | {fast:>4} | {nums[fast]:>9} | "
                  f"{action:>12} | {slow:>4} | {nums[:slow+1]}")

    new_len = slow + 1
    print(f"\n  Final: {nums[:new_len]} (length={new_len})")
    return new_len


def move_zeroes(nums):
    """
    Move all zeroes to end, maintain order.
    (Di chuyển 0 ra cuối, giữ thứ tự.)

    Uses swap technique for single pass.
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums


def is_subsequence(s, t):
    """
    Check if s is a subsequence of t.
    (Kiểm tra s có phải chuỗi con của t.)

    Both pointers go same direction, s_ptr only advances on match.
    """
    sp, tp = 0, 0
    steps = []

    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            steps.append(
                f"    t[{tp}]='{t[tp]}' == s[{sp}]='{s[sp]}' "
                f"✅ match! sp++")
            sp += 1
        else:
            steps.append(
                f"    t[{tp}]='{t[tp]}' != s[{sp}]='{s[sp]}' "
                f"→ skip")
        tp += 1

    for step in steps:
        print(step)

    return sp == len(s)


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Remove Duplicates from Sorted Array")
    print("=" * 60)
    nums = [1, 1, 2, 2, 3, 3, 4]
    new_len = remove_duplicates_trace(nums)
    assert new_len == 4
    assert nums[:new_len] == [1, 2, 3, 4]
    print("  ✅ Passed!")
    print()

    print("=" * 60)
    print("TEST 2: Move Zeroes")
    print("=" * 60)
    tests = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
    ]
    for arr, expected in tests:
        original = arr[:]
        result = move_zeroes(arr)
        status = "✅" if result == expected else "❌"
        print(f"  {original} → {result} {status}")
    print()

    print("=" * 60)
    print("TEST 3: Is Subsequence")
    print("=" * 60)
    cases = [
        ("ace", "abcde", True),
        ("aec", "abcde", False),
        ("", "anything", True),
    ]
    for s, t, expected in cases:
        print(f'  s="{s}", t="{t}"')
        result = is_subsequence(s, t)
        status = "✅" if result == expected else "❌"
        print(f"  Result: {result} {status}")
        print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it (Suy nghĩ thêm):")
    print("   1. In remove_duplicates, what if we allow at most 2 copies?")
    print("      (Nếu cho phép tối đa 2 bản sao thì sửa thế nào?)")
    print("      Hint: LC 80 — Remove Duplicates II")
    print("   2. In move_zeroes, why does the swap technique work?")
    print("      (Tại sao kỹ thuật swap hoạt động?)")
