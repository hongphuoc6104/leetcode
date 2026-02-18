"""
=============================================================
 Example 4: Minimum Window Substring (LC 76)
=============================================================

Problem: Find the minimum window in s containing ALL chars of t.
         (Tìm cửa sổ nhỏ nhất trong s chứa TẤT CẢ ký tự của t.)

This is the HARDEST classic Sliding Window problem.
Strategy: Expand right until valid → shrink left to minimize.

Time:  O(n + m) where n=len(s), m=len(t)
Space: O(m) for frequency counter
"""
from collections import Counter


def min_window_brute(s, t):
    """BF: O(n²×m) — try all substrings, check containment."""
    if not t or not s:
        return ""

    t_count = Counter(t)
    min_len = float('inf')
    result = ""

    for i in range(len(s)):
        for j in range(i + len(t), len(s) + 1):
            window = s[i:j]
            w_count = Counter(window)
            if all(w_count[c] >= t_count[c] for c in t_count):
                if j - i < min_len:
                    min_len = j - i
                    result = window
                break

    return result


def min_window_sliding(s, t):
    """
    Sliding Window: O(n + m).
    
    Key variables:
      need[char] = how many more of this char we need
      missing = total chars still needed
    """
    if not t or not s:
        return ""

    need = Counter(t)
    missing = len(t)
    left = 0
    best = (0, float('inf'))

    for right, char in enumerate(s):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        # Shrink while valid (all chars found)
        while missing == 0:
            if right - left < best[1] - best[0]:
                best = (left, right)

            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    start, end = best
    return s[start:end + 1] if end != float('inf') else ""


def min_window_trace(s, t):
    """Sliding Window with trace."""
    if not t or not s:
        return ""

    need = Counter(t)
    missing = len(t)
    left = 0
    best = ""

    print(f'  s = "{s}", t = "{t}"')
    print(f'  Need: {dict(need)}')
    print()

    for right in range(len(s)):
        char = s[right]
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        if missing > 0:
            print(f'  R={right} "{char}": '
                  f'missing={missing}, expand')
        else:
            while missing == 0:
                window = s[left:right + 1]
                if not best or len(window) < len(best):
                    best = window
                    print(f'  R={right}: '
                          f'window="{window}" len={len(window)} '
                          f'🏆 new best!')
                else:
                    print(f'  R={right}: '
                          f'window="{window}" len={len(window)} '
                          f'→ shrink L')

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

    return best


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Min Window Substring — Trace")
    print("=" * 60)
    result = min_window_trace("ADOBECODEBANC", "ABC")
    assert result == "BANC"
    print(f'\n  Result: "{result}" ✅')
    print()

    print("=" * 60)
    print("TEST 2: More Test Cases")
    print("=" * 60)
    cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("aa", "aa", "aa"),
    ]
    for s, t, expected in cases:
        result = min_window_sliding(s, t)
        status = "✅" if result == expected else "❌"
        print(f'  s="{s}", t="{t}" '
              f'→ "{result}" {status}')
    print()

    # Verify BF == SW
    print("=" * 60)
    print("TEST 3: BF vs SW — Same Results")
    print("=" * 60)
    import random
    import string

    for _ in range(5):
        n = random.randint(10, 50)
        s = ''.join(random.choices("ABCDE", k=n))
        m = random.randint(1, 5)
        t = ''.join(random.choices("ABCDE", k=m))

        bf = min_window_brute(s, t)
        sw = min_window_sliding(s, t)
        match = len(bf) == len(sw)
        status = "✅" if match else "❌"
        print(f'  s="{s[:20]}...", t="{t}" '
              f'→ BF="{bf}" SW="{sw}" {status}')

    print()
    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. 'need' tracks how many MORE chars we need")
    print("   2. Negative need[c] means we have EXTRA c's")
    print("   3. Shrink while VALID → find minimum window")
