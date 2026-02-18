"""
=============================================================
 Example 3: Longest Substring Without Repeating (LC 3)
=============================================================

The CLASSIC Sliding Window problem.
(Bài Sliding Window KINH ĐIỂN.)

BF: O(n³) — check every substring for uniqueness
SW: O(n)  — maintain set of chars in window

Time:  O(n)
Space: O(min(n, alphabet_size))
"""


def longest_brute(s):
    """BF: O(n³) — try every substring, check unique."""
    n = len(s)
    max_len = 0

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if len(set(substring)) == len(substring):
                max_len = max(max_len, j - i + 1)
            else:
                break

    return max_len


def longest_sliding(s):
    """
    Sliding Window: O(n).
    Maintain a set of characters in current window.
    When duplicate found, shrink from left.
    """
    char_set = set()
    left = 0
    max_len = 0
    best_start = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        if right - left + 1 > max_len:
            max_len = right - left + 1
            best_start = left

    return max_len, s[best_start:best_start + max_len]


def longest_sliding_trace(s):
    """Sliding Window with step trace."""
    char_set = set()
    left = 0
    max_len = 0

    print(f'  s = "{s}"')
    print()

    for right in range(len(s)):
        shrinks = []
        while s[right] in char_set:
            shrinks.append(s[left])
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        wlen = right - left + 1
        max_len = max(max_len, wlen)

        shrink_info = (f" (removed: {shrinks})"
                       if shrinks else "")
        is_max = " 🏆" if wlen == max_len else ""
        print(f'  R={right} "{s[right]}": '
              f'window="{s[left:right+1]}" '
              f'len={wlen}{shrink_info}{is_max}')

    return max_len


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Step-by-Step Trace")
    print("=" * 60)
    result = longest_sliding_trace("abcabcbb")
    assert result == 3
    print(f'\n  Longest = {result} ("abc") ✅')
    print()

    print("=" * 60)
    print("TEST 2: More Test Cases")
    print("=" * 60)
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdef", 6),
        ("dvdf", 3),
    ]
    for s, expected in cases:
        length, substr = longest_sliding(s)
        status = "✅" if length == expected else "❌"
        print(f'  "{s}" → len={length} '
              f'"{substr}" {status}')
    print()

    print("=" * 60)
    print("TEST 3: BF O(n³) vs SW O(n) Performance")
    print("=" * 60)
    import time
    import random
    import string

    for n in [100, 500, 1000, 5000]:
        s = ''.join(random.choices(string.ascii_lowercase, k=n))

        start = time.perf_counter()
        bf = longest_brute(s)
        bf_time = time.perf_counter() - start

        start = time.perf_counter()
        sw, _ = longest_sliding(s)
        sw_time = time.perf_counter() - start

        assert bf == sw
        speedup = bf_time / sw_time if sw_time > 0 else float('inf')
        print(f"  n={n:>5}: BF={bf_time*1000:>8.2f}ms | "
              f"SW={sw_time*1000:>6.3f}ms | "
              f"{speedup:>.1f}x")
    print()

    print("✅ All tests passed!")
    print()
    print("🤔 Think about it:")
    print("   1. Could you use a DICT instead of SET to jump left?")
    print("      (Dùng DICT thay SET để nhảy left nhanh hơn?)")
    print("   2. What is the max possible answer for lowercase-only?")
    print("      (Đáp án tối đa cho chuỗi chỉ chữ thường?)")
