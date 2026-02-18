"""
=============================================================
 Example 2: Variable Size Window (Cửa sổ kích thước biến đổi)
=============================================================

Demonstrates Variable Window patterns:
  - Min size subarray with sum >= target (shortest)
  - Longest substring with at most k distinct chars (longest)

Time:  O(n) — each element added/removed at most once
Space: O(k) — window state
"""


def min_subarray_sum(nums, target):
    """
    Find shortest subarray with sum >= target.
    (Tìm subarray ngắn nhất có tổng >= target.)

    Strategy: expand right, shrink left while valid.
    """
    left = 0
    current_sum = 0
    min_len = float('inf')
    best_window = []

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                best_window = nums[left:right + 1]
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0, best_window


def min_subarray_trace(nums, target):
    """Min subarray with step trace."""
    left = 0
    current_sum = 0
    min_len = float('inf')

    print(f"  nums={nums}, target={target}")
    print(f"  {'R':>3} | {'add':>4} | {'sum':>5} | "
          f"{'action':>15} | {'window':>15} | {'min_len':>7}")
    print(f"  {'-'*3}-+-{'-'*4}-+-{'-'*5}-+-"
          f"{'-'*15}-+-{'-'*15}-+-{'-'*7}")

    for right in range(len(nums)):
        current_sum += nums[right]

        if current_sum < target:
            print(f"  {right:>3} | {nums[right]:>4} | "
                  f"{current_sum:>5} | {'expand':>15} | "
                  f"{nums[left:right+1]!s:>15} | "
                  f"{min_len if min_len != float('inf') else '∞':>7}")
        else:
            while current_sum >= target:
                window = nums[left:right + 1]
                wlen = right - left + 1
                if wlen < min_len:
                    min_len = wlen
                print(f"  {right:>3} | {nums[right]:>4} | "
                      f"{current_sum:>5} | {'shrink L=' + str(left):>15} | "
                      f"{window!s:>15} | {min_len:>7}")
                current_sum -= nums[left]
                left += 1

    return min_len if min_len != float('inf') else 0


def longest_k_distinct(s, k):
    """
    Longest substring with at most k distinct characters.
    (Chuỗi con dài nhất với tối đa k ký tự khác nhau.)
    """
    left = 0
    freq = {}
    max_len = 0
    best_start = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            best_start = left

    return max_len, s[best_start:best_start + max_len]


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 65)
    print("TEST 1: Min Subarray Sum — Trace")
    print("=" * 65)
    result = min_subarray_trace([2, 3, 1, 2, 4, 3], 7)
    assert result == 2
    print(f"\n  Shortest length = {result} ✅")
    print()

    print("=" * 65)
    print("TEST 2: Min Subarray Sum — More Cases")
    print("=" * 65)
    cases = [
        ([2, 3, 1, 2, 4, 3], 7, 2),
        ([1, 4, 4], 4, 1),
        ([1, 1, 1, 1, 1], 100, 0),
    ]
    for nums, target, expected in cases:
        result, window = min_subarray_sum(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"  nums={nums}, target={target} → "
              f"len={result} {window} {status}")
    print()

    print("=" * 65)
    print("TEST 3: Longest with K Distinct Characters")
    print("=" * 65)
    cases = [
        ("eceba", 2, 3),
        ("aa", 1, 2),
        ("abcabcabc", 2, 2),
    ]
    for s, k, expected in cases:
        length, substr = longest_k_distinct(s, k)
        status = "✅" if length == expected else "❌"
        print(f'  s="{s}", k={k} → '
              f'len={length} "{substr}" {status}')
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it:")
    print("   1. In min_subarray, why shrink while VALID?")
    print("      (Tại sao thu hẹp khi CÒN hợp lệ?)")
    print("   2. In longest_k_distinct, why shrink while INVALID?")
    print("   3. Could you solve min_subarray with negative numbers?")
