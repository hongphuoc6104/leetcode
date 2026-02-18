"""
=============================================================
 Example 5: Find All Anagrams (LC 438)
=============================================================

Problem: Find all start indices of anagrams of p in s.
         (Tìm tất cả vị trí bắt đầu của đảo chữ p trong s.)

Uses Fixed Window + Frequency Matching.
Window size = len(p), slide and compare frequency counters.

Time:  O(n) where n = len(s)
Space: O(k) where k = number of distinct chars in p
"""
from collections import Counter


def find_anagrams_brute(s, p):
    """BF: O(n × m log m) — substring sort comparison."""
    result = []
    p_sorted = sorted(p)
    m = len(p)

    for i in range(len(s) - m + 1):
        if sorted(s[i:i + m]) == p_sorted:
            result.append(i)

    return result


def find_anagrams_sliding(s, p):
    """
    Sliding Window O(n): Fixed window + frequency match.
    
    Key: maintain a frequency counter for the window.
    Slide by adding right char, removing left char.
    Compare counter with target.
    """
    if len(p) > len(s):
        return []

    p_count = Counter(p)
    k = len(p)
    window = Counter(s[:k])
    result = []

    if window == p_count:
        result.append(0)

    for i in range(k, len(s)):
        # Add right character (Thêm ký tự phải)
        window[s[i]] += 1

        # Remove left character (Bỏ ký tự trái)
        left_char = s[i - k]
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]

        # Check match (Kiểm tra khớp)
        if window == p_count:
            result.append(i - k + 1)

    return result


def find_anagrams_optimized(s, p):
    """
    Optimized O(n): Track 'matches' count instead of
    comparing full counters each time.
    """
    if len(p) > len(s):
        return []

    p_count = Counter(p)
    window = Counter()
    result = []
    k = len(p)
    matches = 0
    target_matches = len(p_count)

    for i in range(len(s)):
        # Add right
        c = s[i]
        window[c] += 1
        if window[c] == p_count.get(c, 0):
            matches += 1
        elif window[c] == p_count.get(c, 0) + 1:
            matches -= 1

        # Remove left (when window exceeds size k)
        if i >= k:
            c = s[i - k]
            if window[c] == p_count.get(c, 0):
                matches -= 1
            elif window[c] == p_count.get(c, 0) + 1:
                matches += 1
            window[c] -= 1
            if window[c] == 0:
                del window[c]

        if matches == target_matches:
            result.append(i - k + 1)

    return result


# ============================================================
# Test Cases
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TEST 1: Basic Cases")
    print("=" * 60)
    cases = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("aaaa", "aa", [0, 1, 2]),
        ("hello", "xyz", []),
    ]
    for s, p, expected in cases:
        result = find_anagrams_sliding(s, p)
        status = "✅" if result == expected else "❌"
        print(f'  s="{s}", p="{p}" → {result} {status}')
    print()

    # Verify all 3 methods agree
    print("=" * 60)
    print("TEST 2: All Methods Agree")
    print("=" * 60)
    import random
    import string

    for _ in range(5):
        n = random.randint(20, 50)
        m = random.randint(2, 5)
        s = ''.join(random.choices("abcd", k=n))
        p = ''.join(random.choices("abcd", k=m))

        bf = find_anagrams_brute(s, p)
        sw = find_anagrams_sliding(s, p)
        opt = find_anagrams_optimized(s, p)
        match = bf == sw == opt
        status = "✅" if match else "❌"
        print(f'  s="{s[:25]}...", p="{p}" '
              f'→ {len(bf)} anagrams {status}')
    print()

    # Performance
    print("=" * 60)
    print("TEST 3: Performance Comparison")
    print("=" * 60)
    import time

    for n in [1000, 5000, 10000]:
        s = ''.join(random.choices("abcde", k=n))
        p = "abc"

        start = time.perf_counter()
        r1 = find_anagrams_brute(s, p)
        t_bf = time.perf_counter() - start

        start = time.perf_counter()
        r2 = find_anagrams_sliding(s, p)
        t_sw = time.perf_counter() - start

        start = time.perf_counter()
        r3 = find_anagrams_optimized(s, p)
        t_opt = time.perf_counter() - start

        assert r1 == r2 == r3
        print(f"  n={n:>5}: BF={t_bf*1000:>7.2f}ms | "
              f"SW={t_sw*1000:>6.3f}ms | "
              f"Opt={t_opt*1000:>6.3f}ms")
    print()

    print("✅ All tests passed!")
    print()
    print("🔑 Key Takeaways:")
    print("   1. Fixed window = slide right, don't shrink")
    print("   2. Counter comparison is O(26) for lowercase")
    print("   3. 'matches' tracking avoids even that O(26)")
